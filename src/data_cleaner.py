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

    return properties

def analyze_data(properties):
    """
    We print the number of rows and number of columns.

    """
    num_rows, num_columns = properties.shape
    print("Number of rows:", num_rows)
    print("Number of columns:", num_columns)
    
    filtered_properties = properties[properties['Price'] != 'Unknown']

    # Calculate average price per region
    average_price_per_region = filtered_properties.groupby('Region')['Price'].mean().reset_index()

    # Create bar plot
    sns.barplot(data=average_price_per_region, x='Region', y='Price')
    plt.title('Average Price by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Price')
    plt.show()

cldata = clean_data(properties)
analyze_data(cldata)