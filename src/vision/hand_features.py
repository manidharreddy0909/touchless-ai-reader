import math

def dist(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def finger_up(lm, tip, pip):
    return lm[tip].y < lm[pip].y

def extract_hand_state(hand):
    lm = hand.landmark

    index = finger_up(lm, 8, 6)
    middle = finger_up(lm, 12, 10)
    ring = finger_up(lm, 16, 14)
    pinky = finger_up(lm, 20, 18)

    pinch = dist(lm[4], lm[8]) < 0.045

    return {
        "index": index,
        "middle": middle,
        "ring": ring,
        "pinky": pinky,
        "pinch": pinch
    }

def is_index_only(s):
    return s["index"] and not (s["middle"] or s["ring"] or s["pinky"])

def is_two_finger(s):
    return s["index"] and s["middle"] and not s["ring"]

def is_palm(s):
    return s["index"] and s["middle"] and s["ring"] and s["pinky"]

def is_fist(s):
    return not (s["index"] or s["middle"] or s["ring"] or s["pinky"])

def is_three_finger(state):
    return (
        state["index"] and
        state["middle"] and
        state["ring"] and
        not state["pinky"]
    )
def is_four_finger(state):
    return (
        state["index"] and
        state["middle"] and
        state["ring"] and
        state["pinky"]
    )

def is_thumb_index_pinch(state):
    return state["pinch"] and state["thumb"]
