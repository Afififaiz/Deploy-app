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
    
    # Display the history DataFrame
    st.dataframe(history_df)
else:
    st.write("No history available.")
