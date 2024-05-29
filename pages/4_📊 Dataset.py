import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

    # Filter out 'Gender' from the list of columns
    attribute_options = [col for col in data.columns if col != 'Gender']

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



   
# Run the interface
if __name__ == "__main__":
    main()
