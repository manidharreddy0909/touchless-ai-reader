
import joblib
import numpy as np
import sys
import os
import shutil
import tempfile

def get_model_path():
    if hasattr(sys, '_MEIPASS'):
        src = os.path.join(sys._MEIPASS, 'gesture_model.pkl')
        # Copy to a temp file to avoid permission issues
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.pkl')
        shutil.copyfile(src, tmp.name)
        tmp.close()
        return tmp.name
    return os.path.join(os.path.dirname(__file__), '../../..', 'gesture_model.pkl')

model = joblib.load(get_model_path())

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
