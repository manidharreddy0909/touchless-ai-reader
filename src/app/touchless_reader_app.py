import sys
import os
import cv2
import joblib
import time

# ---------- PATH FIX ----------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vision.hand_landmarks import HandLandmarkDetector
from vision.hand_features import extract_hand_features
from app.gesture_smoother import GestureSmoother
from app.action_controller import ActionController

# ---------- CONFIG ----------
MODEL_PATH = "models/gesture_model.pkl"
WINDOW_NAME = "Touchless AI Reader"

# ---------- LOAD MODEL ----------
model = joblib.load(MODEL_PATH)

# ---------- INIT MODULES ----------
detector = HandLandmarkDetector()
smoother = GestureSmoother(window_size=7)
controller = ActionController(cooldown=1.0)

labels = {
    0: "OPEN_PALM",
    1: "FIST",
    2: "INDEX_POINT",
    3: "TWO_FINGERS",
    4: "PINCH"
}

# ---------- CAMERA FIX (WINDOWS) ----------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
time.sleep(1)  # camera warm-up

last_gesture = None

print("[INFO] Touchless AI Reader Started")
print("[INFO] Focus Chrome/PDF window")
print("[INFO] Press Q or ESC to exit")

# ---------- MAIN LOOP ----------
while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Camera not detected")
        break

    # mirror for natural interaction
    frame = cv2.flip(frame, 1)

    result = detector.detect(frame)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]

        # feature extraction
        features = extract_hand_features(hand)

        # prediction
        prediction = model.predict([features])[0]
        confidence = max(model.predict_proba([features])[0])

        smoothed = smoother.smooth(prediction)

        if smoothed is not None and confidence > 0.70:
            gesture = labels[smoothed]

            # debug print
            print(f"Gesture: {gesture}, Confidence: {confidence:.2f}")

            # execute only on change
            if gesture != last_gesture:
                controller.execute(gesture)
                last_gesture = gesture

            # overlay
            cv2.putText(
                frame,
                f"{gesture} ({confidence:.2f})",
                (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.1,
                (0, 255, 0),
                3
            )

        detector.draw(frame, hand)

    cv2.imshow(WINDOW_NAME, frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

# ---------- CLEANUP ----------
cap.release()
cv2.destroyAllWindows()
print("[INFO] Touchless AI Reader Stopped")
