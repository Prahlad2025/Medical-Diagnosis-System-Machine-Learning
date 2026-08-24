import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

@st.cache_resource
def get_kidney_resources():
    # Path configuration using pathlib
    model_path = Path(__file__).parent.parent / "models" / "kidney_app"
    
    model = joblib.load(model_path / "kidney_model.pkl")
    scaler = joblib.load(model_path / "kidney_scaler.pkl")
    features = joblib.load(model_path / "kidney_features.pkl")
    return model, features, scaler

def run_kidney_app():
    # Inject CSS once within the module
    st.markdown("""
    <style>
    .result{
        padding:18px;
        border-radius:10px;
        font-size:22px;
        font-weight:bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🩺 Chronic Kidney Disease Prediction")
    st.write("Fill the patient details and click **Predict**.")

    model, features, scaler = get_kidney_resources()

    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.number_input("Age", 0.0, 120.0, 45.0)
        bp = st.number_input("Blood Pressure", 0.0, 250.0, 80.0)
        sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
        al = st.selectbox("Albumin", [0, 1, 2, 3, 4, 5])
        su = st.selectbox("Sugar", [0, 1, 2, 3, 4, 5])
        rbc = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"])
        pc = st.selectbox("Pus Cells", ["Normal", "Abnormal"])
        pcc = st.selectbox("Pus Cell Clumps", ["Present", "Not Present"])

    with c2:
        ba = st.selectbox("Bacteria", ["Present", "Not Present"])
        bgr = st.number_input("Blood Glucose Random", 0.0, 500.0, 120.0)
        bu = st.number_input("Blood Urea", 0.0, 300.0, 40.0)
        sc = st.number_input("Serum Creatinine", 0.0, 20.0, 1.2)
        sod = st.number_input("Sodium", 0.0, 200.0, 138.0)
        pot = st.number_input("Potassium", 0.0, 50.0, 4.5)
        hemo = st.number_input("Hemoglobin", 0.0, 20.0, 13.5)
        pcv = st.number_input("Packed Cell Volume", 0.0, 60.0, 40.0)

    with c3:
        wbc = st.number_input("White Blood Cell Count", 0.0, 30000.0, 8000.0)
        rcc = st.number_input("Red Blood Cell Count", 0.0, 10.0, 4.8)
        htn = st.selectbox("Hypertension", ["No", "Yes"])
        dm = st.selectbox("Diabetes Mellitus", ["No", "Yes"])
        cad = st.selectbox("Coronary Artery Disease", ["No", "Yes"])
        appet = st.selectbox("Appetite", ["Good", "Poor"])
        pe = st.selectbox("Pedal Edema", ["No", "Yes"])
        ane = st.selectbox("Anemia", ["No", "Yes"])

    enc = {
        "Normal": 1, "Abnormal": 0,
        "Present": 1, "Not Present": 0,
        "Yes": 1, "No": 0,
        "Good": 1, "Poor": 0
    }

    data = {
        'Age': age, 'Blood_Pressure': bp, 'Specific_Gravity': sg, 'Albumin': al,
        'Sugar': su, 'Red_Blood_Cells': enc[rbc], 'Pus_Cells': enc[pc],
        'Pus_Cell_Clumps': enc[pcc], 'Bacteria': enc[ba], 'Blood_Glucose_Random': bgr,
        'Blood_Urea': bu, 'Serum_Creatinine': sc, 'Sodium': sod, 'Potassium': pot,
        'Hemoglobin': hemo, 'Packed_Cell_Volume': pcv, 'White_Blood_Cell_Count': wbc,
        'Red_Blood_Cell_Count': rcc, 'Hypertension': enc[htn], 'Diabetes_Mellitus': enc[dm],
        'Coronary_Artery_Disease': enc[cad], 'Appetite': enc[appet], 'Pedal_Edema': enc[pe],
        'Anemia': enc[ane]
    }

    if st.button("Predict"):
        input_df = pd.DataFrame([data])[features]
        scaled = scaler.transform(input_df)
        pred = model.predict(scaled)[0]

        try:
            prob = model.predict_proba(scaled)[0][1]
            st.metric("CKD Probability", f"{prob*100:.2f}%")
        except Exception:
            pass

        if pred == 1:
            st.markdown("<div class='result' style='background:#ffebee;color:#c62828;'>⚠️ Chronic Kidney Disease Detected</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result' style='background:#e8f5e9;color:#2e7d32;'>✅ No Chronic Kidney Disease Detected</div>", unsafe_allow_html=True)