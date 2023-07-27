from fastapi import FastAPI
from pydantic import BaseModel
import joblib


class Input(BaseModel):
    habbitable_surface : int
    bedroom_count : int
    garden_surface : int

def predict_new_data(data):
    
    trained_model = joblib.load("C:\\Users\\woute\\Desktop\\Dev\\Projects\\BeCode\\challenge-data-analysis\\challenge-data-analysis\\models\\decision_tree_model.pkl")

    X =[[data.habitable_surface,
         data.bed_count,
         data.garden_surface
         ]]
    
    predict = trained_model.predict(X)
    return predict