import streamlit as st
from streamlit_option_menu import option_menu
import os
import tempfile
from ffmpy import FFmpeg
from PIL import Image
import shutil
from face_dectected import detect_faces, detect_faces_video
from fruit_dectected.yolov5 import detect
from faceAgeGender_dectected import mainAgeGender
from face_recognize import mainFace

st.set_page_config(
    page_title="Luong Vu Dinh Duy 2113018 App",
    page_icon="🍑",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    selected = option_menu("Main Menu", ["Introduction", "Nhận Dạng Trái Cây", 'Nhận Diện Tuổi & Giới tính',
                           'Nhận Diện Gương Mặt', 'Nhận Diện Chữ Viết'], icons=['🔥', 'fruit', 'people', 'face', '🔡'], menu_icon="cast", default_index=0)


if selected == "Introduction":
    st.title("Đồ án cuối kì môn XLAS")

if selected == "Nhận Diện Gương Mặt":
    mainFace.mainface()
elif selected == "Nhận Diện Tuổi & Giới tính":
    mainAgeGender.runAgeGender()
