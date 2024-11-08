import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Ruta a la imagen local
image_path = "imagenes/fondo.jpg"

# Usar st.markdown para insertar el estilo CSS y establecer la imagen de fondo
st.markdown(
    f"""
    <style>
    body {{
        background: url("{image_path}");
        background-size: cover;  /* Hace que la imagen cubra toda la pantalla */
        background-position: center;  /* Centra la imagen */
        background-attachment: fixed;  /* Mantiene el fondo fijo mientras haces scroll */
    }}
    .reportview-container {{
        background: transparent;  /* Asegura que no haya un fondo blanco en el contenedor */
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.image("imagenes/letras.png")
st.sidebar.image("imagenes/logo.png")
st.title("League Of Legends")
st.write(".")
