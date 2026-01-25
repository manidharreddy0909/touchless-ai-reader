import pyautogui
from src.vision.mouse_actions import toggle_pause, paused

pyautogui.FAILSAFE = False


def perform_face_action(action):
    if action == "LEFT_WINK":
        pyautogui.click(button="left")

    elif action == "RIGHT_WINK":
        pyautogui.click(button="right")

    elif action == "BLINK":
        toggle_pause(not paused)