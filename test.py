import altair as alt
import pandas as pd
import streamlit as st

import cv2  # importing cv 
import imutils 
    
# read an image as input using OpenCV 
image = cv2.imread(r'IMG_8252.jpg') 
  
Rotated_image = imutils.rotate(image, angle=0)

st.write("This is my website")
st.audio('fart-9-228245.mp3')
st.image(Rotated_image)
