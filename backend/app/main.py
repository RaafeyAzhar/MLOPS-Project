from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

# Load your trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    try:
        X = np.array([
            data["humidity"],
            data["wind_speed"],
            data["condition_encoded"]
        ])
        # Prediction: intercept + coefficients · features
        prediction = model["intercept"] + np.dot(model["coefficients"], X)
        return jsonify({"predicted_temperature": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Recommended: use port 5000 for backend
    app.run(host="127.0.0.1", port=5000, debug=True)
