import streamlit as st
import os

def show():
    st.title("📞 Contacto")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👨‍💻 Información del Equipo")
        st.info("""
        **Nombre:** Maria Ignacia Miño Yañez  
        **Rol:** Developer, Product Manager & CEO  
        **Curso:** 3ro Blue  
        **Institución:** Colegio Garden
        """)
        
        st.markdown("---")
        st.subheader("📚 Sobre MealSmart")
        st.markdown("""
        MealSmart nace con la misión de hacer la nutrición 
        personalizada accesible para todos, desde jóvenes 
        hasta adultos mayores.
        
        Con herramientas basadas en ciencia y una interfaz 
        amigable, ayudamos a crear hábitos alimenticios 
        saludables que duran toda la vida.
        """)
        
        st.markdown("---")
        st.subheader("🎯 Nuestra Misión")
        st.markdown("""
        • Democratizar la nutrición personalizada  
        • Educar sobre alimentación balanceada  
        • Facilitar la planificación de comidas  
        • Promover estilos de vida saludables
        """)
    
    with col2:
        logo_path = os.path.join("images", "logo.png")
        if os.path.exists(logo_path):
            try:
                from PIL import Image
                img = Image.open(logo_path)
                st.image(img, width=250)
            except:
                st.info("💡 Logo no encontrado - Agrega logo.png en la carpeta images/")
        else:
            st.info("💡 Logo no encontrado - Agrega logo.png en la carpeta images/")
    
    st.markdown("---")
    
    st.subheader("ℹ️ Sobre el Proyecto")
    st.markdown("""
    **MealSmart** es una aplicación web desarrollada con Streamlit que tiene como objetivo
    ayudar a las personas a planificar sus comidas de manera inteligente según sus objetivos
    nutricionales.
    
    Esta aplicación fue desarrollada como parte del proyecto:
    **Elaboración de apps para dispositivos electrónicos móviles**
    
    ---
    
    ### 🛠️ Tecnologías Utilizadas
    
    - **Streamlit** - Framework para aplicaciones web interactivas
    - **Pandas** - Manipulación y análisis de datos
    - **Plotly** - Visualización de datos interactiva
    - **PIL (Pillow)** - Procesamiento de imágenes
    - **Python** - Lenguaje de programación
    
    ---
    
    ### 📊 Características Principales
    
    ✓ Cálculo automático de TDEE y BMR  
    ✓ Personalización según género, edad, peso y altura  
    ✓ Planificación de macronutrientes  
    ✓ Recomendaciones según objetivos  
    ✓ Interfaz intuitiva y fácil de usar  
    ✓ Visualizaciones interactivas  
    
    ---
    
    ### 📧 Contacto
    
    Para más información sobre el proyecto, consultas o sugerencias:
    
    📧 Email: mariaignacia.mino@estudiantes.colegiotgs.cl  
    🌐 Repositorio: [URL pendiente - actualizar después de subir a GitHub]
    """)
    
    st.markdown("---")
    st.success("Gracias por usar MealSmart! 🍽️")

