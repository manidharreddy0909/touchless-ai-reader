import pyautogui
import time

# Safety
pyautogui.FAILSAFE = False

# Screen size
SCREEN_W, SCREEN_H = pyautogui.size()

# Timing control
last_action_time = 0
ACTION_DELAY = 0.4

# Drag state
dragging = False


def can_trigger():
    global last_action_time
    now = time.time()
    if now - last_action_time > ACTION_DELAY:
        last_action_time = now
        return True
    return False


def perform_action(gesture, cursor=None):
    """
    Execute mouse actions safely based on gesture
    """

    global dragging

    if not can_trigger():
        return

    # ---------------- MOVEMENT ---------------- #

    if gesture == "OPEN_PALM" or gesture == "INDEX_POINT":
        if cursor:
            x, y = cursor
            pyautogui.moveTo(x, y, duration=0.1)

    # ---------------- CLICK ---------------- #

    elif gesture == "FIST":
        pyautogui.click()

    # ---------------- SCROLL ---------------- #

    elif gesture == "TWO_FINGERS":
        pyautogui.scroll(200)

    # ---------------- DRAG ---------------- #

    elif gesture == "PINCH":
        if not dragging:
            pyautogui.mouseDown()
            dragging = True

    else:
        if dragging:
            pyautogui.mouseUp()
            dragging = False
