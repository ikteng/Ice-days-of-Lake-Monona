# Ice-days-of-Lake-Monona

The Downloaded Data is from https://climatology.nelson.wisc.edu/first-order-station-climate-data/madison-climate/lake-ice/history-of-ice-freezing-and-thawing-on-lake-monona/

This code performs linear regression analysis on data extracted from a CSV file to predict the number of frozen days in Lake Monona based on the year

## CSV File Visualization
- reads data from downloaded_data.csv file
- extracts the year and the number of frozen days
- visualizes the data by plotting a line graph, saving it as 'plot.jpg'

## Feature Vector Creation
- create feature vectors for the independent variable (year) and the dependent variable (number of frozen days) by initializing arrays with the appropriate dimensions and assigning values accordingly.

## Matrix Operations
- perform matrix operations required for linear regression analysis
- matrix_product: computes the matrix product of the transpose of the feature vector for the independent variable and the feature vector itself
- inverse_matrix_product: calculates the inverse of the resulting matrix
- pseudo_inverse_X: computes the pseudo-inverse of the feature vector for the independent variable

## Model Calculation & Prediction
- calculate the coefficients of the linear regression model
- make predictions based on the calculated coefficients

## Model Interpretation and Limitation
- interpret the model based on the coefficient value and identify its limitations
- determines whether the relationship between the year and the number of frozen days is positive, negative, or neutral
- estimates the year when the number of frozen days is predicted to be zero

## Main Method
- calls the functions in sequence to perform linear regression analysis on the provided data
- visualizes the data
- creates feature vectors
- computes matrix operations
- calculates the model coefficients
- makes predictions
- interprets the model results
- prints the model interpretation and limitation
