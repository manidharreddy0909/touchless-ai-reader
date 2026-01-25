import pyautogui
import numpy as np

pyautogui.FAILSAFE = False

prev_x = None
prev_y = None
SMOOTHING = 0.25

LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]


def iris_center(face, idxs, w, h):
    xs = [face.landmark[i].x * w for i in idxs]
    ys = [face.landmark[i].y * h for i in idxs]
    return np.mean(xs), np.mean(ys)


def move_mouse_by_eye(face, frame):
    global prev_x, prev_y

    h, w, _ = frame.shape
    sx, sy = pyautogui.size()

    lx, ly = iris_center(face, LEFT_IRIS, w, h)
    rx, ry = iris_center(face, RIGHT_IRIS, w, h)

    cx = (lx + rx) / 2
    cy = (ly + ry) / 2

    mx = np.interp(cx, [w * 0.3, w * 0.7], [0, sx])
    my = np.interp(cy, [h * 0.3, h * 0.7], [0, sy])

    if prev_x is None:
        prev_x, prev_y = mx, my

    mx = prev_x + (mx - prev_x) * SMOOTHING
    my = prev_y + (my - prev_y) * SMOOTHING

    pyautogui.moveTo(mx, my)

    prev_x, prev_y = mx, my