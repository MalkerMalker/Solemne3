import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64

# Ruta de tu imagen de fondo
bg_image = "imagenes/fondo.jpg"

# CSS para el fondo
page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
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
