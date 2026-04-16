import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO PROFESIONAL
st.set_page_config(
    page_title="Repositorio de problemas de Ingeniería Química", 
    page_icon="🧪", 
    layout="wide"
)

# CSS Personalizado para mejorar la estética
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .problem-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .titulo-docente {
        color: #1e3d59;
        font-family: 'Helvetica';
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ENCABEZADO CON BRANDING
with st.container():
    col_logo, col_text = st.columns([1, 4])
    with col_text:
        st.markdown("<h1 class='titulo-docente'>🧪Repositorio de Ingeniería Química</h1>", unsafe_allow_html=True)
        st.markdown("### Dr. Jesús Andrés Arzola Flores")
        #st.info("Universidad Tecnológica de Tehuacán | Especialidad en Simulación y Optimización")

st.divider()

# 3. BASE DE DATOS DE PROBLEMAS (Fácil de actualizar)
# Solo necesitas cambiar los nombres aquí cuando subas nuevos archivos a GitHub
problemas = [
    {
        "titulo": "Balance de Materia y Energía en Destilación",
        "categoria": "Simulación",
        "descripcion": "Cálculo de flujos y composiciones usando DWSIM-Python.",
        "archivo": "Github_Problemas_de_ingeniería_Química.ipynb",
        "icon": "⚗️"
    }
]

# 4. BARRA LATERAL (Filtros interactivos)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1087/1087815.png", width=100) # Un icono decorativo
st.sidebar.title("Panel de Control")
busqueda = st.sidebar.text_input("🔍 Buscar problema...")
filtro_cat = st.sidebar.multiselect("Filtrar por área:", ["Simulación", "BioSTEAM", "Reactores", "Termodinámica"])

# 5. RENDERIZADO DE TARJETAS VISTOSAS
st.subheader("Listado de Problemas Disponibles")

# Configuración de tu GitHub
USUARIO = "jarzolads" 
REPO = "Problemario_Ingeneria_Quimica"

# Filtrar problemas según la búsqueda
for p in problemas:
    # Lógica de filtrado sencilla
    if busqueda.lower() in p["titulo"].lower() or not busqueda:
        if not filtro_cat or p["categoria"] in filtro_cat:
            
            # Crear la tarjeta visual
            with st.container():
                st.markdown(f"""
                <div class="problem-card">
                    <span style="background-color: #e1f5fe; padding: 5px 10px; border-radius: 15px; font-size: 12px; color: #01579b;">{p['categoria']}</span>
                    <h3>{p['icon']} {p['titulo']}</h3>
                    <p style="color: #555;">{p['descripcion']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Botón de apertura
                enlace = f"https://colab.research.google.com/github/{USUARIO}/{REPO}/blob/main/{p['archivo']}"
                st.markdown(f'''
                    <a href="{enlace}" target="_blank" style="text-decoration: none;">
                        <div style="background-color: #f9f9f9; border: 1px solid #ddd; padding: 10px; border-radius: 5px; text-align: center; color: #333; font-weight: bold;">
                            🚀 Abrir en Google Colab
                        </div>
                    </a>
                ''', unsafe_allow_html=True)
                st.write("") # Espaciado
