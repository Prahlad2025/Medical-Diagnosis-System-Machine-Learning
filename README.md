# 🏥 Medical Diagnosis System (CDSS)

## 📌 Project Overview

The **Medical Diagnosis System** is a Machine Learning-based **Clinical Decision Support System (CDSS)** that predicts the risk of multiple diseases based on patient medical data.

The system provides:

* Risk prediction
* Probability score
* Risk level
* Clinical interpretation
* Recommendations

> **Note:** This project is for educational and screening purposes only. It is not a replacement for professional medical advice or diagnosis.

---

## ⚙️ Features

### 🫀 Heart Disease Prediction

Predicts heart disease risk using parameters such as blood pressure, cholesterol, ECG-related values, and other health information.

### 🍬 Diabetes Prediction

Estimates diabetes risk using parameters such as glucose level, insulin, BMI, and other relevant health factors.

### 🧠 Kidney Disease Prediction

Analyzes kidney-related blood and urine parameters to predict the possibility of kidney disease.

### 🧬 Liver Disease Prediction

Evaluates liver health using parameters such as enzyme levels, bilirubin, and other medical information.

---

## 🧠 Core Functionality

For each prediction, the system provides:

* 📊 **Risk Probability (%)**
* ⚠️ **Risk Level** — Low / Moderate / High
* 🧾 **Clinical Interpretation**
* 🚨 **Warning Signs**
* 💡 **Recommendations** related to diet, lifestyle, and precautions

---

## 📄 Report Generation

The system can generate an:

### **Educational Medical Screening Report (PDF)**

The report includes:

* Patient input data
* Prediction result
* Risk analysis
* Recommendations
* Medical disclaimer

---

## 🛠️ Technologies Used

* 🐍 **Python**
* ⚡ **Streamlit**
* 🤖 **Scikit-learn**
* 📊 **Pandas**
* 🔢 **NumPy**
* 💾 **Joblib**

---

## 🚀 How to Run

### 1. Open the Project

Open the project folder in **VS Code**.

Open the terminal:

**Terminal → New Terminal**

### 2. Activate Virtual Environment

Run:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Run:

```powershell
pip install -r requirements.txt
```

This installs all the required Python libraries.

### 4. Run the Application

Run:

```powershell
streamlit run app.py
```

The application will start.

Open the following link in your browser:

```text
http://localhost:8501
```

---

## ⚠️ Disclaimer

This application is developed for **educational and demonstration purposes**.

The predictions and recommendations provided by this system should **not be considered a medical diagnosis or professional medical advice**. Please consult a qualified healthcare professional for medical evaluation and treatment.

---

## 👨‍💻 Author

**Prahlad**

GitHub: **Prahlad2025**
