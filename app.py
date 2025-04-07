import streamlit as st
import pandas as pd
import joblib


model = joblib.load('rf_model.pkl')

st.title('Cálculo da Dureza (HRC) após Revenimento com ML')

st.subheader('Insira os dados de entrada:')


col1, col2, col3 = st.columns(3)

with col1:
    Ttime = st.number_input('Tempo Rev. (s) [115.200 s máx.]', format="%.1f")
    Mn = st.number_input('Manganes (Mn) [0,30 - 1,85 máx.]', format="%.3f")
    Si = st.number_input('Silício (Si) [1,62 máx.]', format="%.3f")
    Mo = st.number_input('Molibdênio (Mo) [0,36 máx.]', format="%.3f")
    Cu = st.number_input('Cobre (Cu) [0,08 máx.]', format="%.3f")
    
with col2:
    Ttemp = st.number_input('Temperatura Rev. (ºC) [100 - 700 máx.]', format="%.1f")
    P = st.number_input('Fósforo (P) [0,054 máx.]', format="%.3f")
    Ni = st.number_input('Níquel (Ni) [3,41 máx.]', format="%.3f")
    V = st.number_input('Vanádio (V) [0,16 máx.]', format="%.3f")
    

with col3:
    C = st.number_input('Carbono (C) [1,15 máx.]', format="%.3f")
    S = st.number_input('Enxofre (S) [0,055 máx.]', format="%.3f")
    Cr = st.number_input('Cromo (Cr) [1,57 máx.]', format="%.3f")
    Al = st.number_input('Alumínio (Al) [1,26 máx.]', format="%.3f")
        

# Previsão
if st.button('Calcular Dureza (HRC)'):
    features = pd.DataFrame({
        'Tempering time (s)': [Ttime],
        'Tempering temperature (ºC)': [Ttemp],
        'C (%wt)': [C],
        'Mn (%wt)': [Mn],
        'P (%wt)': [P],
        'S (%wt)': [S],
        'Si (%wt)': [Si],
        'Ni (%wt)': [Ni],
        'Cr (%wt)': [Cr],
        'Mo (%wt)': [Mo],
        'V (%wt)': [V],
        'Al (%wt)': [Al],
        'Cu (%wt)': [Cu],
               
    })

    prediction = model.predict(features)

    st.write(f'A dureza é: {prediction[0]:,.2f}HRC')

