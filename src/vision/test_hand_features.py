import cv2
from hand_landmarks import HandLandmarkDetector
from hand_features import extract_hand_features

cap = cv2.VideoCapture(0)
detector = HandLandmarkDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect(frame)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        features = extract_hand_features(hand)

        print([round(f, 3) for f in features])
        detector.draw(frame, hand)

    cv2.imshow("Hand Features", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
