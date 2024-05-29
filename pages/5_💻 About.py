import streamlit as st

def about_page():
    st.title("About The Prognostication System")
    st.write("")

    # Create a top bar for navigation
    section = st.radio(
        "Choose to see more information",
        ("Purpose", "Why Use This System?", "Prediction Model", "Model Accuracy", "Features Considered", "Future Enhancements", "Contact Us"),
        horizontal=True
    )
    st.write("")

    if section == "Purpose":
        st.header("Purpose of the System")
        st.write("""
            The Cardiac Arrest Risk Prognosticator is designed to assist medical professionals in 
            evaluating the risk of cardiac arrest based on various health parameters. By inputting specific patient 
            information, the system provides a probabilistic prediction of cardiac arrest risk, helping in early 
            diagnosis and prevention.
        """)
        
    elif section == "Why Use This System?":
        st.header("Why Use This System?")
        st.write("""
            Cardiac arrest is a serious medical condition that can lead to sudden death if not treated immediately. 
            Early prediction and intervention can significantly reduce the mortality rate associated with cardiac 
            arrest. Our system leverages advanced machine learning techniques to offer accurate predictions, 
            aiding healthcare providers in making informed decisions about patient care.
        """)
        
    elif section == "Prediction Model":
        st.header("Prediction Model")
        st.write("""
            The core of our system is powered by the XGBoost algorithm, a highly efficient and scalable implementation 
            of gradient boosting. XGBoost is well-known for its performance and accuracy in various machine learning 
            tasks. Our model has been trained and tested rigorously to ensure reliable predictions.
        """)
        
    elif section == "Model Accuracy":
        st.header("Model Accuracy")
        st.write("""
            Our XGBoost model has been trained on a comprehensive dataset of patient health records, with features 
            including age, gender, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, 
            resting electrocardiogram results, maximum heart rate, number of major vessels affected, thalassemia type, 
            exercise-induced angina, oldpeak, and ST slope. After thorough training and testing, our model achieved 
            an accuracy of 83.61%.
        """)
        
    elif section == "Features Considered":
        st.header("Features Considered")
        st.write("""
            The system takes into account the following features to make its predictions:
            - **Age:** The age of the patient.
            - **Gender:** The gender of the patient.
            - **Chest Pain Type:** The type of chest pain experienced (e.g., Typical Angina, Atypical Angina, etc.).
            - **Resting Blood Pressure:** The patient's blood pressure when at rest.
            - **Serum Cholesterol:** The cholesterol level in the blood.
            - **Fasting Blood Sugar:** Blood sugar levels measured after fasting.
            - **Resting Electrocardiogram Result:** The result of the patient's resting ECG.
            - **Maximum Heart Rate:** The maximum heart rate achieved during exercise.
            - **Number of Major Vessels Affected:** The number of major blood vessels affected by narrowing.
            - **Thalassemia Type:** The type of thalassemia (Normal, Defect, Reversible Defect).
            - **Exercise Angina:** Whether exercise induces angina.
            - **Oldpeak:** The ST depression induced by exercise relative to rest.
            - **ST Slope:** The slope of the peak exercise ST segment.
        """)
        
    elif section == "Future Enhancements":
        st.header("Future Enhancements")
        st.write("""
            We are continuously working to improve the accuracy and functionality of our system. Future enhancements 
            include incorporating more health parameters, using larger and more diverse datasets for training, and 
            adding new features such as real-time data analysis and integration with electronic health record systems.
        """)
        
    elif section == "Contact Us":
        st.header("Contact Us")
        st.write("""
            For more information or any inquiries, please contact us at:
            - **Developer:** AFIFI FAIZ
            - **Email:** afififaiz01@gmail.com
            - **Phone:** +6017 817 5248 
        """)

# Run the interface
if __name__ == "__main__":
    about_page()
