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

# ================= FACE / EYE =================
from src.vision.face_tracker import FaceTracker
from src.vision.eye_gestures import (
    detect_eye_gesture,
    detect_eye_cursor
)
from src.vision.face_gestures import detect_face_zoom

# ================= PEN =================
from src.vision.pen_mouse import (
    pen_down,
    pen_up,
    draw_point,
    overlay
)

# ================= GLOBAL =================
MODE = "HAND"
last_switch = 0
COOLDOWN = 1.2

prev_scroll_y = None
last_scroll_time = 0
SCROLL_COOLDOWN = 0.12


def perform_face_action(action):
    """Executes eye / face actions"""
    if action == "LEFT_WINK":
        pyautogui.click(button="left")

    elif action == "RIGHT_WINK":
        pyautogui.click(button="right")

    elif action == "BLINK_TOGGLE":
        toggle_pause(not paused)

    elif action == "ZOOM_IN":
        pyautogui.hotkey("ctrl", "+")

    elif action == "ZOOM_OUT":
        pyautogui.hotkey("ctrl", "-")


def run_controller():
    global MODE, last_switch
    global prev_scroll_y, last_scroll_time

    cap = cv2.VideoCapture(0)

    hand_detector = HandLandmarkDetector()
    face_tracker = FaceTracker()

    screen_w, screen_h = pyautogui.size()

    print("🟢 Touchless AI Controller Started")
    print("HAND | FACE | PEN MODES ACTIVE")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # ======================================================
        # ======================= HAND MODE ===================
        # ======================================================
        if MODE == "HAND":
            result = hand_detector.detect(frame)

            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                hand_detector.draw(frame, hand)

                state = extract_hand_state(hand)
                lm = hand.landmark

                # -------- MODE SWITCH --------
                if is_palm(state) and time.time() - last_switch > COOLDOWN:
                    MODE = "FACE"
                    last_switch = time.time()
                    prev_scroll_y = None

                elif is_three_finger(state) and time.time() - last_switch > COOLDOWN:
                    MODE = "PEN"
                    last_switch = time.time()
                    prev_scroll_y = None

                # -------- ACTIVE CONTROL --------
                if not paused:
                    # Mouse Move (Index only)
                    if state["index"] and not state["middle"]:
                        move_mouse(lm[8].x, lm[8].y)

                    # Pinch → Drag / Select
                    pinch_control(state["pinch"])

                    # Scroll (Two finger, delta-based)
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

        # ======================================================
        # ======================= FACE MODE ===================
        # ======================================================
        elif MODE == "FACE":
            face_result = face_tracker.detect(frame)

            if face_result.multi_face_landmarks:
                face = face_result.multi_face_landmarks[0]

                # 👁 Eye cursor movement
                ex, ey = detect_eye_cursor(face, frame.shape)
                pyautogui.moveTo(
                    int(ex * screen_w),
                    int(ey * screen_h),
                    duration=0.05
                )

                # Eye gestures
                eye_action = detect_eye_gesture(face, frame)
                if eye_action:
                    perform_face_action(eye_action)

                # Head zoom
                zoom_action = detect_face_zoom(face)
                if zoom_action:
                    perform_face_action(zoom_action)

            # -------- Return to HAND --------
            hand_result = hand_detector.detect(frame)
            if hand_result.multi_hand_landmarks:
                state = extract_hand_state(hand_result.multi_hand_landmarks[0])
                if is_fist(state) and time.time() - last_switch > COOLDOWN:
                    MODE = "HAND"
                    last_switch = time.time()

        # ======================================================
        # ======================= PEN MODE ====================
        # ======================================================
        elif MODE == "PEN":
            result = hand_detector.detect(frame)

            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]
                hand_detector.draw(frame, hand)

                state = extract_hand_state(hand)
                lm = hand.landmark

                # Exit pen mode
                if is_palm(state) and time.time() - last_switch > COOLDOWN:
                    MODE = "HAND"
                    last_switch = time.time()

                # Drawing logic
                if state["pinch"]:
                    pen_down()
                else:
                    pen_up()

                draw_point(lm[8].x, lm[8].y, frame)

            frame = overlay(frame)

        # ================= UI =================
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