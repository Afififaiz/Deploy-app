import streamlit as st
import pandas as pd

st.title("Prognostication History")

# Check if there's history data in session state
if 'history' in st.session_state and st.session_state['history']:
    # Create a DataFrame from the history
    history_df = pd.DataFrame(st.session_state['history'])
    
    # Rearrange columns to put timestamp first
    columns = ['Timestamp', 'Name', 'IC Number', 'Age', 'Gender', 'Chest Pain Type', 'Resting Blood Pressure', 'Serum Cholesterol', 
               'Fasting Blood Sugar', 'ECG Result', 'Max Heart Rate', 'Major Vessels Affected', 
               'Thalassemia', 'Exercise Angina', 'Oldpeak', 'ST Slope', 'Result']
    history_df = history_df[columns]

    # Set the index to start from 1 and label it as "Test"
    history_df.index = history_df.index + 1
    history_df.index.name = 'Test'

    # Select filter type
    filter_type = st.selectbox('Select Filter Type', ['None', 'Gender', 'Chest Pain Type', 'Age', 'Resting Blood Pressure', 'Serum Cholesterol', 'Fasting Blood Sugar', 'ECG Result', 'Max Heart Rate', 'Major Vessels Affected', 'Thalassemia', 'Exercise Angina', 'Oldpeak', 'ST Slope', 'Result'])

    # Initialize filtered DataFrame
    filtered_df = history_df.copy()

    # Apply selected filter
    if filter_type == 'Gender':
        unique_genders = filtered_df['Gender'].unique().tolist()
        selected_genders = st.multiselect('Select Gender', unique_genders, default=unique_genders)
        filtered_df = filtered_df[filtered_df['Gender'].isin(selected_genders)]
    elif filter_type == 'Chest Pain Type':
        unique_chest_pain_types = filtered_df['Chest Pain Type'].unique().tolist()
        selected_chest_pain_types = st.multiselect('Select Chest Pain Type', unique_chest_pain_types, default=unique_chest_pain_types)
        filtered_df = filtered_df[filtered_df['Chest Pain Type'].isin(selected_chest_pain_types)]
    elif filter_type == 'Age':
        min_age, max_age = int(filtered_df['Age'].min()), int(filtered_df['Age'].max())
        if min_age == max_age:
            st.warning("Only one unique age value found. Please add more age data to use this filter.")
        else:
            selected_age_range = st.slider('Select Age Range', min_age, max_age, (min_age, max_age))
            filtered_df = filtered_df[(filtered_df['Age'] >= selected_age_range[0]) & (filtered_df['Age'] <= selected_age_range[1])]
    elif filter_type == 'Resting Blood Pressure':
        min_bp, max_bp = int(filtered_df['Resting Blood Pressure'].min()), int(filtered_df['Resting Blood Pressure'].max())
        if min_bp == max_bp:
            st.warning("Only one unique resting blood pressure value found. Please add more data to use this filter.")
        else:
            selected_bp_range = st.slider('Select Resting Blood Pressure Range', min_bp, max_bp, (min_bp, max_bp))
            filtered_df = filtered_df[(filtered_df['Resting Blood Pressure'] >= selected_bp_range[0]) & (filtered_df['Resting Blood Pressure'] <= selected_bp_range[1])]
    elif filter_type == 'Serum Cholesterol':
        min_chol, max_chol = int(filtered_df['Serum Cholesterol'].min()), int(filtered_df['Serum Cholesterol'].max())
        if min_chol == max_chol:
            st.warning("Only one unique serum cholesterol value found. Please add more data to use this filter.")
        else:
            selected_chol_range = st.slider('Select Serum Cholesterol Range', min_chol, max_chol, (min_chol, max_chol))
            filtered_df = filtered_df[(filtered_df['Serum Cholesterol'] >= selected_chol_range[0]) & (filtered_df['Serum Cholesterol'] <= selected_chol_range[1])]
    elif filter_type == 'Fasting Blood Sugar':
        unique_fbs = filtered_df['Fasting Blood Sugar'].unique().tolist()
        selected_fbs = st.multiselect('Select Fasting Blood Sugar', unique_fbs, default=unique_fbs)
        filtered_df = filtered_df[filtered_df['Fasting Blood Sugar'].isin(selected_fbs)]
    elif filter_type == 'ECG Result':
        unique_ecg = filtered_df['ECG Result'].unique().tolist()
        selected_ecg = st.multiselect('Select ECG Result', unique_ecg, default=unique_ecg)
        filtered_df = filtered_df[filtered_df['ECG Result'].isin(selected_ecg)]
    elif filter_type == 'Max Heart Rate':
        min_hr, max_hr = int(filtered_df['Max Heart Rate'].min()), int(filtered_df['Max Heart Rate'].max())
        if min_hr == max_hr:
            st.warning("Only one unique max heart rate value found. Please add more data to use this filter.")
        else:
            selected_hr_range = st.slider('Select Max Heart Rate Range', min_hr, max_hr, (min_hr, max_hr))
            filtered_df = filtered_df[(filtered_df['Max Heart Rate'] >= selected_hr_range[0]) & (filtered_df['Max Heart Rate'] <= selected_hr_range[1])]
    elif filter_type == 'Major Vessels Affected':
        unique_vessels = filtered_df['Major Vessels Affected'].unique().tolist()
        selected_vessels = st.multiselect('Select Major Vessels Affected', unique_vessels, default=unique_vessels)
        filtered_df = filtered_df[filtered_df['Major Vessels Affected'].isin(selected_vessels)]
    elif filter_type == 'Thalassemia':
        unique_thal = filtered_df['Thalassemia'].unique().tolist()
        selected_thal = st.multiselect('Select Thalassemia', unique_thal, default=unique_thal)
        filtered_df = filtered_df[filtered_df['Thalassemia'].isin(selected_thal)]
    elif filter_type == 'Exercise Angina':
        unique_angina = filtered_df['Exercise Angina'].unique().tolist()
        selected_angina = st.multiselect('Select Exercise Angina', unique_angina, default=unique_angina)
        filtered_df = filtered_df[filtered_df['Exercise Angina'].isin(selected_angina)]
    elif filter_type == 'Oldpeak':
        min_oldpeak, max_oldpeak = float(filtered_df['Oldpeak'].min()), float(filtered_df['Oldpeak'].max())
        if min_oldpeak == max_oldpeak:
            st.warning("Only one unique oldpeak value found. Please add more data to use this filter.")
        else:
            selected_oldpeak_range = st.slider('Select Oldpeak Range', min_oldpeak, max_oldpeak, (min_oldpeak, max_oldpeak))
            filtered_df = filtered_df[(filtered_df['Oldpeak'] >= selected_oldpeak_range[0]) & (filtered_df['Oldpeak'] <= selected_oldpeak_range[1])]
    elif filter_type == 'ST Slope':
        unique_st_slope = filtered_df['ST Slope'].unique().tolist()
        selected_st_slope = st.multiselect('Select ST Slope', unique_st_slope, default=unique_st_slope)
        filtered_df = filtered_df[filtered_df['ST Slope'].isin(selected_st_slope)]
    elif filter_type == 'Result':
        # Create a temporary column for calculation purposes
        filtered_df['Result_temp'] = filtered_df['Result'].str.rstrip('%').astype(float)
        
        if filtered_df.empty:
            st.warning("No data available after filtering.")
        else:
            min_result, max_result = float(filtered_df['Result_temp'].min()), float(filtered_df['Result_temp'].max())
            if min_result == max_result:
                st.warning("Only one unique result value found. Please add more data to use this filter.")
            else:
                selected_result_range = st.slider('Select Result Range', min_result, max_result, (min_result, max_result))
                filtered_df = filtered_df[(filtered_df['Result_temp'] >= selected_result_range[0]) & (filtered_df['Result_temp'] <= selected_result_range[1])]
        
        # Check if 'Result_temp' column exists before dropping it
        if 'Result_temp' in filtered_df.columns:
            filtered_df = filtered_df.drop(columns=['Result_temp'])

    # Display the filtered DataFrame
    st.dataframe(filtered_df)
else:
    st.write("No history available.")
