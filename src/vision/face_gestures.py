import cv2
import mediapipe as mp
import time
import pyautogui
import math
from src.logger import log

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True, max_num_faces=1)

BLINK_THRESHOLD = 0.24
WINK_THRESHOLD = 0.22

BLINK_GAP = 0.55
CLICK_GAP = 0.25
HEAD_GAP = 1.2

last_blink_time = 0
last_click_time = 0
last_head_time = 0

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

NOSE = 1
CHIN = 152
FOREHEAD = 10


def ear(lm, eye):
    p = [lm[i] for i in eye]
    A = ((p[1].x - p[5].x)**2 + (p[1].y - p[5].y)**2)**0.5
    B = ((p[2].x - p[4].x)**2 + (p[2].y - p[4].y)**2)**0.5
    C = ((p[0].x - p[3].x)**2 + (p[0].y - p[3].y)**2)**0.5
    return (A + B) / (2.0 * C + 1e-6)


def detect_head_pitch(lm):
    nose = lm[NOSE]
    chin = lm[CHIN]
    forehead = lm[FOREHEAD]

    dy = chin.y - forehead.y
    dx = chin.x - forehead.x
    angle = math.degrees(math.atan2(dy, dx))

    return angle


def detect_face_gesture(frame):
    global last_blink_time, last_click_time, last_head_time

    now = time.time()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if not result.multi_face_landmarks:
        return None

    lm = result.multi_face_landmarks[0].landmark

    left = ear(lm, LEFT_EYE)
    right = ear(lm, RIGHT_EYE)

    left_closed = left < WINK_THRESHOLD
    right_closed = right < WINK_THRESHOLD

    # ========= BLINK (BOTH) =========
    if left < BLINK_THRESHOLD and right < BLINK_THRESHOLD:
        if now - last_blink_time > BLINK_GAP:
            last_blink_time = now
            return "BLINK"
        return None

    # ========= LEFT WINK =========
    if left_closed and not right_closed:
        if now - last_click_time > CLICK_GAP:
            last_click_time = now
            pyautogui.click(button="left")
            log("Left Wink Click")
            return "LEFT_WINK"
        return None

    # ========= RIGHT WINK =========
    if right_closed and not left_closed:
        if now - last_click_time > CLICK_GAP:
            last_click_time = now
            pyautogui.click(button="right")
            log("Right Wink Right Click")
            return "RIGHT_WINK"
        return None

    # ========= HEAD UP / DOWN =========
    angle = detect_head_pitch(lm)

    if now - last_head_time > HEAD_GAP:

        if angle > 18:
            last_head_time = now
            return "HEAD_UP"

        if angle < -18:
            last_head_time = now
            return "HEAD_DOWN"

    return None
