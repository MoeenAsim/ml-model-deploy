# House Price ML Pipeline

A complete machine learning model serving and deployment pipeline for house price prediction, built with Python, FastAPI, Scikit-learn, Pytest, Docker, GitHub Actions, and GitHub Container Registry.

---

## Overview

House Price ML Pipeline is an end-to-end machine learning application that predicts house prices based on basic property information.

The application accepts:

- House area
- Number of bedrooms
- Number of bathrooms

and uses a trained machine learning regression model to estimate the house price.

The trained model is exposed through a FastAPI REST API, tested automatically using Pytest, containerized using Docker, and integrated with GitHub Actions for Continuous Integration and Continuous Delivery.

The complete workflow is:

```text
House Data
    │
    ▼
Machine Learning Model
    │
    ▼
FastAPI REST API
    │
    ▼
Automated Tests
    │
    ▼
Docker Container
    │
    ▼
GitHub Actions CI
    │
    ▼
GitHub Actions CD
    │
    ▼
GitHub Container Registry
    │
    ▼
Deployment-Ready Docker Image

---

## Project Purpose

The project demonstrates how a trained machine learning model can be transformed into a deployable software application.

Instead of keeping the trained model as a standalone .pkl file, this project:

Trains the machine learning model
Saves the trained model
Loads the model inside a FastAPI application
Provides predictions through a REST API
Validates the API using automated tests
Packages the application using Docker
Builds the Docker image automatically through CI
Publishes the Docker image through CD
Stores the image in GitHub Container Registry

The house price prediction problem is used as the ML use case, while the main engineering focus is on model serving, testing, containerization, and CI/CD automation.

## Machine Learning Component

The project uses a Scikit-learn Linear Regression model to estimate house prices.

The model receives three input features:

Feature	Description	Example
area	House area	1200
bedrooms	Number of bedrooms	3
bathrooms	Number of bathrooms	2

The model is trained using:

train_model.py

After training, the serialized model is stored in:

model/house_price_model.pkl

The FastAPI application loads this trained model and uses it to generate predictions.

## Dataset Note

The current project uses a small sample dataset created for demonstrating the machine learning deployment workflow.

It is intended as a technical and portfolio demonstration rather than a real-world property valuation system.

A future version can use a larger real-world housing dataset with proper preprocessing, train/test splitting, feature engineering, and model evaluation.

## Machine Learning Workflow

The model training process follows:

Training Data
     │
     ▼
Feature Selection
     │
     ▼
Linear Regression Model
     │
     ▼
Model Training
     │
     ▼
Trained Model
     │
     ▼
house_price_model.pkl

The training script can be executed using:

python train_model.py

Example output:

Model trained successfully.
Model saved to: model/house_price_model.pkl
Model exists: True
## FastAPI Application

The trained ML model is served through a REST API built with FastAPI.

The API provides endpoints for:

Health checking
House price prediction
Interactive API documentation

FastAPI acts as the interface between the user/client and the trained machine learning model.

## API Endpoints
1. Health Check
Request
GET /health
Example
curl http://127.0.0.1:8000/health
Response
{
  "status": "healthy"
}

This endpoint can be used by deployment systems or monitoring tools to verify that the API is running correctly.

2. House Price Prediction
Request
POST /predict

The endpoint accepts information about the house.

Request Body
{
  "area": 1200,
  "bedrooms": 3,
  "bathrooms": 2
}
Example using cURL
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d "{\"area\":1200,\"bedrooms\":3,\"bathrooms\":2}"
Example Response
{
  "predicted_price": 11999999.999999996
}

The exact floating-point representation may vary slightly depending on the model and runtime environment.

## Interactive Swagger Documentation

FastAPI automatically generates interactive API documentation.

After starting the application, open:

http://127.0.0.1:8000/docs

The Swagger interface allows you to:

View API endpoints
Inspect request schemas
Send prediction requests
Test the health endpoint
View API responses

Example workflow:

Open /docs
    │
    ▼
Select POST /predict
    │
    ▼
Click "Try it out"
    │
    ▼
Enter house information
    │
    ▼
Execute
    │
    ▼
Receive predicted price
## Automated Testing

The project uses Pytest for automated testing.

Tests are located in:

tests/

Run the tests locally:

pytest

Example test result:

============================= test session starts =============================

collected 4 items

tests/test_api.py ....                                                   [100%]

============================== 4 passed ======================================

The current test suite contains four tests.

Automated testing helps ensure that changes to the application do not break existing functionality.

## Testing Workflow

The local testing workflow is:

Code Change
    │
    ▼
Run pytest
    │
    ├── Tests Pass ──────► Continue
    │
    └── Tests Fail ──────► Fix Code

The same tests are also executed automatically by GitHub Actions.

## Docker Containerization

The application is containerized using Docker.

Docker packages the application and its runtime dependencies into a portable container.

The container includes:

Python runtime
FastAPI
Scikit-learn
Pydantic
Uvicorn
Application source code
Trained ML model

The Docker workflow is:

Application
     │
     ▼
Dockerfile
     │
     ▼
Docker Image
     │
     ▼
Docker Container
     │
     ▼
FastAPI
     │
     ▼
ML Prediction API
## Docker Image

Build the Docker image locally:

docker build -t house-price-ml:1.0 .

Example:

[+] Building ... FINISHED
...
naming to docker.io/library/house-price-ml:1.0

Verify the image:

docker images

Example:

REPOSITORY        TAG
house-price-ml   1.0
## Run Docker Container

Run the application inside Docker:

docker run -d \
  --name house-price-api \
  -p 8000:8000 \
  house-price-ml:1.0

Check the running container:

docker ps

Example:

CONTAINER ID   IMAGE              STATUS        PORTS
xxxxxxxxxxxx   house-price-ml:1.0 Up ...        0.0.0.0:8000->8000/tcp

The API is now available at:

http://localhost:8000

Swagger:

http://localhost:8000/docs

Health check:

http://localhost:8000/health
## Stop Docker Container

Stop the running container:

docker stop house-price-api

Remove the container:

docker rm house-price-api
## CI/CD Pipeline

The project uses GitHub Actions to automate testing, Docker image building, and container image publishing.

The workflow contains two pipelines:

.github/
└── workflows/
    ├── ci.yml
    └── cd.yml
# Continuous Integration (CI)

The CI pipeline automatically validates the project.

The workflow performs:

Git Push
   │
   ▼
Checkout Code
   │
   ▼
Setup Python
   │
   ▼
Install Dependencies
   │
   ▼
Run Pytest
   │
   ▼
Build Docker Image
   │
   ▼
CI Success
CI Responsibilities
Checkout repository
Configure Python
Install dependencies
Run automated tests
Build Docker image

If tests fail, the CI workflow fails.

This prevents broken code from being considered ready for delivery.

# Continuous Delivery (CD)

The CD workflow publishes the Docker image to GitHub Container Registry.

The process is:

Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Authenticate with GHCR
    │
    ▼
Build Docker Image
    │
    ▼
Push Docker Image
    │
    ▼
GitHub Container Registry

The result is a deployment-ready container image.

## GitHub Container Registry

The project publishes its Docker image to GitHub Container Registry (GHCR).

The image follows this format:

ghcr.io/moeenasim/ml-model-deploy:latest

The image can be pulled from a Docker-compatible environment using:

docker pull ghcr.io/moeenasim/ml-model-deploy:latest

This allows the same containerized application to be used in different environments without rebuilding the application from scratch.

## GitHub Authentication

The CD workflow uses GitHub's automatically generated:

GITHUB_TOKEN

for authentication with GitHub Container Registry.

The workflow does not store a personal GitHub token inside the repository.

The required permissions are:

permissions:
  contents: read
  packages: write

This allows the workflow to:

Read repository contents
Publish the Docker image to GHCR

Sensitive credentials should never be hard-coded into source code.

## Complete Architecture

The complete system architecture is:

                         Developer
                             │
                             │ git push
                             ▼
                    GitHub Repository
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
          CI Workflow                CD Workflow
                │                         │
                ▼                         ▼
             Pytest               GHCR Authentication
                │                         │
                ▼                         ▼
         Docker Build             Docker Image Build
                │                         │
                │                         ▼
                │                    Push Image
                │                         │
                └────────────┬────────────┘
                             ▼
                    GitHub Container
                       Registry
                             │
                             ▼
                  Deployment-Ready Image
## Application Architecture

Inside the application itself:

Client
  │
  │ HTTP Request
  ▼
FastAPI
  │
  ▼
Request Validation
  │
  ▼
ML Model
  │
  ▼
Prediction
  │
  ▼
JSON Response
## Project Structure
ml-pipeline/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── model.py
│
├── model/
│   ├── .gitkeep
│   └── house_price_model.pkl
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── Dockerfile
├── .dockerignore
├── docker-compose.yml
├── .gitignore
├── requirements.txt
├── train_model.py
└── README.md
## File Responsibilities
train_model.py

Responsible for:

Creating training data
Training the machine learning model
Saving the trained model
Generating the .pkl model file
app/main.py

Responsible for:

Creating the FastAPI application
Defining API endpoints
Receiving prediction requests
Returning API responses
app/model.py

Responsible for:

Loading the trained ML model
Providing prediction functionality to the API
model/house_price_model.pkl

Serialized trained machine learning model used for inference.

tests/test_api.py

Contains automated tests for the FastAPI application.

Dockerfile

Defines how the application is packaged into a Docker image.

.dockerignore

Prevents unnecessary files such as:

.venv
.git
__pycache__
.pytest_cache

from being included in the Docker build context.

ci.yml

Defines the Continuous Integration workflow.

cd.yml

Defines the Continuous Delivery workflow and publishes the Docker image to GHCR.

## Technology Stack
Technology	Purpose
Python	Application and ML development
Scikit-learn	Machine learning model
FastAPI	REST API and model serving
Pydantic	Request validation
Uvicorn	ASGI application server
Pytest	Automated testing
Docker	Containerization
Git	Version control
GitHub	Source code hosting
GitHub Actions	CI/CD automation
GitHub Container Registry	Docker image storage
## Local Development
1. Clone the Repository
git clone https://github.com/MoeenAsim/ml-model-deploy.git

Move into the project:

cd ml-model-deploy
2. Create Virtual Environment

Windows PowerShell:

python -m venv .venv

Activate:

.venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt
4. Train the Model
python train_model.py

Expected result:

Model trained successfully.
Model saved to: model/house_price_model.pkl
Model exists: True
5. Run the API
uvicorn app.main:app --reload

API:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs
6. Run Tests
pytest
## Example End-to-End Usage

Suppose a user wants an estimated price for a house with:

Area       = 1200
Bedrooms   = 3
Bathrooms  = 2

The request is:

{
  "area": 1200,
  "bedrooms": 3,
  "bathrooms": 2
}

The application processes the request:

User
 │
 ▼
POST /predict
 │
 ▼
FastAPI
 │
 ▼
Input Validation
 │
 ▼
Scikit-learn Model
 │
 ▼
Prediction
 │
 ▼
JSON Response

Example response:

{
  "predicted_price": 11999999.999999996
}

This demonstrates the complete path from user input to machine learning inference.

## Example Testing Workflow

A developer changes the API code.

Before pushing the changes:

pytest

If all tests pass:

4 passed

The developer commits the changes:

git add .
git commit -m "Update prediction API"
git push

GitHub Actions automatically starts the CI pipeline.

Git Push
   │
   ▼
CI
   │
   ├── Install Dependencies
   ├── Run Pytest
   └── Build Docker Image
   │
   ▼
Success
   │
   ▼
CD
   │
   ├── Authenticate with GHCR
   ├── Build Docker Image
   └── Push Image

This removes the need to manually perform the same validation and image publishing steps after every change.

## Development Workflow

The complete development workflow is:

1. Develop
      │
      ▼
2. Train / Update Model
      │
      ▼
3. Update API
      │
      ▼
4. Run Tests
      │
      ▼
5. Build Docker Image
      │
      ▼
6. Commit Changes
      │
      ▼
7. Push to GitHub
      │
      ▼
8. CI Runs Automatically
      │
      ├── Tests
      └── Docker Build
      │
      ▼
9. CD Runs Automatically
      │
      ├── Docker Build
      └── Push to GHCR
      │
      ▼
10. Deployment-Ready Image
## What This Project Demonstrates
Machine Learning
Regression model training
Feature-based prediction
Model serialization
Model loading
Model inference
Backend Development
FastAPI
REST API development
Request validation
API endpoint design
Health check endpoint
Swagger documentation
Testing
Pytest
Automated API tests
Regression testing
CI-based testing
Docker
Dockerfile creation
Docker image building
Docker container execution
Containerized ML model serving
Port mapping
CI/CD
GitHub Actions
Continuous Integration
Continuous Delivery
Automated testing
Automated Docker builds
Automated container publishing
Container Registry
GitHub Container Registry
Docker image tagging
Docker image publishing
Deployment-ready container artifacts
## Current Project Status
Component	Status
ML Model	✅ Complete
House Price Prediction	✅ Complete
FastAPI API	✅ Complete
/predict Endpoint	✅ Complete
/health Endpoint	✅ Complete
Swagger Documentation	✅ Complete
Automated Tests	✅ Complete
Dockerfile	✅ Complete
Local Docker Container	✅ Complete
GitHub Repository	✅ Complete
GitHub Actions CI	✅ Complete
Automated Docker Build	✅ Complete
GitHub Actions CD	✅ Complete
GHCR Publishing	✅ Complete
Public Cloud Deployment	⏳ Future
Production Monitoring	⏳ Future
## Future Improvements

The current project focuses on demonstrating the ML deployment and CI/CD workflow.

Future versions could include:

Machine Learning Improvements
Use a real-world housing dataset
Add train/validation/test splitting
Add data preprocessing
Add feature scaling
Add model evaluation
Add MAE and RMSE metrics
Compare multiple regression algorithms
Add model versioning
Add experiment tracking
API Improvements
Add authentication
Add API rate limiting
Add structured error handling
Add request logging
Add API versioning
Add response validation
DevOps Improvements
Add image versioning using Git commit SHA
Deploy automatically to a cloud server
Add deployment health checks
Add rollback functionality
Add monitoring
Add Infrastructure as Code
Add production reverse proxy
Add HTTPS
Add automated vulnerability scanning
Application Improvements
Add a web frontend
Add interactive house price prediction form
Add prediction history
Add database integration
Add model performance dashboard
##  Why This Project Matters

A machine learning model by itself is not enough to create a complete production application.

This project demonstrates the transition from:

Machine Learning Model
        │
        ▼
Application
        │
        ▼
REST API
        │
        ▼
Automated Testing
        │
        ▼
Docker Container
        │
        ▼
CI/CD Pipeline
        │
        ▼
Container Registry
        │
        ▼
Deployment-Ready Application

This combines three important areas:

Machine Learning
       +
Backend Development
       +
DevOps / CI/CD
- Project Highlights
- House Price Prediction
- Scikit-learn Model
- FastAPI REST API
- Pytest Automated Testing
- Docker Containerization
- GitHub Actions CI
- GitHub Actions CD
- GitHub Container Registry
- Secure GITHUB_TOKEN Authentication
- Swagger API Documentation
- Health Check Endpoint
- Author
Moeen Asim

This project was developed as a practical implementation of machine learning model serving, REST API development, Docker containerization, automated testing, and CI/CD automation.

## Project Summary

House Price ML Pipeline demonstrates how a machine learning model can be transformed into a containerized API and integrated into an automated software delivery workflow.

The project combines:

Python + Scikit-learn + FastAPI + Pytest + Docker + GitHub Actions + GHCR

to create a reproducible and deployment-ready machine learning application.

## License

This project is intended for educational, learning, and portfolio purposes.


**Bas ab isi poore block ko copy → `README.md` → paste → save.**

Phir PowerShell mein:

```powershell
git add README.md
git commit -m "Improve project documentation"
git push