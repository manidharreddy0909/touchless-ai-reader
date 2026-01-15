import cv2
from src.vision.face_gestures import detect_face_gesture

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gesture = detect_face_gesture(frame)
    print(gesture)

    cv2.imshow("FACE TEST", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
