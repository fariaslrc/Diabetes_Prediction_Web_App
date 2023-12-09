# -*- coding: utf-8 -*-
"""
Created on Sat Dec 9 19:31:51 2023

@author: fariaslrc
"""

# Importando as bibliotecas
import numpy as np
import pickle
import streamlit as st
from pages.Sobre import show_creator_page

loaded_model = pickle.load(open('trained_model.sav','rb'))

#criando função para previsão
def diabetes_prediction(input_data):   

    # alterando input_data para array numpy
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape o array para predizer uma instância
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'A pessoa não é diabética'
    else:
        return 'A pessoa é diabética'


def main():
    
    st.set_page_config(layout="wide", page_icon="📊")

    st.title('Previsão de Diabetes')   
    
    # Adiciona informações descritivas para cada variável
    info_pregnancies = "Número de vezes que engravidou."
    info_glucose = "Concentração de glicose plasmática após 2 horas em um teste oral de tolerância à glicose."
    info_blood_pressure = "Pressão arterial diastólica (mm Hg)."
    info_skin_thickness = "Espessura da dobra cutânea do tríceps (mm)."
    info_insulin = "Insulina sérica de 2 horas (mu U/ml)."
    info_bmi = "Índice de massa corporal (peso em kg/(altura em m)^2)."
    info_diabetes_pedigree_function = "Função de pedigree do diabetes."
    info_age = "Idade em anos."

    # Define sliders com informações descritivas
    Pregnancies = st.slider('Número de gestações', min_value=0, max_value=20, value=0, step=1, help=info_pregnancies)
    Glucose = st.slider('Nível de glicose', min_value=0, max_value=199, value=80, step=1, help=info_glucose)
    BloodPressure = st.slider('Nível de pressão arterial em mm Hg', min_value=0, max_value=140, value=80, step=1, help=info_blood_pressure)
    SkinThickness = st.slider('Espessura da pele em mm', min_value=0, max_value=100, value=40, step=1, help=info_skin_thickness)
    Insulin = st.slider('Nível de insulina em mu U/ml', min_value=0, max_value=1000, value=400, step=1, help=info_insulin)
    BMI = st.slider('Valor do IMC', min_value=0.0, max_value=70.0, value=33.3, step=0.01, help=info_bmi)
    DiabetesPedigreeFunction = st.slider('Valor da função de pedigree de diabetes', min_value=0.000, step=0.001, max_value=3.0, value=0.045, format="%3f", help=info_diabetes_pedigree_function)
    Age = st.slider('Idade da pessoa', min_value=10, max_value=100, value=21, step=1, help=info_age)
   
    diagnosis = ''
    if st.button('Resultado do teste de diabetes'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)  


if __name__ == '__main__':
     main()    