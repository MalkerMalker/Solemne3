import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #000000;
    }
    </style>
    """, 
    unsafe_allow_html=True
)
st.title("Mi aplicación Streamlit")
st.write("Este es un ejemplo con fondo personalizado.")
