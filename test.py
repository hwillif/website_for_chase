import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image
from PIL import ImageEnhance

img = 'IMG_8252.jpg'
img = Image.open(img)
enh = ImageEnhance.Contrast(img)
enh = enh.enhance(7)
enh = ImageEnhance.Sharpness(enh)
enh = enh.enhance(1.5)
enh = ImageEnhance.Color(enh)
enh = enh.enhance(10)
Rotated_image = enh.rotate(270)

dry = 'fart-83471.mp3'
wet = 'fart-9-228245.mp3'
spicy = 'fart-8-228244.mp3'

fart = st.selectbox("What kind of fart do you want?",('No Fart :/ I am lame','Dry', "Wet", "Spicy"))
if fart == "Wet":
    st.audio(wet,loop=True,autoplay=True)
if fart == "Dry":
    st.audio(dry,loop=True,autoplay=True)
if fart == "Spicy":
    st.audio(spicy,loop=True,autoplay=True)

st.write("This is Winston")
st.image(Rotated_image)
