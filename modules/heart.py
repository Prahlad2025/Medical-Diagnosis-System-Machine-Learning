import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --- CACHED MODEL LOADING ---
@st.cache_resource
def get_heart_resources():
    model_path = Path(__file__).parent.parent / "models" / "heart_app"
    model = joblib.load(model_path / "heart_model.pkl")
    scaler = joblib.load(model_path / "heart_scaler.pkl")
    expected_columns = joblib.load(model_path / "heart_features.pkl")
    return model, scaler, expected_columns

def run_heart_app():
    model, scaler, expected_columns = get_heart_resources()

    # Added Heart Emoji
    st.title("❤️ Heart Stroke Prediction")
    st.markdown("Provide the following details to check your heart stroke risk:")

    # Your original input logic preserved exactly
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    if st.button("Predict"):
        # Your original raw_input dictionary mapping
        raw_input = {
            'Age': age,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'MaxHR': max_hr,
            'Oldpeak': oldpeak,
            'Sex_' + sex: 1,
            'ChestPainType_' + chest_pain: 1,
            'RestingECG_' + resting_ecg: 1,
            'ExerciseAngina_' + exercise_angina: 1,
            'ST_Slope_' + st_slope: 1
        }

        # Your original dataframe and feature handling
        input_df = pd.DataFrame([raw_input])

        # Fill missing columns with 0s
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Reorder columns
        input_df = input_df[expected_columns]

        # Scale the input
        scaled_input = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(scaled_input)[0]

        # Added Probability display
        try:
            prob = model.predict_proba(scaled_input)[0][1]
            st.metric("Risk Probability", f"{prob*100:.2f}%")
        except:
            st.write("Probability not available.")

        # Show result
        if prediction == 1:
            st.error("⚠️ High Risk of Heart Disease")
        else:
            st.success("✅ Low Risk of Heart Disease")