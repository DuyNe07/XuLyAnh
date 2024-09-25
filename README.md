# Image Processing Personal Project

This project revolves around using computer vision models to recognize basic objects:

-   [Image Processing Personal Project](#image-processing-personal-project)
    -   [Project content](#project-content)
        -   [1. Face recognition](#1-face-recognition)
        -   [2. Object recognition](#2-object-recognition)
        -   [3. Fruit recognition](#3-fruit-recognition)
        -   [4. Age and gender recognition](#4-age-and-gender-recognition)
        -   [5. Helmet recognition](#5-helmet-recognition)
        -   [6. Playing card recognition](#6-playing-card-recognition)
        -   [7. Cheating detection](#7-cheating-detection)
    -   [Running project](#running-project)

<br>

![Tensorflow](https://img.shields.io/badge/Tensorflow-2.17.0-orange?style=flat&link=https%3A%2F%2Fwww.tensorflow.org%2Finstall%2Fpip%3Fhl%3Dvi)
![Python](https://img.shields.io/badge/Python-3.9-lightblue?style=flat&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-390%2F)
![OpenCV](https://img.shields.io/badge/OpenCV-4.10-green?style=flat&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-390%2F)
![Keras](https://img.shields.io/badge/Keras-3.5.0-red?style=flat&link=https%3A%2F%2Fkeras.io%2Fapi%2Fapplications%2F)

## Project content

### 1. Face recognition

The face recognition part uses 2 models yunet_2023mar.onnx and sface_2021dec.onnx to scan the face with the entered name, perform training and recognize it with the camera as well as transmit images for recognition

### 2. Object recognition

This module implements an object recognition application using the YOLOv4 model. The object recognition part uses the DNN module in the OpenCV library, which contains functions and classes related to Deep Neural Networks (DNN), which supports the deployment and use of deep learning models in image and video processing. Then use this module to read a YOLO v4 object recognition model from the images passed in

### 3. Fruit recognition

The 5-fruit recognition module implements an object recognition system based on the ONNX model. I have retrained this model with 5 fruits: Apple, Banana, Pineapple, Strawberry, Watermelon, then exported it as an onnx file and used the OpenCV and ONNX Runtime libraries to predict on the input image and identify the type of fruit.

### 4. Age and gender recognition

This module is built based on caffemodel extended from the OpenCV library. First, we will use OpenCV to detect the face, then use caffemodel to identify the age and gender of the subject through the webcam as well as the transmitted image

### 5. Helmet recognition

This model is trained on a custom dataset using the OpenCV library for image analysis and scikit-learn. It allows to detect helmets in the transmitted images.

### 6. Playing card recognition

This model is trained on a custom dataset of 53 playing cards using the OpenCV library for image analysis and scikit-learn. It allows to detect different types of cards when transmitting images

### 7. Cheating detection

This model is trained with cheating cases, including unusual actions and gestures during exams (eg: turning back, bowing head under the table, ...) to identify that there is a cheating case taking place. Next, use this trained model to identify cheating in exams using the transmitted image or video

## Running project

I run this project in Conda environment to easily manage my packages. Before running, you should activate your conda environment first

Install the required packages
`pip install -r requirements.txt`

Run the model
`streamlit run final.py`

When loading images for recognition, you should add the images to the `/input` directory of the root directory
