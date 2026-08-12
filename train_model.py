import pickle
from pathlib import Path

from sklearn.linear_model import LinearRegression


# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Model directory
MODEL_DIR = BASE_DIR / "model"
MODEL_DIR.mkdir(exist_ok=True)

# Model file path
MODEL_PATH = MODEL_DIR / "house_price_model.pkl"


# Training data
X = [
    [500, 1, 1],
    [750, 2, 1],
    [1000, 2, 2],
    [1200, 3, 2],
    [1500, 3, 2],
    [1800, 4, 3],
    [2200, 4, 3],
]

y = [
    5000000,
    7500000,
    10000000,
    12000000,
    15000000,
    18000000,
    22000000,
]


# Create model
model = LinearRegression()

# Train model
model.fit(X, y)


# Save trained model
with open(MODEL_PATH, "wb") as file:
    pickle.dump(model, file)


print("Model trained successfully.")
print(f"Model saved to: {MODEL_PATH}")
print(f"Model exists: {MODEL_PATH.exists()}")