import streamlit as st
from modules import heart, diabetes, kidney, liver

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Medical Diagnosis System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# SESSION STATE
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# PAGE LIST
pages = [
    "🏠 Home",
    "❤️ Heart Disease",
    "🩸 Diabetes",
    "🩺 Kidney Disease",
    "🧬 Liver Disease"
]

# SIDEBAR
with st.sidebar:

    st.title("🏥 Medical Diagnosis")

    st.caption(
        "AI-powered preliminary health screening"
    )

    st.divider()

    selected_page = st.radio(
        "Select Diagnostic Module",
        pages,
        index=pages.index(st.session_state.page)
    )

    if selected_page != st.session_state.page:
        st.session_state.page = selected_page
        st.rerun()

    st.divider()

    st.info(
        "Select a disease module to enter health "
        "parameters and receive a preliminary risk assessment."
    )

    st.divider()

    st.caption("Medical Diagnosis System")
    st.caption("Machine Learning Project • 2026")


# CURRENT PAGE
page = st.session_state.page


# HOME PAGE
if page == "🏠 Home":

    # HEADER
    st.title("🏥 Medical Diagnosis System")

    st.subheader(
        "AI-Powered Health Screening & Risk Assessment"
    )

    st.write(
        "An integrated machine learning platform for "
        "preliminary screening and risk assessment of "
        "multiple diseases using patient health parameters."
    )

    st.divider()


    # --------------------------------------------------------
    # SYSTEM OVERVIEW
    # --------------------------------------------------------

    st.header("📊 System Overview")

    st.write(
        "Quick overview of the diagnostic platform."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Disease Modules",
            value="4"
        )

    with col2:
        st.metric(
            label="ML Algorithms",
            value="5+"
        )

    with col3:
        st.metric(
            label="Prediction",
            value="Real-Time"
        )

    with col4:
        st.metric(
            label="Platform",
            value="Streamlit"
        )

    st.divider()


    # --------------------------------------------------------
    # DIAGNOSTIC MODULES
    # --------------------------------------------------------

    st.header("🩺 Diagnostic Modules")

    st.write(
        "Select a disease module to perform a preliminary "
        "risk assessment."
    )

    st.write("")


    # ========================================================
    # HEART + DIABETES
    # ========================================================

    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # HEART DISEASE
    # --------------------------------------------------------

    with col1:

        with st.container(border=True):

            st.subheader("❤️ Heart Disease")

            st.write(
                "Analyze cardiovascular health parameters "
                "and estimate the potential risk of heart disease."
            )

            st.caption(
                "Risk Assessment • Cardiovascular Parameters"
            )

            if st.button(
                "Open Heart Disease →",
                key="heart_button",
                use_container_width=True
            ):
                st.session_state.page = "❤️ Heart Disease"
                st.rerun()


    # --------------------------------------------------------
    # DIABETES
    # --------------------------------------------------------

    with col2:

        with st.container(border=True):

            st.subheader("🩸 Diabetes")

            st.write(
                "Evaluate important health parameters "
                "to estimate the potential risk of diabetes."
            )

            st.caption(
                "Risk Assessment • Blood Glucose Parameters"
            )

            if st.button(
                "Open Diabetes →",
                key="diabetes_button",
                use_container_width=True
            ):
                st.session_state.page = "🩸 Diabetes"
                st.rerun()


    st.write("")


    # ========================================================
    # KIDNEY + LIVER
    # ========================================================

    col3, col4 = st.columns(2)


    # --------------------------------------------------------
    # KIDNEY DISEASE
    # --------------------------------------------------------

    with col3:

        with st.container(border=True):

            st.subheader("🩺 Kidney Disease")

            st.write(
                "Assess clinical health parameters associated "
                "with potential kidney disease risk."
            )

            st.caption(
                "Risk Assessment • Kidney Function Parameters"
            )

            if st.button(
                "Open Kidney Disease →",
                key="kidney_button",
                use_container_width=True
            ):
                st.session_state.page = "🩺 Kidney Disease"
                st.rerun()


    # --------------------------------------------------------
    # LIVER DISEASE
    # --------------------------------------------------------

    with col4:

        with st.container(border=True):

            st.subheader("🧬 Liver Disease")

            st.write(
                "Analyze liver-related health parameters "
                "and estimate the potential risk of liver disease."
            )

            st.caption(
                "Risk Assessment • Liver Function Parameters"
            )

            if st.button(
                "Open Liver Disease →",
                key="liver_button",
                use_container_width=True
            ):
                st.session_state.page = "🧬 Liver Disease"
                st.rerun()


    st.divider()


    # --------------------------------------------------------
    # HOW IT WORKS
    # --------------------------------------------------------

    st.header("⚙️ How It Works")

    st.write(
        "The system follows a simple three-step "
        "machine learning workflow."
    )

    step1, step2, step3 = st.columns(3)


    with step1:

        with st.container(border=True):

            st.subheader("01")

            st.subheader("Enter Parameters")

            st.write(
                "Enter the required patient health "
                "parameters in the selected disease module."
            )


    with step2:

        with st.container(border=True):

            st.subheader("02")

            st.subheader("ML Analysis")

            st.write(
                "The trained machine learning model "
                "analyzes the provided parameters."
            )


    with step3:

        with st.container(border=True):

            st.subheader("03")

            st.subheader("View Assessment")

            st.write(
                "View the predicted result and "
                "preliminary risk assessment."
            )


    st.divider()


    # --------------------------------------------------------
    # MACHINE LEARNING TECHNOLOGY
    # --------------------------------------------------------

    st.header("🤖 Machine Learning Technology")

    st.write(
        "Multiple machine learning algorithms are used "
        "across the diagnostic modules."
    )

    tech1, tech2, tech3 = st.columns(3)


    with tech1:
        st.info(
            "🌲 **Random Forest**\n\n"
            "An ensemble learning algorithm based on "
            "multiple decision trees."
        )


    with tech2:
        st.info(
            "📈 **Gradient Boosting**\n\n"
            "A boosting technique that combines "
            "multiple weak learners."
        )


    with tech3:
        st.info(
            "📊 **Logistic Regression**\n\n"
            "A classification algorithm used for "
            "disease risk prediction."
        )


    tech4, tech5 = st.columns(2)


    with tech4:
        st.info(
            "⚡ **XGBoost**\n\n"
            "An efficient gradient boosting algorithm "
            "for structured data."
        )


    with tech5:
        st.info(
            "🧠 **CatBoost**\n\n"
            "A gradient boosting algorithm designed "
            "to handle different types of data."
        )


    st.divider()


    # --------------------------------------------------------
    # IMPORTANT NOTICE
    # --------------------------------------------------------

    st.warning(
        """
        **⚠️ Important Notice**

        This application is intended for educational and
        preliminary screening purposes only.

        The predictions generated by the machine learning
        models should not be considered a medical diagnosis.

        Always consult a qualified healthcare professional
        for medical advice, diagnosis, or treatment.
        """
    )


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    st.divider()

    st.caption(
        "Medical Diagnosis System • "
        "Machine Learning Project • 2026"
    )


# ============================================================
# HEART DISEASE PAGE
# ============================================================

elif page == "❤️ Heart Disease":

    if st.button(
        "← Back to Home",
        key="back_heart"
    ):
        st.session_state.page = "🏠 Home"
        st.rerun()
    
    heart.run_heart_app()


# ============================================================
# DIABETES PAGE
# ============================================================

elif page == "🩸 Diabetes":

    if st.button(
        "← Back to Home",
        key="back_diabetes"
    ):
        st.session_state.page = "🏠 Home"
        st.rerun()

    diabetes.run_diabetes_app()


# ============================================================
# KIDNEY DISEASE PAGE
# ============================================================

elif page == "🩺 Kidney Disease":

    if st.button(
        "← Back to Home",
        key="back_kidney"
    ):
        st.session_state.page = "🏠 Home"
        st.rerun()

    kidney.run_kidney_app()


# ============================================================
# LIVER DISEASE PAGE
# ============================================================

elif page == "🧬 Liver Disease":

    if st.button(
        "← Back to Home",
        key="back_liver"
    ):
        st.session_state.page = "🏠 Home"
        st.rerun()

    liver.run_liver_app()
