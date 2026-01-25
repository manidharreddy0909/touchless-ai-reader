import pyautogui
import time

pyautogui.FAILSAFE = False

# ---------------- GLOBAL STATES ----------------
paused = False
pinch_active = False
last_click_time = 0
CLICK_COOLDOWN = 0.35


# ---------------- MOUSE MOVE (SMOOTH) ----------------
def move_mouse(x, y):
    if paused:
        return

    screen_w, screen_h = pyautogui.size()

    px = int(x * screen_w)
    py = int(y * screen_h)

    pyautogui.moveTo(px, py, duration=0.05)


# ---------------- LEFT CLICK ----------------
def left_click():
    global last_click_time

    if paused:
        return

    now = time.time()
    if now - last_click_time > CLICK_COOLDOWN:
        pyautogui.click()
        last_click_time = now


# ---------------- PINCH → DRAG / SELECT ----------------
def pinch_control(pinch):
    global pinch_active

    if paused:
        return

    if pinch and not pinch_active:
        pyautogui.mouseDown()
        pinch_active = True

    elif not pinch and pinch_active:
        pyautogui.mouseUp()
        pinch_active = False


# ---------------- SCROLL ----------------
def scroll(amount):
    if paused:
        return

    pyautogui.scroll(amount)


# ---------------- PAUSE / RESUME ----------------
def toggle_pause(state):
    global paused, pinch_active

    paused = state

    # Safety: release mouse if paused while dragging
    if paused and pinch_active:
        pyautogui.mouseUp()
        pinch_active = False

def perform_face_action(action):
    if action == "LEFT_CLICK":
        pyautogui.click(button="left")

    elif action == "RIGHT_CLICK":
        pyautogui.click(button="right")

    elif action == "PAUSE_TOGGLE":
        toggle_pause(not paused)

    elif action == "ZOOM_IN":
        pyautogui.hotkey("ctrl", "+")

    elif action == "ZOOM_OUT":
        pyautogui.hotkey("ctrl", "-")