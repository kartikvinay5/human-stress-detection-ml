# Human Stress Detection Using Machine Learning

This project is an end-to-end machine learning web application that analyzes typing and mouse interaction behavior to identify stress patterns. The system demonstrates how behavioral data can be modeled and analyzed using machine learning to classify stress-related states.

The application includes an offline-trained machine learning model, a Flask-based backend for inference, and a clean web-based user interface.

---

## Problem Statement

Stress can significantly impact productivity and performance. Behavioral patterns such as typing speed, pause duration, error frequency, and mouse movement characteristics often change under stress. The objective of this project is to analyze these interaction patterns and classify whether a user is in a normal or stressed state using machine learning techniques.

---

## Solution Overview

The project models stress detection as a supervised classification problem. Behavioral features derived from typing and mouse interaction metrics are used as inputs to a trained machine learning model. The backend processes these features and returns a stress prediction through a web interface.

This implementation focuses on behavioral pattern analysis and model deployment rather than real-time data capture.

---

## Features Used

- Typing speed (keys per second)
- Pause duration between keystrokes
- Error rate (backspace frequency)
- Mouse movement speed
- Idle time during interaction
- Mouse movement variance

---

## Machine Learning Approach

- Synthetic behavioral data generation for training
- Feature scaling using standard normalization
- Random Forest classifier for stress prediction
- Model evaluation using accuracy and confusion matrix
- Trained model and scaler serialized using Joblib

The model selection emphasizes interpretability and robustness over complexity.

---

## Tech Stack

- Python
- Scikit-learn
- Flask
- HTML, CSS, Bootstrap
- Joblib

---

## Application Architecture

1. Model training performed offline
2. Trained model and scaler saved as serialized files
3. Flask backend loads the model and handles inference
4. Frontend collects behavioral metrics via a web form
5. Backend returns stress classification result

---


---

## How to Run the Project

1. Install required dependencies:
pip install -r requirements.txt

2. Start the Flask application:
python app.py


3. Open the application in a web browser:


http://127.0.0.1:5000/


4. Enter behavioral metrics and view the stress prediction.

---

## Important Note

This project is intended for educational and analytical purposes only. It does not perform medical or psychological diagnosis. Behavioral data used in this project is simulated, and real-time interaction capture is outside the scope of this implementation.

---

## Future Enhancements

- Automatic real-time keystroke and mouse data capture
- Session-based continuous stress monitoring
- Advanced explainability for model predictions
- Multi-class stress level classification
- Integration with analytics dashboards

