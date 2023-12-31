from ultralytics import YOLO
import cv2
from moviepy.editor import VideoFileClip
import streamlit as st
import cv2
import time
import shutil
import os
from PIL import Image
import numpy as np

blackjack_classes = [
    '10 chuon', '10 ro', '10 co', '10 bich',
    '2 chuon', '2 ro', '2 co', '2 bich',
    '3 chuon', '3 ro', '3 co', '3 bich',
    '4 chuon', '4 ro', '4 co', '4 bich',
    '5 chuon', '5 ro', '5 co', '5 bich',
    '6 chuon', '6 ro', '6 co', '6 bich',
    '7 chuon', '7 ro', '7 co', '7 bich',
    '8 chuon', '8 ro', '8 co', '8 bich',
    '9 chuon', '9 ro', '9 co', '9 bich',
    'A chuon', 'A ro', 'A co', 'A bich',
    'J chuon', 'J ro', 'J co', 'J bich',
    'Joker',
    'K chuon', 'K ro', 'K co', 'K bich',
    'Q chuon', 'Q ro', 'Q co', 'Q bich',
    'black chip', 'blue chip', 'card back', 'chips', 'green chip', 'red chip', 'white chip'
]


model_blackjack = YOLO("./Module/BlackJackRecognize/weights/best.pt")


def detect_blackjack_video(video_path, result_path):
    os.makedirs(result_path, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    # Lấy thông số của video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                  int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # Tạo đối tượng VideoWriter
    out = cv2.VideoWriter(result_path + "output.mp4",
                          cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)

    notice = []
    frame_count = 0

    while cap.isOpened():
        frame_count += 1
        ret, frame = cap.read()
        if not ret:
            break

        # Gửi frame vào hàm nhận diện
        # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        str_result, frame = detect_blackjack_frame(frame)

        # Ghi frame đã được xử lý vào video output
        out.write(frame)
        if (frame_count % 10 == 0):
            notice.append("Frame Recognized: "+str(frame_count))
    cap.release()
    out.release()
    for i in range(0, len(notice)):
        notice[i] += "/"+str(frame_count-1)
    notice.append("Frame Recognized: " +
                  str(frame_count-1)+"/"+str(frame_count-1))
    return notice


def detect_blackjack_frame(frame):
    result_string = []
    # nhận dạng biển số trước
    plates_detected = model_blackjack(frame, stream=True)

    for plate in plates_detected:
        boxes = plate.boxes

        for box in boxes:
            # Lấy ra tọa độ của các box biển số
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(
                x2), int(y2)  # convert to int values
            blackjack_char = blackjack_classes[int(box.cls[0])]

            # In số lên trên biển xe
            org = [x1, y1-1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 0.6
            color = (0, 0, 255)
            thickness = 2
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.putText(frame, blackjack_char, org, font,
                        fontScale, color, thickness)
            result_string.append("Tìm thấy: " + blackjack_char)
    return result_string, frame


def convert_video(input_path, output_path):
    codec = 'libx264'
    audio_codec = 'aac'
    try:
        video_clip = VideoFileClip(input_path)
        video_clip.write_videofile(
            output_path, codec=codec, audio_codec=audio_codec)
        return True
    except Exception as e:
        print(f"Lỗi khi chuyển đổi video: {e}")
        return False


def runBlackJack():
    st.title("Nhận dạng lá bài tây")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
                #### Mô tả
                Model này được training trên tập dữ liệu custom về 53 lá bài tây bằng thư viện OpenCV để phân tích ảnh và scikit-learn. Cho phép phát hiện ra các loại bài khác nhau khi truyền ảnh vào
                """
        )
    with col2:
        st.markdown(
            """
                #### Model được sử dụng
                📌Tự train trên data custom
                """
        )
    st.divider()

    result_path = ".\\Module\\BlackJackRecognize\\result\\"

    # Upload file
    uploaded_file = st.file_uploader(
        "Upload a JPG, JPEG, PNG, MP4 file",
        type=["jpg", "jpeg", "png", "mp4"],
        help="Scanned file are not supported yet!",
    )

    col1, col2 = st.columns(2)
    bt1 = col1.button("Nhận dạng", type="primary")
    bt2 = col2.button("Xóa", type="primary")

    if not uploaded_file:
        st.warning("Vui lòng upload file để nhận dạng!!!")
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.progress(100)
        if "image" in uploaded_file.type:
            st.image(uploaded_file)
            if bt1:
                with st.status("Black Jack Recognization Start!", expanded=True) as status:
                    st.write("Open image: "+uploaded_file.name)
                    image = Image.open(uploaded_file)
                    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                    st.write("Recognizing...")
                    result_string, image = detect_blackjack_frame(frame)
                    for s in result_string:
                        st.write(s)
                        time.sleep(0.5)
                    st.write("Done!")
                    status.update(label="Completed recognize BlackJack",
                                  state="complete", expanded=False)
                st.image(
                    image, "Ảnh đã nhận diện (Để biết thêm chi tiết, click vào status)", channels="BGR")

            if "video" in uploaded_file.type:
                os.makedirs(result_path, exist_ok=True)
                st.video(uploaded_file)
                with st.status("Licesen Plate Recognization Start!", expanded=True) as status:
                    st.write("Open video: "+uploaded_file.name)
                    if os.path.exists(result_path):
                        shutil.rmtree(result_path)
                    # lưu video
                    video_bytes = uploaded_file.read()
                    input_filepath = ".\Module\BlackJackRecognize\input.mp4"
                    with open(input_filepath, 'wb') as file:
                        file.write(video_bytes)

                    st.write("Recognizing...")
                    detect_blackjack_video(input_filepath, result_path)
                    st.write("Recognization done!")
                    st.write("Start convert video!")
                    convert_video(input_path=result_path + "output.mp4",
                                  output_path=result_path + 'output_convert.mp4')
                    st.write("All done!")
                    status.update(
                        label="Recognization successfully! Video is available!", state="complete", expanded=False)
                st.video(result_path + 'output_convert.mp4')
    if bt2:
        if os.path.exists(".\Module\BlackJackRecognize\input.mp4"):
            os.remove(".\Module\BlackJackRecognize\input.mp4")
        if os.path.exists(result_path):
            shutil.rmtree(result_path)
    st.divider()
    st.title('Kết quả training')
    col1, col2 = st.columns(2)
    col1.image('./Module/BlackJackRecognize/result_train/confusion_matrix.png',
               caption='confusion_matrix')
    col2.image('./Module/BlackJackRecognize/result_train/results.png',
               caption='results')
    col2.image('./Module/BlackJackRecognize/result_train/val_batch0_labels.jpg')
