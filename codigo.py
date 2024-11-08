import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

[theme] backgroundColor = "#F0F0F0"
st.image("imagenes/letras.png")
st.sidebar.image("imagenes/logo.png")
st.title("League Of Legends")
st.write(".")
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.wallpaperbetter.com/wallpaper/806/22/557/league-of-legends-landscape-magic-hd-1080P-wallpaper.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)
