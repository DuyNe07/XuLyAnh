import streamlit as st
from streamlit_option_menu import option_menu

from Module.faceAgeGender_dectected.mainAgeGender import runAgeGender
from Module.face_recognize.mainFace import mainface
from Module.nhan_dang_chu_so.home import runChuViet
from Module.HandWriting.runhand import handwriting_streamlit_show
from Module.pt_bac2.giai_pt_bac_2 import runPtBac2
from Module.Object_detect.Objectdetect import nhan_dang_doi_tuong
from Module.Fruit_recognize.runFruit import nhan_dang_trai_cay
from Module.XuLyAnh.xulyanh import runXuLyAnh
from Module.HelmetDetection.detect_custom import runDetect
from Module.BlackJackRecognize.detect_blackjack_custom import runBlackJack
from Module.ExamCheatingDetection.ExamCheatingDetect_streamlit import ExamCheatingDetect_streamlit_show

st.set_page_config(
    page_title="Luong Vu Dinh Duy 2113018",
    page_icon="🍑",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("styles.css") as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .nav-link {{
            font-family: "Arial", sans-serif !important;
        }}
    <\style>

""", unsafe_allow_html=True
)

with st.sidebar:
    selected = option_menu("Main Menu", ["Introduction", 'Giải Phương Trình Bậc 2', 'Nhận Diện Gương Mặt',
                                         'Nhận dạng đối tượng',  'Nhận Diện Chữ Số', "Nhận Dạng Trái Cây",
                                         'Xử lí ảnh', 'Nhận Diện Tuổi & Giới tính', 'Nhận Diện Chữ Viết Tay',
                                         'Nhận diện nón bảo hiểm', 'Nhận diện bài tây', 'Nhận diện gian lận'],
                           icons=['rocket', 'calculator', 'person', 'robot', 'pencil', 'apple', 'image', 'people', 'pencil', 'fire', 'heart', 'book'], menu_icon="book", default_index=0)


if selected == "Introduction":
    st.image('image/HCMUTE-fit.png')
    st.divider()
    st.title("Đồ án cuối kì môn Xử lí ảnh số")
    st.divider()
    st.header("Sinh viên thực hiện")
    col1, col2 = st.columns(2)
    with col1:
        st.text("")
        st.markdown(
            """
            ## Lương Vũ Đình Duy
            ##### MSSV: 21133018
            ##### Mã lớp: DIPR430685_23_1_02
            ##### Giảng viên: ThS. Trần Tiến Đức
            """
        )
    with col2:
        st.image("image/duy.png")

    st.divider()
    st.subheader("Nội dung project")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("6 chức năng chính trong bài")
        st.write("⚡Giải phương trình bậc 2")
        st.write("⚡Nhận dạng gương mặt")
        st.write("⚡Nhận dạng đối tượng")
        st.write("⚡Nhận dạng chữ số viết tay")
        st.write("⚡Nhận dạng 5 loại trái cây")
        st.write("⚡Xử lý ảnh số")
    with col2:
        st.subheader("Phần làm thêm")
        st.write("⚡Nhận diện độ tuổi, giới tính")
        st.write("⚡Nhận diện chữ viết tay")
        st.write("⚡Nhận diện nón bảo hiểm")
        st.write("⚡Nhận diện bài tây")
        st.write("⚡Nhận diện gian lận")
    st.divider()
    st.write("Chúc thầy thật nhiều sức khoẻ")


if selected == "Nhận Diện Gương Mặt":
    mainface()

elif selected == "Nhận Diện Tuổi & Giới tính":
    runAgeGender()

elif selected == 'Nhận Diện Chữ Số':
    runChuViet()

elif selected == 'Nhận Diện Chữ Viết Tay':
    handwriting_streamlit_show()

elif selected == 'Giải Phương Trình Bậc 2':
    runPtBac2()

elif selected == 'Nhận dạng đối tượng':
    nhan_dang_doi_tuong()

elif selected == 'Nhận Dạng Trái Cây':
    nhan_dang_trai_cay()

elif selected == 'Xử lí ảnh':
    runXuLyAnh()
elif selected == 'Nhận diện nón bảo hiểm':
    runDetect()

elif selected == 'Nhận diện bài tây':
    runBlackJack()

elif selected == 'Nhận diện gian lận':
    ExamCheatingDetect_streamlit_show()
