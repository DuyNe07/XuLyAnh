import streamlit as st
import time
import os
import subprocess
import shutil


def handwriting_streamlit_show():
    result_path = ".\\Module\\Handwriting\\data\\result\\"
    classes_path = ".\\Module\\Handwriting\\data\\words_alpha.txt"
    st.title("Nhận dạng chữ viết tay")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
                #### Mô tả
                Phần này được training bằng thư viện OpenCV và scikit-learn giúp nhận dạng chữ được viết bằng tay. Cho phép nhận dạng bằng cách truyền file vào và điều chỉnh các thông số nhận dạng.
                """
        )
    with col2:
        st.markdown(
            """
                #### Model được sử dụng
                📌detector.onnx (Tự training)

                📌reader.onnx (Tự training)
                """
        )
    st.divider()

    # Upload file
    uploaded_file = st.file_uploader(
        "Upload a JPG, JPEG, PNG file",
        type=["jpg", "jpeg", "png"],
        help="Scanned file are not supported yet!",
    )

    if not uploaded_file:
        st.stop()

    # Xử lý khi đã upload file
    if uploaded_file is not None:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.progress(100)
        if "image" in uploaded_file.type:
            st.image(uploaded_file)
            dest_path = result_path+uploaded_file.name
            os.makedirs(result_path, exist_ok=True)
            with open(dest_path, "wb") as dest_file:
                dest_file.write(uploaded_file.read())

            scale = st.slider("Điều chỉnh Scale: ", 0.0, 10.0,
                              step=0.01, value=0.4, key="scale")
            margin = st.slider("Điều chỉnh margin: ", 0, 25,
                               step=1, value=1, key="margin")
            method = st.checkbox(
                "Mặc định: best_path (Tick để dùng Word beam search)")
            min_words_per_line = st.slider(
                "Số từ tối thiểu trên mỗi dòng: ", 1, 10, step=1, value=5, key="min_words_per_line")
            text_scale = st.slider(
                "Text size in visualization: ", 0.5, 2.0, step=0.01, value=1.0, key="text_scale")

            scale = str(scale)
            margin = str(margin)
            method = str(method)
            min_words_per_line = str(min_words_per_line)
            text_scale = str(text_scale)

            with st.status("Regconize HandWriting Start!", expanded=True) as status:
                st.write("Loading Picture File: " + uploaded_file.name)
                time.sleep(0.5)
                st.write("Start detect handwriting")
                time.sleep(0.5)
                st.write("Finished Detection!")
                st.write("Start regconize handwriting")
                result = subprocess.run(["python", "./Module/Handwriting/detect.py", "--image", dest_path, "--scale", scale, "--margin", margin,
                                        "--method", method, "--min_words_per_line", min_words_per_line, "--text_scale", text_scale,
                                         "--output", result_path, "--classes", classes_path], stdout=subprocess.PIPE, text=True)
                st.write("Finished Regconization!")
                status.update(label="Successfully! Picture is available!",
                              state="complete", expanded=False)
            result_string = result.stdout
            print(result_string)
            st.image(result_path + "output_image.jpg")
            st.text_area("Kết quả nhận dạng:", result_string)

            bt2 = st.button("Xóa bộ nhớ", type="primary")
            if bt2:
                if os.path.exists(result_path):
                    shutil.rmtree(result_path)
