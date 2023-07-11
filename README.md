# Challenge data collection Immo Eliza
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



