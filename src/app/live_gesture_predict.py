import sys
import os
import cv2
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vision.hand_landmarks import HandLandmarkDetector
from vision.hand_features import extract_hand_features

MODEL_PATH = "models/gesture_model.pkl"

model = joblib.load(MODEL_PATH)
detector = HandLandmarkDetector()

labels = {
    0: "OPEN_PALM",
    1: "FIST",
    2: "INDEX_POINT",
    3: "TWO_FINGERS",
    4: "PINCH"
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect(frame)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        features = extract_hand_features(hand)

        prediction = model.predict([features])[0]
        label = labels[prediction]

        detector.draw(frame, hand)

        cv2.putText(frame, label,
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 255, 0), 3)

    cv2.imshow("Live Gesture Prediction", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
