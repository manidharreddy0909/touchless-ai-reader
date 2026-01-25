import cv2
import numpy as np
import time

# ---------------- CONFIG ----------------
DRAW_COLOR = (0, 255, 0)   # Green
DRAW_THICKNESS = 4
CLEAR_HOLD_TIME = 1.5
EXIT_HOLD_TIME = 1.5
# ---------------------------------------

class PenController:
    def __init__(self):
        self.canvas = None
        self.prev_point = None
        self.drawing = False

        self.palm_start = None
        self.fist_start = None

    def reset_canvas(self, frame):
        self.canvas = np.zeros_like(frame)

    def process(self, frame, hand, state):
        if self.canvas is None:
            self.reset_canvas(frame)

        lm = hand.landmark
        h, w, _ = frame.shape

        x = int(lm[8].x * w)
        y = int(lm[8].y * h)
        point = (x, y)

        # -------- DRAW CONTROL --------
        if state["pinch"]:
            self.drawing = True
            if self.prev_point:
                cv2.line(
                    self.canvas,
                    self.prev_point,
                    point,
                    DRAW_COLOR,
                    DRAW_THICKNESS
                )
            self.prev_point = point
        else:
            self.drawing = False
            self.prev_point = None

        # -------- CLEAR CANVAS --------
        if state["palm"]:
            if self.palm_start is None:
                self.palm_start = time.time()
            elif time.time() - self.palm_start > CLEAR_HOLD_TIME:
                self.canvas[:] = 0
                self.palm_start = None
        else:
            self.palm_start = None

        # -------- EXIT PEN MODE --------
        exit_pen = False
        if state["fist"]:
            if self.fist_start is None:
                self.fist_start = time.time()
            elif time.time() - self.fist_start > EXIT_HOLD_TIME:
                exit_pen = True
                self.fist_start = None
        else:
            self.fist_start = None

        # -------- MERGE --------
        frame = cv2.addWeighted(frame, 1.0, self.canvas, 1.0, 0)

        return frame, exit_pen