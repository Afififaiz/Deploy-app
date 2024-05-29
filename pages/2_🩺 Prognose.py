import streamlit as st
import joblib
import numpy as np
from datetime import datetime
import pytz

# Define the interface and functions
def main():
    # Load the trained XGBoost model
    xgb_model = joblib.load('xgb_model.pkl')

    st.title("Cardiac Arrest Risk Prognosticator")

    st.write("Patient Information details:")

    # Get user input for age
    age = st.number_input("Age (years):", min_value=29, max_value=77)

    # Get user input for gender
    gender = st.selectbox("Gender:", options=["Male", "Female"])

    # Get user input for chest pain type
    chest_pain_type = st.selectbox("Chest Pain Type:",
                                   options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])

    # Get user input for resting blood pressure
    resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg):", min_value=94, max_value=200)

    # Get user input for serum cholesterol levels
    serum_cholesterol = st.number_input("Serum Cholesterol (mg/dl):", min_value=126, max_value=564)

    # Get user input for fasting blood sugar levels
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar Level (mg/dl):", options=["Below 120", "Above 120"])

    # Get user input for resting electrocardiogram result
    ecg_result = st.selectbox("Resting Electrocardiogram Result:",
                              options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])

    # Get user input for maximum heart rate reached during exercise
    max_heart_rate = st.number_input("Maximum Heart Rate (bpm):", min_value=71, max_value=202)

    # Get user input for number of major vessels affected
    num_major_vessels = st.selectbox("Number of Major Vessels Affected:",
                                     options=[0, 1, 2, 3])

    # Get user input for thalassemia type
    thalassemia = st.selectbox("Thalassemia Type:", options=["Normal", "Defect", "Reversible Defect"])

    # Get user input for exercise angina
    exercise_angina = st.selectbox("Exercise Angina:", options=["Yes", "No"])

    # Get user input for oldpeak
    oldpeak = st.number_input("Oldpeak (mm):", min_value=-2.6, max_value=6.2)

    # Get user input for ST slope
    st_slope = st.selectbox("ST Slope:", options=["Upsloping", "Flat", "Downsloping"])
      
    # Define a function for calculating the prediction
    def calculate_prediction():
        # Convert categorical inputs to numerical
        gender_num = 1 if gender == "Male" else 0
        chest_pain_type_num = ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"].index(chest_pain_type)
        fasting_blood_sugar_num = 1 if fasting_blood_sugar == "Above 120" else 0
        ecg_result_num = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(ecg_result)
        thalassemia_num = ["Normal", "Defect", "Reversible Defect"].index(thalassemia)
        exercise_angina_num = 1 if exercise_angina == "Yes" else 0
        st_slope_num = ["Upsloping", "Flat", "Downsloping"].index(st_slope)

        # Prepare input for prediction
        input_data = np.array([[age, gender_num, chest_pain_type_num, resting_blood_pressure, serum_cholesterol,
                                fasting_blood_sugar_num, ecg_result_num, max_heart_rate, num_major_vessels,
                                thalassemia_num, exercise_angina_num, oldpeak, st_slope_num]])

        # Predict
        probability = xgb_model.predict_proba(input_data)[0][1]
        result_col.write(f"There is a {probability * 100:.2f}% chance of developing cardiac arrest.")


     # Store result in session state
        if 'history' not in st.session_state:
            st.session_state['history'] = []
        st.session_state['history'].append({
            "Age": age,
            "Gender": gender,
            "Chest Pain Type": chest_pain_type,
            "Resting Blood Pressure": resting_blood_pressure,
            "Serum Cholesterol": serum_cholesterol,
            "Fasting Blood Sugar": fasting_blood_sugar,
            "ECG Result": ecg_result,
            "Max Heart Rate": max_heart_rate,
            "Major Vessels Affected": num_major_vessels,
            "Thalassemia": thalassemia,
            "Exercise Angina": exercise_angina,
            "Oldpeak": oldpeak,
            "ST Slope": st_slope,
            "Result": f"{probability * 100:.2f}%",
            "Timestamp": datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).strftime('%Y-%m-%d %H:%M:%S')
        })    

    # Define your button layout
    buttons_col1, button_col2 , result_col, = st.columns([1, 2, 4])

    # Add separate button for calculation
    if buttons_col1.button("Calculate"):
        calculate_prediction()

    # Add reset button
    if  button_col2.button("Reset All"):
        st.experimental_rerun()

# Run the interface
if __name__ == "__main__":
    main()
