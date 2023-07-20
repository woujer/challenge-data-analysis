import pandas as pd
from src.challenge_recursion import *

data_path = 'C:\\Users\\woute\\Desktop\\Dev\\Projects\\BeCode\\challenge-regression\\data\\house_details_v3.csv'

"""Evaluation
i'm personally not statisfied with the results i got i lost to mutch time with Import error and Type errors those were easily solved when i started all over again
Cause i started over with the project i made a simplified version of a DataCleaner that drops to mutch columns.
I wanted to focus on the main part of regression and did it with the data i had avaible.
Cause of that reason i have pretty low scores the only high score i have right now is my Decision tree training.
Personally i would like to work some more on it to realy have a good program where i'm happy with the results. 

I've disabled the privious data_analyze.py so i don't have to mutch going on.
Wasn't able to intergrate XGboost wasn't able to start on it in my notebook cause i had a wierd problem where i wasn't able to import my libary.
Conclusion: I'm not happy with my result i would like to work do some more work on my data_cleaner function so i am able to have some more features.
"""

def Startup(data_path):
    properties = pd.read_csv(data_path)
    properties = data_clean(properties)
    data_analyse(properties)

Startup(data_path)