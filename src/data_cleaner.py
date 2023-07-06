import pandas as pd

def clean_data(file_path):
    # Load the data from CSV
    data = pd.read_csv(file_path)

    # Remove duplicates
    data = data.drop_duplicates()

    # Remove leading/trailing white spaces
    string_columns = data.select_dtypes(include=['object']).columns
    data[string_columns] = data[string_columns].applymap(str.strip)

    # Remove rows with errors
    data = data.dropna()

    # Replace empty values with "Unknown"
    data = data.fillna("Unknown")

    return data

def test_data(data):
    # Check for duplicates
    has_duplicates = data.duplicated().any()
    print("Duplicates exist in the dataset:", has_duplicates)

    # Check for errors (missing values)
    has_errors = data.isnull().any().any()
    print("Errors exist in the dataset:", has_errors)

    # Check for empty values
    has_empty_values = data.eq('').any().any()
    print("Empty values exist in the dataset:", has_empty_values)

# Example usage
file_path = 'filtered_data/house_details_v1.csv'
cleaned_data = clean_data(file_path)
test_data(cleaned_data)

# Save cleaned data to a new file
cleaned_data.to_csv('filtered_data/cleaned_data.csv', index=False)


import pandas as pd

def compare_csv_files(file1_path, file2_path):
    # Read the contents of both CSV files into DataFrames
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Perform a comparison between the two DataFrames
    are_equal = df1.equals(df2)

    return are_equal

# Example usage
file1_path = 'filtered_data/house_details_v1.csv'
file2_path = 'filtered_data/cleaned_data.csv'
are_files_equal = compare_csv_files(file1_path, file2_path)
print("The CSV files are equal:", are_files_equal)
