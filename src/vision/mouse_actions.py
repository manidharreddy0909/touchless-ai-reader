import pyautogui

pyautogui.FAILSAFE = False

paused = False
pinch_active = False


# ================= MOUSE MOVE =================
def move_mouse(x, y):
    screen_w, screen_h = pyautogui.size()
    px = int(x * screen_w)
    py = int(y * screen_h)
    pyautogui.moveTo(px, py, duration=0.04)


# ================= CLICK =================
def left_click():
    pyautogui.click()


def right_click():
    pyautogui.click(button="right")


# ================= DRAG =================
def pinch_control(pinch):
    global pinch_active

    if pinch and not pinch_active:
        pyautogui.mouseDown()
        pinch_active = True

    elif not pinch and pinch_active:
        pyautogui.mouseUp()
        pinch_active = False


# ================= SCROLL =================
def scroll(amount):
    pyautogui.scroll(amount)


# ================= PAUSE =================
def toggle_pause(state):
    global paused
    paused = state