import streamlit as st

# 1. Configuración básica (Interfaz limpia)
st.set_page_config(page_title="Repositorio de Problemas", layout="centered")

st.title("📚 Repositorio de Problemas Interactivos")
st.write("Selecciona un problema para resolverlo directamente en Google Colab.")

# 2. CONFIGURACIÓN ÚNICA (Esto es lo único que necesitas para que los links funcionen)
USUARIO_GITHUB = "jarzolads"
REPO_GITHUB = "Problemario_Ingenieria_Quimica"

# 3. LISTA DE PROBLEMAS (Agrega aquí tantos como quieras)
# Solo pones el nombre que quieres que se vea y el nombre del archivo en GitHub
problemas = {
    "Balance de Materia y Energía": "https://colab.research.google.com/drive/1OgHhVboBcZ5Rx3qaFs4ODryLQB8eAuzH?usp=sharing",
    "Simulación de Reactores": "simulacion_reactores.ipynb",
    "Termodinámica Avanzada": "termo_ejercicio.ipynb",
    "Diseño de Plantas": "diseno_plantas.ipynb"
}

st.markdown("---")

# 4. CREACIÓN DE LA INTERFAZ VISUAL (Limpia y con botones)
for nombre, archivo in problemas.items():
    # Creamos una "tarjeta" visual sencilla
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(nombre)
            st.caption(f"Archivo: {archivo}")
            
        with col2:
            # El link directo que pide Google Colab para abrir el archivo
            url_directa = f"https://colab.research.google.com/github/{USUARIO_GITHUB}/{REPO_GITHUB}/blob/main/{archivo}"
            
            # Botón visual que abre el link en una pestaña nueva
            st.link_button("🚀 Abrir en Colab", url_directa)
        
        st.markdown("---")
