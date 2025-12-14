import platform
from flask import Flask, request
import joblib
import numpy as np
from sklearn.datasets import load_iris
import os
import json

MODEL_VERSION=os.environ.get('MODEL_VERSION', "v1.1.0")
MODEL_PATH=os.environ.get('MODEL_PATH', f"models/iris_model_{MODEL_VERSION}.joblib")

app = Flask(__name__)

def load_model():
    model = None
    if os.path.exists(MODEL_PATH):
        print("Loading model...", end="")
        model = joblib.load(MODEL_PATH)
    else:
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    print("done!")
    return model

model = load_model()
iris_data = load_iris()
feature_names = iris_data["feature_names"]
target_names = iris_data["target_names"]

# Module 1: healthcheck
@app.route('/health')
def system_info():
    return {
        'status': 'ok',
        "version": MODEL_VERSION
    }

# Module 2: prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        try:
            data = json.loads(list(request.form.keys())[0])
            features = data['x']
            features_array = np.array(features, dtype=float).reshape(1, -1)
        except ValueError:
            return {"error": "Check data format, should be : '{\"x\": [1,2,3,4]}'"}, 400
        
        # Prediction
        prediction = model.predict(features_array)[0]
        return {
            "prediction": target_names[prediction],
            "version": MODEL_VERSION
            }
    except Exception as e:
        return {"error": str(e), "version": MODEL_VERSION}, 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
