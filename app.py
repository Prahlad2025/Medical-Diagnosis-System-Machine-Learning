import streamlit as st
from modules import heart, diabetes, kidney, liver

# Page Configuration
st.set_page_config(
    page_title="Medical Diagnosis System",
    page_icon="🏥",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f0f2f6; }
    .stApp { background-color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("🏥 Medical Diagnosis")
    st.markdown("---")
    page = st.radio("Select Diagnostic Module", [
        "🏠 Home", 
        "❤️ Heart Disease", 
        "🩸 Diabetes", 
        "🩺 Kidney Disease", 
        "🧬 Liver Disease"
    ])
    st.markdown("---")
    st.info("Version 1.0.0 | Production Ready")

# Routing
if page == "🏠 Home":
    st.title("Professional Medical Diagnosis System")
    st.write("Welcome to the integrated clinical decision support system.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Overview")
        st.write("This application provides a centralized interface for AI-powered disease screening.")
    with col2:
        st.subheader("Available Modules")
        st.write("- Heart Disease Screening")
        st.write("- Diabetes Risk Assessment")
        st.write("- Chronic Kidney Disease Screening")
        st.write("- Liver Patient Analysis")
        
elif page == "❤️ Heart Disease":
    heart.run_heart_app()
elif page == "🩸 Diabetes":
    diabetes.run_diabetes_app()
elif page == "🩺 Kidney Disease":
    kidney.run_kidney_app()
elif page == "🧬 Liver Disease":
    liver.run_liver_app()

# Footer
st.sidebar.markdown("<br><br><br><center>System © 2026</center>", unsafe_allow_html=True)