import fastapi, uvicorn
from pydantic import BaseModel
from src.predict import *
from src.preprocessing import *
import pickle

app = fastapi.FastAPI(debug=True)

pickle_in = open('C:\\Users\\woute\\Desktop\\Dev\\Projects\\BeCode\\challenge-data-analysis\\challenge-data-analysis\\models\\descision_tree.pickle', 'rb')
model = pickle.load(pickle_in)

@app.get('/')
def index():
    return "We expect 3 numerical values, Habitable are, bedcount, garden area"


@app.post('/predict_price')
def predict_price(data: Input):
    new_data = preproces_new_data(data)
    return predict_new_data(new_data)
