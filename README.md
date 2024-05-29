# Ice-days-of-Lake-Monona

Dataset: https://climatology.nelson.wisc.edu/first-order-station-climate-data/madison-climate/lake-ice/history-of-ice-freezing-and-thawing-on-lake-monona/

This code performs linear regression analysis on data extracted from a CSV file to predict the number of frozen days in Lake Monona based on the year

## Data Visualization
The function visualize_data(filename) reads a CSV file and plots the data:
- Reading Data: Opens and reads the CSV file, skipping the header.
- Extracting Points: Extracts the years and the corresponding number of frozen days into two lists (xpoints and ypoints).
- Plotting: Uses matplotlib to plot the data with appropriate labels for the X and Y axes. The plot is saved as plot.jpg.
- Return Values: Returns the lists of years and frozen days.

## Feature Vector Creation
The functions create_feature_vector_X(x) and create_feature_vector_Y(y) create feature vectors for the linear regression model:
- X Vector: create_feature_vector_X creates a feature vector X with a bias term (column of ones) and the year values.
- Y Vector: create_feature_vector_Y creates a vector Y with the number of frozen days.

## Matrix Operations for Linear Regression
- perform matrix operations required for linear regression analysis
- matrix_product: computes the matrix product of the transpose of the feature vector for the independent variable and the feature vector itself
- inverse_matrix_product: calculates the inverse of the resulting matrix
- pseudo_inverse_X: computes the pseudo-inverse of the feature vector for the independent variable
- calculate_B(PI,Y): calculates the regression coefficients B using the pseudo-inverse and the target vector Y

## Prediction and Interpretation
Functions for prediction and model interpretation:
- Prediction: prediction(B) uses the computed coefficients to predict the number of frozen days for the year 2022 and prints the prediction.
- Model Interpretation: model_interpretation(B1) interprets the sign of the slope 𝐵1 to determine if the likelihood of frozen days is increasing or decreasing.
- Model Limitation: model_limitation(B) estimates the year when Lake Monona will no longer freeze based on the model.

## Main Method
- calls the functions in sequence to perform linear regression analysis on the provided data
- visualizes the data
- creates feature vectors
- computes matrix operations
- calculates the model coefficients
- makes predictions for the year 2022 and interprets the model.
- interprets the model results
- prints the model interpretation and limitation
- Estimates the model's limitation by predicting the year when Lake Monona will no longer freeze

# Summary
This code provides a comprehensive pipeline for visualizing annual data and performing simple linear regression. It includes:
- Data extraction and visualization.
- Feature vector creation.
- Matrix operations for linear regression.
- Prediction and model interpretation
