import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image

img = 'IMG_8252.jpg'
img = Image.open(img)
Rotated_image = img.rotate(270)

dry = 'fart-83471.mp3'
wet = 'fart-9-228245.mp3'
spicy = 'fart-8-228244.mp3'

fart = st.selectbox("What kind of fart do you want?",('Dry', "Wet", "Spicy"))
if fart == "Wet":
    st.audio(wet)
if fart == "Dry":
    st.audio(dry)
if fart == "Spicy":
    st.audio(spicy)

st.write("This is Winston")
st.image(Rotated_image)
