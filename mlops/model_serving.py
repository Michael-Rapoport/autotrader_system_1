# mlops/model_serving.py
import joblib

def load_model(model_path):
    model = joblib.load(model_path)
    return model

def predict(model, data):
    predictions = model.predict(data)
    return predictions
