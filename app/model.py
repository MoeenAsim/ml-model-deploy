import pickle
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "house_price_model.pkl"


with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


def predict_price(area: float, bedrooms: int, bathrooms: int) -> float:
    prediction = model.predict([[area, bedrooms, bathrooms]])
    return float(prediction[0])
def predict_price(area: float, bedrooms: int, bathrooms: int) -> float:
    prediction = model.predict([[area, bedrooms, bathrooms]])
    return round(float(prediction[0]), 2)