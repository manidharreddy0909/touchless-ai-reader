import sys
import os
import cv2
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vision.hand_landmarks import HandLandmarkDetector
from vision.hand_features import extract_hand_features

DATASET_PATH = "data/dataset.csv"

os.makedirs("data", exist_ok=True)

detector = HandLandmarkDetector()
cap = cv2.VideoCapture(0)

current_label = None

print("""
GESTURE LABELS
0 → OPEN_PALM
1 → FIST
2 → INDEX_POINT
3 → TWO_FINGERS
4 → PINCH

Press:
0-4 → set label
s   → save sample
q   → quit
""")

with open(DATASET_PATH, "a", newline="") as file:
    writer = csv.writer(file)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = detector.detect(frame)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            features = extract_hand_features(hand)
            detector.draw(frame, hand)

            cv2.putText(frame, f"Label: {current_label}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        cv2.imshow("Hand Gesture Dataset Collection", frame)

        key = cv2.waitKey(1) & 0xFF

        if key in [ord(str(i)) for i in range(5)]:
            current_label = int(chr(key))
            print(f"Label set → {current_label}")

        elif key == ord('s') and current_label is not None:
            writer.writerow(features + [current_label])
            print("Sample saved")

        elif key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
