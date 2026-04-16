import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="IALabs - Repositorio IQ", page_icon="🧪", layout="wide")

# 2. Encabezado institucional (Dr. Jesús Andrés Arzola Flores)
st.title("🧪 Repositorio de Ingeniería Química")
st.markdown("### Dr. Jesús Andrés Arzola Flores")
st.caption("Universidad Tecnológica de Tehuacán | Diseño de Plantas y Simulación")

# 3. Variables de conexión (Cámbialas por tus datos reales)
USUARIO = "jarzolads"
REPO = "Problemario_Ingenieria_Quimica"

# 4. Lista de problemas (Asegúrate de que cada uno tenga sus datos)
problemas = [
    {
        "titulo": "Balance de Materia y Energía en Destilación",
        "descripcion": "Cálculo de flujos y composiciones usando DWSIM-Python.",
        "archivo": "Github_Problemas_de_ingeniería_química"
    },
    {
        "titulo": "Producción de Bioetanol (Agave)",
        "descripcion": "Modelado de biorrefinerías y análisis tecnoeconómico con BioSTEAM.",
        "archivo": "bioetanol_agave.ipynb"
    }
]

st.divider()

# 5. Buscador
busqueda = st.text_input("🔍 Buscar problema por título o descripción", "").lower()

# 6. Generación de la interfaz
for p in problemas:
    # Usamos .get() con un valor por defecto para evitar el error TypeError
    titulo = p.get("titulo", "Problema sin título")
    descripcion = p.get("descripcion", "Sin descripción disponible")
    archivo = p.get("archivo", "")
    
    # Lógica de búsqueda segura
    if busqueda in titulo.lower() or busqueda in descripcion.lower():
        with st.expander(f"📘 {titulo}", expanded=True):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.write(descripcion)
                st.caption(f"Archivo fuente: `{archivo}`")
            
            with col2:
                # El hipervínculo directo al archivo de Colab
                if archivo:
                    url_colab = f"https://colab.research.google.com/github/{USUARIO}/{REPO}/blob/main/{archivo}"
                    st.link_button("🚀 Abrir en Colab", url_colab, use_container_width=True)
                else:
                    st.warning("Archivo no definido")
