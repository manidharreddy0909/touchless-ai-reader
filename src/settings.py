import json
import os

SETTINGS_FILE = "settings.json"

default_settings = {
    "hud": True,
    "sounds": True,
    "gesture_stability": 5,
    "mode": "HAND",
    "enable_hand": True,
    "enable_face": True,
    "enable_eye": True
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings

    try:
        with open(SETTINGS_FILE, "r") as f:
            data = json.load(f)
    except Exception:
        save_settings(default_settings)
        return default_settings

    for k, v in default_settings.items():
        data.setdefault(k, v)

    return data

def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)
