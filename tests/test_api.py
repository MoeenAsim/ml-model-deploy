from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "ML Pipeline API is running"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_prediction():
    response = client.post(
        "/predict",
        json={
            "area": 1200,
            "bedrooms": 3,
            "bathrooms": 2,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_price" in data
    assert data["predicted_price"] > 0


def test_invalid_prediction_input():
    response = client.post(
        "/predict",
        json={
            "area": "invalid",
            "bedrooms": 3,
            "bathrooms": 2,
        },
    )

    assert response.status_code == 422