import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Description
st.title("Capstone Project Analysis")
st.markdown("This Streamlit app showcases the analysis from my capstone project.")

# Upload File Section
st.header("Upload Your Data")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load data based on file type
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        
        st.success("File uploaded successfully!")
        
        # Display first few rows
        st.subheader("Data Preview")
        st.write(data.head())

        # Basic Data Insights
        st.subheader("Basic Insights")
        st.write(f"Number of Rows: {data.shape[0]}")
        st.write(f"Number of Columns: {data.shape[1]}")
        st.write("Data Types:")
        st.write(data.dtypes)

        # Visualization Example
        st.subheader("Visualization")
        column_to_plot = st.selectbox("Select a column to visualize", data.columns)
        
        if data[column_to_plot].dtype in ['int64', 'float64']:
            fig, ax = plt.subplots()
            data[column_to_plot].hist(ax=ax, bins=20)
            ax.set_title(f"Histogram of {column_to_plot}")
            st.pyplot(fig)
        else:
            st.write("Selected column is not numeric, unable to plot histogram.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a file to get started.")
