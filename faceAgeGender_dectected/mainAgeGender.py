import streamlit as st
from streamlit_option_menu import option_menu
import os
import tempfile
from ffmpy import FFmpeg
from PIL import Image
import shutil
import time
import cv2 as cv


def getFaceBox(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [
                                104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2),
                         (0, 255, 0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, bboxes


result_path = './faceAgeGender_dectected/output'


def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(suffix="." + uploaded_file.type.rsplit("/", 1)[-1], delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        return temp_file.name


def get_absolute_path(file_name):
    return os.path.abspath(file_name)


def delete_temporary_file_by_name(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass  # Xử lý trường hợp tệp không tồn tại


path = './faceAgeGender_dectected/'
faceProto = "./faceAgeGender_dectected/model/opencv_face_detector.pbtxt"
faceModel = "./faceAgeGender_dectected/model/opencv_face_detector_uint8.pb"

ageProto = "./faceAgeGender_dectected/model/age_deploy.prototxt"
ageModel = "./faceAgeGender_dectected/model/age_net.caffemodel"

genderProto = "./faceAgeGender_dectected/model/gender_deploy.prototxt"
genderModel = "./faceAgeGender_dectected/model/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)',
           '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# Load network
ageNet = cv.dnn.readNet(ageModel, ageProto)
ageNet.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)

genderNet = cv.dnn.readNet(genderModel, genderProto)
genderNet.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)

faceNet = cv.dnn.readNet(faceModel, faceProto)
faceNet.setPreferableBackend(cv.dnn.DNN_TARGET_CPU)


def detec_img(img_path):
    padding = 15

    # Read frame
    frame = cv.imread(img_path)
    scale_factor = 1
    frame = cv.resize(frame, (0, 0), fx=scale_factor, fy=scale_factor)

    frameFace, bboxes = getFaceBox(faceNet, frame)
    if not bboxes:
        print("No face Detected, Checking next frame")

    for bbox in bboxes:
        face = frame[max(0, bbox[1]-padding):min(bbox[3]+padding, frame.shape[0]-1),
                     max(0, bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]

        blob = cv.dnn.blobFromImage(
            face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)

        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        print("Gender : {}, conf = {:.3f}".format(
            gender, genderPreds[0].max()))

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        print("Age : {}, conf = {:.3f}".format(age, agePreds[0].max()))

        label = "{},{}".format(gender, age)
        cv.putText(frameFace, label, (bbox[0], bbox[1]-10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv.LINE_AA)

    rgb_image = cv.cvtColor(frameFace, cv.COLOR_BGR2RGB)
    print('---------------------')
    return rgb_image


if 'stop' not in st.session_state:
    st.session_state.stop = False
    stop = False


def detec_cam():
    FRAME_WINDOW = st.image([])
    cap = cv.VideoCapture(0)
    padding = 15
    if 'stop' not in st.session_state:
        st.session_state.stop = False
        stop = False

    press = st.button('Stop')

    if press:
        if st.session_state.stop == False:
            st.session_state.stop = True
            cap.release()
        else:
            st.session_state.stop = False

    if 'frame_stop' not in st.session_state:
        frame_stop = None
        st.session_state.frame_stop = frame_stop

    if st.session_state.stop == True:
        FRAME_WINDOW.empty()

    while True:
        # Read frame
        t = time.time()
        hasFrame, frame = cap.read()
        if not hasFrame:
            print('No frames grabbed!')
            break

        frameFace, bboxes = getFaceBox(faceNet, frame)
        if not bboxes:
            print("No face Detected, Checking next frame")
            continue

        for bbox in bboxes:
            # print(bbox)
            face = frame[max(0, bbox[1]-padding):min(bbox[3]+padding, frame.shape[0]-1),
                         max(0, bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]

            blob = cv.dnn.blobFromImage(
                face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPreds = genderNet.forward()
            gender = genderList[genderPreds[0].argmax()]
            # print("Gender Output : {}".format(genderPreds))
            print("Gender : {}, conf = {:.3f}".format(
                gender, genderPreds[0].max()))

            ageNet.setInput(blob)
            agePreds = ageNet.forward()
            age = ageList[agePreds[0].argmax()]
            print("Age Output : {}".format(agePreds))
            print("Age : {}, conf = {:.3f}".format(age, agePreds[0].max()))

            label = "{},{}".format(gender, age)
            cv.putText(frameFace, label, (bbox[0], bbox[1]-10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv.LINE_AA)
            FRAME_WINDOW.image(frameFace, channels='BGR')
    cv.destroyAllWindows()


def runAgeGender():
    st.title('Nhận diện độ tuổi và giới tính')

    if st.button("Nhận dạng bằng camera"):
        detec_cam()

    if os.path.exists(result_path):
        shutil.rmtree(result_path)

    uploaded_file = st.file_uploader(
        "Upload a JPG, JPEG, PNG, MP4 file",
        type=["jpg", "jpeg", "png", "mp4"],
        help="Scanned file are not supported yet!",
    )
    if not uploaded_file:
        st.stop()
    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        absolute_path = get_absolute_path(file_path)
        if "image" in uploaded_file.type:
            image = Image.open(absolute_path)
            st.image(image, caption='Image you uploaded')
            nhandang = st.button("Nhận dạng", type="primary")
            if nhandang:
                img = detec_img(absolute_path)
                st.image(image=img)
                if st.button("Xoá ảnh"):
                    st.experimental_rerun()
                    shutil.rmtree(result_path)
                    delete_temporary_file_by_name(file_path)


if __name__ == '__main__':
    runAgeGender()
