# Part 1 Challenge data collection Immo Eliza
## Description
The provided Python 3 program performs data analysis on a CSV file containing house details. The code utilizes various libraries such as Pandas, NumPy, Matplotlib, and Seaborn for data manipulation, cleaning, visualization, and analysis.

The clean_data function is responsible for preprocessing the data. It drops duplicate rows based on the 'id' column, removes leading and trailing white spaces from string columns, updates specific columns based on given conditions, drops rows with missing values, and performs some data transformations.

The analyze_data function conducts data analysis and generates visualizations. It calculates the number of rows and columns, filters out properties without a price, calculates the average price per region and visualizes it using a bar plot, explores correlations between variables and price, examines the influence of variables on price, calculates the percentage of missing values, identifies outliers using a scatter plot, suggests variables to delete based on their importance and missing values, creates a histogram to represent the distribution of property surfaces, determines the most important variables based on personal opinion, identifies the most expensive municipalities in Belgium, Wallonia, and Flanders in terms of average price, median price, and price per square meter, and lists the least expensive municipalities in Belgium.

The code demonstrates various data analysis techniques and provides insights into the house market based on the given dataset. It showcases data cleaning, visualization, and interpretation skills in Python.

Please note that the provided description assumes the code is functioning correctly and produces the expected results.

## Installation

To run this project, follow the steps below:

1. Clone the repository to your local machine using the following command:
  git clone https://github.com/your-username/your-repository.git

2. Navigate to the project directory:
   cd your-repository
   
3. Install the required dependencies by running the following command:
   pip install pandas numpy matplotlib seaborn

This will install the necessary Python libraries (`pandas`, `numpy`, `matplotlib`, and `seaborn`) required for the project.

4. Place the `house_details_v1.csv` file in the same directory as your Python script.
5. You are now ready to use the project. Run the Python script to execute the data analysis:
   python your_script_name.py

Make sure to replace `your_script_name.py` with the name of your Python script file.
By following these steps, you should be able to set up the project and run the data analysis on your local machine.
Note: The installation instructions assume that you have Git and Python installed on your machine. If not, please install them before proceeding with the steps above.

## Features
    Data cleaning: The project includes a function that performs data cleaning operations on the provided CSV file. It removes duplicates, handles missing values, and applies necessary transformations to ensure data integrity.

    Data analysis: The project offers various data analysis capabilities. It calculates the number of rows and columns, explores correlations between variables and price, identifies influential variables, and analyzes the distribution of property surfaces using histograms.

    Visualizations: The project utilizes the Matplotlib and Seaborn libraries to create visualizations. It generates bar plots to showcase the average price by region and the most expensive cities by price per square meter. It also includes scatter plots to highlight the relationship between price and habitable surface.

    Insights and interpretations: The project provides insights and interpretations based on the data analysis. It identifies the most and least expensive municipalities in Belgium, Wallonia, and Flanders. It examines the importance of variables in determining price and suggests variables to be deleted based on their influence. It also calculates the percentage of missing values and offers troubleshooting tips.

    Customization: The project allows for customization and configuration. It provides instructions on how to modify specific columns based on given conditions and adjust settings to suit specific requirements.

    User-friendly documentation: The project includes a README.md file with clear instructions for installation, usage, and contribution. It aims to provide an accessible and user-friendly guide for users and developers.

## Configuration
To configure or customize the project, follow the steps below:

    Open the Python script file in a text editor of your choice.

    Modify the specific columns based on the given conditions in the clean_data function. This allows you to tailor the data cleaning process to your specific needs.

    Adjust any settings or variables in the script that are marked for customization. These may include file paths, data filters, or visualizations parameters.

    Save the modified Python script file.

By following these steps, you can easily configure the project to suit your requirements

# Part 2 Challenge_recursion

This repository contains code for performing a regression analysis on property prices using various regression techniques. The dataset used in this analysis is assumed to be in the variable properties, and the goal is to predict property prices based on features such as Habitable surface, Bedroom Count, and Garden surface. The code also includes data cleaning steps and visualizations to aid in the analysis.
Requirements

    pandas
    numpy
    scikit-learn
    matplotlib

Data Cleaning

The data_clean function is responsible for cleaning the dataset. However, it should be noted that the current data cleaning implementation is not ideal due to time constraints. There might be some issues with dropping too many columns and not handling missing values effectively. Improving the data cleaning process could potentially lead to better model performance.
Data Analysis and Regression

The data_analyse function performs data analysis and regression on the cleaned dataset. The steps include:

    Splitting the data into training and testing sets.
    Implementing Polynomial Linear Regression, Stochastic Gradient Descent (SGD) Regression, and Decision Tree Regression.
    Displaying training and testing scores for each regression model.
    Plotting the actual vs. predicted prices for each regression model.

Usage

To use this code, make sure you have installed the required libraries. You can then execute the code and observe the regression analysis results.

# Part 3: Deployment

This project implements a simple FastAPI API to predict the price of a house based on input features. The model used for prediction is a decision tree model.

## Requirements

- Python 3.10
- FastAPI
- uvicorn
- pickle

## Setup and Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using the following command: pip install -r requirements.txt
3. To start the FastAPI app, run the following command: uvicorn app:app --host 0.0.0.0 --port 8000

4. The API will be accessible at `http://localhost:8000`.

## Endpoints

### `GET /`

This endpoint returns a simple string explaining the format of data expected for the prediction.

### `POST /predict_price`

This endpoint accepts a POST request with JSON data containing the features of the house to predict. The required format is as follows:

```json
{
 "habbitable_surface": 150,
 "bedroom_count": 3,
 "garden_surface": 200
}

## Docker Support
You can also run the House Price Prediction API inside a Docker container. To do this, follow these steps:

1. Build the Docker image using the following command: docker build -t house-price-prediction .
2. Run the Docker container using the following command:docker run -d -p 8000:8000 house-price-prediction

The API will be accessible at http://localhost:8000.

Please make sure to adjust the paths and file names in the code to match your specific project structure and file locations.

# Author
Wouter Daneels