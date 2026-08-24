import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

@st.cache_resource
def get_liver_resources():
    # Points to Medical_Diagnosis_System/models/liver_app/
    model_path = Path(__file__).parent.parent / "models" / "liver_app"
    
    model = joblib.load(model_path / "liver_model.pkl")
    features = joblib.load(model_path / "liver_features.pkl")
    scaler = joblib.load(model_path / "liver_scaler.pkl") if (model_path / "liver_scaler.pkl").exists() else None
    
    return model, features, scaler

def run_liver_app():
    st.title("🧬 Liver Disease Prediction Tool")
    st.markdown("Enter clinical and demographic details to assess liver disease risk.")
    
    model, features, scaler = get_liver_resources()
    
    with st.form("liver_form"):
        st.subheader("Patient Demographics & Clinical Markers")
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age (Years)", min_value=1, max_value=100, value=45, step=1)
            gender_input = st.selectbox("Gender", options=["Male", "Female"])
            tot_bilirubin = st.number_input("Total Bilirubin (mg/dL)", min_value=0.0, value=1.0, step=0.1)
            direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)", min_value=0.0, value=0.3, step=0.1)
            tot_proteins = st.number_input("Total Proteins (g/dL)", min_value=0.0, value=6.5, step=0.1)
        with col2:
            albumin = st.number_input("Albumin (g/dL)", min_value=0.0, value=3.5, step=0.1)
            ag_ratio = st.number_input("A/G Ratio", min_value=0.0, value=1.0, step=0.1)
            sgpt = st.number_input("SGPT / ALT (U/L)", min_value=0.0, value=25.0, step=1.0)
            sgot = st.number_input("SGOT / AST (U/L)", min_value=0.0, value=25.0, step=1.0)
            alkphos = st.number_input("Alkaline Phosphatase (IU/L)", min_value=0.0, value=120.0, step=1.0)

        submit_button = st.form_submit_button(label="Predict Liver Disease", use_container_width=True)

    if submit_button:
        gender = 1 if gender_input == "Male" else 0
        
        input_data = {
            'age': age, 'gender': gender, 'tot_bilirubin': tot_bilirubin,
            'direct_bilirubin': direct_bilirubin, 'tot_proteins': tot_proteins,
            'albumin': albumin, 'ag_ratio': ag_ratio, 'sgpt': sgpt,
            'sgot': sgot, 'alkphos': alkphos
        }
        
        # Ensure column ordering matches training
        input_df = pd.DataFrame([input_data])[features]
        
        # Scale if scaler is present
        if scaler:
            input_scaled = pd.DataFrame(scaler.transform(input_df), columns=input_df.columns)
        else:
            input_scaled = input_df
            
        # Prediction
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]
        
        st.markdown("---")
        st.subheader("Prediction Results")
        
        if prediction == 1:
            st.error("🚨 **High Risk of Liver Disease Detected**")
            st.write("Clinical markers are consistent with liver disease. Please consult a healthcare professional.")
        else:
            st.success("✅ **Low Risk / Healthy Profile**")
            st.write("Clinical markers are currently within a healthy range.")
            
        st.markdown("### Model Confidence")
        mcol1, mcol2 = st.columns(2)
        mcol1.metric(label="Probability of Liver Disease", value=f"{probabilities[1] * 100:.1f}%")
        mcol2.metric(label="Probability of Healthy", value=f"{probabilities[0] * 100:.1f}%")