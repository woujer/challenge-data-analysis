import pandas as pd
from src.data_cleaner import clean_data, analyze_data

properties = pd.read_csv('C:\\Users\\woute\\Desktop\\Dev\\Projects\\BeCode\\challenge-data-analysis\\challenge-data-analysis\\data\\house_details_v1.csv')

cldata = clean_data(properties)
analyze_data(cldata)