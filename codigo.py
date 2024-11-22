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
                           ("imagenes/iconos/elisse.jpg", "Elise"),
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
                           ("imagenes/iconos/yi.jpg", "Maestro Yi"),
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
    if title:
    # Filtrar la fila con el mensaje dado
        fila = dfchamp[dfchamp["Name"] == mensaje]
    
    if not fila.empty:  # Verifica si existe alguna coincidencia
        # Obtener información y roles
        informacion = fila["Informacion"].values[0]
        role = fila["Role"].values[0]
        roles_split = role.split(",") 
        role1 = roles_split[0] if len(roles_split) > 0 else None
        role2 = roles_split[1] if len(roles_split) > 1 else None
        
        # Variables de texto inicializadas
        txtinvisible = "‎‎ "
        roltexto2 = "‎‎ "
        if role1 == "Top":
            rolimagen = "imagenes/assets/top.png"
            roltexto = "Carril superior"
        elif role1 == "Middle":
            rolimagen = "imagenes/assets/mid.png"
            roltexto = "Carril del medio"
        elif role1 == "Bottom":
            rolimagen = "imagenes/assets/botlane.png"
            roltexto = "Carril inferior"
        elif role1 == "Support":
            rolimagen = "imagenes/assets/supp.png"
            roltexto = "Soporte"
        elif role1 == "Jungle":
            rolimagen = "imagenes/assets/jungla.png"
            roltexto = "Jungla"
            
        if role2 == "Top":
            rolimagen2 = "imagenes/assets/top.png"
            roltexto2 = "Carril superior"
        elif role2 == "Middle":
            rolimagen2 = "imagenes/assets/mid.png"
            roltexto2 = "Carril del medio"
        elif role2 == "Bottom":
            rolimagen2 = "imagenes/assets/botlane.png"
            roltexto2 = "Carril inferior"
        elif role2 == "Support":
            rolimagen2 = "imagenes/assets/supp.png"
            roltexto2 = "Soporte"
        elif role2 == "Jungle":
            rolimagen2 = "imagenes/assets/jungla.png"
            roltexto2 = "Jungla"
        elif role2 == None:
            rolimagen2 = "imagenes/assets/invisible.png"
            roltexto2 = "‎ "
            
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
        elif tag2 == "Marksman":
            tagimagen2 = "imagenes/assets/adcarry.png"
            tagtexto2 = "Tirador"
        elif tag2 == None:
            tagimagen2 = "imagenes/assets/invisible.png"
            tagtexto2 = "‎ "

        
        range = dfchamp.loc[dfchamp["Name"] == mensaje, "Range type"].values[0]
        if range == "Melee":
            rangeimagen = "imagenes/assets/melee.png"
            rangetexto = "Cuerpo a cuerpo"
        elif range == "Ranged":
            rangeimagen = "imagenes/assets/rango.png"
            rangetexto = "Distancia"

        rtype = dfchamp.loc[dfchamp["Name"] == mensaje, "Resourse type"].values[0]
        if rtype == "Blood Well":
            rtypeimagen = "imagenes/assets/manaresource.png"
            rtypetexto = "Pozo de sangre"
        elif rtype == "Mana":
            rtypeimagen = "imagenes/assets/manaresource.png"
            rtypetexto = "Mana"
        elif rtype == "Energy":
            rtypeimagen = "imagenes/assets/energy.png"
            rtypetexto = "Energia"
        elif rtype == "Fury":
            rtypeimagen = "imagenes/assets/furia.png"
            rtypetexto = "Furia"
        elif rtype == "Ferocity":
            rtypeimagen = "imagenes/assets/furia.png"
            rtypetexto = "Ferocidad"
        elif rtype == "Heat":
            rtypeimagen = "imagenes/assets/carga.png"
            rtypetexto = "Calor"
        elif rtype == "Grit":
            rtypeimagen = "imagenes/assets/furia.png"
            rtypetexto = "Coraje"
        elif rtype == "Flow":
            rtypeimagen = "imagenes/assets/flujo.png"
            rtypetexto = "Flujo"
        elif rtype == "Courage":
            rtypeimagen = "imagenes/assets/furia.png"
            rtypetexto = "Coraje"
        elif rtype == "Crimson Rush":
            rtypeimagen = "imagenes/assets/manaresource.png"
            rtypetexto = "Drenaje de sangre"
        elif rtype == "z":
            rtypeimagen = "imagenes/assets/manaless.png"
            rtypetexto = "‎Sin recurso"

        hpbase = dfchamp.loc[dfchamp["Name"] == mensaje, "Base HP"].values[0]
        hpnivel = dfchamp.loc[dfchamp["Name"] == mensaje, "HP per lvl"].values[0]
        
        manabase = dfchamp.loc[dfchamp["Name"] == mensaje, "Base mana"].values[0]
        mananivel = dfchamp.loc[dfchamp["Name"] == mensaje, "Mana per lvl"].values[0]

        velmov = dfchamp.loc[dfchamp["Name"] == mensaje, "Movement speed"].values[0]

        armor = dfchamp.loc[dfchamp["Name"] == mensaje, "Base armor"].values[0]
        armorlvl = dfchamp.loc[dfchamp["Name"] == mensaje, "Armor per lvl"].values[0]
        
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
        
        col1, col2 = st.columns([1, 1.5]) 
        with col1:
            st.markdown(
                """
                <div style="margin-left: 80px; margin-right: 0px;">
                   <h3 style="color: white;">Historia</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(informacion)
        
        with col2:
            st.markdown(
                """
                <div style="margin-left: 140px; margin-right: 0px;">
                    <h3 style="color: white;">Información</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            desc, icon_col1, texto, icon_col2, texto2 = st.columns([2,1,3,1,3])
            with desc:
                st.write("Rol:")
                st.write("Pocisión:")
                st.write("Rango:")
                st.write("Recurso:")
                st.write("HP/HP+:")
                st.write("Mana/M+:")
                st.write("Vel.Mov:")
                st.write("Arm/Ar+:")
            with icon_col1:
                st.image(tagimagen, width=30)
                st.image(rolimagen, width=30)
                st.image(rangeimagen, width=30)
                st.image(rtypeimagen, width=30)
                st.image("imagenes/assets/salud.png", width=20)
                st.image("imagenes/assets/mana.png", width=23)
                st.image("imagenes/assets/velocidad de movimiento.png")
                st.image("imagenes/assets/armadurabase.png", width=30)
            with texto:
                st.write(tagtexto)
                st.write(roltexto)
                st.write(rangetexto)
                st.write(rtypetexto)
                st.write(hpbase)
                st.write(manabase)
                st.write(velmov)
                st.write(armor)
            with icon_col2:
                st.image(tagimagen2, width=30)
                st.image(rolimagen2, width=30)
                st.image("imagenes/assets/invisible.png",width=30)
                st.image("imagenes/assets/invisible.png",width=30)
                st.image("imagenes/assets/saludpornivel.png",width=30)
                st.image("imagenes/assets/manapornivel.png", width=30)
                st.image("imagenes/assets/invisible.png",width=30)
                st.image("imagenes/assets/armadurapornivel.png",width=20)
            with texto2:
                st.write(tagtexto2)  
                st.write(roltexto2)
                st.write(txtinvisible)
                st.write(txtinvisible)
                st.write(hpnivel)
                st.write(mananivel)
                st.write(txtinvisible)
                st.write(armorlvl)
                
        chart = alt.Chart(dfinf).mark_bar().encode(
        x=alt.X("Playing", title="Escalado de recurso"),
        y=alt.Y("Title", title=f"Campeones", sort=None),
        color=alt.Color('highlight:N', legend=None, scale=alt.Scale(domain=['normal', 'highlight'], range=['#cccccc', 'lightgreen']))
        ).properties(
        title=f"Comparacion de {mensaje} con todos los {roltexto}",
        width=200,
        height=400
        )
    
        # Mostrar el gráfico en Streamlit
        st.altair_chart(chart, use_container_width=True)
        
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











