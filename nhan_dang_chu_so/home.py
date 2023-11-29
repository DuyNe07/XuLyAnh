import streamlit as st
import tensorflow as tf
from tensorflow.keras import datasets
from tensorflow.keras.models import model_from_json
import numpy as np
import random
import cv2


def tao_anh_ngau_nhien():
    image = np.zeros((10*28, 10*28), np.uint8)
    data = np.zeros((100, 28, 28, 1), np.uint8)

    for i in range(0, 100):
        n = random.randint(0, 9999)
        sample = st.session_state.X_test[n]
        data[i] = st.session_state.X_test[n]
        x = i // 10
        y = i % 10
        image[x*28:(x+1)*28, y*28:(y+1)*28] = sample[:, :, 0]
    return image, data


if 'is_load' not in st.session_state:
    # load model
    model_architecture = r'nhan_dang_chu_so/digit_config.json'
    model_weights = r'nhan_dang_chu_so/digit_weight.h5'
    model = model_from_json(open(model_architecture).read())
    model.load_weights(model_weights)

    OPTIMIZER = tf.keras.optimizers.Adam()
    model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER,
                  metrics=["accuracy"])
    st.session_state.model = model

    # load data
    (_, _), (X_test, y_test) = datasets.mnist.load_data()
    X_test = X_test.reshape((10000, 28, 28, 1))
    st.session_state.X_test = X_test

    st.session_state.is_load = True


def runChuViet():
    if st.button('Tạo ảnh'):
        image, data = tao_anh_ngau_nhien()
        st.session_state.image = image
        st.session_state.data = data

    if 'image' in st.session_state:
        image = st.session_state.image
        st.image(image)

        if st.button('Nhận dạng'):
            data = st.session_state.data
            data = data/255.0
            data = data.astype('float32')
            ket_qua = st.session_state.model.predict(data)
            dem = 0
            s = ''
            for x in ket_qua:
                s = s + '%d ' % (np.argmax(x))
                dem = dem + 1
                if (dem % 10 == 0) and (dem < 100):
                    s = s + '\n'
            st.text(s)
