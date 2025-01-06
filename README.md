# Frozen Days Prediction Model for Lake Monona

Dataset: https://climatology.nelson.wisc.edu/first-order-station-climate-data/madison-climate/lake-ice/history-of-ice-freezing-and-thawing-on-lake-monona/

This repository contains a Python script that predicts the future freeze behavior of Lake Monona using historical data. The script uses a dataset with information on the annual number of frozen days on Lake Monona, which is analyzed through linear regression to create a predictive model. The model provides insights into the likelihood of Lake Monona freezing in the future and estimates the year when the lake might no longer freeze.

## Description
The project consists of two main parts:

Data Processing: Reads data from a CSV file containing annual frozen days and extracts relevant columns to create a new dataset.
Data Visualization & Prediction: Visualizes the data as a graph and uses the least-squares method to calculate a linear model to predict future frozen days.
The script predicts when Lake Monona may no longer freeze based on the historical trend. It also provides insights into the relationship between the year and the number of frozen days, as well as the interpretation of the model.

## Getting Started
### Prerequisites
Ensure you have Python installed on your system. The code relies on the following Python packages:
* numpy
* matplotlib

You can install the required packages using pip by running:
```bash
pip install -r requirements.txt
```

### Preparing the Data
Make sure you downloaded the data in csv format! It should look like this:
```CSV
"Category","Annual number of days","Five-year running average"
"1855-56",118,
"1856-57",151,
"1857-58",119,119
"1858-59",94,121
"1859-60",111,117
```

## Features
### CSV Data Processing
The script reads a CSV file (chart.csv), processes the data, and creates a new CSV (data.csv) containing two columns:
* year: The year when the data was collected.
* days: The number of frozen days in that year.

### Data Visualization
It generates a plot of frozen days over time using matplotlib, which is saved as plot.jpg. The graph helps visualize trends in the data.

### Linear Regression Model
Using the least squares method, the script calculates a linear regression model to determine the relationship between the year and the number of frozen days. The model provides:
* The coefficients B0 (intercept) and B1 (slope).
* A prediction for the year 2024 based on the model.
* An interpretation of the model's behavior (positive or negative trend).
* A limitation on when the lake will no longer freeze based on the calculated coefficients.
