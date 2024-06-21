import streamlit as st
import pickle 
import numpy as np 

with open("xgb_classifier.pkl", "rb") as file:
    xgb_model = pickle.load(file)

st.title("Apollo Drug Prediction")
drug_dct = {0:"drugA",1:"drugB",2:"drugC",3:"drugX",
            4:"drugY"}

def predict_function(Age,Sex,Bp,Cholesterol,Na_to_K):
    input_array = np.array([[Age,Sex,Bp,Cholesterol,Na_to_K]])
    prediction = xgb_model.predict(input_array)
    prediction = drug_dct[prediction[0]]
    return prediction

Age = st.slider('Age',min_value=1, max_value=100, value= 50)
Sex = st.selectbox('Sex', ['Male','Female'])
Bp = st.selectbox('Blood Pressure', ['Low','Normal','High'])
Cholesterol = st.selectbox('Cholesterol', ['Normal','High'])
Na_to_K = st.slider('Na_to_K',min_value=1, max_value=50, value= 22)

Sex = 1 if Sex == "Female" else 0
bp_mapping = {'Low':0,'Normal' : 1, 'High':2}
Cholesterol_mapping = {'Normal' : 0, 'High':1}
Bp = bp_mapping[Bp]
Cholesterol = Cholesterol_mapping[Cholesterol]

if st.button("Predict"):
    prediction = predict_function(Age,Sex,Bp,Cholesterol,Na_to_K)
    st.write(f"The prescribed drug for this subject is {prediction}")