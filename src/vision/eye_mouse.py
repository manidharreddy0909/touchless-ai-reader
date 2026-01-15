import cv2
import mediapipe as mp
import pyautogui
import numpy as np

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh(refine_landmarks=True)

LEFT_IRIS = [468]
RIGHT_IRIS = [473]

SCREEN_W, SCREEN_H = pyautogui.size()

last_x, last_y = SCREEN_W//2, SCREEN_H//2
SMOOTHING = 0.2

def eye_controlled_mouse(frame):
    global last_x, last_y

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face.process(rgb)
    if not results.multi_face_landmarks:
        return

    h, w, _ = frame.shape
    pts = results.multi_face_landmarks[0].landmark

    lx = int(pts[LEFT_IRIS[0]].x * w)
    ly = int(pts[LEFT_IRIS[0]].y * h)

    x = np.interp(lx, [0, w], [0, SCREEN_W])
    y = np.interp(ly, [0, h], [0, SCREEN_H])

    last_x = last_x + (x - last_x) * SMOOTHING
    last_y = last_y + (y - last_y) * SMOOTHING

    pyautogui.moveTo(last_x, last_y)
