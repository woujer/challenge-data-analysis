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
    We drop all duplicates with the same 'id' since ID is unique.
    Then we remove all leading and trailing white spaces from string columns.
    """
    properties.drop_duplicates(subset='id', inplace=True)
    string_columns = ['Stad', 'Property type', 'Region', 'Subtype', 'Type of sale', 'Kitchen type', 'Condition']
    properties[string_columns] = properties[string_columns].applymap(str.strip)
    
    """
    Update specific columns as per the given conditions:
    - ID: Drop rows with ID = 0
    - Price: If Price is 0, make it 'UNKNOWN'. Convert all values to numeric.
    - Construction year: If Construction year is 0, make it 'UNKNOWN'. Convert all values to numeric.
    - Habitable surface: If Habitable surface is 0, make it 'UNKNOWN'. Convert all values to numeric.
    - Region: Keep only the values 'BRUSSELS', 'WALLONIE', 'FLANDERS', drop others
    """
    properties = properties[properties['id'] != 0]
    properties['Price'] = pd.to_numeric(properties['Price'], errors='coerce')
    properties.loc[properties['Price'] == 0, 'Price'] = 'UNKNOWN'
    properties['Construction year'] = pd.to_numeric(properties['Construction year'], errors='coerce')
    properties.loc[properties['Construction year'] == 0, 'Construction year'] = 'UNKNOWN'
    properties['Habitable surface'] = pd.to_numeric(properties['Habitable surface'], errors='coerce')
    properties.loc[properties['Habitable surface'] == 0, 'Habitable surface'] = 'UNKNOWN'
    properties = properties[properties['Region'].isin(['BRUSSELS', 'WALLONIE', 'FLANDERS'])]
    properties.loc[properties['Kitchen type'] == '0', 'Kitchen type'] = 'UNKNOWN'
    
    """
    Drop rows with missing values and reset the index.
    """
    city_variations = {
        'Knokke-Het Zoute': 'Knokke-Zoute',
        'KNOKKE-ZOUTE': 'Knokke-Zoute',
        'Knokke-Zoute': 'Knokke-Zoute'
    }
    properties['Stad'] = properties['Stad'].replace(city_variations)
    
    city_variations= {
        'Knokke-Heist':'Knokke-Heist',
        'Knokke-Heist Knokke':'Knokke-Heist',
        'KNOKKE': 'Knokke-Heist',
        '8300':'Knokke-Heist'
    }
    properties['Stad'] = properties['Stad'].replace(city_variations)

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
    
    """
    Filter out the properties without a price.
    Convert 'Price' column to numeric type.
    """
    filtered_properties = properties[properties['Price'] != 'Unknown']
    filtered_properties['Price'] = pd.to_numeric(filtered_properties['Price'], errors='coerce')

    """
    Calculate the average price per region.
    Filter regions of interest.
    """
    average_price_per_region = filtered_properties.groupby('Region')['Price'].mean().reset_index()
    regions_of_interest = ['BRUSSELS', 'WALLONIE', 'FLANDERS']
    filtered_average_price_per_region = average_price_per_region[average_price_per_region['Region'].isin(regions_of_interest)]

    plt.figure(figsize=(12, 6))
    sns.barplot(data=filtered_average_price_per_region, x='Region', y='Price', palette='viridis')
    plt.title('Average Price by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Price')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show() 
    """How vars correlate to eachother
    We can clearly see if a stad is knokke or a region brussel and then a more expandsive city it will also give a rise in the price. 

    """
    properties['Price'] = pd.to_numeric(properties['Price'], errors='coerce')
    sorted_properties = properties.sort_values(by='Price', ascending=False)
    table_correlation = sorted_properties[['Price', 'Stad', 'Region']]
    print(table_correlation.head(20))

    """Which vars have the greatest influence on the price.
    We can clearly see the correlation when a habitable surface is bigger the price will also get biggger.
    This also counts for the garden but it has less influence.
    To check this we will first convert our values to numeric. After that we will drop all properties without a surface and price.
    At last we will order all values by price.
    We also already check our least influencial vars. As we can see Kitchen type and construction year don't have alot to do with the price
    We can also see that the 'Stad' also a influence certain citys have a great influence on the price. 
    """
    properties['Habitable surface'] = pd.to_numeric(properties['Habitable surface'], errors='coerce')
    properties['Garden surface'] = pd.to_numeric(properties['Garden surface'], errors='coerce')

    filtered_properties = properties.dropna(subset=['Habitable surface', 'Price'])

    table = filtered_properties[['Habitable surface', 'Garden surface', 'Price','Stad','Kitchen type', 'Construction year']]

    table = table.sort_values('Price', ascending=False)
    print(table.head(25))

    """Checking for qualitative or quantitative values
    """
    """Calculate the percentage of missing values
    
    """
    """
    Calculate the number of missing values and "UNKNOWN" values for each variable and display the result.
    """
    total_missing_values = properties.isnull().sum().sum() + (properties == 'UNKNOWN').sum().sum()
    total_values = properties.size
    
    missing_values_percentage = (total_missing_values / total_values) * 100
    
    missing_values_data = pd.DataFrame({
        'Total Missing Values': [total_missing_values],
        'Missing Values Percentage': [missing_values_percentage]
    })
    
    print("Missing Values:")
    print(missing_values_data)

    """Step3: Data interpretation
    The outliers???
    """
    plt.figure(figsize=(12, 6))
    for region in ['BRUSSELS', 'WALLONIE', 'FLANDERS']:
        subset = properties[properties
        ['Region'] == region]
        plt.scatter(subset['Price'], subset['Habitable surface'], label=region)

    plt.title('Scatter Plot: Price vs Habitable Surface')
    plt.xlabel('Price in milions')
    plt.ylabel('Habitable Surface')
    plt.legend()
    plt.show()

    """Which variables would you delete and why ?
    I would delete the Kitchen Type. Most people aren't familiar with the lingo and it has the most missing values.
    I think people rather want to see the kitchen on a photo than just see what kind of kitchen it is. 
    """
    """Represent the number of properties according to their surface using a histogram.
    """
    plt.figure(figsize=(12, 6))
    bins = range(0, 2000, 100) 
    plt.hist(properties['Habitable surface'], bins=bins, edgecolor='black')
    plt.title('Number of Properties by Surface')
    plt.xlabel('Habitable Surface')
    plt.ylabel('Count')
    plt.xticks(bins) 
    plt.show()

    """In your opinion, which 5 variables are the most important and why?
    In my opinion the most important variables are: Price, ID , Habitable surface, Stad,Garden surface
    """
    """What are the **most** expensive municipalities in Belgium? (Average price, median price, price per square meter)
    We will calculate the average median and average per square meter. Then we will print a list of the median and the average.
    I made a barplot visualization of the average/sqm in a bar plot.
    
    """
    average_price_stad = properties.groupby('Stad')['Price'].mean().sort_values(ascending=False)

    median_price_stad = properties.groupby('Stad')['Price'].median().sort_values(ascending=False)

    properties['Price per sqm'] = properties['Price'] / properties['Habitable surface']
    price_per_sqm_stad = properties.groupby('Stad')['Price per sqm'].mean().sort_values(ascending=False)

    print("Most Expensive cities by Average Price:")
    print(average_price_stad.head(10))

    print("\nMost Expensive cities by Median Price:")
    print(median_price_stad.head(10))

    
    plt.figure(figsize=(12, 6))
    price_per_sqm_stad.head(10).plot(kind='bar')
    plt.title('Most Expensive Cities by Price per Square Meter')
    plt.xlabel('City (Stad)')
    plt.ylabel('Average Price per Square Meter')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    """What are the **most** expensive municipalities in Wallonia? (Average price, median price, price per square meter;
    First let's filter all properties for WALLONIE. Than we calculate the average, median and average per square meter per city.
    Then we will create a new df  where we put our values in.
    """

    wallonie_properties = properties[properties['Region'] == 'WALLONIE']

    average_price_stad = wallonie_properties.groupby('Stad')['Price'].mean().sort_values(ascending=False).head(10)

    median_price_stad = wallonie_properties.groupby('Stad')['Price'].median().sort_values(ascending=False).head(10)

    wallonie_properties.loc['Price per sqm'] = wallonie_properties['Price'] / wallonie_properties['Habitable surface']
    price_per_sqm_stad = wallonie_properties.groupby('Stad')['Price per sqm'].mean().sort_values(ascending=False).head(10)

    table = pd.DataFrame({
        'Stad': average_price_stad.index,
        'Average Price': average_price_stad.values,
        'Median Price': median_price_stad.values,
        'Average Price per Sqm': price_per_sqm_stad.values
    })

    table = table.sort_values(by='Average Price', ascending=False)
    table.columns = ['Stad', 'Average Price', 'Median Price', 'Average Price per Sqm']
    table = table.sort_values(by='Average Price', ascending=False)

    print(table)

    """What are the **most** expensive municipalities in Flanders? (Average price, median price, price per square meter)
    So we will start with filtering properties Region=FLANDERS. Then we will calculate the average median and average/sqm.
    We will put our found data in a new dataframe. and after that We will sort it for average price. Almost the same as Wallonie
    """

    flanders_properties = properties[properties['Region'] == 'FLANDERS'].copy()

    average_price_municipality = flanders_properties.groupby('Stad')['Price'].mean().sort_values(ascending=False).head(10)

    median_price_municipality = flanders_properties.groupby('Stad')['Price'].median().sort_values(ascending=False).head(10)

    flanders_properties.loc[:, 'Price per sqm'] = flanders_properties['Price'] / flanders_properties['Habitable surface']
    price_per_sqm_municipality = flanders_properties.groupby('Stad')['Price per sqm'].mean().sort_values(ascending=False).head(10)

    table = pd.DataFrame({
        'Municipality': average_price_municipality.index,
        'Average Price': average_price_municipality.values.astype(int),
        'Median Price': median_price_municipality.values,
        'Average Price per Sqm': price_per_sqm_municipality.values
    })

    table = table.sort_values(by='Average Price', ascending=False)

    print(table)


cldata = clean_data(properties)
analyze_data(cldata)