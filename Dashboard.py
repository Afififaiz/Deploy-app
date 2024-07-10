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

st.write("Cardialyze is your personal assistant to help prognose the risk of cardiac arrest based on user inputs.")

if 'history' in st.session_state and st.session_state['history']:
    # Create a DataFrame from the history
    history_df = pd.DataFrame(st.session_state['history'])
    
    # Rearrange columns to put timestamp first
    columns = ['Timestamp', 'Age', 'Gender', 'Chest Pain Type', 'Resting Blood Pressure', 'Serum Cholesterol', 
               'Fasting Blood Sugar', 'ECG Result', 'Max Heart Rate',
                'Exercise Angina', 'Oldpeak', 'ST Slope', 'Result']
    history_df = history_df[columns]

    # Remove '%' sign from 'Result' column and convert to float
    history_df['Result'] = history_df['Result'].str.replace('%', '').astype(float)

    
    # Filter by Test (Timestamp)
    unique_tests = history_df['Timestamp'].unique().tolist()
    test_options = [f"Test {i+1} - {timestamp}" for i, timestamp in enumerate(unique_tests)]
    selected_tests = st.sidebar.multiselect('Filter Tests:', test_options, default=test_options)

    # Extract the selected timestamps
    selected_timestamps = [opt.split(" - ")[1] for opt in selected_tests]

    # Filter the DataFrame based on the selected tests
    filtered_df = history_df[history_df['Timestamp'].isin(selected_timestamps)]
    
    # Calculate total tests, highest test result, and lowest test result for the filtered data
    total_tests = len(filtered_df)
    highest_result = filtered_df['Result'].max()
    lowest_result = filtered_df['Result'].min()

    st.write("")

    # Display metrics using gauge meters
    col1, col2, col3 = st.columns(3)
    
    gauge_layout = {
        'margin': {'t': 50, 'b': 0, 'l': 0, 'r': 0},
        'height': 250  # Adjust height if needed
    }
    
    with col1:
        fig_total_tests = go.Figure(go.Indicator(
            mode="gauge+number",
            value=total_tests,
            title={'text': "<b>Total Tests</b>", 'font': {'size': 24, 'color': 'purple'}},
            number={'font': {'color': 'purple'}},
            gauge={'axis': {'range': [None, total_tests * 1.2]},
                   'bar': {'color': 'purple'}}
        ))
        fig_total_tests.update_layout(gauge_layout)
        st.plotly_chart(fig_total_tests, use_container_width=True)
    
    with col2:
        fig_highest_result = go.Figure(go.Indicator(
            mode="gauge+number",
            value=highest_result,
            title={'text': "<b>Highest Test Result (%)</b>", 'font': {'size': 24, 'color': '#BB2525'}},
            number={'font': {'color': '#BB2525'}},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': '#BB2525'}
            }
        ))
        fig_highest_result.update_layout(gauge_layout)
        st.plotly_chart(fig_highest_result, use_container_width=True)
    
    with col3:
        fig_lowest_result = go.Figure(go.Indicator(
            mode="gauge+number",
            value=lowest_result,
            title={'text': "<b>Lowest Test Result (%)</b>", 'font': {'size': 24, 'color': 'green'}},
            number={'font': {'color': 'green'}},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': 'green'}
            }
        ))
        fig_lowest_result.update_layout(gauge_layout)
        st.plotly_chart(fig_lowest_result, use_container_width=True)
    
    # Plotly chart for history with markers
    fig = px.line(filtered_df, x='Timestamp', y='Result', title='Cardiac Arrest Test History', markers=True, color_discrete_sequence=px.colors.qualitative.Plotly, orientation='h')
    fig.update_traces(marker=dict(size=10), line=dict(width=2))

    st.plotly_chart(fig, use_container_width=True)

    # Create another row for more visualizations
    col4, col5, col6 = st.columns(3)
    
    # Additional visualization: Bar chart for Age vs Result with color by Timestamp
    with col4:
        fig2 = px.bar(filtered_df, x='Age', y='Result', title='Age vs Cardiac Arrest Risk', color='Timestamp', color_continuous_scale=px.colors.sequential.Viridis, orientation='h')
        fig2.update_layout(legend_title_text='Test Timestamp')
        st.plotly_chart(fig2, use_container_width=True)

    # Additional visualization: Histogram for Serum Cholesterol
    with col5:
        fig3 = px.histogram(filtered_df, x='Serum Cholesterol', title='Serum Cholesterol Distribution', color_discrete_sequence=px.colors.qualitative.T10)
        st.plotly_chart(fig3, use_container_width=True)
        
    # Additional visualization: Box plot for Max Heart Rate
    with col6:
        fig4 = px.box(filtered_df, y='Max Heart Rate', title='Max Heart Rate Distribution', color_discrete_sequence=px.colors.qualitative.D3)
        st.plotly_chart(fig4, use_container_width=True)

    # New advanced visualizations
    col7, col8, col9 = st.columns(3)
    
    # Donut Chart for Chest Pain Type
    with col7:
        chest_pain_counts = filtered_df['Chest Pain Type'].value_counts().reset_index()
        chest_pain_counts.columns = ['Chest Pain Type', 'Count']
        fig5 = px.pie(chest_pain_counts, values='Count', names='Chest Pain Type', title='Distribution of Chest Pain Types', hole=0.4, color_discrete_sequence=px.colors.qualitative.Prism)
        st.plotly_chart(fig5, use_container_width=True)

    # Scatter Plot for Resting Blood Pressure vs. Max Heart Rate
    with col8:
        fig6 = px.scatter(filtered_df, x='Resting Blood Pressure', y='Max Heart Rate', color='Gender', title='Resting Blood Pressure vs Max Heart Rate', labels={'Resting Blood Pressure': 'Resting Blood Pressure', 'Max Heart Rate': 'Max Heart Rate'}, color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig6, use_container_width=True)
    
    # Violin Plot for Oldpeak distribution across different ST Slope categories
    with col9:
        fig7 = px.violin(filtered_df, y='Oldpeak', x='ST Slope', color='Gender', box=True, points="all", title='Oldpeak Distribution by ST Slope', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig7, use_container_width=True)

    st.write("")
    
    # New row for additional visualizations
    col10, col11, col12 = st.columns(3)

    # Pie Chart for Gender distribution
    with col10:
        gender_counts = filtered_df['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']
        fig8 = px.pie(gender_counts, values='Count', names='Gender', title='Gender Distribution', color_discrete_sequence=px.colors.qualitative.Dark2)
        st.plotly_chart(fig8, use_container_width=True)

    # Sunburst Chart for hierarchical data (e.g., Age, Gender, Chest Pain Type)
    with col11:
        fig9 = px.sunburst(filtered_df, path=['Age', 'Gender', 'Chest Pain Type'], title='Hierarchical View of Age, Gender, and Chest Pain Type', color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig9, use_container_width=True)

    # Treemap for hierarchical data (e.g., Age, Gender, Chest Pain Type)
    with col12:
        fig11 = px.treemap(filtered_df, path=['Age', 'Gender', 'Chest Pain Type'], title='Treemap of Age, Gender, and Chest Pain Type', color_discrete_sequence=px.colors.qualitative.Alphabet)
        st.plotly_chart(fig11, use_container_width=True)

    # Adjust the index of filtered_df to start from 1 and label it as "Test"
    filtered_df.index = filtered_df.index + 1
    filtered_df.index.name = 'Test'

    # Display the filtered DataFrame
    st.dataframe(filtered_df)
else:
    st.write("No history available.")
