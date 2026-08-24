# Medical Diagnosis System | Machine Learning

An **AI-powered Medical Diagnosis System** developed using **Python, Streamlit, and Machine Learning** to predict the likelihood of **Heart, Diabetes, Kidney, and Liver diseases** based on patient health parameters.

The system integrates multiple machine learning models to provide real-time disease prediction, risk assessment, and clinical recommendations through an interactive web interface.

## Features

* Heart Disease Prediction
* Diabetes Prediction
* Kidney Disease Prediction
* Liver Disease Prediction
* Multiple Machine Learning Models
* Real-time Disease Prediction
* Risk Assessment
* Clinical Recommendations
* Interactive Streamlit Web Interface

## Machine Learning Models

| Model               | Purpose                                                    |
| ------------------- | ---------------------------------------------------------- |
| Logistic Regression | Baseline classification model                              |
| Random Forest       | Ensemble learning using multiple decision trees            |
| Gradient Boosting   | Sequential ensemble learning technique                     |
| XGBoost             | Optimized gradient boosting algorithm                      |
| CatBoost            | Gradient boosting algorithm with categorical data handling |

## Technologies Used

| Technology           | Purpose                             |
| -------------------- | ----------------------------------- |
| Python               | Core programming language           |
| Scikit-learn         | Machine learning and preprocessing  |
| XGBoost              | Gradient boosting                   |
| CatBoost             | Gradient boosting                   |
| Pandas               | Data preprocessing and manipulation |
| NumPy                | Numerical operations                |
| Streamlit            | Web application interface           |
| Matplotlib / Seaborn | Data visualization                  |

## System Workflow

```text
Patient Health Parameters
          ↓
    Data Preprocessing
          ↓
   Feature Transformation
          ↓
    Trained ML Models
          ↓
    Disease Prediction
          ↓
 Risk Assessment & Recommendation
          ↓
   Streamlit Web Interface
```

## Project Structure

```text
Medical-Diagnosis-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── heart_model.pkl
│   ├── diabetes_model.pkl
│   ├── kidney_model.pkl
│   └── liver_model.pkl
│
├── datasets/
│   ├── heart.csv
│   ├── diabetes.csv
│   ├── kidney.csv
│   └── liver.csv
│
└── notebooks/
    └── model_training.ipynb
```

> The exact project structure may vary depending on the implementation.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/medical-diagnosis-system.git
cd medical-diagnosis-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## How It Works

1. The user selects the required disease prediction module.
2. Patient health parameters are entered through the Streamlit interface.
3. Input data is preprocessed according to the trained model.
4. The corresponding machine learning model generates a prediction.
5. The system displays the predicted disease risk.
6. Risk assessment and clinical recommendations are provided through the interface.

## Model Pipeline

```text
Raw Patient Data
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
Data Preprocessing
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Saving
       ↓
Streamlit Deployment
```

## Future Improvements

* Hyperparameter tuning for improved model performance
* Explainable AI using SHAP or LIME
* Model performance comparison dashboard
* Patient prediction history
* Secure user authentication
* Cloud deployment
* Improved clinical recommendation system

## Disclaimer

This project is developed **for educational and demonstration purposes only**. It is not intended to replace professional medical diagnosis, medical advice, or consultation with a qualified healthcare professional.

## Author

**Piyush Bhivgade**

Machine Learning | Data Science | Python
