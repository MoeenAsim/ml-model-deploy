from fastapi import FastAPI
from pydantic import BaseModel

from app.model import predict_price


app = FastAPI(title="ML Pipeline API")


class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int


@app.get("/")
def root():
    return {"message": "ML Pipeline API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: HouseData):
    price = predict_price(
        data.area,
        data.bedrooms,
        data.bathrooms,
    )

    return {
        "predicted_price": price
    }