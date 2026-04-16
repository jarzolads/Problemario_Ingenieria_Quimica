import streamlit as st
from PIL import Image

# 1. Configuración básica
st.set_page_config(
    page_title="Repositorio de Problemas de Ingeniería Química - FIQ BUAP",
    page_icon="🧪",
    layout="wide",
)

# --- CSS Personalizado ---
st.markdown("""
<style>
    .stApp {
        background-color: #f8f9fa;
    }
    .problem-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: 1px solid #eaecef;
        margin-bottom: 10px;
        transition: transform 0.2s ease;
    }
    .problem-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    }
    .stButton>button {
        border-radius: 20px;
        font-weight: 600;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 2. ENCABEZADO
with st.container():
    col_logo, col_text = st.columns([1, 4])
    
    with col_logo:
        try:
            # Usamos el nombre exacto del archivo subido
            logo = Image.open('Logo.png')
            st.image(logo, use_container_width=True)
        except:
            st.write("🧪") # Icono de respaldo si no carga la imagen
    
    with col_text:
        st.title("📚 Repositorio de Problemas de Ingeniería Química")
        st.markdown("### Facultad de Ingeniería Química | BUAP")
        st.markdown("**Dr. Jesús Andrés Arzola Flores**")

st.divider()

# 3. CONFIGURACIÓN DE GITHUB
USUARIO_GITHUB = "jarzolads"
REPO_GITHUB = "Problemario_Ingenieria_Quimica"

# 4. LISTA DE PROBLEMAS
# He simplificado la lógica: si es un link completo (Drive), se usa tal cual.
# Si es solo el nombre del archivo, se construye el link de GitHub.
problemas = [
    {
        "titulo": "Balance de Materia y Energía", 
        "archivo": "https://colab.research.google.com/drive/1OgHhVboBcZ5Rx3qaFs4ODryLQB8eAuzH?usp=sharing", 
        "tipo": "directo",
        "icono": "⚗️", 
        "descripcion": "Resolución de balances de masa y energía en sistemas reaccionantes."
    },
    {
        "titulo": "Simulación de Reactores", 
        "archivo": "simulacion_reactores.ipynb", 
        "tipo": "github",
        "icono": "☢️",
        "descripcion": "Modelado y simulación de reactores químicos (CSTR, PFR)."
    },
    {
        "titulo": "Termodinámica Avanzada", 
        "archivo": "termo_ejercicio.ipynb", 
        "tipo": "github",
        "icono": "🌡️",
        "descripcion": "Cálculos de equilibrio de fases y fugacidad."
    },
    {
        "titulo": "Diseño de Plantas", 
        "archivo": "diseno_plantas.ipynb", 
        "tipo": "github",
        "icono": "🏗️",
        "descripcion": "Análisis tecnoeconómico y dimensionamiento de equipos."
    }
]

st.subheader("Listado de Problemas Interactivos")
st.write("Haz clic en el botón para abrir el cuaderno de trabajo en Google Colab.")

# 5. GENERACIÓN DE INTERFAZ
for p in problemas:
    # Lógica de construcción de URL corregida
    if p["tipo"] == "directo":
        url_final = p["archivo"]
    else:
        # Construcción estándar para archivos en GitHub
        url_final = f"https://colab.research.google.com/github/{USUARIO_GITHUB}/{REPO_GITHUB}/blob/main/{p['archivo']}"
    
    # Renderizado de la tarjeta
    with st.container():
        col_info, col_btn = st.columns([4, 1])
        
        with col_info:
            st.markdown(f"""
            <div class="problem-card">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 2.5em;">{p['icono']}</div>
                    <div>
                        <h4 style="margin: 0;">{p['titulo']}</h4>
                        <p style="margin: 0; color: #666; font-size: 0.9em;">{p['descripcion']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col_btn:
            st.write("") # Espaciado para alinear con la tarjeta
            st.write("")
            st.link_button("🚀 Abrir Colab", url_final, type="primary")

st.divider()
st.caption("© 2026 - Repositorio de Ingeniería Química - Dr. Jesús Andrés Arzola Flores")
