import pyautogui
import numpy as np

SCREEN_W, SCREEN_H = pyautogui.size()

last_x, last_y = SCREEN_W//2, SCREEN_H//2
SMOOTHING = 0.15

def pen_mouse_control(landmarks, frame):
    global last_x, last_y

    h, w, _ = frame.shape

    index = landmarks.landmark[8]

    x = np.interp(index.x * w, [0, w], [0, SCREEN_W])
    y = np.interp(index.y * h, [0, h], [0, SCREEN_H])

    last_x = last_x + (x - last_x) * SMOOTHING
    last_y = last_y + (y - last_y) * SMOOTHING

    pyautogui.moveTo(last_x, last_y)
