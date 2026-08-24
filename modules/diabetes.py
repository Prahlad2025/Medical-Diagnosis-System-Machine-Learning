import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

@st.cache_resource
def get_diabetes_resources():
    # Points to Medical_Diagnosis_System/models/diabetes_app/
    model_path = Path(__file__).parent.parent / "models" / "diabetes_app"
    
    model = joblib.load(model_path / "diabetes_model.pkl")
    scaler = joblib.load(model_path / "diabetes_scaler.pkl")
    features = joblib.load(model_path / "diabetes_features.pkl")
    return model, features, scaler

def run_diabetes_app():
    st.title("🩸 Diabetes Risk Prediction")
    st.markdown("Clinical-grade screening tool for diabetes risk assessment.")
    
    model, expected_columns, scaler = get_diabetes_resources()
    
    with st.form("diabetes_form"):
        col1, col2 = st.columns(2)
        with col1:
            pregnancies = st.number_input("Pregnancies", 0, 20, 1)
            glucose = st.number_input("Glucose Level (mg/dL)", 0.0, 300.0, 120.0)
            blood_pressure = st.number_input("Blood Pressure (mm Hg)", 0.0, 200.0, 70.0)
            skin_thickness = st.number_input("Skin Thickness (mm)", 0.0, 100.0, 20.0)
        with col2:
            insulin = st.number_input("Insulin Level (mu U/ml)", 0.0, 900.0, 80.0)
            bmi = st.number_input("BMI (Body Mass Index)", 0.0, 70.0, 32.0, step=0.1)
            dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5, step=0.01)
            age = st.number_input("Age (Years)", 1, 120, 30)
        
        submit = st.form_submit_button("Calculate Diabetes Risk", type="primary")
    
    if submit:
        data_vector = {
            "Pregnancies": pregnancies, "Glucose": glucose, "BloodPressure": blood_pressure,
            "SkinThickness": skin_thickness, "Insulin": insulin, "BMI": bmi,
            "DiabetesPedigreeFunction": dpf, "Age": age
        }
        
        # Align with training features
        input_df = pd.DataFrame([data_vector])[expected_columns]
        
        # Preprocessing
        input_df['DiabetesPedigreeFunction'] = np.log1p(input_df['DiabetesPedigreeFunction'])
        input_df[['Glucose', 'BloodPressure']] = input_df[['Glucose', 'BloodPressure']].replace(0, np.nan).fillna(120.0)
        
        # Scale and Predict
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]
        
        st.markdown("---")
        st.subheader("Diagnostic Evaluation")
        if prediction == 1:
            st.error(f"🚨 **High Risk Identified:** {probability:.2%} likelihood of diabetes.")
        else:
            st.success(f"💚 **Low Risk Identified:** {probability:.2%} likelihood of diabetes.")
        
        st.write("---")
        st.caption("Medical Disclaimer: This diagnostic output is for screening purposes and requires formal verification by a physician.")