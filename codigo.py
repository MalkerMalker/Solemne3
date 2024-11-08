import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://www.wallpaperbetter.com/wallpaper/806/22/557/league-of-legends-landscape-magic-hd-1080P-wallpaper.jpg")
background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.image("imagenes/letras.png")
st.sidebar.image("imagenes/logo.png")
st.title("League Of Legends")
st.write(".")
