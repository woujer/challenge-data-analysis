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

    """
    The line properties_unique_stad = properties.drop_duplicates(subset='Stad') is used to filter 
    the DataFrame and keep only the unique rows based on the "Stad" column.
    Once we have the DataFrame with unique "Stad" values, we can proceed to calculate the average
    price per "Stad" using the groupby operation and display the results.
    """
    properties_unique_stad = properties.drop_duplicates(subset='Stad')
    properties_unique_stad['Price'] = pd.to_numeric(properties_unique_stad['Price'], errors='coerce')

    # Create pivot table of average prices per "Stad" with the corresponding region
    avg_price_per_stad = properties_unique_stad.pivot_table(values='Price', index='Stad', columns='Region', aggfunc='mean')
    avg_price_per_stad_sorted = avg_price_per_stad.mean(axis=1).sort_values(ascending=False).reset_index()

    # Get the corresponding region for each "Stad"
    avg_price_per_stad_sorted['Region'] = avg_price_per_stad_sorted['Stad'].map(properties_unique_stad.set_index('Stad')['Region'])
    pd.set_option('display.float_format', '{:.2f}'.format)
    avg_price_per_stad_sorted = avg_price_per_stad_sorted.reset_index(drop=True).rename(columns={0: 'Price'})

    print(avg_price_per_stad_sorted)

    """
    
    """
    qualitative_vars = ['Stad', 'Property type', 'Region', 'Subtype', 'Type of sale', 'Kitchen type', 'Condition']

    # Apply one-hot encoding
    encoded_data = pd.get_dummies(properties, columns=qualitative_vars)
    print(encoded_data)

cldata = clean_data(properties)
analyze_data(cldata)