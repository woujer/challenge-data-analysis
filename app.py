import fastapi, uvicorn
from pydantic import BaseModel
from src.predict import predict_new_data
import joblib

trained_model = joblib.load("C:\\Users\\woute\\Desktop\\Dev\\Projects\\BeCode\\challenge-data-analysis\\challenge-data-analysis\\models\\decision_tree_model.pkl")

app = fastapi.FastAPI()

class Input(BaseModel):
    habitable_surface = int,
    bedroom_count = int,
    garden_surface = int


@app.post('/predict_price')
def predict_price(data:Input):
    predict_new_data(data)


