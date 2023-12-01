from ultralytics import YOLO
import cv2
import math
import streamlit as st
import os
import shutil
from PIL import Image
import numpy as np

model_helmet = YOLO("./Module/HelmetDetection/weights/best.pt")


def detect_helmet_video(video_path, result_path):
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
        frame = detect_helmet_frame(frame)

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


def detect_helmet_frame(frame):
    result_string = []
    # nhận dạng biển số trước
    helmets_detected = model_helmet(frame, stream=True)

    for helmet in helmets_detected:
        boxes = helmet.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(
                x2), int(y2)  # convert to int values

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

    return frame


def runDetect():
    st.title('Nhận diện nón bảo hiểm')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
                #### Mô tả
                Model này được training trên tập dữ liệu custom bằng thư viện OpenCV để phân tích ảnh và scikit-learn. Cho phép phát hiện ra mũ bảo hiểm trong các tấm ảnh được truyền vào.
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
    col1, col2 = st.columns(2)
    with col1:
        image_path = st.file_uploader(
            "Upload Images", type=["bmp", "png", "jpg", "jpeg"])
        detect = st.button("Nhận diện", type='primary')
        delete = st.button("Xoá bộ nhớ")
    if image_path is not None:
        image = Image.open(image_path)
        frame = np.array(image)
        col2.image(image, caption='Input')
        if detect:
            frame_output = detect_helmet_frame(frame)
            col2.image(frame_output, caption='Output')
            if delete:
                st.experimental_rerun()
                shutil.rmtree(image_path)

    st.divider()
    st.markdown(""" ### Kết quả traning model """)
    col1, col2 = st.columns(2)
    col1.image(
        '.\\Module\\HelmetDetection\\result_train\\results.png', caption='Results')
    col2.image('.\\Module\\HelmetDetection\\result_train\\confusion_matrix.png',
               caption='confusion_matrix')
    col1.image(
        '.\\Module\\HelmetDetection\\result_train\\val_batch0_labels.jpg', caption='Example')
