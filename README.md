# 🏥 Medical Diagnosis System (CDSS)

## 📌 Project Overview
This is an AI-powered Clinical Decision Support System (CDSS) that predicts the risk of multiple diseases using machine learning models.

The system analyzes patient medical data and provides:
- Risk prediction
- Probability score
- Clinical interpretation
- Recommendations

---

## ⚙️ Features

### 🫀 Heart Disease Prediction
Predicts risk based on ECG, BP, cholesterol, and other parameters.

### 🍬 Diabetes Prediction
Estimates diabetes risk using glucose, insulin, BMI, and related factors.

### 🧠 Kidney Disease Prediction
Analyzes kidney health using blood and urine parameters.

### 🧬 Liver Disease Prediction
Evaluates liver condition using enzyme and bilirubin levels.

---

## 🧠 Core Functionality

For each prediction, the system provides:

- 📊 Risk Probability (%)
- ⚠️ Risk Level (Low / Moderate / High)
- 🧾 Clinical Interpretation
- 🚨 Warning Signs
- 💡 Recommendations (diet, lifestyle, precautions)

---

## 📄 Report Generation

The system generates a:

👉 **Educational Medical Screening Report (PDF)**

Includes:
- Patient input data
- Prediction result
- Risk analysis
- Recommendations
- Disclaimer

---

## 🛠️ Technologies Used

- Python 🐍
- Streamlit ⚡
- Scikit-learn 🤖
- Pandas 📊
- NumPy
- Joblib

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt