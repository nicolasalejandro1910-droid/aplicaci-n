import streamlit as st
from PIL import Image
import os

def show():
    st.title("🍽️ MealSmart")
    st.markdown("### Tu Asistente Inteligente para Planificar Comidas Saludables")
    
    # Imagen principal
    image_path = os.path.join("images", "healthy_food.jpg")
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            st.image(img, use_container_width=True, caption="Comidas saludables al alcance de todos")
        except Exception as e:
            st.info("💡 Imagen healthy_food.jpg no encontrada. Por favor agrega la imagen en la carpeta images/")
    else:
        st.info("💡 Imagen healthy_food.jpg no encontrada. Por favor agrega la imagen en la carpeta images/")
    
    st.markdown("---")
    
    # Sección 1: Problema a resolver
    st.header("🎯 Problema a Resolver")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### El desafío
        Actualmente, muchas personas luchan con:
        - **Falta de tiempo** para planificar comidas saludables
        - **Desconocimiento** sobre sus necesidades calóricas y nutricionales
        - **Dificultad** para saber qué comer según sus objetivos (bajar de peso, ganar masa muscular, mantener un peso saludable)
        - **Confusión** con la información nutricional contradictoria en internet
        """)
    
    with col2:
        fitness_image = os.path.join("images", "fitness.jpg")
        if os.path.exists(fitness_image):
            try:
                img2 = Image.open(fitness_image)
                st.image(img2, width=500)
            except:
                pass
    
    # Sección 2: Usuario objetivo
    st.header("👥 Usuario Objetivo")
    st.markdown("""
    **Características del usuario:**
    - **Edad**: 12-99 años (para que niños y jóvenes también puedan cuidar su alimentación)
    - **Ubicación**: Personas urbanas con acceso a internet
    - **Estilo de vida**: 
      - Ocupados con trabajos o estudios
      - Interés en mejorar su salud y bienestar
      - Buscan soluciones prácticas y rápidas
      - Tienen acceso a internet y dispositivos móviles/computadores
    - **Necesidades**: Calcular requerimientos nutricionales y recibir recomendaciones personalizadas de comidas
    """)
    
    # Sección 3: Solución
    st.header("💡 ¿Cómo MealSmart ayuda?")
    
    col3, col4 = st.columns(2)
    
    with col3:
        nutrition_image = os.path.join("images", "nutrition_chart.png")
        if os.path.exists(nutrition_image):
            try:
                img3 = Image.open(nutrition_image)
                st.image(img3, width=500)
            except:
                pass
    
    with col4:
        st.markdown("""
        En la actualidad, muchas personas desean mejorar su alimentación, pero no saben por dónde comenzar. Calcular calorías, entender los macronutrientes o planificar comidas equilibradas puede ser una tarea confusa y tediosa.
        
        **MealSmart** nace como una solución práctica y accesible para quienes buscan comer mejor sin complicaciones.
        
        La aplicación te guía paso a paso para alcanzar tus objetivos nutricionales mediante:
        
        ✅ **Calculadora de calorías personalizada**, adaptada a tu edad, peso, altura y nivel de actividad.
        
        ✅ **Planificación automática de comidas**, ajustada a tu meta: bajar de peso, ganar masa o mantenerte saludable.
        
        ✅ **Información nutricional clara y visual**, fácil de comprender incluso para principiantes.
        
        ✅ **Recomendaciones personalizadas** de recetas y platos, para que tu alimentación sea variada y sabrosa.
        
        ✅ **Seguimiento de macronutrientes** (proteínas, carbohidratos y grasas) mediante gráficos interactivos.
        
        ✅ **Interfaz simple e intuitiva**, diseñada para usarse desde cualquier dispositivo.
        
        Con MealSmart, podrás cuidar tu salud y alcanzar tus metas sin necesidad de contratar a un nutricionista ni perder horas buscando información en internet.
        """)
    
    st.markdown("---")
    
    # Llamado a la acción
    st.info("""
    🚀 **¡Comienza ahora!** Ve a la sección de **Planificador** en el menú lateral 
    para calcular tus necesidades nutricionales y obtener tu plan de comidas personalizado.
    """)

