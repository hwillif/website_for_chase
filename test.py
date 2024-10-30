import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

img = Image.open(img)
Rotated_image = img.rotate(270)

st.write("This is my website")
st.audio('fart-9-228245.mp3')
st.image(Rotated_image)
