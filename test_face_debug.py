import cv2
from src.vision.face_gestures import detect_face_gesture

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gesture = detect_face_gesture(frame)

    print("FACE:", gesture)

    cv2.putText(frame, str(gesture), (40,80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)

    cv2.imshow("FACE DEBUG", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
