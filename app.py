import streamlit as st
from PIL import Image

# 1. Configuración básica para una interfaz "premium" y centrada
st.set_page_config(
    page_title="Repositorio de Problemas de Ingeniería Química - FIQ BUAP",
    page_icon="🧪",
    layout="wide", # Usamos wide para columns, y luego centramos el contenido
)

# --- CSS Personalizado para mejorar la estética ---
# Esto añade un borde sutil, espaciado y estilos a las tarjetas y botones.
st.markdown("""
<style>
    .reportview-container .main .block-container{
        padding-top: 2rem;
    }
    .stApp {
        background-color: #f8f9fa;
    }
    /* Estilo para las "tarjetas" de problemas */
    .problem-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #eaecef;
        margin-bottom: 25px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .problem-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    /* Estilo del subtítulo dentro de la tarjeta */
    .stSubheader {
        font-weight: 700;
        color: #31333f;
        margin-top: 0;
    }
    /* Estilo del caption dentro de la tarjeta */
    .stCaption {
        color: #7d8089;
        font-style: italic;
    }
    /* Estilo del botón */
    .stButton>button {
        border-radius: 30px;
        padding: 12px 24px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        transition: background-color 0.2s ease;
    }
    .stButton>button:hover {
        opacity: 0.9;
    }
    /* Centrar contenido en las columnas */
    .css-1r6slb0 { # class for st.columns inner contents
        align-items: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# 2. ENCABEZADO CON LOGO Y TÍTULOS (Centrado usando columnas)
with st.container():
    col_logo, col_text = st.columns([1.5, 3.5])
    
    with col_logo:
        # Cargamos y mostramos el logo (se asume que image_0.png está en el mismo directorio)
        try:
            logo = Image.open('Logo.png')
            st.image(logo, use_container_width=True, caption="FIQ - CIAYP Logo")
        except FileNotFoundError:
            st.warning("⚠️ Logo no encontrado. Asegúrate de que 'image_0.png' esté en el directorio de la aplicación.")
    
    with col_text:
        st.title("📚 Repositorio de Problemas de Ingeniería Química")
        st.markdown("<h2 style='text-align: center; color: #555;'>Módulo de Problemas Interactivos</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 1.1em;'><b>Dr. Jesús Andrés Arzola Flores</b></p>", unsafe_allow_html=True)
        st.caption("Facultad de Ingeniería Química | Benemérita Universidad Autónoma de Puebla")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# 3. CONFIGURACIÓN ÚNICA (GitHub)
# Esto es esencial para que los enlaces se construyan automáticamente.
USUARIO_GITHUB = "jarzolads"
REPO_GITHUB = "Problemario_Ingenieria_Quimica"

# 4. LISTA DE PROBLEMAS MEJORADA
# Solo pones el nombre que quieres que se vea y el nombre del archivo en GitHub.
# Puedes añadir descripciones breves aquí para mejorar la interfaz.
# ¡RECUERDA CORREGIR EL ENLACE DE DRIVE EN EL ARCHIVO SI EXISTE! 
# El primer problema ahora usa una clave especial para Drive.
problemas = [
    {
        "titulo": "Balance de Materia y Energía", 
        "archivo": "Github_Problemas_de_ingeniería_Química.ipynb", # Solo la ID para Drive
        "plataforma": "drive", # Indicamos que es Drive
        "icono": "⚗️", 
        "descripcion": "Resolución de balances de masa y energía en sistemas reaccionantes."
    },
    {
        "titulo": "Simulación de Reactores", 
        "archivo": "simulacion_reactores.ipynb", 
        "icono": "☢️",
        "descripcion": "Modelado y simulación de reactores químicos (CSTR, PFR) en régimen estacionario."
    },
    {
        "titulo": "Termodinámica Avanzada", 
        "archivo": "termo_ejercicio.ipynb", 
        "icono": "🌡️",
        "descripcion": "Cálculos de equilibrio de fases y fugacidad para mezclas multicomponente."
    },
    {
        "titulo": "Diseño de Plantas", 
        "archivo": "diseno_plantas.ipynb", 
        "icono": "🏗️",
        "descripcion": "Análisis tecnoeconómico y dimensionamiento preliminar de equipos de proceso."
    }
]

# 5. CREACIÓN DE LA INTERFAZ VISUAL "PREMIUM"
st.subheader("📚 Listado de Problemas Disponibles")
st.write("Haz clic en un problema para abrirlo directamente en el entorno interactivo de Google Colab.")
st.markdown("<br>", unsafe_allow_html=True)

for p in problemas:
    # Creamos una tarjeta visual más bonita usando markdown y css personalizado
    st.markdown(f"""
    <div class="problem-card">
        <div style="display: flex; align-items: start; gap: 15px;">
            <div style="font-size: 3em;">{p['icono']}</div>
            <div>
                <h3 style="margin: 0; padding: 0;">{p['titulo']}</h3>
                <p class="stCaption" style="margin-top: 5px;">{p['descripcion']}</p>
                <p class="stCaption" style="margin-top: 5px; font-size: 0.8em;">Archivo fuente: <code>{p['archivo']}</code></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # El link directo se construye según la plataforma
    if p.get("plataforma") == "drive":
        # Enlace para Drive (asumiendo formato estándar)
        url_directa = f"https://colab.research.google.com/drive/{p['archivo']}?usp=sharing"
    else:
        # Enlace para GitHub
        url_directa = f"https://colab.research.google.com/github/{USUARIO_GITHUB}/{REPO_GITHUB}/blob/main/{p['archivo']}"
    
    # Botón visual dentro de la tarjeta (Streamlit no permite meter un botón de Streamlit dentro de un bloque HTML personalizado, así que lo ponemos debajo)
    col_vacia, col_boton = st.columns([4, 1])
    with col_boton:
        st.link_button("🚀 Abrir en Colab", url_directa, type="primary")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
# Un pequeño pie de página
st.caption("© 2023 - Repositorio de Ingeniería Química - FIQ BUAP | Powered by Streamlit & Google Colab")
