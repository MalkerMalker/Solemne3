import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import base64

st.markdown("""
<iframe width="0" height="0" 
    src="https://www.youtube.com/embed/aR-KAldshAE?autoplay=1&loop=1&playlist=aR-KAldshAE" 
    frameborder="0" 
    allow="autoplay" 
    style="display:none;">
</iframe>
""", unsafe_allow_html=True)


#base de datos pandas en informacion
dfinf = pd.read_csv("backloggd_games.csv")
def convertir_k(valor):
    if isinstance(valor, str) and "K" in valor:
        return float(valor.replace("K", "")) * 1000
    else:
        return float(valor)
dfinf["Playing"] = dfinf["Playing"].apply(convertir_k)
dfinf = dfinf.sort_values("Playing", ascending=False)
dfinf['highlight'] = dfinf['Title'].apply(lambda x: 'highlight' if x == 'League of Legends' else 'normal')
dfinf = dfinf.head(30)


#fondo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image_path = "imagenes/fondo.jpg"
bg_image_base64 = get_base64_of_bin_file(bg_image_path)

page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image_base64}");
        background-size: cover;
        background-position: center;  /* Centra la imagen */
    }}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.image('imagenes/logo.png', use_column_width=True)
st.image('imagenes/letras.png', use_column_width=True)

opcion = st.sidebar.selectbox('Selecciona una sección', ['Información', 'Campeones', 'Competitivo', 'Acerca de'])

if opcion == 'Información':
    #TITULO
    st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: white;">Información</h1>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    #QUE ES LEAGUE OF LEGENDS?
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
    <h3 style="color: white;">¿Qué es League of Legends?</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>League of Legends (también conocido por sus siglas LoL) es un videojuego multijugador de arena de batalla en línea desarrollado y publicado por Riot Games. Inspirándose en Defense of the Ancients, un mapa personalizado para Warcraft III, los fundadores de Riot buscaron desarrollar un juego independiente del mismo género. Desde su lanzamiento en octubre de 2009, LoL ha sido un juego gratuito y se monetiza a través de la compra de elementos para la personalización de personajes y otros accesorios. El juego está disponible para Microsoft Windows y macOS.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image('imagenes/informacionuno.jpg', use_column_width=True)
    
    #DESTRUYE EL NEXO DEL ENEMIGO
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Destruye el nexo del enemigo</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>El nexo es el corazón de las bases de ambos equipos los cuales no permitiran tan facil que los destruyas. Abrete paso entre los enemigos y destruye su nexo ganar la partida.</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("imagenes/nexoazul.jpg", caption="Los súbditos se generan en tu nexo. Detrás del nexo se encuentra la fuente, donde podrás recuperar vida y maná con rapidez y acceder a la tienda.")
    with col2:
        st.image("imagenes/nexorojo.jpg", caption="El nexo enemigo, que se encuentra en la base del equipo contrario, es igual que el de tu equipo. Si acabas con él, ganarás la partida.")
        
    #Abrete paso
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Abrete paso</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Para llegar hasta el nexo enemigo, tu equipo tendrá que avanzar por al menos una calle. Hay estructuras defensivas que bloquean tu avance: las torretas y los inhibidores. Cada calle cuenta con tres torretas y un inhibidor. Además, cada nexo tiene dos torretas adicionales.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image('imagenes/torretainhibidores.jpg', use_column_width=True)
    
    #USA TUS HABILIDADES
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">Usa tus habilidades</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>Los campeones cuentan con cinco habilidades básicas y dos hechizos especiales, y pueden equiparse con un máximo de siete objetos. Para que tu equipo se alce con la victoria, tendrás que ir descubriendo cuál es el orden de habilidades, hechizos de invocador y la configuración de objetos óptimos para tu campeón.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image('imagenes/habilidadescast.gif',caption="Personaje disparando la primera habilidad", use_column_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("imagenes/eclipseinf.jpg", caption="Objeto ideal para comprar cuando eres luchador, te otorga escudo, daño a enemigos con mucha vida y reestablecimiento de habilidades.")
    with col2:
        st.image("imagenes/ludencompanioninf.jpg", caption="Objeto ideal para comprar cuando eres mago, te otorga daño magico dispersivo, maná y reestablecimiento de habilidades.")
        
    # VIDEO JUEGO CON MAS JUGADORES
    st.markdown(
    """
    <div style="margin-left: -75px; margin-right: -75px;">
        <h3 style="color: white;">De lo mas jugado...</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("""
    <div style="margin-left: -75px;">
    <div style="margin-right: -75px;">
    <div style="text-align: justify; text-justify: inter-word;">
        <p style='color: white;'>League of legends es un videojuego muy popular entre la cultura del videojuego, representado en la siguiente grafica sobre como ha sido uno de los mas jugados atraves del tiempo.</p>
    </div>
    """, unsafe_allow_html=True
    )

    chart = alt.Chart(dfinf).mark_bar().encode(
    x=alt.X("Playing", title="Jugadores activos"),
    y=alt.Y("Title", title="Juegos", sort=None),
    color=alt.Color('highlight:N', legend=None, scale=alt.Scale(domain=['normal', 'highlight'], range=['#cccccc', 'lightgreen']))
    ).properties(
    title="Número de Jugadores por Título",
    width=200,
    height=400
    )
    
    # Mostrar el gráfico en Streamlit
    st.altair_chart(chart, use_container_width=True)
    
elif opcion == 'Campeones':
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
    with col1:
        st.markdown("""
<a href="https://www.youtube.com/watch?v=aR-KAldshAE" target="_blank">
    <img src="imagenes/eclipseinf.jpg" alt="Imagen de fondo" style="width:100%; height:auto; cursor: pointer;">
</a>
""", unsafe_allow_html=True)
        #st.image("imagenes/eclipseinf.jpg")
    with col2:
        st.image("imagenes/ludencompanioninf.jpg")
    with col3:
        st.image("imagenes/eclipseinf.jpg")
    with col4:
        st.image("imagenes/ludencompanioninf.jpg")
    with col5:
        st.image("imagenes/eclipseinf.jpg")
    with col6:
        st.image("imagenes/ludencompanioninf.jpg")
    with col7:
        st.image("imagenes/eclipseinf.jpg")
    with col8:
        st.image("imagenes/ludencompanioninf.jpg")
    with col9:
        st.image("imagenes/eclipseinf.jpg")
    with col10:
        st.image("imagenes/ludencompanioninf.jpg")


elif opcion == 'Competitivo':
# Encabezado principal
    st.markdown(
    """
    <div style="text-align: center; margin-bottom: 15px;">
        <h1 style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 2em;">Acerca De</h1>
    </div>
    """,
    unsafe_allow_html=True
)

elif opcion == 'Acerca de':
# Sección de Integrantes
st.markdown(
    """
    <div style="margin-bottom: 10px;">
        <h3 style="color: #FFAD33; font-family: 'Trebuchet MS', sans-serif; font-size: 1.2em;">Integrantes</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Lista de Integrantes alineada a la izquierda
integrantes = ["Diego Abarca", "Cristobal Camousseight", "Rodrigo Manríquez"]
st.markdown("<div style='margin-left: 20px;'>", unsafe_allow_html=True)  # Contenedor para alineación izquierda
for integrante in integrantes:
    st.markdown(
        f"""
        <div style="margin: 3px 0;">
            <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 12px;">{integrante}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)

# Sección de Profesora justo debajo de los integrantes
st.markdown(
    """
    <div style="margin-top: 10px; margin-left: 20px;">
        <h3 style="color: #FFAD33; font-family: 'Trebuchet MS', sans-serif; font-size: 1.2em;">Profesora</h3>
        <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 12px;">Monica Otero Ferreiro</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Ingeniería Civil Informática alineada a la derecha
st.markdown(
    """
    <div style="text-align: right; margin-top: 20px; margin-right: 20px;">
        <h3 style="color: #FFAD33; font-family: 'Trebuchet MS', sans-serif; font-size: 1.2em;">Ing. Civil Informática</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Derechos reservados al centro
st.markdown(
    """
    <div style="text-align: center; margin-top: 15px;">
        <p style="color: #CCCCCC; font-family: 'Trebuchet MS', sans-serif; font-size: 12px;">USS - All rights reserved</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Nota adicional
st.markdown(
    """
    <div style="text-align: center; margin-top: 15px;">
        <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 12px;">League of Legends es un juego de Riot Games</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.image('imagenes/logo-original.png', use_column_width=True)












