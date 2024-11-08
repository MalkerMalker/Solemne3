import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ruta de tu imagen de fondo
bg_image_path = "imagenes/fondo.jpg"
bg_image_base64 = get_base64_of_bin_file(bg_image_path)

# CSS para el fondo
page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
    }}
</style>
"""

# Insertar CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

st.image("imagenes/letras.png")
st.sidebar.image("imagenes/logo.png")
st.title("League Of Legends")
st.write(".")
