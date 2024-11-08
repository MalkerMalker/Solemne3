import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('imagenes/fondo.png')



st.image("imagenes/letras.png")
st.sidebar.image("imagenes/logo.png")
st.title("League Of Legends")
st.write(".")
