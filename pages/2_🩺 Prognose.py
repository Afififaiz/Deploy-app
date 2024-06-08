import streamlit as st
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import pytz

# Define the interface and functions
def main():
    # Load the trained XGBoost model
    xgb_model = joblib.load('C:/Users/Afifi Faiz/Documents/Cardialyze-app/xgb_model.pkl')

    st.title("Cardiac Arrest Risk Prognosticator")

    st.write("Patient Information details:")

    # Initialize session state for input fields if not already done
    if 'inputs' not in st.session_state:
        st.session_state['inputs'] = {
            'name': '',
            'ic_number': '',
            'age': 29,
            'gender': 'Male',
            'chest_pain_type': 'Typical Angina',
            'resting_blood_pressure': 94,
            'serum_cholesterol': 126,
            'fasting_blood_sugar': 'Below 120',
            'ecg_result': 'Normal',
            'max_heart_rate': 71,
            'num_major_vessels': 0,
            'thalassemia': 'Normal',
            'exercise_angina': 'No',
            'oldpeak': -2.6,
            'st_slope': 'Upsloping'
        }

    if 'current_result' not in st.session_state:
        st.session_state['current_result'] = None

    if 'history' not in st.session_state:
        st.session_state['history'] = []

    def reset_inputs():
        st.session_state['inputs'] = {
            'name': '',
            'ic_number': '',
            'age': 29,
            'gender': 'Male',
            'chest_pain_type': 'Typical Angina',
            'resting_blood_pressure': 94,
            'serum_cholesterol': 126,
            'fasting_blood_sugar': 'Below 120',
            'ecg_result': 'Normal',
            'max_heart_rate': 71,
            'num_major_vessels': 0,
            'thalassemia': 'Normal',
            'exercise_angina': 'No',
            'oldpeak': -2.6,
            'st_slope': 'Upsloping'
        }
        st.session_state['current_result'] = None

    # Get user input for patient name
    st.session_state['inputs']['name'] = st.text_input("Patient Name:", value=st.session_state['inputs']['name'])

    # Get user input for IC number
    st.session_state['inputs']['ic_number'] = st.text_input("Identification Number (with '-'):", value=st.session_state['inputs']['ic_number'])

    # Get user input for age
    st.session_state['inputs']['age'] = st.number_input("Age (years):", min_value=29, max_value=77, value=st.session_state['inputs']['age'])

    # Get user input for gender
    st.session_state['inputs']['gender'] = st.selectbox("Gender:", options=["Male", "Female"], index=["Male", "Female"].index(st.session_state['inputs']['gender']))

    # Get user input for chest pain type
    st.session_state['inputs']['chest_pain_type'] = st.selectbox("Chest Pain Type:",
                                   options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"], index=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"].index(st.session_state['inputs']['chest_pain_type']))

    # Get user input for resting blood pressure
    st.session_state['inputs']['resting_blood_pressure'] = st.number_input("Resting Blood Pressure (mm Hg):", min_value=94, max_value=200, value=st.session_state['inputs']['resting_blood_pressure'])

    # Get user input for serum cholesterol levels
    st.session_state['inputs']['serum_cholesterol'] = st.number_input("Serum Cholesterol (mg/dl):", min_value=126, max_value=564, value=st.session_state['inputs']['serum_cholesterol'])

    # Get user input for fasting blood sugar levels
    st.session_state['inputs']['fasting_blood_sugar'] = st.selectbox("Fasting Blood Sugar Level (mg/dl):", options=["Below 120", "Above 120"], index=["Below 120", "Above 120"].index(st.session_state['inputs']['fasting_blood_sugar']))

    # Get user input for resting electrocardiogram result
    st.session_state['inputs']['ecg_result'] = st.selectbox("Resting Electrocardiogram Result:",
                              options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"], index=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(st.session_state['inputs']['ecg_result']))

    # Get user input for maximum heart rate reached during exercise
    st.session_state['inputs']['max_heart_rate'] = st.number_input("Maximum Heart Rate (bpm):", min_value=71, max_value=202, value=st.session_state['inputs']['max_heart_rate'])

    # Get user input for number of major vessels affected
    st.session_state['inputs']['num_major_vessels'] = st.selectbox("Number of Major Vessels Affected:", options=[0, 1, 2, 3], index=st.session_state['inputs']['num_major_vessels'])

    # Get user input for thalassemia type
    st.session_state['inputs']['thalassemia'] = st.selectbox("Thalassemia Type:", options=["Normal", "Defect", "Reversible Defect"], index=["Normal", "Defect", "Reversible Defect"].index(st.session_state['inputs']['thalassemia']))

    # Get user input for exercise angina
    st.session_state['inputs']['exercise_angina'] = st.selectbox("Exercise Angina:", options=["Yes", "No"], index=["Yes", "No"].index(st.session_state['inputs']['exercise_angina']))

    # Get user input for oldpeak
    st.session_state['inputs']['oldpeak'] = st.number_input("Oldpeak (mm):", min_value=-2.6, max_value=6.2, value=st.session_state['inputs']['oldpeak'])

    # Get user input for ST slope
    st.session_state['inputs']['st_slope'] = st.selectbox("ST Slope:", options=["Upsloping", "Flat", "Downsloping"], index=["Upsloping", "Flat", "Downsloping"].index(st.session_state['inputs']['st_slope']))
    
    # Define a function for calculating the prediction
    def calculate_prediction():
        # Convert categorical inputs to numerical
        gender_num = 1 if st.session_state['inputs']['gender'] == "Male" else 0
        chest_pain_type_num = ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"].index(st.session_state['inputs']['chest_pain_type'])
        fasting_blood_sugar_num = 1 if st.session_state['inputs']['fasting_blood_sugar'] == "Above 120" else 0
        ecg_result_num = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(st.session_state['inputs']['ecg_result'])
        thalassemia_num = ["Normal", "Defect", "Reversible Defect"].index(st.session_state['inputs']['thalassemia'])
        exercise_angina_num = 1 if st.session_state['inputs']['exercise_angina'] == "Yes" else 0
        st_slope_num = ["Upsloping", "Flat", "Downsloping"].index(st.session_state['inputs']['st_slope'])

        # Prepare input for prediction
        input_data = np.array([[st.session_state['inputs']['age'], gender_num, chest_pain_type_num, st.session_state['inputs']['resting_blood_pressure'], st.session_state['inputs']['serum_cholesterol'],
                                fasting_blood_sugar_num, ecg_result_num, st.session_state['inputs']['max_heart_rate'], st.session_state['inputs']['num_major_vessels'],
                                thalassemia_num, exercise_angina_num, st.session_state['inputs']['oldpeak'], st_slope_num]])

        # Predict
        probability = xgb_model.predict_proba(input_data)[0][1]
        result_col.write(f"There is a {probability * 100:.2f}% chance of developing cardiac arrest.")

        st.session_state['current_result'] = {
            
            "Name": st.session_state['inputs']['name'],
            "IC Number": st.session_state['inputs']['ic_number'],
            "Age": st.session_state['inputs']['age'],
            "Gender": st.session_state['inputs']['gender'],
            "Chest Pain Type": st.session_state['inputs']['chest_pain_type'],
            "Resting Blood Pressure": st.session_state['inputs']['resting_blood_pressure'],
            "Serum Cholesterol": st.session_state['inputs']['serum_cholesterol'],
            "Fasting Blood Sugar": st.session_state['inputs']['fasting_blood_sugar'],
            "ECG Result": st.session_state['inputs']['ecg_result'],
            "Max Heart Rate": st.session_state['inputs']['max_heart_rate'],
            "Major Vessels Affected": st.session_state['inputs']['num_major_vessels'],
            "Thalassemia": st.session_state['inputs']['thalassemia'],
            "Exercise Angina": st.session_state['inputs']['exercise_angina'],
            "Oldpeak": st.session_state['inputs']['oldpeak'],
            "ST Slope": st.session_state['inputs']['st_slope'],
            "Result": f"{probability * 100:.2f}%",
            "Timestamp": datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).strftime('%Y-%m-%d %H:%M:%S')
        }
        st.session_state['history'].append(st.session_state['current_result'])

    # Define your button layout
    buttons_col1, button_col2, result_col = st.columns([1, 5, 4])

    # Add separate button for calculation
    if buttons_col1.button("Calculate"):
        if st.session_state['inputs']['name'] and st.session_state['inputs']['ic_number']:
            calculate_prediction()
        else:
            st.warning("Please fill in both the Patient Name and Identification Number before calculating.")

    # Add reset button
    if button_col2.button("Reset All"):
        reset_inputs()
        st.experimental_rerun()

    st.write("")
    st.write("")
    # Display current result
    if st.session_state['current_result'] is not None:
        result_df = pd.DataFrame([st.session_state['current_result']])
        columns = ['Timestamp', 'Name', 'IC Number', 'Age', 'Gender', 'Chest Pain Type', 'Resting Blood Pressure', 
                   'Serum Cholesterol', 'Fasting Blood Sugar', 'ECG Result', 'Max Heart Rate', 'Major Vessels Affected', 
                   'Thalassemia', 'Exercise Angina', 'Oldpeak', 'ST Slope', 'Result']
        result_df = result_df[columns]
        st.write("Current Test Result:")
        st.dataframe(result_df)

# Run the interface
if __name__ == "__main__":
    main()
