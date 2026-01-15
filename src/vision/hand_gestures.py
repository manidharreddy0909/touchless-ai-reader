import joblib
import numpy as np

model = joblib.load("gesture_model.pkl")

LABELS = {
    0: "GESTURE_0",
    1: "GESTURE_1",
    2: "GESTURE_2",
    3: "GESTURE_3",
    4: "GESTURE_4"
}

def classify_gesture(features):
    x = np.array(features).reshape(1, -1)
    pred = model.predict(x)[0]
    return LABELS[pred]
