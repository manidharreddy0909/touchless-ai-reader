import cv2
import time
import pyautogui
from collections import deque

from src.settings import load_settings
from src.logger import log

from src.vision.hand_tracker import detect_hand
from src.vision.hand_features import extract_hand_features
from src.vision.hand_gestures import classify_gesture
from src.vision.face_gestures import detect_face_gesture
from src.vision.eye_mouse import eye_controlled_mouse
from src.vision.pen_mouse import pen_mouse_control


settings = load_settings()

MODE = settings["mode"]
ACTION_DELAY = 0.35

paused = False
drag_state = False
last_action_time = 0
last_page_time = 0

gesture_history = deque(maxlen=8)
MIN_STABLE_FRAMES = settings["gesture_stability"]

mode_hold_start = 0
mode_hold_gesture = None
MODE_HOLD_TIME = 2.0


def do_action(action):
    global drag_state, last_action_time
    now = time.time()
    if now - last_action_time < ACTION_DELAY:
        return
    last_action_time = now

    if action == "SCROLL_UP":
        pyautogui.scroll(300)

    elif action == "SCROLL_DOWN":
        pyautogui.scroll(-300)

    elif action == "ZOOM_IN":
        pyautogui.keyDown("ctrl")
        pyautogui.scroll(300)
        pyautogui.keyUp("ctrl")

    elif action == "ZOOM_OUT":
        pyautogui.keyDown("ctrl")
        pyautogui.scroll(-300)
        pyautogui.keyUp("ctrl")

    elif action == "DRAG":
        if not drag_state:
            pyautogui.mouseDown()
            drag_state = True
        else:
            pyautogui.mouseUp()
            drag_state = False


def draw_hud(frame, gesture, paused):
    if not settings["hud"]:
        return
    overlay = frame.copy()
    cv2.rectangle(overlay,(10,10),(430,220),(20,20,20),-1)
    frame[:] = cv2.addWeighted(overlay,0.6,frame,0.4,0)
    cv2.putText(frame,f"Mode: {MODE}",(25,60),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    cv2.putText(frame,f"Gesture: {gesture}",(25,110),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
    cv2.putText(frame,"Paused" if paused else "Active",(25,160),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255) if paused else (0,255,0),2)


def set_mode(new_mode):
    global MODE
    if MODE != new_mode:
        MODE = new_mode
        print("Mode:", MODE)


def handle_hand_actions(gesture):
    if gesture == "GESTURE_0":
        do_action("SCROLL_UP")
    elif gesture == "GESTURE_1":
        do_action("SCROLL_DOWN")
    elif gesture == "GESTURE_2":
        do_action("DRAG")
    elif gesture == "GESTURE_3":
        do_action("ZOOM_IN")
    elif gesture == "GESTURE_4":
        do_action("ZOOM_OUT")


def run_controller():
    global paused, last_page_time, mode_hold_start, mode_hold_gesture

    cap = cv2.VideoCapture(0)

    head_up = {"start": None, "cooldown": 0}
    head_down = {"start": None, "cooldown": 0}
    blink_cool = 0
    wink_left_cool = 0
    wink_right_cool = 0

    HOLD_TIME = 1.3
    COOLDOWN = 4.5
    PAGE_COOL = 1.1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        now = time.time()

        face = detect_face_gesture(frame)

        # === PAUSE TOGGLE — BOTH EYES ===
        if face == "BLINK" and now > blink_cool:
            paused = not paused
            blink_cool = now + 1.2

        # === LEFT CLICK — LEFT EYE ONLY ===
        elif face == "LEFT_WINK" and now > wink_left_cool:
            if not paused:
                pyautogui.click(button="left")
            wink_left_cool = now + 0.9

        # === RIGHT CLICK — RIGHT EYE ONLY ===
        elif face == "RIGHT_WINK" and now > wink_right_cool:
            if not paused:
                pyautogui.click(button="right")
            wink_right_cool = now + 0.9

        # === PAGE TURN LEFT ===
        elif face == "HEAD_LEFT" and now - last_page_time > PAGE_COOL:
            pyautogui.hotkey("ctrl","left")
            last_page_time = now

        # === PAGE TURN RIGHT ===
        elif face == "HEAD_RIGHT" and now - last_page_time > PAGE_COOL:
            pyautogui.hotkey("ctrl","right")
            last_page_time = now


        # === OPEN KEYBOARD (HOLD HEAD UP) ===
        if face == "HEAD_UP":
            if head_up["start"] is None:
                head_up["start"] = now
            elif now - head_up["start"] > HOLD_TIME and now > head_up["cooldown"]:
                pyautogui.hotkey("win","ctrl","o")
                head_up["cooldown"] = now + COOLDOWN
                head_up["start"] = None
        else:
            head_up["start"] = None


        # === CLOSE WINDOW (HOLD HEAD DOWN — SAFER) ===
        if face == "HEAD_DOWN":
            if head_down["start"] is None:
                head_down["start"] = now
            elif now - head_down["start"] > HOLD_TIME and now > head_down["cooldown"]:
                pyautogui.hotkey("alt","f4")
                head_down["cooldown"] = now + COOLDOWN
                head_down["start"] = None
        else:
            head_down["start"] = None


        # === HAND CONTROL ===
        hand = detect_hand(frame)
        current_gesture = None

        if hand and not paused:
            features = extract_hand_features(hand)
            g = classify_gesture(features)

            gesture_history.append(g)

            if gesture_history.count(g) >= MIN_STABLE_FRAMES:
                current_gesture = g
                handle_hand_actions(g)

                if g in ["GESTURE_0","GESTURE_1","GESTURE_3"]:
                    if mode_hold_gesture != g:
                        mode_hold_gesture = g
                        mode_hold_start = now
                    elif now - mode_hold_start > MODE_HOLD_TIME:
                        if g == "GESTURE_0": set_mode("HAND")
                        elif g == "GESTURE_1": set_mode("PEN")
                        elif g == "GESTURE_3": set_mode("EYE")
                        mode_hold_gesture = None
                else:
                    mode_hold_gesture = None

                if MODE == "PEN":
                    pen_mouse_control(hand, frame)

        if MODE == "EYE" and not paused:
            eye_controlled_mouse(frame)

        draw_hud(frame, current_gesture, paused)

        cv2.imshow("Touchless AI Reader", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_controller()
