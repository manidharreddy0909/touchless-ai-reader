import pyautogui
import time

pyautogui.FAILSAFE = False

_last_action_time = 0
ACTION_DELAY = 0.6  # seconds


def can_trigger():
    global _last_action_time
    now = time.time()
    if now - _last_action_time > ACTION_DELAY:
        _last_action_time = now
        return True
    return False


def perform_action(gesture):
    if not can_trigger():
        return

    if gesture == "OPEN_PALM":
        pyautogui.scroll(300)

    elif gesture == "FIST":
        pyautogui.scroll(-300)

    elif gesture == "INDEX_POINT":
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 15, y)

    elif gesture == "TWO_FINGERS":
        pyautogui.click()

    elif gesture == "THREE_FINGERS":
        pyautogui.rightClick()

    elif gesture == "PINCH":
        pyautogui.hotkey("ctrl", "+")

