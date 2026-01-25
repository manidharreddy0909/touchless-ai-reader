import cv2
from src.vision.face_tracker import FaceTracker
from src.vision.eye_gestures import detect_eye_gesture

cap = cv2.VideoCapture(0)
tracker = FaceTracker()

print("👁 Eye Gesture Debug Started")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = tracker.detect(frame)

    if result.multi_face_landmarks:
        face = result.multi_face_landmarks[0]
        gesture = detect_eye_gesture(face, frame)

        if gesture:
            print("DETECTED:", gesture)

    cv2.imshow("Eye Debug", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()