import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv(r"OHCA.csv")
    return df

# Define the interface and functions
def main():
    st.title("Dataset Overview")
    st.write("This is the overview of the dataset from the CSV file.")

    # Load the data
    data = load_data()

    # Display the data
    st.write("### Dataset")
    st.dataframe(data)

    # Map numerical values to gender labels
    gender_map = {0: 'Male', 1: 'Female'}
    data['Gender'] = data['sex'].map(gender_map)

    # Create a Sankey chart to visualize relationships between selected attributes
    st.write("### Features Distribution Between Gender")

     # Map numerical values to labels
    gender_map = {0: 'Male', 1: 'Female'}
    cp_map = {0: 'Typical Angina', 1: 'Atypical Angina', 2: 'Non-Anginal Pain', 3: 'Asymptomatic'}
    fbs_map = {0: 'Below 120', 1: 'Above 120'}
    restecg_map = {0: 'Normal', 1: 'ST-T Wave Abnormality', 2: 'Left Ventricular Hypertrophy'}
    exang_map = {0: 'No', 1: 'Yes'}
    slope_map = {0: 'Upsloping', 1: 'Flat', 2: 'Downsloping'}
    thal_map = {3: 'Normal', 6: 'Fixed Defect', 7: 'Reversible Defect'}

    data['Gender'] = data['sex'].map(gender_map)
    data['cp'] = data['cp'].map(cp_map)
    data['fbs'] = data['fbs'].map(fbs_map)
    data['restecg'] = data['restecg'].map(restecg_map)
    data['exang'] = data['exang'].map(exang_map)
    data['slope'] = data['slope'].map(slope_map)
    data['thal'] = data['thal'].map(thal_map)

    # Filter out 'Gender' from the list of columns
    attribute_options = [col for col in data.columns if col != 'Gender' and data[col].dtype == 'object']

    # Select attribute for Sankey chart
    selected_attribute = st.selectbox("Select an attribute:", attribute_options)

    # Group by the selected attribute and gender
    grouped_data = data.groupby([selected_attribute, 'Gender']).size().reset_index(name='Count')

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            label=grouped_data[selected_attribute].unique().tolist() + grouped_data['Gender'].unique().tolist(),
        ),
        link=dict(
            source=grouped_data[selected_attribute].map(lambda x: grouped_data[selected_attribute].unique().tolist().index(x)),
            target=grouped_data['Gender'].map(lambda x: len(grouped_data[selected_attribute].unique().tolist()) + grouped_data['Gender'].unique().tolist().index(x)),
            value=grouped_data['Count']
        )
    )])

    st.plotly_chart(fig)


    # Create scatter plots to visualize relationships between numerical features
    st.write("### Serum Cholestrol Between Gender")
    scatter_fig = px.scatter(data, x='age', y='chol', color='Gender', hover_data=['Gender'], labels={'age': 'Age', 'chol': 'Serum Cholesterol'})
    st.plotly_chart(scatter_fig)

    st.write("### Cardiac Presence Between Gender and Age")

    # Convert the 'output' column values to meaningful labels
    data['output'] = data['output'].map({0: 'No Presence', 1: 'Presence'})

    # Create a double bar chart to show the distribution of age between genders
    fig = px.histogram(data, x='age', color='Gender', facet_col='output', color_discrete_map={'Presence': 'red', 'No Presence': 'blue'},
                       labels={'output': 'Cardiac Arrest', 'age': 'Age', 'Gender': 'Gender'})
    fig.update_layout(barmode='group')
    fig.update_xaxes(title_text='Age')
    st.plotly_chart(fig)

    # New visualizations

    # Histogram of Age Distribution
    st.write("### Age Distribution")
    hist_fig = px.histogram(data, x='age', nbins=30, title='Age Distribution', labels={'age': 'Age'})
    st.plotly_chart(hist_fig)

    # Box Plot of Serum Cholesterol by Gender
    st.write("### Serum Cholesterol by Gender")
    box_fig = px.box(data, x='Gender', y='chol', title='Serum Cholesterol by Gender', labels={'chol': 'Serum Cholesterol'})
    st.plotly_chart(box_fig)

    # Correlation Heatmap
    st.write("### Correlation Heatmap")
    numeric_data = data.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
    corr = numeric_data.corr()
    plt.figure(figsize=(15, 8))
    heatmap = sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    st.pyplot(plt)
    

# Run the interface
if __name__ == "__main__":
    main()
