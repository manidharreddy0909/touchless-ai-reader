import cv2
import time

# ================= CANVAS =================
canvas = None
pen_active = False
last_clear_time = 0

# ================= DRAW SETTINGS =================
colors = [
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
    (0, 255, 255),
    (255, 255, 255)
]

color_index = 0
pen_color = colors[color_index]
pen_thickness = 5
eraser = False

# ================= POSITION =================
prev_x, prev_y = None, None


# ================= DRAW =================
def pen_down():
    global pen_active
    pen_active = True


def pen_up():
    global pen_active, prev_x, prev_y
    pen_active = False
    prev_x, prev_y = None, None


def draw_point(x, y, frame):
    global canvas, prev_x, prev_y

    h, w, _ = frame.shape
    cx, cy = int(x * w), int(y * h)

    if canvas is None:
        canvas = frame.copy() * 0

    if not pen_active:
        prev_x, prev_y = cx, cy
        return

    if prev_x is None:
        prev_x, prev_y = cx, cy
        return

    color = (0, 0, 0) if eraser else pen_color

    cv2.line(
        canvas,
        (prev_x, prev_y),
        (cx, cy),
        color,
        pen_thickness
    )

    prev_x, prev_y = cx, cy


# ================= CANVAS OVERLAY =================
def overlay(frame):
    if canvas is None:
        return frame
    return cv2.addWeighted(frame, 1, canvas, 1, 0)


# ================= COLOR =================
def next_color():
    global color_index, pen_color
    color_index = (color_index + 1) % len(colors)
    pen_color = colors[color_index]


# ================= THICKNESS =================
def increase_thickness():
    global pen_thickness
    pen_thickness = min(pen_thickness + 2, 20)


# ================= ERASER =================
def enable_eraser(state):
    global eraser
    eraser = state


# ================= CLEAR =================
def fist_hold_clear(fist_state):
    global canvas, last_clear_time

    if fist_state:
        now = time.time()
        if now - last_clear_time > 1.5:
            canvas = None
            last_clear_time = now