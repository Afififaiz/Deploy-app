import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    fig = px.line(history_df, x='Timestamp', y='Result', title='Cardiac Arrest Test History', markers=True, color_discrete_sequence=px.colors.qualitative.Plotly)
    fig.update_traces(marker=dict(size=10), line=dict(width=2))

    st.plotly_chart(fig, use_container_width=True)

    # Create another row for more visualizations
    col4, col5, col6 = st.columns(3)
    
    # Additional visualization: Bar chart for Age vs Result
    with col4:
        fig2 = px.bar(history_df, x='Age', y='Result', title='Age vs Cardiac Arrest Risk', color='Result', color_continuous_scale=px.colors.sequential.Viridis)
        st.plotly_chart(fig2, use_container_width=True)

    # Additional visualization: Histogram for Serum Cholesterol
    with col5:
        fig3 = px.histogram(history_df, x='Serum Cholesterol', title='Serum Cholesterol Distribution', color_discrete_sequence=px.colors.qualitative.T10)
        st.plotly_chart(fig3, use_container_width=True)
        
    # Additional visualization: Box plot for Max Heart Rate
    with col6:
        fig4 = px.box(history_df, y='Max Heart Rate', title='Max Heart Rate Distribution', color_discrete_sequence=px.colors.qualitative.D3)
        st.plotly_chart(fig4, use_container_width=True)

    # New advanced visualizations
    col7, col8, col9 = st.columns(3)
    
    # Donut Chart for Chest Pain Type
    with col7:
        chest_pain_counts = history_df['Chest Pain Type'].value_counts().reset_index()
        chest_pain_counts.columns = ['Chest Pain Type', 'Count']
        fig5 = px.pie(chest_pain_counts, values='Count', names='Chest Pain Type', title='Distribution of Chest Pain Types', hole=0.4, color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig5, use_container_width=True)

    # Scatter Plot for Resting Blood Pressure vs. Max Heart Rate
    with col8:
        fig6 = px.scatter(history_df, x='Resting Blood Pressure', y='Max Heart Rate', color='Gender', title='Resting Blood Pressure vs. Max Heart Rate', labels={'Resting Blood Pressure': 'Resting Blood Pressure', 'Max Heart Rate': 'Max Heart Rate'}, color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig6, use_container_width=True)
    
    # Violin Plot for Oldpeak distribution across different ST Slope categories
    with col9:
        fig7 = px.violin(history_df, y='Oldpeak', x='ST Slope', color='Gender', box=True, points="all", title='Oldpeak Distribution by ST Slope', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig7, use_container_width=True)

    st.write("")
    
    # New row for additional visualizations
    col10, col11, col12 = st.columns(3)

    # Pie Chart for Gender distribution
    with col10:
        gender_counts = history_df['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']
        fig8 = px.pie(gender_counts, values='Count', names='Gender', title='Gender Distribution', color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig8, use_container_width=True)

    # Sunburst Chart for hierarchical data (e.g., Age, Gender, Chest Pain Type)
    with col11:
        fig9 = px.sunburst(history_df, path=['Age', 'Gender', 'Chest Pain Type'], title='Hierarchical View of Age, Gender, and Chest Pain Type', color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig9, use_container_width=True)

    # Treemap for hierarchical data (e.g., Age, Gender, Chest Pain Type)
    with col12:
        fig11 = px.treemap(history_df, path=['Age', 'Gender', 'Chest Pain Type'], title='Treemap of Age, Gender, and Chest Pain Type', color_discrete_sequence=px.colors.qualitative.Alphabet)
        st.plotly_chart(fig11, use_container_width=True)

    st.dataframe(history_df)
else:
    st.write("No history available.")
