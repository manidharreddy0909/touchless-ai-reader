import sys
import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_DIR)

from vision.face_gestures import detect_blink

cap = cv2.VideoCapture(0)
print("Camera started")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detect_blink(frame)
    cv2.imshow("Blink Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
