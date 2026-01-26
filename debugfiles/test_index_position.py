import cv2
from src.vision.hand_landmarks import HandLandmarkDetector

cap = cv2.VideoCapture(0)
detector = HandLandmarkDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect(frame)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        index_tip = hand.landmark[8]

        h, w, _ = frame.shape
        x = int(index_tip.x * w)
        y = int(index_tip.y * h)

        cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)
        cv2.putText(frame, f"{x},{y}", (x+10, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    cv2.imshow("INDEX TEST", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
