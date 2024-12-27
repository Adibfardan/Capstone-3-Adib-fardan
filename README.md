# CAPSTONE MODULE 3 ADIB FARDAN

## Project Overview
This project focuses on analyzing travel insurance data to predict claims using various machine learning models. The primary goal is to enhance the detection of positive claims while managing the trade-off with negative claims.

## Data Description
The dataset consists of 39,661 entries and 10 columns including:
Agency: The agency selling the insurance.
Agency Type: Type of agency (e.g., Airlines, Travel Agency).
Distribution Channel: The channel through which the product is sold (Online/Offline).
Product Name: The name of the insurance product.
Duration: Duration of the insurance coverage.
Destination: The destination covered by the insurance.
Net Sales: Total sales amount.
Commision: Commission earned.
Age: Age of the customer.
Claim: Whether a claim was made (Yes/No).

## Data Cleaning
The data was cleaned to remove duplicates and handle missing values, particularly in the Gender column.
The Gender column was dropped due to a high number of missing values.

## Feature Engineering
Categorical features were encoded using:
One-Hot Encoding for binary features (Agency Type, Distribution Channel).
Binary Encoding for features with many unique values (Agency, Product Name, Destination).
Numeric features were scaled using RobustScaler to handle outliers.

## Model Selection
Various models were evaluated, including:
Logistic Regression
K-Nearest Neighbors (KNN)
Decision Tree Classifier
Random Forest Classifier
Gradient Boosting Classifier
XGBoost
Support Vector Classifier (SVC)

## Model Evaluation
The models were evaluated using Stratified K-Fold Cross-Validation to ensure balanced representation of classes.
Key metrics included:
Recall: Focused on minimizing false negatives.
Precision: Evaluated the accuracy of positive predictions.
F1 Score: Harmonic mean of precision and recall.

## Results
The Tuned Gradient Boosting Classifier showed the best performance with a recall of 74% for positive claims, indicating an improvement of 6% over the default model.
The model's performance on negative claims slightly decreased, which is an acceptable trade-off given the focus on improving positive claim detection.

## Recommendations for Further Improvement
Threshold Optimization: Adjust the probability threshold for predictions to maximize recall.
Feature Engineering: Add or transform features to enhance model effectiveness.
Further Hyperparameter Tuning: Conduct deeper hyperparameter optimization or apply cross-validation to improve model robustness.

# Streamlit
## Project Overview
This Streamlit application is designed to showcase the analysis from a capstone project. It allows users to upload their own datasets in CSV or Excel format and provides insights and visualizations based on the uploaded data.

Features
File Upload: Users can upload CSV or Excel files for analysis.
Data Preview: Displays the first few rows of the uploaded dataset.
Basic Insights: Provides basic statistics about the dataset, including:
Number of rows
Number of columns
Data types of each column
Data Visualization: Users can select a numeric column to visualize its distribution through a histogram.

## Requirements
To run this application, ensure you have the following Python packages installed:

streamlit
pandas
matplotlib
You can install these packages using pip:

pip install streamlit pandas matplotlib

## How to Run the Application
Save the provided code in a file named streamlit.py.
Open a terminal and navigate to the directory containing streamlit.py.
Run the following command:
streamlit run streamlit.py

The application will open in your default web browser.

## Usage Instructions
Upload Your Data: Click on the "Choose a file" button to upload a CSV or Excel file.
Data Preview: After uploading, the first few rows of the dataset will be displayed.
Basic Insights: The application will show the number of rows, columns, and data types.
Visualization: Select a numeric column from the dropdown to generate a histogram of its distribution.

## Error Handling
If an error occurs during file upload or data processing, an error message will be displayed.
If no file is uploaded, an informational message prompts the user to upload a file.

## Conclusion
This Streamlit app serves as a user-friendly interface for analyzing datasets and visualizing data distributions. It is a valuable tool for anyone looking to gain insights from their data quickly.

### This README provides a comprehensive overview of the project, including data handling, model selection, evaluation metrics, results and provides a clear overview of the Streamlit application, its features, requirements, and instructions for use.
