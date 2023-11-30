import streamlit as st
import numpy as np
from PIL import Image
import cv2
import shutil

classes = ['Apple', 'Banana', 'Pineapple', 'Strawberry', 'Watermelon']
# Constants.
INPUT_WIDTH = 640
INPUT_HEIGHT = 640
SCORE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.45
CONFIDENCE_THRESHOLD = 0.45

# Text parameters.
FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
THICKNESS = 1

# Colors.
BLACK = (0, 0, 0)
BLUE = (255, 178, 50)
YELLOW = (0, 255, 255)


def draw_label(im, label, x, y):
    """Draw text onto image at location."""
    # Get text size.
    text_size = cv2.getTextSize(label, FONT_FACE, FONT_SCALE, THICKNESS)
    dim, baseline = text_size[0], text_size[1]
    # Use text size to create a BLACK rectangle.
    cv2.rectangle(
        im, (x, y), (x + dim[0], y + dim[1] + baseline), (0, 0, 0), cv2.FILLED)
    # Display text inside the rectangle.
    cv2.putText(im, label, (x, y + dim[1]), FONT_FACE,
                FONT_SCALE, YELLOW, THICKNESS, cv2.LINE_AA)


def pre_process(input_image, net):
    # Create a 4D blob from a frame.
    blob = cv2.dnn.blobFromImage(
        input_image, 1 / 255, (INPUT_WIDTH, INPUT_HEIGHT), [0, 0, 0], 1, crop=False)

    # Sets the input to the network.
    net.setInput(blob)

    # Run the forward pass to get output of the output layers.
    outputs = net.forward(net.getUnconnectedOutLayersNames())
    return outputs


def post_process(input_image, outputs):
    # Lists to hold respective values while unwrapping.
    class_ids = []
    confidences = []
    boxes = []
    # Rows.
    rows = outputs[0].shape[1]
    image_height, image_width = input_image.shape[:2]
    # Resizing factor.
    x_factor = image_width / INPUT_WIDTH
    y_factor = image_height / INPUT_HEIGHT
    # Iterate through detections.
    for r in range(rows):
        row = outputs[0][0][r]
        confidence = row[4]
        # Discard bad detections and continue.
        if confidence >= CONFIDENCE_THRESHOLD:
            classes_scores = row[5:]
            # Get the index of max class score.
            class_id = np.argmax(classes_scores)
            #  Continue if the class score is above threshold.
            if (classes_scores[class_id] > SCORE_THRESHOLD):
                confidences.append(confidence)
                class_ids.append(class_id)
                cx, cy, w, h = row[0], row[1], row[2], row[3]
                left = int((cx - w / 2) * x_factor)
                top = int((cy - h / 2) * y_factor)
                width = int(w * x_factor)
                height = int(h * y_factor)
                box = np.array([left, top, width, height])
                boxes.append(box)

    # Perform non maximum suppression to eliminate redundant, overlapping boxes with lower confidences.
    indices = cv2.dnn.NMSBoxes(
        boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    for i in indices:
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        # Draw bounding box.
        cv2.rectangle(input_image, (left, top),
                      (left + width, top + height), BLUE, 3 * THICKNESS)
        # Class label.
        label = "{}:{:.2f}".format(classes[class_ids[i]], confidences[i])
        # Draw label.
        draw_label(input_image, label, left, top)
    return input_image


def nhan_dang_trai_cay():
    try:
        if st.session_state["LoadModel9"] == True:
            print('Đã load model rồi')
    except:
        st.session_state["LoadModel9"] = True
        st.session_state["Net4"] = cv2.dnn.readNet(
            r"./Module/Fruit_recognize/trai_cay.onnx")
        print(st.session_state["LoadModel9"])
        print('Load model lần đầu')

    col1, col2, col3 = st.columns([1, 9, 1])
    with col2:
        st.header(
            'NHẬN DẠNG NĂM LOẠI TRÁI CÂY \n(Apple, Banana, Pineapple, Strawberry, Watermelon)')
        st.divider()
        img_file_buffer = st.file_uploader(
            "Upload an image", type=["bmp", "png", "jpg", "jpeg"])

        if img_file_buffer is not None:
            col4, col5 = st.columns(2)
            image = Image.open(img_file_buffer)
            # Chuyển sang cv2 để dùng sau này
            frame = np.array(image)
            frame = frame[:, :, [2, 1, 0]]  # BGR -> RGB

            col4.image(image, caption='Input')
            if st.button('Predict'):
                # Process image.
                detections = pre_process(frame, st.session_state["Net4"])
                img = post_process(frame.copy(), detections)
                """
                Put efficiency information. The function getPerfProfile returns       the overall time for inference(t) 
                and the timings for each of the layers(in layersTimes).
                """
                t, _ = st.session_state["Net4"].getPerfProfile()
                label = 'Inference time: %.2f ms' % (
                    t * 1000.0 / cv2.getTickFrequency())
                print(label)
                cv2.putText(img, label, (20, 40), FONT_FACE,
                            FONT_SCALE, (0, 0, 255), THICKNESS, cv2.LINE_AA)
                img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                col5.image(img_color, channels='RGB', caption='Output')
                if st.button("Xoá bộ nhớ"):
                    st.experimental_rerun()
                    shutil.rmtree(img_file_buffer)


if __name__ == "__main__":
    nhan_dang_trai_cay()
