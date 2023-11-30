import json
import cv2
import argparse
from htr_pipeline import read_page, DetectorConfig, LineClusteringConfig, ReaderConfig, PrefixTree


def process_page(img, scale, margin, use_dictionary, min_words_per_line, text_scale, output, classes):
    with open(classes) as f:
        word_list = [w.strip().upper() for w in f.readlines()]
    prefix_tree = PrefixTree(word_list)

    # read page
    read_lines = read_page(img,
                           detector_config=DetectorConfig(
                               scale=scale, margin=margin),
                           line_clustering_config=LineClusteringConfig(
                               min_words_per_line=min_words_per_line),
                           reader_config=ReaderConfig(decoder='word_beam_search' if use_dictionary else 'best_path',
                                                      prefix_tree=prefix_tree))

    # create text to show
    res = ''
    for read_line in read_lines:
        res += ' '.join(read_word.text for read_word in read_line) + '\n'

    # create visualization to show
    for i, read_line in enumerate(read_lines):
        for read_word in read_line:
            aabb = read_word.aabb
            cv2.rectangle(img,
                          (aabb.xmin, aabb.ymin),
                          (aabb.xmin + aabb.width, aabb.ymin + aabb.height),
                          (0, 128, 0),
                          2)
            cv2.putText(img,
                        read_word.text,
                        (aabb.xmin, aabb.ymin + aabb.height // 2),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        text_scale,
                        color=(0, 0, 255))
    print(res)
    cv2.imwrite(output+'output_image.jpg', img)


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('--image', type=str)
    parse.add_argument('--scale', type=float,)
    parse.add_argument('--margin', type=float)
    parse.add_argument('--method', type=bool)
    parse.add_argument('--min_words_per_line', type=int)
    parse.add_argument('--text_scale', type=float)
    parse.add_argument('--output', type=str, default="")
    parse.add_argument('--classes', type=str, default="")
    opt = parse.parse_args()

    img = cv2.imread(opt.image, cv2.IMREAD_COLOR)  # cv2.IMREAD_GRAYSCALE
    process_page(img, opt.scale, opt.margin, opt.method,
                 opt.min_words_per_line, opt.text_scale, opt.output, opt.classes)
