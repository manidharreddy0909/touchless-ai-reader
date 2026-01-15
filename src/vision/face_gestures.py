import cv2
import mediapipe as mp
import time
import math
import mediapipe as mp
mp.solutions.hands

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True, max_num_faces=1)

BLINK_THRESHOLD = 0.24
WINK_THRESHOLD = 0.22

BLINK_GAP = 0.6
WINK_GAP = 0.4
HEAD_GAP = 0.9

last_blink = 0
last_wink = 0
last_head = 0

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

NOSE = 1
LEFT_FACE = 234
RIGHT_FACE = 454
CHIN = 152
FOREHEAD = 10


def ear(lm, eye):
    p = [lm[i] for i in eye]
    A = ((p[1].x - p[5].x)**2 + (p[1].y - p[5].y)**2)**0.5
    B = ((p[2].x - p[4].x)**2 + (p[2].y - p[4].y)**2)**0.5
    C = ((p[0].x - p[3].x)**2 + (p[0].y - p[3].y)**2)**0.5
    return (A + B) / (2.0 * C + 1e-6)


def detect_face_gesture(frame):
    global last_blink, last_wink, last_head

    now = time.time()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if not result.multi_face_landmarks:
        return None

    lm = result.multi_face_landmarks[0].landmark

    left_ear = ear(lm, LEFT_EYE)
    right_ear = ear(lm, RIGHT_EYE)

    left_closed = left_ear < WINK_THRESHOLD
    right_closed = right_ear < WINK_THRESHOLD

    if left_ear < BLINK_THRESHOLD and right_ear < BLINK_THRESHOLD:
        if now - last_blink > BLINK_GAP:
            last_blink = now
            return "BLINK"
        return None

    if left_closed and not right_closed:
        if now - last_wink > WINK_GAP:
            last_wink = now
            return "LEFT_WINK"
        return None

    if right_closed and not left_closed:
        if now - last_wink > WINK_GAP:
            last_wink = now
            return "RIGHT_WINK"
        return None

    nose = lm[NOSE]
    left_face = lm[LEFT_FACE]
    right_face = lm[RIGHT_FACE]

    yaw = (nose.x - left_face.x) - (right_face.x - nose.x)

    chin = lm[CHIN]
    forehead = lm[FOREHEAD]
    pitch = math.degrees(math.atan2(chin.y - forehead.y, abs(chin.x - forehead.x) + 1e-6))

    if now - last_head > HEAD_GAP:

        if yaw > 0.03:
            last_head = now
            return "HEAD_RIGHT"

        if yaw < -0.03:
            last_head = now
            return "HEAD_LEFT"

        if pitch > 18:
            last_head = now
            return "HEAD_UP"

        if pitch < -18:
            last_head = now
            return "HEAD_DOWN"

    return None
