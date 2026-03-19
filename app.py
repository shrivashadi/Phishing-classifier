from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(
    title="Phishing Website Detector",
    description="Detects Phishing Websites using ML",
    version="1.0.0"
)

# Pipeline load karo
with open('models/pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

class WebsiteFeatures(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Phishing Detection API is Running!"}

@app.post("/predict")
def predict(data: WebsiteFeatures):
    features = np.array(data.features).reshape(1, -1)
    prediction = pipeline.predict(features)[0]
    result = "Phishing" if prediction == -1 else "Legitimate"
    return {"prediction": result}