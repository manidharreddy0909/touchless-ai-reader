import cv2
import numpy as np

drawing = False
canvas = None
prev_point = None


def init_canvas(frame):
    global canvas
    h, w, _ = frame.shape
    canvas = np.zeros((h, w, 3), dtype=np.uint8)


def pen_down():
    global drawing
    drawing = True


def pen_up():
    global drawing, prev_point
    drawing = False
    prev_point = None


def draw_point(x, y, frame):
    global prev_point, canvas

    if canvas is None:
        init_canvas(frame)

    h, w, _ = frame.shape
    px = int(x * w)
    py = int(y * h)

    if drawing:
        if prev_point is not None:
            cv2.line(canvas, prev_point, (px, py), (0, 255, 0), 3)
        prev_point = (px, py)


def overlay(frame):
    if canvas is None:
        return frame
    return cv2.addWeighted(frame, 1.0, canvas, 1.0, 0)