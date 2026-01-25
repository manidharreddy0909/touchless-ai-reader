import cv2
from src.vision.hand_landmarks import HandLandmarkDetector

cap = cv2.VideoCapture(0)
detector = HandLandmarkDetector()

print("SHOW YOUR HAND — ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect(frame)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            detector.draw(frame, hand)

    cv2.imshow("HAND TEST", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
