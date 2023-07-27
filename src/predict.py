from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import  pickle


class Input(BaseModel):
    habbitable_surface : int
    bedroom_count : int
    garden_surface : int

def predict_new_data(data):
    try:
        pickle_in = open('C:\\Users\\woute\\Desktop\\Dev\\Projects\\BeCode\\challenge-data-analysis\\challenge-data-analysis\\models\\descision_tree.pickle', 'rb')
        model = pickle.load(pickle_in)
        
        prediction = model.predict(data)
        return {"prediction": prediction.tolist()}
    except TypeError:
        return "Type error use the correct type"
    except KeyError:
        return "No key like that"
    except SyntaxError:
        return "wrong Syntax"
    except KeyError:
        return "Enter a correct key"