import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Cardialyze",
    page_icon="🏥",
    layout='wide'
)

st.title("Welcome to Cardialyze 👨‍⚕️")
st.sidebar.success("Select a page above")

st.write("## *Overview*")

st.write("Cardialyze is your personal assistant to help prognose the risk of cardiac arrest based on user inputs.")
st.write("")
st.write("")

if 'history' in st.session_state and st.session_state['history']:
    # Create a DataFrame from the history
    history_df = pd.DataFrame(st.session_state['history'])
    
    # Rearrange columns to put timestamp first
    columns = ['Timestamp', 'Age', 'Gender', 'Chest Pain Type', 'Resting Blood Pressure', 'Serum Cholesterol', 
               'Fasting Blood Sugar', 'ECG Result', 'Max Heart Rate', 'Major Vessels Affected', 
               'Thalassemia', 'Exercise Angina', 'Oldpeak', 'ST Slope', 'Result']
    history_df = history_df[columns]

    # Calculate total tests and highest test result
    total_tests = len(history_df)
    highest_result = history_df['Result'].max()
    lowest_result = history_df['Result'].min()
   

    # Display metrics with a border box
    col1, col2, col3 = st.columns(3)
    col1.markdown(f"""
        <div style="border:5px solid #d3d3d3; padding: 10px; border-radius: 10px; text-align: center;">
            <h4>Total Tests</h4>
            <p style="font-size: 35px; font-weight: bold;">{total_tests}</p>
        </div>
    """, unsafe_allow_html=True)
    col2.markdown(f"""
        <div style="border:5px solid #d3d3d3; padding: 10px; border-radius: 10px; text-align: center;">
            <h4>Highest Test</h4>
            <p style="font-size: 35px; font-weight: bold; color: #FA0D0A">{highest_result}</p>
        </div>
    """, unsafe_allow_html=True)
    col3.markdown(f"""
        <div style="border:5px solid #d3d3d3; padding: 10px; border-radius: 10px; text-align: center;">
            <h4>Lowest Test</h4>
            <p style="font-size: 35px; font-weight: bold; color: #07901D">{lowest_result}</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.write("")

    # Plotly chart for history with markers
    fig = px.line(history_df, x='Timestamp', y='Result', title='Cardiac Arrest Test History', markers=True)
    fig.update_traces(marker=dict(size=10), line=dict(width=2))

    st.plotly_chart(fig, use_container_width=True)

     # Create another row for more visualizations
    col4, col5, col6 = st.columns(3)
    
    # Additional visualization: Bar chart for Age vs Result
    with col4:
        fig2 = px.bar(history_df, x='Age', y='Result', title='Age vs Cardiac Arrest Risk', color='Result')
        st.plotly_chart(fig2, use_container_width=True)


    # Additional visualization: Histogram for Serum Cholesterol
    with col5:
        fig3 = px.histogram(history_df, x='Serum Cholesterol', title='Serum Cholesterol Distribution')
        st.plotly_chart(fig3, use_container_width=True)
        
    # Additional visualization: Box plot for Max Heart Rate
    with col6:
        fig4 = px.box(history_df, y='Max Heart Rate', title='Max Heart Rate Distribution')
        st.plotly_chart(fig4, use_container_width=True)


    st.dataframe(history_df)
else:
    st.write("No history available.")
