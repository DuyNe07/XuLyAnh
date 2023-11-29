import streamlit as st
from streamlit_option_menu import option_menu

from faceAgeGender_dectected.mainAgeGender import runAgeGender
from face_recognize.mainFace import mainface
from nhan_dang_chu_so import home
from HandWriting.runhand import handwriting_streamlit_show

st.set_page_config(
    page_title="Luong Vu Dinh Duy 2113018 App",
    page_icon="🍑",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("styles.css") as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("Main Menu", ["Introduction", "Nhận Dạng Trái Cây", 'Nhận Diện Tuổi & Giới tính',
                           'Nhận Diện Gương Mặt', 'Nhận Diện Chữ Số', 'Giải Phương Trình Bậc 2', 'Nhận Diện Chữ Viết Tay'], icons=['rocket', 'apple', 'people', 'robot', 'pencil', 'calculator', 'pen'], menu_icon="book", default_index=0)


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
            ##### Giảng viên: GVC, ThS Trần Tiến Đức
            """
        )
    with col2:
        st.image("image/duy.png")

    st.divider()
    st.subheader("Nội dung project")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("6 chức năng chính trong bài")
        st.write("📖Giải phương trình bậc 2")
        st.write("📖Nhận dạng gương mặt")
        st.write("📖Nhận dạng đối tượng")
        st.write("📖Nhận dạng chữ số viết tay")
        st.write("📖Nhận dạng 5 loại trái cây")
        st.write("📖Xử lý ảnh số")
    with col2:
        st.subheader("Phần làm thêm")
        st.write("📖Nhận diện độ tuổi, giới tính")
        st.write("📖Nhận diện chữ viết tay")


if selected == "Nhận Diện Gương Mặt":
    mainface()
elif selected == "Nhận Diện Tuổi & Giới tính":
    runAgeGender()

elif selected == 'Nhận Diện Chữ Số':
    st.title("Nhận Diện Chữ Viết")
    home.runChuViet()

elif selected == 'Nhận Diện Chữ Viết Tay':
    handwriting_streamlit_show()
