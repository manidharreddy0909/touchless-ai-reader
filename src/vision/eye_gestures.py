import numpy as np
import time

# Eye landmark indices (MediaPipe FaceMesh)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

last_blink_time = 0
BLINK_COOLDOWN = 1.0


def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C + 1e-6)


def get_eye_points(face_landmarks, idx, w, h):
    return np.array([
        [
            face_landmarks.landmark[i].x * w,
            face_landmarks.landmark[i].y * h
        ]
        for i in idx
    ])


# ================== MAIN EYE GESTURE ==================
def detect_eye_gesture(face_landmarks, frame):
    global last_blink_time

    h, w, _ = frame.shape

    left_eye = get_eye_points(face_landmarks, LEFT_EYE, w, h)
    right_eye = get_eye_points(face_landmarks, RIGHT_EYE, w, h)

    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)

    BLINK = 0.18
    WINK = 0.14

    now = time.time()

    # 👁 Both-eye blink → pause toggle
    if left_ear < BLINK and right_ear < BLINK:
        if now - last_blink_time > BLINK_COOLDOWN:
            last_blink_time = now
            return "BLINK_TOGGLE"

    # 👁 Left wink → left click
    if left_ear < WINK and right_ear > BLINK:
        return "LEFT_WINK"

    # 👁 Right wink → right click
    if right_ear < WINK and left_ear > BLINK:
        return "RIGHT_WINK"

    return None


# ================== EYE CURSOR ==================
def detect_eye_cursor(face_landmarks, frame_shape):
    """
    Returns normalized (x, y) for mouse movement
    """
    h, w, _ = frame_shape

    # Use nose tip as stable reference
    nose = face_landmarks.landmark[1]

    x = nose.x
    y = nose.y

    return x, y