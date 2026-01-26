import cv2
import mediapipe as mp

from src.vision.hand_tracker import detect_hand
from src.vision.hand_features import extract_hand_features
from src.vision.hand_gestures import classify_gesture

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
print("✅ Camera opened")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hand = detect_hand(frame)

    if hand:
        mp_draw.draw_landmarks(frame, hand,
            mp.solutions.hands.HAND_CONNECTIONS)

        features = extract_hand_features(hand)

        gesture = classify_gesture(features)

        cv2.putText(frame, gesture, (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0, (0,255,0), 2)

    cv2.imshow("Hand Gestures Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
