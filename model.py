import csv
import numpy as np
import matplotlib.pyplot as plt

def create_csv(input_filename, output_filename):
    """
    Reads the input CSV, processes the data, and creates a new CSV with two columns:
    'year' and 'days', based on the 'Category' and 'Annual number of days' columns in the input file.
    """
    try:
        # Open the input CSV for reading and output CSV for writing
        with open(input_filename, 'r', encoding='utf-8-sig') as read_file, open(output_filename, 'w', newline='') as write_file:
            reader = csv.DictReader(read_file)  # Read the CSV as a dictionary
            writer = csv.writer(write_file)  # Prepare to write to the output CSV
            writer.writerow(['year', 'days'])  # Write header row with 'year' and 'days' columns

            # Loop through each row in the input CSV
            for row in reader:
                try:
                    # Extract the 'year' from the 'Category' column by splitting the value at '-'
                    year = row['Category'].split('-')[0]
                    # Extract the number of days from the 'Annual number of days' column
                    days = row['Annual number of days']
                    # Ensure that the 'days' column contains valid digits before writing
                    if days.isdigit():
                        writer.writerow([year, int(days)])  # Write the year and days to the output CSV
                    else:
                        print(f"Skipping invalid days data in row: {row}")  # Skip rows with invalid 'days' values
                except KeyError as e:
                    print(f"Missing expected column in row: {row}. Skipping row.")  # Handle missing columns
                except Exception as e:
                    print(f"Error processing row {row}: {e}")  # Handle other errors

        print(f"CSV file created successfully: {output_filename}")  # Success message
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")  # Error if the input file is missing
    except Exception as e:
        print(f"An error occurred while creating CSV: {e}")  # General error handling

def visualize_data(filename):
    """Reads data from the CSV and plots a graph."""
    try:
        # Load data from the CSV file, skipping the header row, and converting values to integers
        data = np.genfromtxt(filename, delimiter=',', skip_header=1, dtype=int)
        if data.size == 0:
            print("No data found in the file.")  # If the data is empty, print a message and return empty lists
            return [], []

        # Separate the data into x (years) and y (days) arrays
        xpoints, ypoints = data[:, 0], data[:, 1]

        # Create the plot with a specified figure size
        plt.figure(figsize=(10, 6))
        plt.plot(xpoints, ypoints, marker='o', linestyle='-', color='b', label="Frozen Days")  # Plot the data points
        plt.xlabel("Year")  # Label for the x-axis
        plt.ylabel("Number of Frozen Days")  # Label for the y-axis
        plt.title("Frozen Days Over Time")  # Title for the plot
        plt.grid(True)  # Show gridlines for better readability
        plt.legend()  # Add a legend to the plot

        # Annotate each data point with its corresponding value
        for i, txt in enumerate(ypoints):
            plt.annotate(f'{txt}', (xpoints[i], ypoints[i]), textcoords="offset points", xytext=(0, 5), ha='center')

        # Save the plot as a .jpg file
        plt.savefig("plot.jpg")
        print("Plot saved successfully.")  # Success message
        return xpoints, ypoints  # Return the x and y data points for further processing
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")  # Error if the file is missing
    except ValueError:
        print(f"Error: The data in {filename} could not be converted to integers.")  # Error if the data can't be converted to integers
    except Exception as e:
        print(f"An error occurred: {e}")  # General error handling
        return [], []  # Return empty lists if an error occurred

def calculate_B(X, Y):
    """Performs the least squares method to calculate the model coefficients B."""
    try:
        # Calculate the matrix product of X^T (transpose of X) and X
        Z = np.dot(X.T, X)
        # Calculate the inverse of Z
        I = np.linalg.inv(Z)
        # Calculate the pseudo-inverse of X
        PI = np.dot(I, X.T)
        # Calculate the model coefficients B using the least squares formula: B = (X^T * X)^(-1) * X^T * Y
        B = np.dot(PI, Y)
        # Return the calculated coefficients
        return B  
    
    # Handle matrix inversion errors
    except np.linalg.LinAlgError:
        print("Error: Matrix inversion failed. The matrix may be singular.")  
        return None  # Return None if there's an issue with matrix inversion
    # General error handling
    except Exception as e:
        print(f"An error occurred during model calculation: {e}")  
        return None

def model_interpretation(B1):
    """Interprets the model coefficient B1."""
    # Positive coefficient interpretation
    if B1 > 0:
        return "It is more likely to have Monona ice in the future."  
    # Negative coefficient interpretation
    elif B1 < 0:
        return "It is less likely to have Monona ice in the future."  
    # Zero coefficient interpretation
    else:
        return "There is an equal chance of having and not having Monona ice in the future."  

def model_limitation(B):
    """Determines the year when Lake Monona will no longer freeze."""
    # Ensure that B1 is non-zero to avoid division by zero
    if B[1] != 0:  
        # Calculate the year when the lake will no longer freeze using the formula: year = -B0 / B1
        x = -B[0] / B[1]
        # Handle future projections
        if x < 2024:
            return "Model Limitation: The model predicts that the lake will not freeze in the near future."  
        # Provide the year when the lake will no longer freeze
        return f"Model Limitation: It is estimated that during the year {x:.3f}, Lake Monona will no longer freeze."  
    # Handle case where B1 is zero
    return "Model Limitation: No specific year predicted."  

def main():
    # Create the data.csv file by processing the input chart.csv file
    create_csv('chart.csv', 'data.csv')

    # Visualize the data and get the x (years) and y (days) values
    x, y = visualize_data('data.csv')

    # Proceed only if data is successfully loaded
    if len(x) == 0 or len(y) == 0:  
        print("Data visualization failed, so no further analysis.")
        return

    # Prepare the feature vector for the input data, adding a column of ones for the intercept term
    X = np.column_stack((np.ones(len(x)), x))
    # Convert the y data to a NumPy array for compatibility with matrix operations
    Y = np.array(y)  

    # Calculate the model coefficients using the least squares method
    B = calculate_B(X, Y)
    if B is not None:
        # Print the model coefficients
        print(f"Model coefficients: B0 = {B[0]:.3f}, B1 = {B[1]:.3f}") 
        # Make a prediction for the year 2024 based on the model
        B1, Y_test = B[1], B[0] + B[1] * 2024
        # Print the prediction for 2024
        print(f"Prediction for 2024: {Y_test:.3f}")  
        # Print the interpretation of the model
        print(f"Model Interpretation: {model_interpretation(B1)}")  
        # Print the model limitation based on the calculated coefficients
        print(model_limitation(B))  

    # Error if the model calculation fails
    else:
        print("Failed to calculate model coefficients.")  

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()  
