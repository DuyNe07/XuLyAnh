import streamlit as st
import numpy as np
import cv2 as cv
import joblib
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import shutil
import time
import tempfile
from PIL import Image

from sklearn.metrics import f1_score, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.manifold import TSNE

face_detection = "./face_recognize/model/face_detection_yunet_2023mar.onnx"
face_recognition = "./face_recognize/model/face_recognition_sface_2021dec.onnx"
score_threshold = 0.8
nms_threshold = 0.3

detector = cv.FaceDetectorYN.create(
    face_detection,
    "",
    (320, 320),
    score_threshold,
    nms_threshold,
    5
)

recognizer = cv.FaceRecognizerSF.create(face_recognition, "")


def str2bool(v):
    if v.lower() in ['on', 'yes', 'true', 'y', 't']:
        return True
    elif v.lower() in ['off', 'no', 'false', 'n', 'f']:
        return False
    else:
        raise NotImplementedError


def visualize(input, faces, fps, thickness=2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            coords = face[:-1].astype(np.int32)

            # Hiển thị hộp giới hạn và tên người trên khung chứa khuôn mặt
            cv.rectangle(input, (coords[0], coords[1]), (coords[0] +
                         coords[2], coords[1]+coords[3]), (0, 255, 0), thickness)
            # cv.putText(input, mydict[test_predict[0]], (coords[0], coords[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Hiển thị các điểm trên khuôn mặt
            cv.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv.circle(input, (coords[10], coords[11]),
                      2, (255, 0, 255), thickness)
            cv.circle(input, (coords[12], coords[13]),
                      2, (0, 255, 255), thickness)

    cv.putText(input, 'FPS: {:.2f}'.format(fps), (1, 16),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


if 'stop' not in st.session_state:
    st.session_state.stop = False
    stop = False


# region getData


def getData(nameUser):

    FRAME_WINDOW = st.image([])
    cap = cv.VideoCapture(0)

    output_dir = f'./face_recognize/image/{nameUser}/'
    if os.path.exists(output_dir):
        # Nếu tồn tại, xóa thư mục
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    tm = cv.TickMeter()

    frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    detector.setInputSize([frameWidth, frameHeight])

    dem = 0
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            print('No frames grabbed!')
            break

        # Inference
        tm.start()
        faces = detector.detect(frame)  # faces is a tuple
        tm.stop()

        key = cv.waitKey(1) & 0xFF
        if dem == 150:
            break

        if faces[1] is not None:
            face_align = recognizer.alignCrop(frame, faces[1][0])
            file_name = f'./face_recognize/image/{nameUser}/{nameUser}_{dem:03d}.bmp'
            cv.imwrite(file_name, face_align)
            dem += 1
        # Draw results on the input image
        visualize(frame, faces, tm.getFPS())

        # Visualize results
        FRAME_WINDOW.image(frame, channels='BGR')
    cv.destroyAllWindows()
    FRAME_WINDOW.empty()
# endregion

# region Training


class IdentityMetadata():
    def __init__(self, base, name, file):
        # dataset base directory
        self.base = base
        # identity name
        self.name = name
        # image file name
        self.file = file

    def __repr__(self):
        return self.image_path()

    def image_path(self):
        return os.path.join(self.base, self.name, self.file)


def load_metadata(path):
    metadata = []
    for i in sorted(os.listdir(path)):
        for f in sorted(os.listdir(os.path.join(path, i))):
            # Check file extension. Allow only jpg/jpeg' files.
            ext = os.path.splitext(f)[1]
            if ext == '.jpg' or ext == '.jpeg' or ext == '.bmp':
                metadata.append(IdentityMetadata(path, i, f))
    return np.array(metadata)


def Training():
    with st.status("Processing training", expanded=True) as status:
        st.write("Loading image...")
        time.sleep(3)
        st.write("Training model...")

        metadata = load_metadata('./face_recognize/image')
        embedded = np.zeros((metadata.shape[0], 128))

        oldname = ''

        for i, m in enumerate(metadata):

            username = m.image_path().split("\\")[1]
            if (username != oldname):
                st.write("Traning " + username + "'s face...")
                oldname = username
            print(m.image_path())
            img = cv.imread(m.image_path(), cv.IMREAD_COLOR)
            face_feature = recognizer.feature(img)
            embedded[i] = face_feature

            targets = np.array([m.name for m in metadata])

            encoder = LabelEncoder()
            encoder.fit(targets)

            # Numerical encoding of identities
            y = encoder.transform(targets)

            train_idx = np.arange(metadata.shape[0]) % 5 != 0
            test_idx = np.arange(metadata.shape[0]) % 5 == 0
            X_train = embedded[train_idx]
            X_test = embedded[test_idx]
            y_train = y[train_idx]
            y_test = y[test_idx]
            svc = LinearSVC(dual=False)
            svc.fit(X_train, y_train)
            acc_svc = accuracy_score(y_test, svc.predict(X_test))
            joblib.dump(svc, './face_recognize/model/svc.pkl')

        status.update(label="Training complete!",
                      state="complete", expanded=False)
# endregion


# region predict
def predict(type, img):
    svc = joblib.load('./face_recognize/model/svc.pkl')
    tm = cv.TickMeter()
    mydict = []
    pathImg = './face_recognize/image'
    for i in sorted(os.listdir(pathImg)):
        mydict.append(i)
    if type == 'cam':
        FRAME_WINDOW = st.image([])
        cap = cv.VideoCapture(0)

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

        frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        detector.setInputSize([frameWidth, frameHeight])

        while True:
            hasFrame, frame = cap.read()
            if not hasFrame:
                print('No frames grabbed!')
                break

            # Inference
            tm.start()
            faces = detector.detect(frame)  # faces is a tuple
            tm.stop()

            if faces[1] is not None:
                for face in faces[1]:
                    face_align = recognizer.alignCrop(frame, face)
                    face_feature = recognizer.feature(face_align)
                    test_predict = svc.predict(face_feature)
                    result = mydict[test_predict[0]]

                    # Visualize results
                    visualize(frame, faces, tm.getFPS())

                    # Display the result directly on the frame
                    coords = face[:-1].astype(np.int32)
                    cv.putText(frame, result, (coords[0], coords[1] - 10),
                               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Display the result
                FRAME_WINDOW.image(frame, channels='BGR')
        cv.destroyAllWindows()
    if type == 'img':
        frame = cv.imread(img)
        scale_factor = 0.4
        frame = cv.resize(frame, (0, 0), fx=scale_factor, fy=scale_factor)

        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        detector.setInputSize([frameWidth, frameHeight])

        tm.start()
        faces = detector.detect(frame)  # faces is a tuple
        tm.stop()

        if faces[1] is not None:
            for face in faces[1]:
                face_align = recognizer.alignCrop(frame, face)
                face_feature = recognizer.feature(face_align)
                test_predict = svc.predict(face_feature)
                result = mydict[test_predict[0]]

                # Visualize results
                visualize(frame, faces, tm.getFPS())

                # Display the result directly on the frame
                coords = face[:-1].astype(np.int32)
                cv.putText(frame, result, (coords[0], coords[1] - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            st.image(frame)


# endregion

result_path = './face_recognize/output'


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


def mainface():
    st.title('Nhận diện gương mặt')
    nameUser = st.text_input(
        'Nhập tên người thu thập dữ liệu', placeholder='VD: Bạn A')
    if (st.button('Nhận dữ liệu')):
        getData(nameUser)

    if st.button("Tiến hành training face recognize"):
        Training()

    if (st.button('Nhận diện bằng camera')):
        predict('cam', None)

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
                predict('img', absolute_path)
                if st.button("Xoá ảnh"):
                    st.experimental_rerun()
                    shutil.rmtree(result_path)
                    delete_temporary_file_by_name(file_path)


if __name__ == '__main__':
    mainface()
