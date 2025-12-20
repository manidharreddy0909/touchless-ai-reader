import pyautogui
import time

pyautogui.FAILSAFE = True

class ActionController:
    def __init__(self, cooldown=1.0):
        self.last_action_time = 0
        self.cooldown = cooldown

    def execute(self, gesture):
        now = time.time()
        if now - self.last_action_time < self.cooldown:
            return

        if gesture == "OPEN_PALM":
            pyautogui.press("right")

        elif gesture == "FIST":
            pyautogui.press("left")

        elif gesture == "INDEX_POINT":
            pyautogui.scroll(-300)

        elif gesture == "TWO_FINGERS":
            pyautogui.hotkey("ctrl", "+")

        elif gesture == "PINCH":
            pyautogui.click()

        self.last_action_time = now
