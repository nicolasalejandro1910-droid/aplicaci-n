import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import json
import random

# Configuración de la página
st.set_page_config(
    page_title="MealSmart - Planificador de Comidas",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para diseño responsivo en móviles
st.markdown("""
<style>
@media (max-width: 768px) {
    h1 {
        font-size: 1.8rem !important;
    }
    h2 {
        font-size: 1.5rem !important;
    }
    h3 {
        font-size: 1.2rem !important;
    }
    .stMarkdown h1 {
        font-size: 1.8rem !important;
    }
    .stMarkdown h2 {
        font-size: 1.5rem !important;
    }
    .stMarkdown h3 {
        font-size: 1.2rem !important;
    }
}

/* Ajustes generales para títulos */
h1 {
    font-size: 2.5rem;
}
h2 {
    font-size: 2rem;
}
h3 {
    font-size: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# Navegación
st.sidebar.title("🍽️ MealSmart")
st.sidebar.markdown("---")
page = st.sidebar.selectbox(
    "Navegación",
    ["🏠 Página Principal", "📊 Planificador", "📞 Contacto"]
)

# Router de páginas
if page == "🏠 Página Principal":
    from _pages_backup import home
    home.show()
elif page == "📊 Planificador":
    from _pages_backup import planificador
    planificador.show()
elif page == "📞 Contacto":
    from _pages_backup import contacto
    contacto.show()
