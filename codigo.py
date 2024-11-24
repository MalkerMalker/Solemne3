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

        
        ranger = dfchamp.loc[dfchamp["Name"] == mensaje, "Range type"].values[0]
        if ranger == "Melee":
            rangeimagen = "imagenes/assets/melee.png"
            rangetexto = "Cuerpo a cuerpo"
        elif ranger == "Ranged":
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
        elif rtype == "Shield":
            rtypeimagen = "imagenes/assets/escudoresource.png"
            rtypetexto = "Escudo"
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

        mr = dfchamp.loc[dfchamp["Name"] == mensaje, "Base magic resistance"].values[0]
        mrlvl = dfchamp.loc[dfchamp["Name"] == mensaje, "Magic resistance per lvl"].values[0]

        attackrange = dfchamp.loc[dfchamp["Name"] == mensaje, "Attack range"].values[0]

        hpreg = dfchamp.loc[dfchamp["Name"] == mensaje, "HP regeneration"].values[0]
        hpregniv = dfchamp.loc[dfchamp["Name"] == mensaje, "HP regeneration"].values[0]
        
        manareg = dfchamp.loc[dfchamp["Name"] == mensaje, "Mana regeneration"].values[0]
        manaregniv = dfchamp.loc[dfchamp["Name"] == mensaje, "Mana regeneration per lvl"].values[0]

        attackdmg = dfchamp.loc[dfchamp["Name"] == mensaje, "Attack damage"].values[0]
        attackdmgpl = dfchamp.loc[dfchamp["Name"] == mensaje, "Attack damage per lvl"].values[0]

        if tag1 == "Mage" or tag2 == "Mage":
            imagendaño = "imagenes/assets/dañomagico.png"
        else:
            imagendaño = "imagenes/assets/dañofisico.png"
            
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
                st.write("Mr/Mr+:")
                st.write("Attack R:")
                st.write("HPReg/+:")
                st.write("M Reg/+:")
                st.write("AttckDmg:")
            with icon_col1:
                st.image(tagimagen, width=30)
                st.image(rolimagen, width=30)
                st.image(rangeimagen, width=30)
                st.image(rtypeimagen, width=25)
                st.image("imagenes/assets/salud.png", width=20)
                st.image("imagenes/assets/mana.png", width=23)
                st.image("imagenes/assets/velocidad de movimiento.png")
                st.image("imagenes/assets/armadurabase.png", width=25)
                st.image("imagenes/assets/resistenciamagica.png", width=25)
                st.image("imagenes/assets/rangodeataque.png", width=25)
                st.image("imagenes/assets/healpower.png", width=25)
                st.image("imagenes/assets/manaregenration.png", width=25)
                st.image(imagendaño, width=25)
            with texto:
                st.write(tagtexto)
                st.write(roltexto)
                st.write(rangetexto)
                st.write(rtypetexto)
                st.write(hpbase)
                st.write(manabase)
                st.write(velmov)
                st.write(armor)
                st.write(mr)
                st.write(attackrange)
                st.write(hpreg)
                st.write(manareg)
                st.write(attackdmg)
            with icon_col2:
                st.image(tagimagen2, width=30)
                st.image(rolimagen2, width=30)
                st.image("imagenes/assets/invisible.png",width=25)
                st.image("imagenes/assets/invisible.png",width=25)
                st.image("imagenes/assets/saludpornivel.png",width=30)
                st.image("imagenes/assets/manapornivel.png", width=30)
                st.image("imagenes/assets/invisible.png",width=16)
                st.image("imagenes/assets/armadurabase.png", width=25)
                st.image("imagenes/assets/resistenciamagica.png", width=25)
                st.image("imagenes/assets/invisible.png",width=25)
                st.image("imagenes/assets/healpower.png", width=25)
                st.image("imagenes/assets/manaregenration.png", width=25)
                st.image(imagendaño, width=25)
            with texto2:
                st.write(tagtexto2)  
                st.write(roltexto2)
                st.write(txtinvisible)
                st.write(txtinvisible)
                st.write(hpnivel)
                st.write(mananivel)
                st.write(txtinvisible)
                st.write(armorlvl)
                st.write(mrlvl)
                st.write(txtinvisible)
                st.write(hpregniv)
                st.write(manaregniv)
                st.write(attackdmgpl)


        st.subheader(f"Comparacion de {mensaje} con otros campeones")
        
        dfchamp['highlight'] = dfchamp['Name'] == mensaje
        dfrol = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
        
        if role1 == "Top":
            comparartodo = "Rango de ataque"
            comparartodo2 = "Velocidad de ataque"
            comparar = "Escalado de vida"
            comparar2 = "Escalado de Resistencia magica"
            comparar3 = "Escalado de Armadura"
        elif role1 == "Middle":
            comparartodo = "Daño de ataque"
            comparartodo2 = "Velocidad de movimiento"
            comparar = "Escalado de vida"
            comparar2 = "Escalado de mana"
            comparar3 = "Daño de ataque"
        elif role1 == "Bottom":
            comparartodo = "Escalado de vida"
            comparartodo2 = "Velocidad de movimiento"
            comparar = "Daño de ataque"
            comparar2 = "Velocidad de ataque ratio"
            comparar3 = "Velocidad de ataque"
        elif role1 == "Support":
            comparartodo = "Escalado de armadura"
            comparartodo2 = "Velocidad de movimiento"
            comparar = "Escalado de vida"
            comparar2 = "Regeneración de vida"
            comparar3 = "Regeneracion de mana"
        elif role1 == "Jungle":
            comparartodo = "Rango de ataque"
            comparartodo2 = "Escalado de armadura"
            comparar = "Escalado de vida"
            comparar2 = "Daño de ataque"
            comparar3 = "Velocidad de movimiento"
        
        
        #Primer grafico informacion
        if comparartodo == "Rango de ataque":
            dfchampordenado = dfchamp.sort_values(by='Attack range', ascending=True)
            ejex1 = np.array(dfchampordenado["Attack range"])
            ejey1 = np.array(dfchampordenado["Name"])
            highlight1 = np.array(dfchampordenado["highlight"])
        elif comparartodo == "Daño de ataque":
            dfchampordenado = dfchamp.sort_values(by='Attack damage', ascending=True)
            ejex1 = np.array(dfchampordenado["Attack damage"])
            ejey1 = np.array(dfchampordenado["Name"])
            highlight1 = np.array(dfchampordenado["highlight"])
        elif comparartodo == "Escalado de vida":
            level_data = pd.DataFrame()
            levels = list(range(1, 19))
            for index, row in dfchamp.iterrows():
                base_hp = row['Base HP']
                hp_per_level = row['HP per lvl']
                hp_values = [base_hp + (level - 1) * hp_per_level for level in levels]
                champion_data = pd.DataFrame({
                    'Level': levels,
                    'HP': hp_values,
                    'Champion': [row['Name']] * 18
                })
                level_data = pd.concat([level_data, champion_data])
            level_data['highlight'] = level_data['Champion'] == mensaje
            highlight1 = np.array(level_data["highlight"])
            ejex1 = np.array(level_data['Level'])
            ejey1 = np.array(level_data['HP'])
        elif comparartodo == "Escalado de armadura":
            level_data = pd.DataFrame()
            levels = list(range(1, 19))
            for index, row in dfchamp.iterrows():
                base_armor = row['Base armor']
                armor_per_level = row['Armor per lvl']
                armor_values = [base_armor + (level - 1) * armor_per_level for level in levels]
                champion_data = pd.DataFrame({
                    'Level': levels,
                    'Armor': armor_values,
                    'Champion': [row['Name']] * 18
                })
                level_data = pd.concat([level_data, champion_data])
            level_data['highlight'] = level_data['Champion'] == mensaje
            ejex1 = np.array(level_data['Level'])
            ejey1 = np.array(level_data['Armor'])
            highlight1 = np.array(level_data["highlight"])
        
        ###################################
        if comparartodo2 == "Velocidad de ataque":
            dfchampordenado2 = dfchamp.sort_values(by='Attack range', ascending=True)
            ejex2 = np.array(dfchampordenado2["Attack range"])
            ejey2 = np.array(dfchampordenado2["Name"])
            highlight2 = np.array(dfchampordenado2["highlight"])
        elif comparartodo2 == "Velocidad de movimiento":
            dfchampordenado2 = dfchamp.sort_values(by='Attack damage', ascending=True)
            ejex2 = np.array(dfchampordenado2["Attack damage"])
            ejey2 = np.array(dfchampordenado2["Name"])
            highlight2 = np.array(dfchampordenado2["highlight"])
        elif comparartodo2 == "Escalado de armadura":
            level_data2 = pd.DataFrame()
            levels = list(range(1, 19))
            for index, row in dfchamp.iterrows():
                base_armor2 = row['Base armor']
                armor_per_level2 = row['Armor per lvl']
                armor_values2 = [base_armor2 + (level2 - 1) * armor_per_level2 for level2 in levels]
                champion_data2 = pd.DataFrame({
                    'Level': levels,
                    'Armor': armor_values2,
                    'Champion': [row['Name']] * 18 
                })
                level_data2 = pd.concat([level_data2, champion_data2])
            level_data2['highlight'] = level_data2['Champion'] == mensaje
            ejex2 = np.array(level_data2['Level'])
            ejey2 = np.array(level_data2['Armor'])
            highlight2 = np.array(level_data2['highlight'])
        ###################################################### comparar por 
        if comparar == "Escalado de vida":
            level_data3 = pd.DataFrame()
            levels = list(range(1, 19))
            df_filtered = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
            for index, row in df_filtered.iterrows():
                base_hp3 = row['Base HP']
                hp_per_level3 = row['HP per lvl']
                hp_values3 = [base_hp3 + (level - 1) * hp_per_level3 for level in levels]
                champion_data = pd.DataFrame({
                    'Level': levels,
                    'HP': hp_values3,
                    'Champion': [row['Name']] * 18
                })
                level_data3 = pd.concat([level_data3, champion_data])
            level_data3['highlight'] = level_data3['Champion'] == mensaje
            highlight3 = np.array(level_data3["highlight"])
            ejex3 = np.array(level_data3['Level'])
            ejey3 = np.array(level_data3['HP'])
        elif comparar == "Daño de ataque":
            df_filtered3 = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
            dfchampordenado3 = df_filtered3.sort_values(by="Attack damage", ascending=True)
            ejex3 = np.array(dfchampordenado3["Attack damage"])
            ejey3 = np.array(dfchampordenado3["Name"])
            highlight3 = np.array(dfchampordenado3["highlight"])
        
        ############################
        if comparar2 == "Escalado de Resistencia magica":
            level_data4 = pd.DataFrame()
            levels = list(range(1, 19))
            for index, row in dfchamp.iterrows():
                base_mr4 = row['Base magic resistance']
                mr_per_level4 = row['Magic resistance per lvl']
                mr_values4 = [base_mr4 + (level - 1) * mr_per_level4 for level in levels]
                champion_data = pd.DataFrame({
                    'Level': levels,
                    'MR': mr_values4,
                    'Champion': [row['Name']] * 18  
                })
                level_data4 = pd.concat([level_data4, champion_data])
            level_data4['highlight'] = level_data4['Champion'] == mensaje
            highlight4 = np.array(level_data4['highlight'])
            ejex4 = np.array(level_data4['Level'])
            ejey4 = np.array(level_data4['MR'])
        
        elif comparar2 == "Escalado de mana":
            level_data4 = pd.DataFrame()
            levels = list(range(1, 19))
            for index, row in dfchamp.iterrows():
                base_mana4 = row['Base mana']
                mana_per_level4 = row['Mana per lvl']
                mana_values4 = [base_mana4 + (level - 1) * mana_per_level4 for level in levels]
                champion_data = pd.DataFrame({
                    'Level': levels,
                    'Mana': mana_values4,
                    'Champion': [row['Name']] * 18
                })
                level_data4 = pd.concat([level_data4, champion_data])
            highlight4 = np.array(level_data4["highlight"])
            ejex4 = np.array(level_data4['Level'])
            ejey4 = np.array(level_data4['Base magic resistance'])
        
        elif comparar2 == "Velocidad de ataque ratio":
            df_filtered4 = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
            dfchampordenado = df_filtered4.sort_values(by="AS ratio", ascending=True)
            ejex4 = np.array(dfchampordenado["AS ratio"])
            ejey4 = np.array(dfchampordenado["Name"])
            highlight4 = np.array(dfchampordenado["highlight"])
        
        elif comparar2 == "Regeneración de vida":
            df_filtered4 = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
            dfchampordenado = df_filtered4.sort_values(by="HP regeneration", ascending=True)
            ejex4 = np.array(dfchampordenado["HP regeneration"])
            ejey4 = np.array(dfchampordenado["Name"])
            highlight4 = np.array(dfchampordenado["highlight"])
        
        elif comparar2 == "Daño de ataque":
            df_filtered4 = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
            dfchampordenado = df_filtered4.sort_values(by="Attack damage", ascending=True)
            ejex4 = np.array(dfchampordenado["Attack damage"])
            ejey4 = np.array(dfchampordenado["Name"])
            highlight4 = np.array(dfchampordenado["highlight"])
        ###################################
        if comparar3 == "Escalado de Armadura":
            level_data5 = pd.DataFrame()
            levels = list(range(1, 19))
            for index, row in dfchamp.iterrows():
                base_armor5 = row['Base armor']
                armor_per_level5 = row['Armor per lvl']
                armor_values5 = [base_armor5 + (level5 - 1) * armor_per_level5 for level5 in levels]
                champion_data5 = pd.DataFrame({
                    'Level': levels,
                    'Armor': armor_values5,
                    'Champion': [row['Name']] * 18 
                })
                level_data5 = pd.concat([level_data5, champion_data5])
            level_data5['highlight'] = level_data5['Champion'] == mensaje
            ejex5 = np.array(level_data5['Level'])
            ejey5 = np.array(level_data5['Armor'])
            highlight5 = np.array(level_data5['highlight'])
        
        elif comparar3 == "Daño de ataque":
            df_filtered5 = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
            dfchampordenado5 = df_filtered5.sort_values(by="Attack damage", ascending=True)
            ejex5 = np.array(dfchampordenado5["Attack damage"])
            ejey5 = np.array(dfchampordenado5["Name"])
            highlight5 = np.array(dfchampordenado5["highlight"])
        
        elif comparar3 == "Velocidad de ataque":
            dfchampordenado5 = dfchamp.sort_values(by='Attack range', ascending=True)
            ejex5 = np.array(dfchampordenado5["Attack range"])
            ejey5 = np.array(dfchampordenado5["Name"])
            highlight5 = np.array(dfchampordenado5["highlight"])
        
        elif comparar3 == "Regeneracion de mana":
            level_data5 = pd.DataFrame()
            levels = list(range(1, 19))
            for index, row in dfchamp.iterrows():
                base_regmana5 = row['Mana regeneration']
                regmana_per_level5 = row['Mana regeneration per lvl']
                regmana_values5 = [base_regmana5 + (level5 - 1) * regmana_per_level5 for level5 in levels]
                champion_data5 = pd.DataFrame({
                    'Level': levels,
                    'Regmana': regmana_values5,
                    'Champion': [row['Name']] * 18 
                })
                level_data5 = pd.concat([level_data5, champion_data5])
            level_data5['highlight'] = level_data5['Champion'] == mensaje
            ejex5 = np.array(level_data5['Level'])
            ejey5 = np.array(level_data5['Regmana'])
            highlight5 = np.array(level_data5['highlight'])
        
        elif comparar3 == "Velocidad de movimiento":
            dfchampordenado5 = dfchamp[dfchamp['Role'].str.contains(role1, case=False, na=False)]
            dfchampordenado5 = dfchampordenado5.sort_values(by='Movement speed', ascending=True)
            ejex5 = np.array(dfchampordenado5["Movement speed"])
            ejey5 = np.array(dfchampordenado5["Name"])
            highlight5 = np.array(dfchampordenado5["highlight"])

        line_chart = alt.Chart(data).mark_line().encode(
            x='Attack range',
            y=alt.Y('Name', sort=None)  # Mantener el orden tal como está en los datos
        )
        
        # Crear el punto destacado
        highlight_point = alt.Chart(data).mark_point(size=100, color='red').encode(
            x='Attack range',
            y='Name'
        ).transform_filter(
            alt.datum.highlight  # Filtrar solo los puntos destacados
        )
        
        # Combinar ambos gráficos
        chart = line_chart + highlight_point
        chart
        
    else:
        st.write("Selecciona un campeon de la barra lateral")


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











