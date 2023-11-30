import streamlit as st


st.markdown(
    """
    <style>
        .stHeadingContainer span {
            color: #000000;
            font-size: 36px;
            text-align: center;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 20px;
        }

        [data-testid="stMarkdownContainer"] {
            text-align: center;
        }
    </style>
"""
)

#! cái này là tuỳ đứa chọn introduction nhé
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
        # st.subheader("6 chức năng chính trong bài")
        st.markdown("""####6 chức năng chính trong bài""")
        st.write("📖Giải phương trình bậc 2")
        st.write("📖Nhận dạng gương mặt")
        st.write("📖Nhận dạng đối tượng")
        st.write("📖Nhận dạng chữ số viết tay")
        st.write("📖Nhận dạng 5 loại trái cây")
        st.write("📖Xử lý ảnh số")
    with col2:
        st.markdown("""####Phần làm thêm""")
        st.write("📖Nhận diện độ tuổi, giới tính")
        st.write("📖Nhận diện chữ viết tay")
        st.write("📖Nhận diện nón bảo hiểm")
