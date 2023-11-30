from cProfile import label
import Module.XuLyAnh.Chapter09 as c9
import Module.XuLyAnh.Chapter05 as c5
import Module.XuLyAnh.Chapter04 as c4
import Module.XuLyAnh.Chapter03 as c3
import streamlit as st
import os
import cv2
import shutil
from PIL import Image
import numpy as np
import time


def clear_uploaded_files(session_state):
    for key, uploaded_file in session_state.uploaded_files.items():
        if os.path.exists(uploaded_file):
            os.remove(uploaded_file)
    session_state.uploaded_files = {}


class SessionState:
    def __init__(self):
        self.uploaded_files = {}
        self.display_output = False


# Create a session state instance
session_state = SessionState()


def runXuLyAnh():
    st.title("Xử lí ảnh")
    col1, col2 = st.columns(2)
    with col1:
        chuong = st.selectbox(
            "Chọn chương", ('Chương 3: Biến đổi độ sáng và lọc trong không gian', 'Chương 4: Lọc trong miền tần số', 'Chương 5: Khôi phục ảnh', 'Chương 9: Xử lý ảnh hình thái'))
    with col2:
        if chuong == 'Chương 3: Biến đổi độ sáng và lọc trong không gian':
            xulyanh = st.selectbox("Chọn phương pháp xử lí ảnh",
                                   ('Negative', 'Logarit ảnh', 'Power', 'PiecewiseLinear', 'Histogram', 'Cân bằng Histogram', 'Cân bằng Histogram của ảnh màu', 'Local Histogram', 'Histogram Statistics', 'Smoothing', 'SmoothingGauss', 'Threshold', 'MedianFilter', 'Sharpen', 'Gradient'))

        if chuong == 'Chương 4: Lọc trong miền tần số':
            xulyanh = st.selectbox("Chọn phương pháp xử lí ảnh", (
                'Spectrum', 'FrequencyFilter', 'Vẽ bộ lọc Notch Reject', 'RemoveMoire'))

        if chuong == 'Chương 5: Khôi phục ảnh':
            xylyanh = st.selectbox("Chọn phương pháp xử lí ảnh", ('Tạo nhiễu chuyển động',
                                   'Gỡ nhiễu của ảnh có ít nhiễu', 'Gỡ nhiễu của ảnh có nhiều nhiễu'))
        if chuong == 'Chương 9: Xử lý ảnh hình thái':
            xulyanh = st.selectbox(
                "Chọn phương pháp xử lí ảnh", ('Connected Component', 'Count Rice'))
    st.divider()
    if chuong == 'Chương 3: Biến đổi độ sáng và lọc trong không gian':
        if xulyanh == 'Negative':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp negative
            Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.Negative(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Logarit ảnh':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp Logarit
            Dùng để để cải thiện độ tương phản của ảnh hoặc để thực hiện các phép toán như tăng cường độ sáng hoặc giảm độ sáng của ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.Logarit(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Power':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp Power (Phép biến đổi gamma)
            Được dùng để điều chỉnh độ tương phản và độ sáng của ảnh. Phương pháp này thường được sử dụng để tăng cường hoặc giảm độ sáng của ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.Power(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'PiecewiseLinear':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp PiecewiseLinear
            Dùng để tạo ra hiệu ứng tăng cường, làm mịn, chỉnh sửa màu sắc và nhiều hiệu ứng khác trên ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.PiecewiseLinear(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Histogram':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp Histogram
            Dùng để cân bằng histogram, chuyển đổi mức xám hoặc phân ngưỡng.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.Histogram(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Cân bằng Histogram':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Cân bằng Histogram
            Dùng để làm phẳng phân bố của các mức xám trong ảnh, từ đó làm tăng độ tương phản và làm cho ảnh trở nên rõ ràng hơn.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.HistEqual(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Cân bằng Histogram của ảnh màu':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Cân bằng Histogram của ảnh màu
            Dùng để làm phẳng phân bố của các mức màu trong ảnh, từ đó làm tăng độ tương phản và làm cho ảnh trở nên rõ ràng hơn.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_color = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
                    col2.image(c3.HistEqualColor(frame_color),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Local Histogram':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp LocalHistogram
            Làm thay đổi độ tương phản và độ sáng trong ảnh dựa trên phân bố các mức xám trong các vùng nhỏ cục bộ của ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.LocalHist(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Histogram Statistics':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp Histogram Statistics
            Dùng để cải thiện độ tương phản và độ sáng của tổng thể ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.HistStat(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Smoothing':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp Smoothing
            Dùng để giảm nhiễu và làm mờ các chi tiết không mong muốn trong ảnh. Phương pháp này nhằm làm giảm sự biến động cục bộ trong ảnh để tạo ra một phiên bản làm mờ của ảnh gốc.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(cv2.blur(frame_gray, (21, 21)),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'SmoothingGauss':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp SmoothingGauss
            Dùng để làm mờ và giảm nhiễu.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(cv2.GaussianBlur(frame_gray, (43, 43), 7.0),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'MedianFilter':
            # st.subheader("Phương pháp negative")
            # st.write('Dùng để tạo một biến thể của ảnh: đảo ngược màu sắc của các điểm ảnh so với ảnh gốc')
            st.markdown("""
            ## Phương pháp MedianFilter
            Dùng để làm mờ và giảm nhiễu bằng cách giảm ảnh hưởng của các điểm ảnh nhiễu (điểm ảnh có giá trị không phản ánh đúng thông tin của ảnh) bằng cách thay thế giá trị của mỗi pixel bằng giá trị trung vị (median) của các giá trị pixel trong một vùng lân cận xác định.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.MedianFilter(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Threshold':
            st.markdown("""
            ## Phương pháp Phân ngưỡng (Threshold)
            Dùng để  chuyển đổi một ảnh xám thành ảnh nhị phân, nơi mỗi pixel của ảnh đầu ra được gán một giá trị nhất định dựa trên giá trị của pixel tương ứng trong ảnh đầu vào và một ngưỡng (threshold)
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png", "tif"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
                    col2.image(c3.Threshold(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Sharpen':
            st.markdown("""
            ## Phương pháp Sharpen
            Dùng để làm nổi bật các đặc trưng và tăng độ rõ nét của ảnh. Thường được dùng làm nổi bật các biên cạnh và chi tiết.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.Sharpen(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Gradient':
            st.markdown("""
            ## Phương pháp Gradient
            Dùng để làm nổi bật các biên cạnh và các chi tiết trong ảnh. Phương pháp này dựa trên việc tính toán độ dốc (gradient) của ảnh, tức là sự thay đổi độ sáng giữa các điểm ảnh liền kề.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c3.Gradient(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()

    if chuong == 'Chương 4: Lọc trong miền tần số':
        if xulyanh == 'Spectrum':
            st.markdown("""
            ## Phương pháp Spectrum
            Xử lý quang phổ bằng các công thức tần số sóng điện tử, ánh sáng, điểm ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c4.Spectrum(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'FrequencyFilter':
            st.markdown("""
            ## Phương pháp FrequencyFilter
            Bộ lọc cho tín hiệu có tần số thấp hơn tần số cắt đã chọn và làm suy giảm tín hiệu có tần số cao hơn tần số cắt để xử lý ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c4.FrequencyFilter(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Vẽ bộ lọc Notch Reject':
            st.markdown("""
            ## Vẽ bộ lọc Notch Reject
            Hiển thị hoặc vẽ bộ lọc Notch Reject, có thể hữu ích để hiểu cách bộ lọc được thiết kế để loại bỏ các tần số cụ thể gây ra hiện tượng moiré trong ảnh. Bằng cách này, có thể kiểm tra hoặc hiểu cấu trúc của bộ lọc và làm rõ tần số cụ thể nào được loại bỏ bởi nó.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
                if execute:
                    col2.image(c4.DrawNotchRejectFilter(),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'RemoveMoire':
            st.markdown("""
            ## Phương pháp RemoveMoire
            Dùng để xóa các điểm nhiễu ảnh bằng cách sử dụng một bộ lọc để loại bỏ các tần số thấp trong ảnh.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c4.RemoveMoire(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()

    if chuong == 'Chương 5: Khôi phục ảnh':
        if xylyanh == 'Tạo nhiễu chuyển động':
            st.markdown("""
            ## Tạo nhiễu chuyển động
            Mô phỏng hiện tượng nhiễu xuất hiện khi có chuyển động trong quá trình chụp ảnh
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c5.CreateMotionNoise(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xylyanh == 'Gỡ nhiễu của ảnh có ít nhiễu':
            st.markdown("""
            ## Gỡ nhiễu của ảnh có ít nhiễu
            Loại bỏ nhiễu từ ảnh bị mờ do chuyển động. Nó thực hiện việc này bằng cách áp dụng bộ lọc miền tần số cho ảnh. Bộ lọc được thiết kế để làm suy giảm các thành phần tần số cao của ảnh, thường liên quan đến nhiễu.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c5.DenoiseMotion(frame_gray),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xylyanh == 'Gỡ nhiễu của ảnh có nhiều nhiễu':
            st.markdown("""
            ## Gỡ nhiễu của ảnh có nhiều nhiễu
            Đầu tiên sử dụng hàm cv2.medianBlur() để lọc ảnh img bằng bộ lọc trung vị có kích thước 7x7. Bộ lọc trung vị sẽ thay thế mỗi pixel trong ảnh bằng giá trị trung vị của các pixel xung quanh nó. Điều này có thể giúp loại bỏ nhiễu hạt từ ảnh. Tiếp theo sử dụng một bộ lọc miền tần số để loại bỏ nhiễu từ ảnh bị mờ do chuyển động.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    temp = cv2.medianBlur(frame_gray, 7)
                    col2.image(c5.DenoiseMotion(temp),
                               use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()

    if chuong == 'Chương 9: Xử lý ảnh hình thái':
        if xulyanh == 'Connected Component':
            st.markdown("""
            ## Đếm thành phần liên thông của miếng phi lê gà (Connected Component)
            Xử lí ConnectedComponent trong OpenCV được sử dụng để nhận dạng và phân tích các thành phần liên thông trong ảnh nhị phân. Hàm này có thể được sử dụng cho các tác vụ như phân đoạn đối tượng, đếm đối tượng và theo dõi đối tượng.
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c9.ConnectedComponent(
                        frame_gray), use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
        if xulyanh == 'Count Rice':
            st.markdown("""
            ## Đếm hạt gạo (Count Rice)
            Xử lí CountRice được sử dụng để đếm số hạt gạo trong ảnh nhị phân. Nó hoạt động bằng cách áp dụng một loạt các hoạt động hình thái và xử lý ngưỡng để tách các hạt gạo khỏi nền ảnh sau đó đếm số lượng các thành phần liên thông trong ảnh nhị phân.
            """, unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                uploaded_file = st.file_uploader(
                    "Upload a image",
                    type=["jpg", "jpeg", "png"],
                    help="Scanned file are not supported yet!")
                execute = st.button('Hiển thị xử lí ảnh', type='primary')
                remove = st.button('Xoá bộ nhớ')
            if uploaded_file is not None:
                col2.image(uploaded_file, use_column_width=True,
                           caption='Input')
                if execute:
                    image = Image.open(uploaded_file)
                    frame = np.array(image)
                    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                    col2.image(c9.CountRice(
                        frame_gray), use_column_width=True, caption='Output')
                if remove:
                    clear_uploaded_files(session_state)
                    st.experimental_rerun()
