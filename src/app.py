from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo
model = joblib.load("model.joblib")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API de predicción Breast Cancer activa 🚀"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "features" not in data:
        return jsonify({"error": "El JSON debe contener la clave 'features'"}), 400

    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]

    result = "Maligno" if prediction == 0 else "Benigno"
    return jsonify({"prediction": int(prediction), "resultado": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
