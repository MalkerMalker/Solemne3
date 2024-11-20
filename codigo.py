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

#base de datos campeones
dfchamp = pd.read_csv("LoL_champions.csv")


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

with st.sidebar:
    container = st.container()
    with container:
        st.image("logo.png", width=300)
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
    st.sidebar.title("Lista de campeones")
    mensaje = "Selecciona un campeón"
    with st.sidebar:    
        for img, title in [("imagenes/iconos/aatrox.jpg", "Aatrox"),
                           ("imagenes/iconos/ahri.jpg", "Ahri"),
                           ("imagenes/iconos/akali.jpg", "Akali"),
                           ("imagenes/iconos/akshan.jpg", "Akshan"),
                           ("imagenes/iconos/alistar.jpg", "Alistar"),
                           ("imagenes/iconos/ambessa.jpg", "Ambessa"),
                           ("imagenes/iconos/amumu.jpg", "Amumu"),
                           ("imagenes/iconos/anivia.jpg", "Anivia"),
                           ("imagenes/iconos/annie.jpg", "Annie"),
                           ("imagenes/iconos/aphelios.jpg", "Aphelios"),
                           ("imagenes/iconos/ashe.jpg", "Ashe"),
                           ("imagenes/iconos/aurelion.jpg", "Aurelion"),
                           ("imagenes/iconos/azir.jpg", "Azir"),
                           ("imagenes/iconos/bardo.jpg", "Bardo"),
                           ("imagenes/iconos/belvet.jpg", "Belvet"),
                           ("imagenes/iconos/blitzcrank.jpg", "Blitzcrank"),
                           ("imagenes/iconos/brand.jpg", "Brand"),
                           ("imagenes/iconos/braum.jpg", "Braum"),
                           ("imagenes/iconos/caitlyn.jpg", "Caitlyn"),
                           ("imagenes/iconos/camille.jpg", "Camille"),
                           ("imagenes/iconos/cassiopeia.jpg", "Cassiopeia"),
                           ("imagenes/iconos/chogath.jpg", "Chogath"),
                           ("imagenes/iconos/corki.jpg", "Corki"),
                           ("imagenes/iconos/darius.jpg", "Darius"),
                           ("imagenes/iconos/diana.jpg", "Diana"),
                           ("imagenes/iconos/draven.jpg", "Draven"),
                           ("imagenes/iconos/drmundo.jpg", "Dr. Mundo"),
                           ("imagenes/iconos/ekko.jpg", "Ekko"),
                           ("imagenes/iconos/elisse.jpg", "Elisse"),
                           ("imagenes/iconos/evelynn.jpg", "Evelynn"),
                           ("imagenes/iconos/ezreal.jpg", "Ezreal"),
                           ("imagenes/iconos/fiddlesticks.jpg", "Fiddlesticks"),
                           ("imagenes/iconos/fiora.jpg", "Fiora"),
                           ("imagenes/iconos/fizz.jpg", "Fizz"),
                           ("imagenes/iconos/galio.jpg", "Galio"),
                           ("imagenes/iconos/gangplank.jpg", "Gangplank"),
                           ("imagenes/iconos/garen.jpg", "Garen"),
                           ("imagenes/iconos/gnar.jpg", "Gnar"),
                           ("imagenes/iconos/gragas.jpg", "Gragas"),
                           ("imagenes/iconos/graves.jpg", "Graves"),
                           ("imagenes/iconos/gwen.jpg", "Gwen"),
                           ("imagenes/iconos/hecarim.jpg", "Hecarim"),
                           ("imagenes/iconos/heimerdinger.jpg", "Heimerdinger"),
                           ("imagenes/iconos/illaoi.jpg", "Illaoi"),
                           ("imagenes/iconos/irelia.jpg", "Irelia"),
                           ("imagenes/iconos/ivern.jpg", "Ivern"),
                           ("imagenes/iconos/janna.jpg", "Janna"),
                           ("imagenes/iconos/jarvan.jpg", "Jarvan"),
                           ("imagenes/iconos/jax.jpg", "Jax"),
                           ("imagenes/iconos/jayce.jpg", "Jayce"),
                           ("imagenes/iconos/jhin.jpg", "Jhin"),
                           ("imagenes/iconos/jinx.jpg", "Jinx"),
                           ("imagenes/iconos/kaisa.jpg", "Kaisa"),
                           ("imagenes/iconos/kalista.jpg", "Kalista"),
                           ("imagenes/iconos/karma.jpg", "Karma"),
                           ("imagenes/iconos/karthus.jpg", "Karthus"),
                           ("imagenes/iconos/kassadin.jpg", "Kassadin"),
                           ("imagenes/iconos/katarina.jpg", "Katarina"),
                           ("imagenes/iconos/kayle.jpg", "Kayle"),
                           ("imagenes/iconos/kayn.jpg", "Kayn"),
                           ("imagenes/iconos/kennen.jpg", "Kennen"),
                           ("imagenes/iconos/khazix.jpg", "Khazix"),
                           ("imagenes/iconos/kindred.jpg", "Kindred"),
                           ("imagenes/iconos/kled.jpg", "Kled"),
                           ("imagenes/iconos/kogmaw.jpg", "Kogmaw"),
                           ("imagenes/iconos/ksante.jpg", "Ksante"),
                           ("imagenes/iconos/leblanc.jpg", "Leblanc"),
                           ("imagenes/iconos/leesin.jpg", "Leesin"),
                           ("imagenes/iconos/leona.jpg", "Leona"),
                           ("imagenes/iconos/lillia.jpg", "Lillia"),
                           ("imagenes/iconos/lissandra.jpg", "Lissandra"),
                           ("imagenes/iconos/lucian.jpg", "Lucian"),
                           ("imagenes/iconos/lulu.jpg", "Lulu"),
                           ("imagenes/iconos/lux.jpg", "Lux"),
                           ("imagenes/iconos/malphite.jpg", "Malphite"),
                           ("imagenes/iconos/malzahar.jpg", "Malzahar"),
                           ("imagenes/iconos/maokai.jpg", "Maokai"),
                           ("imagenes/iconos/miss fortune.jpg", "Miss fortune"),
                           ("imagenes/iconos/mordekaiser.jpg", "Mordekaiser"),
                           ("imagenes/iconos/morgana.jpg", "Morgana"),
                           ("imagenes/iconos/nami.jpg", "Nami"),
                           ("imagenes/iconos/nasus.jpg", "Nasus"),
                           ("imagenes/iconos/nautilus.jpg", "Nautilus"),
                           ("imagenes/iconos/neeko.jpg", "Neeko"),
                           ("imagenes/iconos/nidalee.jpg", "Nidalee"),
                           ("imagenes/iconos/nilah.jpg", "Nilah"),
                           ("imagenes/iconos/nocturne.jpg", "Nocturne"),
                           ("imagenes/iconos/nunu.jpg", "Nunu"),
                           ("imagenes/iconos/olaf.jpg", "Olaf"),
                           ("imagenes/iconos/orianna.jpg", "Orianna"),
                           ("imagenes/iconos/ornn.jpg", "Ornn"),
                           ("imagenes/iconos/pantheon.jpg", "Pantheon"),
                           ("imagenes/iconos/poppy.jpg", "Poppy"),
                           ("imagenes/iconos/pyke.jpg", "Pyke"),
                           ("imagenes/iconos/qiyana.jpg", "Qiyana"),
                           ("imagenes/iconos/quinn.jpg", "Quinn"),
                           ("imagenes/iconos/rammus.jpg", "Rammus"),
                           ("imagenes/iconos/renataglasc.jpg", "Renataglasc"),
                           ("imagenes/iconos/renekton.jpg", "Renekton"),
                           ("imagenes/iconos/rengar.jpg", "Rengar"),
                           ("imagenes/iconos/riven.jpg", "Riven"),
                           ("imagenes/iconos/rumble.jpg", "Rumble"),
                           ("imagenes/iconos/ryze.jpg", "Ryze"),
                           ("imagenes/iconos/sejuani.jpg", "Sejuani"),
                           ("imagenes/iconos/senna.jpg", "Senna"),
                           ("imagenes/iconos/seraphine.jpg", "Seraphine"),
                           ("imagenes/iconos/sett.jpg", "Sett"),
                           ("imagenes/iconos/shaco.jpg", "Shaco"),
                           ("imagenes/iconos/shen.jpg", "Shen"),
                           ("imagenes/iconos/shyvana.jpg", "Shyvana"),
                           ("imagenes/iconos/singed.jpg", "Singed"),
                           ("imagenes/iconos/sion.jpg", "Sion"),
                           ("imagenes/iconos/sivir.jpg", "Sivir"),
                           ("imagenes/iconos/skarner.jpg", "Skarner"),
                           ("imagenes/iconos/sona.jpg", "Sona"),
                           ("imagenes/iconos/soraka.jpg", "Soraka"),
                           ("imagenes/iconos/swain.jpg", "Swain"),
                           ("imagenes/iconos/sylas.jpg", "Sylas"),
                           ("imagenes/iconos/syndra.jpg", "Syndra"),
                           ("imagenes/iconos/taliyah.jpg", "Taliyah"),
                           ("imagenes/iconos/talon.jpg", "Talon"),
                           ("imagenes/iconos/taric.jpg", "Taric"),
                           ("imagenes/iconos/teemo.jpg", "Teemo"),
                           ("imagenes/iconos/thresh.jpg", "Thresh"),
                           ("imagenes/iconos/tristana.jpg", "Tristana"),
                           ("imagenes/iconos/trundle.jpg", "Trundle"),
                           ("imagenes/iconos/tryndamere.jpg", "Tryndamere"),
                           ("imagenes/iconos/twistedfate.jpg", "Twistedfate"),
                           ("imagenes/iconos/twitch.jpg", "Twitch"),
                           ("imagenes/iconos/udyr.jpg", "Udyr"),
                           ("imagenes/iconos/urgot.jpg", "Urgot"),
                           ("imagenes/iconos/varus.jpg", "Varus"),
                           ("imagenes/iconos/vayne.jpg", "Vayne"),
                           ("imagenes/iconos/veigar.jpg", "Veigar"),
                           ("imagenes/iconos/velkoz.jpg", "Velkoz"),
                           ("imagenes/iconos/vex.jpg", "Vex"),
                           ("imagenes/iconos/vi.jpg", "Vi"),
                           ("imagenes/iconos/viego.jpg", "Viego"),
                           ("imagenes/iconos/viktor.jpg", "Viktor"),
                           ("imagenes/iconos/vladimir.jpg", "Vladimir"),
                           ("imagenes/iconos/volibear.jpg", "Volibear"),
                           ("imagenes/iconos/warwick.jpg", "Warwick"),
                           ("imagenes/iconos/wukong.jpg", "Wukong"),
                           ("imagenes/iconos/xerath.jpg", "Xerath"),
                           ("imagenes/iconos/xinzhao.jpg", "Xinzhao"),
                           ("imagenes/iconos/yasuo.jpg", "Yasuo"),
                           ("imagenes/iconos/yi.jpg", "Yi"),
                           ("imagenes/iconos/yone.jpg", "Yone"),
                           ("imagenes/iconos/yuumi.jpg", "Yuumi"),
                           ("imagenes/iconos/zac.jpg", "Zac"),
                           ("imagenes/iconos/zed.jpg", "Zed"),
                           ("imagenes/iconos/zeri.jpg", "Zeri"),
                           ("imagenes/iconos/ziggs.jpg", "Ziggs"),
                           ("imagenes/iconos/zilean.jpg", "Zilean"),
                           ("imagenes/iconos/zoe.jpg", "Zoe"),
                           ("imagenes/iconos/zyra.jpg", "Zyra")]:
            col1, col2 = st.columns([1, 1]) 
            with col1:
                st.image(img, width=60) 
            with col2:
                if st.button(title): 
                    mensaje = title
    if title :
        
        fila = dfchamp[dfchamp["Name"] == mensaje]
        informacion = dfchamp.loc[dfchamp["Name"] == mensaje, "Informacion"].values[0]
        
        tags = dfchamp.loc[dfchamp["Name"] == mensaje, "Tags"].values[0]
        tags_split = tags.split(",") 
        tag1 = tags_split[0] if len(tags_split) > 0 else None
        tag2 = tags_split[1] if len(tags_split) > 1 else None
        tagtexto2 = ""
        if tag1 == "Fighter":
            tagimagen = "imagenes/assets/peleador.png"
            tagtexto = "Peleador"
        elif tag1 == "Assassin":
            tagimagen = "imagenes/assets/asesino.png"
            tagtexto = "Asesino"
        elif tag1 == "Mage":
            tagimagen = "imagenes/assets/mago.png"
            tagtexto = "Mago"
        elif tag1 == "Tank":
            tagimagen = "imagenes/assets/tanque.png"
            tagtexto = "Tanque"
        elif tag1 == "Support":
            tagimagen = "imagenes/assets/support.png"
            tagtexto = "Soporte"
        elif tag1 == "Marksman":
            tagimagen = "imagenes/assets/adcarry.png"
            tagtexto = "Tirador"
        if tag2 == "Fighter":
            tagimagen2 = "imagenes/assets/peleador.png"
            tagtexto2 = "Peleador"
        elif tag2 == "Assassin":
            tagimagen2 = "imagenes/assets/asesino.png"
            tagtexto2 = "Asesino"
        elif tag2 == "Mage":
            tagimagen2 = "imagenes/assets/mago.png"
            tagtexto2 = "Mago"
        elif tag2 == "Tank":
            tagimagen2 = "imagenes/assets/tanque.png"
            tagtexto2 = "Tanque"
        elif tag2 == "Support":
            tagimagen2 = "imagenes/assets/support.png"
            tagtexto2 = "Soporte"
        elif tag2 == "Support":
            tagimagen2 = "imagenes/assets/support.png"
            tagtexto2 = "Soporte"
        elif tag2 == None:
            tagimagen2 = "imagenes/assets/invisible.png"
            tagtexto2 = ""
        
        rutaimagen = dfchamp.loc[dfchamp["Name"] == mensaje, "Icono"].values
        rutasplash = dfchamp.loc[dfchamp["Name"] == mensaje, "SplashArt"].values
        

        col1, col2 = st.columns([1, 9]) 
        with col1:
            st.image(rutaimagen[0], width=60)
        with col2:
            st.markdown(
            f"""
            <div style="text-align: left;">
                <h1 style="color: white; margin: 0;">{mensaje}</h1>
            </div>
            """,
            unsafe_allow_html=True
            )
            
        st.image(rutasplash[0],caption="SplashArt del campeón")
        
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown(
                """
                <div style="margin-left: -75px; margin-right: -75px;">
                   <h3 style="color: white;">Historia</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(informacion)
        
        with col2:
            st.markdown(
                """
                <div style="margin-left: -75px; margin-right: -75px;">
                    <h3 style="color: white;">Información</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            icon_col1, text_col1 = st.columns([1, 3]) 
            with icon_col1:
                st.image(tagimagen, width=40)  
            with text_col1:
                st.write(tagtexto)  
        
            if tagimagen2: 
                icon_col2, text_col2 = st.columns([1, 3])
                with icon_col2:
                    st.image(tagimagen2, width=40)
                with text_col2:
                    st.write(tagtexto2) 
    else:
        st.write("Selecciona un campeon")


elif opcion == 'Competitivo':
    st.write("wenaboki")

elif opcion == 'Acerca de':

# Encabezado principal
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 15px;">
            <h1 style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 2em;">Acerca De</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Sección de Integrantes
    st.markdown(
        """
        <div style="margin: 0 20px; margin-bottom: 15px;">
            <h3 style="color: #FFAD33; font-family: 'Trebuchet MS', sans-serif; font-size: 1.2em;">Integrantes</h3>
            <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 20px;">Diego Abarca</p>
            <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 20px;">Cristobal Camousseight</p>
            <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 20px;">Rodrigo Manríquez</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Sección de Profesora
    st.markdown(
        """
        <div style="margin: 0 20px; margin-bottom: 10px;">
            <h3 style="color: #FFAD33; font-family: 'Trebuchet MS', sans-serif; font-size: 1.2em;">Profesora</h3>
            <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 20px;">Monica Otero Ferreiro</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Sección de Carrera
    st.markdown(
        """
        <div style="margin: 0 25px; text-align: right;">
            <h3 style="color: #FFAD33; font-family: 'Trebuchet MS', sans-serif; font-size: 1.2em;">Carrera</h3>
            <p style="color: #FFFFFF; font-family: 'Trebuchet MS', sans-serif; font-size: 20px;">Ingeniería Civil Informática</p>
        </div>
        """,
        unsafe_allow_html=True
)











