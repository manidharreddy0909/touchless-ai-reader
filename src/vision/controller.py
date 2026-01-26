import cv2
import time
import pyautogui

# ================= HAND =================
from src.vision.hand_landmarks import HandLandmarkDetector
from src.vision.hand_features import (
    extract_hand_state,
    is_palm,
    is_fist,
    is_three_finger
)
from src.vision.mouse_actions import (
    move_mouse,
    pinch_control,
    scroll,
    toggle_pause,
    paused
)

# ================= FACE =================
from src.vision.face_tracker import FaceTracker
from src.vision.eye_gestures import detect_eye_gesture
from src.vision.face_gestures import detect_face_zoom

# ================= PEN ==================
from src.vision.pen_mouse import (
    pen_down,
    pen_up,
    draw_point,
    overlay,
    next_color,
    fist_hold_clear
)

# ================= GLOBAL =================
MODE = "HAND"
last_switch = 0
MODE_COOLDOWN = 1.2

gesture_hold_start = None
HOLD_TIME = 0.6

prev_scroll_y = None
last_scroll_time = 0
SCROLL_COOLDOWN = 0.12

# ================= FACE CURSOR STATE =================
face_origin = None
smooth_x, smooth_y = pyautogui.position()
SMOOTHING = 0.18
DEAD_ZONE = 0.015


# ================= FACE CURSOR MOVE =================
def face_move_cursor(face):
    global face_origin, smooth_x, smooth_y

    nose = face.landmark[1]

    if face_origin is None:
        face_origin = (nose.x, nose.y)
        smooth_x, smooth_y = pyautogui.position()
        return

    # X normal, Y inverted (MediaPipe fix)
    dx = nose.x - face_origin[0]
    dy = face_origin[1] - nose.y

    if abs(dx) < DEAD_ZONE:
        dx = 0
    if abs(dy) < DEAD_ZONE:
        dy = 0

    screen_w, screen_h = pyautogui.size()

    target_x = smooth_x + dx * screen_w * 2.0
    target_y = smooth_y + dy * screen_h * 2.0

    smooth_x += (target_x - smooth_x) * SMOOTHING
    smooth_y += (target_y - smooth_y) * SMOOTHING

    pyautogui.moveTo(int(smooth_x), int(smooth_y), duration=0)


# ================= MAIN CONTROLLER =================
def run_controller():
    global MODE, last_switch, gesture_hold_start
    global prev_scroll_y, last_scroll_time, face_origin

    cap = cv2.VideoCapture(0)
    hand_detector = HandLandmarkDetector()
    face_tracker = FaceTracker()

    print("🟢 Touchless AI Controller Started")
    print("MODES: HAND | FACE | PEN")
    print("ESC → Exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # ================= HAND MODE =================
        if MODE == "HAND":
            result = hand_detector.detect(frame)

            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                hand_detector.draw(frame, hand)

                state = extract_hand_state(hand)
                lm = hand.landmark

                # ---- SWITCH TO FACE ----
                if is_palm(state):
                    if gesture_hold_start is None:
                        gesture_hold_start = time.time()
                    elif time.time() - gesture_hold_start > HOLD_TIME and time.time() - last_switch > MODE_COOLDOWN:
                        MODE = "FACE"
                        face_origin = None
                        last_switch = time.time()
                        gesture_hold_start = None
                        continue
                # ---- SWITCH TO PEN ----
                elif is_three_finger(state):
                    if gesture_hold_start is None:
                        gesture_hold_start = time.time()
                    elif time.time() - gesture_hold_start > HOLD_TIME and time.time() - last_switch > MODE_COOLDOWN:
                        MODE = "PEN"
                        last_switch = time.time()
                        gesture_hold_start = None
                        continue
                else:
                    gesture_hold_start = None

                if paused:
                    continue

                # Mouse move
                if state["index"] and not state["middle"]:
                    move_mouse(lm[8].x, lm[8].y)

                # Drag
                pinch_control(state["pinch"])

                # Scroll
                if state["index"] and state["middle"]:
                    current_y = lm[8].y
                    if prev_scroll_y is not None:
                        dy = current_y - prev_scroll_y
                        now = time.time()
                        if abs(dy) > 0.01 and now - last_scroll_time > SCROLL_COOLDOWN:
                            scroll(-60 if dy > 0 else 60)
                            last_scroll_time = now
                    prev_scroll_y = current_y
                else:
                    prev_scroll_y = None

        # ================= FACE MODE =================
        elif MODE == "FACE":
            face_result = face_tracker.detect(frame)

            if face_result.multi_face_landmarks:
                face = face_result.multi_face_landmarks[0]

                face_move_cursor(face)

                eye = detect_eye_gesture(face, frame)
                if eye:
                    if eye == "LEFT_WINK":
                        pyautogui.click(button="left")
                    elif eye == "RIGHT_WINK":
                        pyautogui.click(button="right")
                    elif eye == "BLINK_TOGGLE":
                        toggle_pause(not paused)

                zoom = detect_face_zoom(face)
                if zoom == "ZOOM_IN":
                    pyautogui.hotkey("ctrl", "+")
                elif zoom == "ZOOM_OUT":
                    pyautogui.hotkey("ctrl", "-")

            # ---- RETURN TO HAND ----
            hand_result = hand_detector.detect(frame)
            if hand_result.multi_hand_landmarks:
                state = extract_hand_state(hand_result.multi_hand_landmarks[0])

                if is_fist(state):
                    if gesture_hold_start is None:
                        gesture_hold_start = time.time()
                    elif time.time() - gesture_hold_start > HOLD_TIME and time.time() - last_switch > MODE_COOLDOWN:
                        MODE = "HAND"
                        face_origin = None
                        last_switch = time.time()
                        gesture_hold_start = None
                else:
                    gesture_hold_start = None

        # ================= PEN MODE =================
        elif MODE == "PEN":
            result = hand_detector.detect(frame)

            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                hand_detector.draw(frame, hand)

                state = extract_hand_state(hand)
                lm = hand.landmark

                if is_palm(state):
                    if gesture_hold_start is None:
                        gesture_hold_start = time.time()
                    elif time.time() - gesture_hold_start > HOLD_TIME and time.time() - last_switch > MODE_COOLDOWN:
                        MODE = "HAND"
                        pen_up()
                        last_switch = time.time()
                        gesture_hold_start = None
                        continue
                else:
                    gesture_hold_start = None

                if state["pinch"]:
                    pen_down()
                else:
                    pen_up()

                draw_point(lm[8].x, lm[8].y, frame)

                if state["index"] and state["middle"]:
                    next_color()

                fist_hold_clear(is_fist(state))

            frame = overlay(frame)

        # ================= HUD =================
        cv2.putText(
            frame,
            f"MODE: {MODE}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Touchless AI Reader", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()