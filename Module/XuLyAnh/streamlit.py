import Module.XuLyAnh.Chapter09 as c9
import Module.XuLyAnh.Chapter05 as c5
import Module.XuLyAnh.Chapter04 as c4
import Module.XuLyAnh.Chapter03 as c3
import streamlit as st
import time
import os
import cv2
import numpy as np
import shutil


# cái nào không dùng xóa đi


def Chuong3():
    st.markdown('''<h2 class="title">
                Chương 3: Biến đổi độ sáng và lọc trong không gian
                </h2>
                ''', unsafe_allow_html=True)
    # File ảnh
    path = ".\\Module\\XuLyAnhSo\\img\\chuong3\\"

    # Làm âm ảnh (Negative)
    st.markdown('''<h2 class="subheader-text">
                3.1/ Làm âm ảnh (Negative)
                </h2>
                ''', unsafe_allow_html=True)
    bt3_1, bt3_1_delete = st.columns(2)
    bt3_1_state = bt3_1.button("Xử lý làm âm ảnh", type="primary")
    if bt3_1_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_1.tif", use_column_width=True)
        img = cv2.imread(path+"3_1.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.Negative(img), use_column_width=True)
        bt3_1_delete_state = bt3_1_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_1.tif")

    # Logarit ảnh
    st.markdown('''<h2 class="subheader-text">
                3.2/ Logarit ảnh
                </h2>
                ''', unsafe_allow_html=True)
    bt3_2, bt3_2_delete = st.columns(2)
    bt3_2_state = bt3_2.button("Xử lý logarit ảnh", type="primary")
    if bt3_2_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_2.tif", use_column_width=True)
        img = cv2.imread(path+"3_2.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.Logarit(img), use_column_width=True)
        bt3_2_delete_state = bt3_2_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_2.tif")

    # Lũy thừa ảnh
    st.markdown('''<h2 class="subheader-text">
                3.3/ Lũy thừa ảnh
                </h2>
                ''', unsafe_allow_html=True)
    bt3_3, bt3_3_delete = st.columns(2)
    bt3_3_state = bt3_3.button("Xử lý Lũy thừa ảnh", type="primary")
    if bt3_3_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_3.tif", use_column_width=True)
        img = cv2.imread(path+"3_3.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.Power(img), use_column_width=True)
        bt3_3_delete_state = bt3_3_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_3.tif")

    # Biến đổi tuyến tính từng phần
    st.markdown('''<h2 class="subheader-text">
                3.4/ Biến đổi tuyến tính từng phần
                </h2>
                ''', unsafe_allow_html=True)
    bt3_4, bt3_4_delete = st.columns(2)
    bt3_4_state = bt3_4.button(
        "Xử lý biến đổi tuyến tính từng phần", type="primary")
    if bt3_4_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_4.jpg", use_column_width=True)
        img = cv2.imread(path+"3_4.jpg", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.PiecewiseLinear(img), use_column_width=True)
        bt3_4_delete_state = bt3_4_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_4.jpg")

    # Histogram
    st.markdown('''<h2 class="subheader-text">
                3.5/ Histogram
                </h2>
                ''', unsafe_allow_html=True)
    bt3_5, bt3_5_delete = st.columns(2)
    bt3_5_state = bt3_5.button("Xử lý Histogram", type="primary")
    if bt3_5_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_5.tif", use_column_width=True)
        img = cv2.imread(path+"3_5.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.Histogram(img), use_column_width=True)
        bt3_5_delete_state = bt3_5_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_5.tif")

    # Cân bằng Histogram
    st.markdown('''<h2 class="subheader-text">
                3.6/ Cân bằng Histogram
                </h2>
                ''', unsafe_allow_html=True)
    bt3_6, bt3_6_delete = st.columns(2)
    bt3_6_state = bt3_6.button("Xử lý Cân bằng Histogram", type="primary")
    if bt3_6_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_6.jpg", use_column_width=True)
        img = cv2.imread(path+"3_6.jpg", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.HistEqual(img), use_column_width=True)
        bt3_6_delete_state = bt3_6_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_6.jpg")

    # Cân bằng Histogram của ảnh màu
    st.markdown('''<h2 class="subheader-text">
                3.7/ Cân bằng Histogram của ảnh màu
                </h2>
                ''', unsafe_allow_html=True)
    bt3_7, bt3_7_delete = st.columns(2)
    bt3_7_state = bt3_7.button(
        "Xử lý Cân bằng Histogram của ảnh màu", type="primary")
    if bt3_7_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_7.tif", use_column_width=True)
        img = cv2.imread(path+"3_7.tif", cv2.IMREAD_COLOR)
        cot2.image(c3.HistEqualColor(img), use_column_width=True)
        bt3_7_delete_state = bt3_7_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_7.tif")

    # Local Histogram
    st.markdown('''<h2 class="subheader-text">
                3.8/ Local Histogram
                </h2>
                ''', unsafe_allow_html=True)
    bt3_8, bt3_8_delete = st.columns(2)
    bt3_8_state = bt3_8.button("Xử lý Local Histogram", type="primary")
    if bt3_8_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_8.tif", use_column_width=True)
        img = cv2.imread(path+"3_8.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.LocalHist(img), use_column_width=True)
        bt3_8_delete_state = bt3_8_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_8.tif")

    # Thống kê histogram
    st.markdown('''<h2 class="subheader-text">
                3.9/ Thống kê histogram
                </h2>
                ''', unsafe_allow_html=True)
    bt3_9, bt3_9_delete = st.columns(2)
    bt3_9_state = bt3_9.button("Xử lý Thống kê histogram", type="primary")
    if bt3_9_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_9.tif", use_column_width=True)
        img = cv2.imread(path+"3_9.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.HistStat(img), use_column_width=True)
        bt3_9_delete_state = bt3_9_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_9.tif")

    # Lọc box
    st.markdown('''<h2 class="subheader-text">
                3.10/ Lọc box
                </h2>
                ''', unsafe_allow_html=True)
    bt3_10, bt3_10_delete = st.columns(2)
    bt3_10_state = bt3_10.button("Xử lý Lọc box", type="primary")
    if bt3_10_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_10.tif", use_column_width=True)
        img = cv2.imread(path+"3_10.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(cv2.blur(img, (21, 21)), use_column_width=True)
        bt3_10_delete_state = bt3_10_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_10.tif")

    # Lọc Gauss
    st.markdown('''<h2 class="subheader-text">
                3.11/ Lọc Gauss
                </h2>
                ''', unsafe_allow_html=True)
    bt3_11, bt3_11_delete = st.columns(2)
    bt3_11_state = bt3_11.button("Xử lý Lọc Gauss", type="primary")
    if bt3_11_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_11.tif", use_column_width=True)
        img = cv2.imread(path+"3_11.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(cv2.GaussianBlur(img, (43, 43), 7.0), use_column_width=True)
        bt3_11_delete_state = bt3_11_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_11.tif")

    # Phân ngưỡng
    st.markdown('''<h2 class="subheader-text">
                3.12/ Phân ngưỡng
                </h2>
                ''', unsafe_allow_html=True)
    bt3_12, bt3_12_delete = st.columns(2)
    bt3_12_state = bt3_12.button("Xử lý Phân ngưỡng", type="primary")
    if bt3_12_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_12.tif", use_column_width=True)
        img = cv2.imread(path+"3_12.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.Threshold(img), use_column_width=True)
        bt3_12_delete_state = bt3_12_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_12.tif")

    # Lọc median
    st.markdown('''<h2 class="subheader-text">
                3.13.1/ Lọc median
                </h2>
                ''', unsafe_allow_html=True)
    bt3_13_1, bt3_13_1_delete = st.columns(2)
    bt3_13_1_state = bt3_13_1.button("Xử lý Lọc median", type="primary")
    if bt3_13_1_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_13_1.tif", use_column_width=True)
        img = cv2.imread(path+"3_13_1.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.MedianFilter(img), use_column_width=True)
        bt3_13_1_delete_state = bt3_13_1_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_13_1.tif")

    # Sharpen
    st.markdown('''<h2 class="subheader-text">
                3.13.2/ Sharpen
                </h2>
                ''', unsafe_allow_html=True)
    bt3_13_2, bt3_13_2_delete = st.columns(2)
    bt3_13_2_state = bt3_13_2.button("Xử lý Sharpen", type="primary")
    if bt3_13_2_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_13_2.tif", use_column_width=True)
        img = cv2.imread(path+"3_13_2.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.Sharpen(img), use_column_width=True)
        bt3_13_2_delete_state = bt3_13_2_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_13_2.tif")

    # Gradient
    st.markdown('''<h2 class="subheader-text">
                3.13.3/ Gradient
                </h2>
                ''', unsafe_allow_html=True)
    bt3_13_3, bt3_13_3_delete = st.columns(2)
    bt3_13_3_state = bt3_13_3.button("Xử lý Gradient", type="primary")
    if bt3_13_3_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"3_13_3.tif", use_column_width=True)
        img = cv2.imread(path+"3_13_3.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c3.Gradient(img), use_column_width=True)
        bt3_13_3_delete_state = bt3_13_3_delete.button("Xóa", type="primary")
    else:
        st.image(path+"3_13_3.tif")


def Chuong4():
    st.markdown('''<h2 class="title">
                Chương 4: Lọc trong miền tần số
                </h2>
                ''', unsafe_allow_html=True)
    # File ảnh
    path = ".\\Module\\XuLyAnh\\img\\chuong4\\"

    # Spectrum
    st.markdown('''<h2 class="subheader-text">
                4.1/ Spectrum
                </h2>
                ''', unsafe_allow_html=True)
    bt4_1, bt4_1_delete = st.columns(2)
    bt4_1_state = bt4_1.button("Xử lý Spectrum", type="primary")
    if bt4_1_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"4_1.tif", use_column_width=True)
        img = cv2.imread(path+"4_1.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c4.Spectrum(img), use_column_width=True)
        bt4_1_delete_state = bt4_1_delete.button("Xóa", type="primary")
    else:
        st.image(path+"4_1.tif")

    # Lọc trong miền tần số - highpass filter
    st.markdown('''<h2 class="subheader-text">
                4.2/ Lọc trong miền tần số - highpass filter
                </h2>
                ''', unsafe_allow_html=True)
    bt4_2, bt4_2_delete = st.columns(2)
    bt4_2_state = bt4_2.button(
        "Xử lý Lọc trong miền tần số - highpass filter", type="primary")
    if bt4_2_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"4_2.tif", use_column_width=True)
        img = cv2.imread(path+"4_2.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c4.FrequencyFilter(img), use_column_width=True)
        bt4_2_delete_state = bt4_2_delete.button("Xóa", type="primary")
    else:
        st.image(path+"4_2.tif")

    # Vẽ bộ lọc Notch Reject
    st.markdown('''<h2 class="subheader-text">
                4.3.1/ Vẽ bộ lọc Notch Reject
                </h2>
                ''', unsafe_allow_html=True)
    bt4_3_1, bt4_3_1_delete = st.columns(2)
    bt4_3_1_state = bt4_3_1.button(
        "Xử lý Vẽ bộ lọc Notch Reject", type="primary")
    if bt4_3_1_state:
        st.image(c4.DrawNotchRejectFilter())
        bt4_3_1_delete.button("Xóa", type="primary")

    # Xóa nhiễu moire
    st.markdown('''<h2 class="subheader-text">
                4.3.2/ Xóa nhiễu moire
                </h2>
                ''', unsafe_allow_html=True)
    bt4_3_2, bt4_3_2_delete = st.columns(2)
    bt4_3_2_state = bt4_3_2.button("Xử lý Xóa nhiễu moire", type="primary")
    if bt4_3_2_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"4_3_2.tif", use_column_width=True)
        img = cv2.imread(path+"4_3_2.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c4.RemoveMoire(img), use_column_width=True)
        bt4_3_2_delete_state = bt4_3_2_delete.button("Xóa", type="primary")
    else:
        st.image(path+"4_3_2.tif")


def Chuong5():
    st.markdown('''<h2 class="title">
                Chương 5: Khôi phục ảnh
                </h2>
                ''', unsafe_allow_html=True)
    # File ảnh
    path = ".\\Module\\XuLyAnh\\img\\chuong5\\"

    # Tạo nhiễu chuyển động
    st.markdown('''<h2 class="subheader-text">
                5.1/ Tạo nhiễu chuyển động
                </h2>
                ''', unsafe_allow_html=True)
    bt5_1, bt5_1_delete = st.columns(2)
    bt5_1_state = bt5_1.button("Xử lý Tạo nhiễu chuyển động", type="primary")
    if bt5_1_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"5_1.tif", use_column_width=True)
        img = cv2.imread(path+"5_1.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c5.CreateMotionNoise(img), use_column_width=True)
        bt5_1_delete_state = bt5_1_delete.button("Xóa", type="primary")
    else:
        st.image(path+"5_1.tif")

    # Gỡ nhiễu của ảnh có ít nhiễu
    st.markdown('''<h2 class="subheader-text">
                5.2/ Gỡ nhiễu của ảnh có ít nhiễu
                </h2>
                ''', unsafe_allow_html=True)
    bt5_2, bt5_2_delete = st.columns(2)
    bt5_2_state = bt5_2.button(
        "Xử lý Gỡ nhiễu của ảnh có ít nhiễu", type="primary")
    if bt5_2_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"5_2.tif", use_column_width=True)
        img = cv2.imread(path+"5_2.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c5.DenoiseMotion(img), use_column_width=True)
        bt5_2_delete_state = bt5_2_delete.button("Xóa", type="primary")
    else:
        st.image(path+"5_2.tif")

    # Gỡ nhiễu của ảnh có nhiều nhiễu
    st.markdown('''<h2 class="subheader-text">
                5.3/ Gỡ nhiễu của ảnh có nhiều nhiễu
                </h2>
                ''', unsafe_allow_html=True)
    bt5_3, bt5_3_delete = st.columns(2)
    bt5_3_state = bt5_3.button(
        "Xử lý Gỡ nhiễu của ảnh có nhiều nhiễu", type="primary")
    if bt5_3_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"5_3.tif", use_column_width=True)
        img = cv2.imread(path+"5_3.tif", cv2.IMREAD_GRAYSCALE)
        temp = cv2.medianBlur(img, 7)
        cot2.image(c5.DenoiseMotion(temp), use_column_width=True)
        bt5_3_delete_state = bt5_3_delete.button("Xóa", type="primary")
    else:
        st.image(path+"5_3.tif")


def Chuong9():
    st.markdown('''<h2 class="title">
                Chương 9: Xử lý ảnh hình thái
                </h2>
                ''', unsafe_allow_html=True)
    # File ảnh
    path = ".\\Module\\XuLyAnh\\img\\chuong9\\"

    # Đếm thành phần liên thông của miếng phi lê gà (Connected Component)
    st.markdown('''<h2 class="subheader-text">
                9.1/ Đếm thành phần liên thông của miếng phi lê gà (Connected Component)
                </h2>
                ''', unsafe_allow_html=True)
    bt9_1, bt9_1_delete = st.columns(2)
    bt9_1_state = bt9_1.button("Xử lý Connected Component", type="primary")
    if bt9_1_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"9_1.tif", use_column_width=True)
        img = cv2.imread(path+"9_1.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c9.ConnectedComponent(img), use_column_width=True)
        bt9_1_delete_state = bt9_1_delete.button("Xóa", type="primary")
    else:
        st.image(path+"9_1.tif")

    # Đếm hạt gạo (Count Rice)
    st.markdown('''<h2 class="subheader-text">
                9.2/ Đếm hạt gạo (Count Rice)
                </h2>
                ''', unsafe_allow_html=True)
    bt9_2, bt9_2_delete = st.columns(2)
    bt9_2_state = bt9_2.button("Xử lý Count Rice", type="primary")
    if bt9_2_state:
        cot1, cot2 = st.columns(2)
        cot1.image(path+"9_2.tif", use_column_width=True)
        img = cv2.imread(path+"9_2.tif", cv2.IMREAD_GRAYSCALE)
        cot2.image(c9.CountRice(img), use_column_width=True)
        bt9_2_delete_state = bt9_2_delete.button("Xóa", type="primary")
    else:
        st.image(path+"9_2.tif")


def runXuLyAnh():
    st.title("Xử lí ảnh số")
    col1, col2 = st.columns(2)
    with col1:
        chuong = st.selectbox(
            "Chọn chương", ('Chương 3', 'Chương 4', 'Chương 5', 'Chương 9'))
    with col2:
        if chuong == 'Chương 3':
            xulyanh = st.selectbox("Chọn phương pháp",
                                   ('Negative', 'Logarit ảnh', 'Lũy thừa ảnh', 'Biến đổi tuyến tính từng phần', 'Histogram', 'Cân bằng Histogram', 'Cân bằng Histogram của ảnh màu', 'Local Histogram', 'Thống kê histogram', 'Lọc box', 'Lọc Gauss', 'Phân ngưỡng', 'Lọc median', 'Sharpen', 'Gradient'))
