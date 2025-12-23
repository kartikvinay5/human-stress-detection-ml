from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("stress_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["typing_speed"]),
        float(request.form["pause_duration"]),
        float(request.form["error_rate"]),
        float(request.form["mouse_speed"]),
        float(request.form["idle_time"]),
        float(request.form["movement_variance"])
    ]

    data = np.array([features])
    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)[0]

    result = "STRESSED" if prediction == 1 else "NORMAL"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
