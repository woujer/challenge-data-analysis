import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""
We designate the variable properties to our CVS file.
"""
properties = pd.read_csv('C:\\Users\\woute\\Desktop\\Dev\\Projects\\BeCode\\challenge-data-analysis\\challenge-data-analysis\\data\\house_details_v1.csv')



def clean_data(properties):
    """
    We drop all duplicates with the same 'id' cause id is unique.
    Then we remove all white spaces before and after the words
    """
    properties.drop_duplicates(subset='id', inplace=True)
    string_columns = ['Stad', 'Property type', 'Region', 'Subtype', 'Type of sale', 'Kitchen type', 'Condition']
    properties[string_columns] = properties[string_columns].applymap(str.strip)
    """
    Make if price is 0 make it say Unknown cause price can't be 0.
    Then we drop all empty rows and reset our index.
    """
    properties.loc[properties['Price'] <= 0, 'Price'] = 'Unknown'
    properties.dropna(inplace=True)
    properties.reset_index(drop=True, inplace=True)
    properties = properties.loc[~((properties['Region'] == '0') | properties['Region'].isnull())]


    return properties

def analyze_data(properties):
    """
    We print the number of rows and number of columns.

    """
    num_rows, num_columns = properties.shape
    print("Number of rows:", num_rows)
    print("Number of columns:", num_columns)
    
    """
    Filter out the properties without a price. Then we will calculate the average of evry city.
    Then we merge the information with tht region information cause i couldn't find provinces.
    Then we calculate the average per region. And sort it by regions average descending.
    """
    filtered_properties = properties[properties['Price'] != 'Unknown']
    average_price_per_city = filtered_properties.groupby('Stad')['Price'].mean().reset_index()
    average_price_per_city = average_price_per_city.merge(properties[['Stad', 'Region']], on='Stad')
    average_price_per_region = average_price_per_city.groupby('Region')['Price'].mean().reset_index()
    average_price_per_region.sort_values('Price', ascending=False, inplace=True)

    """
    Plot average per region
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=average_price_per_region, x='Region', y='Price', palette='viridis')
    plt.title('Average Price by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Price')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    # Select only numeric columns for correlation calculation
    numeric_columns = properties.select_dtypes(include=['float64', 'int64']).columns
    numeric_properties = properties[numeric_columns]

    # Calculate correlation matrix
    correlation_matrix = numeric_properties.corr()

    # Sort variables by their correlation with the price
    price_column = properties['Price']
    price_correlation = correlation_matrix[price_column].abs().sort_values(ascending=False)

    print(price_correlation)

cldata = clean_data(properties)
analyze_data(cldata)