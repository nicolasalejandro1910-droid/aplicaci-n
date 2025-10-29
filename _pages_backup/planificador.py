import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import json
import os

def calculate_bmr(weight, height, age, gender):
    """Calcula la Tasa Metabólica Basal (BMR) usando la ecuación de Mifflin-St Jeor"""
    if gender == "Masculino":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:  # Femenino
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

def calculate_tdee(bmr, activity_level):
    """Calcula el Total Daily Energy Expenditure (TDEE) multiplicando BMR por factor de actividad"""
    activity_factors = {
        "Sedentario (poco o nada de ejercicio)": 1.2,
        "Ligero (ejercicio ligero 1-3 días/semana)": 1.375,
        "Moderado (ejercicio moderado 3-5 días/semana)": 1.55,
        "Intenso (ejercicio duro 6-7 días/semana)": 1.725,
        "Muy intenso (ejercicio muy duro y trabajo físico)": 1.9
    }
    return bmr * activity_factors[activity_level]

def get_goal_calories(tdee, goal):
    """Ajusta las calorías según el objetivo del usuario"""
    goal_adjustments = {
        "Bajar de peso": -500,
        "Ganar masa muscular": +300,
        "Mantenerse": 0
    }
    return tdee + goal_adjustments.get(goal, 0)

def calculate_macros(calories, goal):
    """Calcula la distribución de macronutrientes"""
    if goal == "Bajar de peso":
        protein_pct = 0.35  # 35% proteína
        carb_pct = 0.35     # 35% carbohidratos
        fat_pct = 0.30      # 30% grasa
    elif goal == "Ganar masa muscular":
        protein_pct = 0.30
        carb_pct = 0.45
        fat_pct = 0.25
    else:  # Mantenerse
        protein_pct = 0.30
        carb_pct = 0.40
        fat_pct = 0.30
    
    protein_g = (calories * protein_pct) / 4
    carb_g = (calories * carb_pct) / 4
    fat_g = (calories * fat_pct) / 9
    
    return protein_g, carb_g, fat_g

def show():
    st.title("📊 Planificador de Comidas MealSmart")
    st.markdown("### Calcula tus necesidades nutricionales y obtén recomendaciones personalizadas")
    
    # Formulario de entrada
    with st.form("nutrition_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Información Personal")
            age = st.slider("Edad", min_value=12, max_value=99, value=30, help="Selecciona tu edad")
            gender = st.selectbox("Género", ["Masculino", "Femenino"])
            weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)
            height = st.number_input("Altura (cm)", min_value=100, max_value=250, value=170, step=1)
        
        with col2:
            st.subheader("🎯 Objetivos y Actividad")
            goal = st.selectbox(
                "Tu objetivo",
                ["Bajar de peso", "Ganar masa muscular", "Mantenerse"],
                help="Selecciona tu objetivo principal"
            )
            
            activity = st.selectbox(
                "Nivel de actividad física",
                [
                    "Sedentario (poco o nada de ejercicio)",
                    "Ligero (ejercicio ligero 1-3 días/semana)",
                    "Moderado (ejercicio moderado 3-5 días/semana)",
                    "Intenso (ejercicio duro 6-7 días/semana)",
                    "Muy intenso (ejercicio muy duro y trabajo físico)"
                ]
            )
        
        submitted = st.form_submit_button("🚀 Calcular Mi Plan", type="primary")
    
    # Cálculos y resultados
    if submitted:
        # Realizar cálculos
        bmr = calculate_bmr(weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity)
        goal_calories = get_goal_calories(tdee, goal)
        protein, carbs, fat = calculate_macros(goal_calories, goal)
        
        # Mostrar resultados
        st.success("✅ ¡Cálculo completado!")
        st.markdown("---")
        
        # Métricas principales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("TDEE (Calorías Base)", f"{int(tdee)} kcal")
        
        with col2:
            st.metric("Calorías Objetivo", f"{int(goal_calories)} kcal", 
                     delta=int(goal_calories-tdee))
        
        with col3:
            st.metric("Proteína", f"{int(protein)}g")
        
        with col4:
            st.metric("Carbohidratos", f"{int(carbs)}g")
        
        st.markdown("---")
        
        # Gráfico de macronutrientes
        st.subheader("📊 Distribución de Macronutrientes")
        
        fig = px.pie(
            values=[protein*4, carbs*4, fat*9],
            names=["Proteína", "Carbohidratos", "Grasas"],
            color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#FFE66D"],
            title="Distribución de Calorías por Macronutriente"
        )
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
        
        # Plan de comidas sugerido
        st.subheader("🍽️ Plan de Comidas Sugerido")
        
        # Dividir calorías en las 3 comidas principales
        breakfast_cals = int(goal_calories * 0.25)
        lunch_cals = int(goal_calories * 0.40)
        dinner_cals = int(goal_calories * 0.35)
        
        meals = {
            "Desayuno": breakfast_cals,
            "Almuerzo": lunch_cals,
            "Cena": dinner_cals
        }
        
        # Mostrar plan de comidas
        col1, col2, col3 = st.columns(3)
        
        for i, (meal, cals) in enumerate(meals.items()):
            with [col1, col2, col3][i]:
                st.info(f"""
                **{meal}**  
                📍 {cals} kcal
                
                *Comidas sugeridas próximamente...*
                """)
        
        st.markdown("---")
        
        # Tabla detallada de macronutrientes
        st.subheader("📋 Resumen Nutricional Diario")
        
        df = pd.DataFrame({
            "Macronutriente": ["Proteína", "Carbohidratos", "Grasas"],
            "Cantidad (g)": [int(protein), int(carbs), int(fat)],
            "Calorías": [int(protein*4), int(carbs*4), int(fat*9)],
            "% del total": ["30-35%", "35-45%", "25-30%"]
        })
        
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Recomendaciones
        st.markdown("---")
        st.subheader("💡 Recomendaciones")
        
        recommendations = {
            "Bajar de peso": [
                "• Consume proteínas en cada comida para mantener la saciedad",
                "• Prioriza carbohidratos complejos (avena, arroz integral, quinoa)",
                "• Aumenta tu ingesta de vegetales frescos",
                "• Bebe al menos 2 litros de agua al día",
                "• Realiza 3-4 comidas al día sin saltarte ninguna"
            ],
            "Ganar masa muscular": [
                "• Consume proteínas de calidad (pollo, pescado, huevos, legumbres)",
                "• Incluye carbohidratos post-entrenamiento",
                "• Distribuye las proteínas uniformemente a lo largo del día",
                "• Considera consumir un snack proteico antes de dormir",
                "• No te saltes las comidas, especialmente desayuno y cena"
            ],
            "Mantenerse": [
                "• Mantén una dieta balanceada con todos los grupos alimenticios",
                "• Consume 5 porciones de frutas y verduras al día",
                "• Mantén una rutina de ejercicio regular",
                "• Hidrátate adecuadamente durante todo el día",
                "• Escucha a tu cuerpo y ajusta según sea necesario"
            ]
        }
        
        for rec in recommendations.get(goal, []):
            st.markdown(rec)
        
        # Imagen motivacional
        st.markdown("---")
        fruits_image = os.path.join("images", "fruits.jpg")
        if os.path.exists(fruits_image):
            try:
                img = Image.open(fruits_image)
                st.image(img, width=600, caption="Alimentación saludable = Vida saludable")
            except:
                pass

