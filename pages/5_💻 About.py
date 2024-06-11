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
        st.video("https://www.youtube.com/watch?v=VhOBLRyiXx0&ab_channel=ClevelandClinic")
        
    elif section == "Why Use This System?":
        st.header("Why Use This System?")
        st.write("""
            Cardiac arrest is a serious medical condition that can lead to sudden death if not treated immediately. 
            Early prediction and intervention can significantly reduce the mortality rate associated with cardiac 
            arrest. Our system leverages advanced machine learning techniques to offer accurate predictions, 
            aiding healthcare providers in making informed decisions about patient care.
        """)
        st.video("https://www.youtube.com/watch?v=VidtcN_tPn0&t=335s&ab_channel=Forbes")
        
    elif section == "Prediction Model":
        st.header("Prediction Model")
        st.write("""
            The core of our system is powered by the XGBoost algorithm, a highly efficient and scalable implementation 
            of gradient boosting. XGBoost is well-known for its performance and accuracy in various machine learning 
            tasks. Our model has been trained and tested rigorously to ensure reliable predictions.
        """)
        st.video("https://www.youtube.com/watch?v=rtJ2e02FbtY&t=392s&ab_channel=SamuelSeymour")
        
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

        - **Age:** The age of the patient. Age is a critical factor as the risk of cardiac conditions generally increases with age.
         ****         
        - **Gender:** The gender of the patient. Men generally have a higher risk of heart disease at a younger age, while the risk for women increases post-menopause.
         ****   
        - **Chest Pain Type:** 
            - **Typical Angina:** Pain typically associated with exertion and relieved by rest or nitroglycerin.
            - **Atypical Angina:** Pain that doesn't fit the typical pattern but is still related to the heart.
            - **Non-Anginal Pain:** Chest pain not related to the heart.
            - **Asymptomatic:** No chest pain.
        ****
        - **Resting Blood Pressure:** The patient's blood pressure when at rest, measured in mm Hg. Elevated resting blood pressure (hypertension) is a significant risk factor for heart disease.
        ****
        - **Serum Cholesterol:** The cholesterol level in the blood, measured in mg/dl. High cholesterol levels can lead to atherosclerosis.
        ****
        - **Fasting Blood Sugar:** Blood sugar levels measured after fasting for at least 8 hours. Levels above 120 mg/dl can indicate diabetes, which is a risk factor for heart disease.
        ****
        - **Resting Electrocardiogram Result (ECG):** 
            - **Normal:** No significant abnormalities detected.
            - **ST-T Wave Abnormality:** Indicates issues like ischemia or myocardial infarction.
            - **Left Ventricular Hypertrophy:** Thickening of the heart's left ventricular wall, often due to high blood pressure.
        ****    
        - **Maximum Heart Rate:** The highest heart rate achieved by the patient during exercise, measured in bpm. Lower maximum heart rates during stress tests can indicate poor cardiovascular fitness or underlying heart issues.
        ****
        - **Number of Major Vessels Affected:** The number of major coronary arteries (out of 0, 1, 2, or 3) that have significant narrowing or blockages. The greater the number, the higher the risk of heart disease.
        ****
        - **Thalassemia Type:** 
            - **Normal:** No thalassemia.
            - **Defect:** Presence of abnormal hemoglobin, causing mild to severe anemia.
            - **Reversible Defect:** Temporary abnormality in hemoglobin.
        ****
        - **Exercise Angina:** Whether exercise induces angina. Positive exercise angina suggests significant coronary artery disease.
        ****
        - **Oldpeak:** The ST depression induced by exercise relative to rest, measured in mm. It indicates the severity of ischemia.
        ****
        - **ST Slope:** 
            - **Upsloping:** Generally less concerning, though still needs attention.
            - **Flat:** Can indicate ischemia or a higher risk of heart disease.
            - **Downsloping:** Strongly associated with coronary artery disease.
        """)
        st.video("https://www.youtube.com/watch?v=9emAmwJ3vFw&ab_channel=Cedars-Sinai")
        
    elif section == "Future Enhancements":
        st.header("Future Enhancements")
        st.write("""
            We are continuously working to improve the accuracy and functionality of our system. Future enhancements 
            include incorporating more health parameters, using larger and more diverse datasets for training, and 
            adding new features such as real-time data analysis and integration with electronic health record systems.
        """)
        
    elif section == "Contact Us":
        st.header("Contact Us")
        st.write("For more information or any inquiries, please contact us at:")
        st.image(r"C:\Users\Afifi Faiz\Downloads\Cardialyze-deploy\pic.jpg", width=500)
        st.write("""
        - **Developer:** AFIFI FAIZ
        - **Email:** [afififaiz01@gmail.com](mailto:afififaiz01@gmail.com)
        - **Phone:** +6017 817 5248
        """, unsafe_allow_html=True)
    

# Run the interface
if __name__ == "__main__":
    about_page()
