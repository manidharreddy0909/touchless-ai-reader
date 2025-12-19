import cv2
from hand_landmarks import HandLandmarkDetector


cap = cv2.VideoCapture(0)
detector = HandLandmarkDetector()

print("Starting Hand Tracking... Press 'ESC' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)

    result = detector.detect(frame)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            detector.draw(frame, hand)

            index_tip = hand.landmark[8]
            h, w, _ = frame.shape
            cx, cy = int(index_tip.x * w), int(index_tip.y * h)

            cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            cv2.putText(
                frame,
                f"Index: {cx}, {cy}",
                (cx + 10, cy - 10),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (255, 255, 255),
                2
            )

    cv2.putText(
        frame,
        "Hand Landmarks: ACTIVE",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
