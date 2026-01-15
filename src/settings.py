import json
import os

SETTINGS_FILE = "settings.json"

default_settings = {
    "hud": True,
    "sounds": True,
    "gesture_stability": 5,
    "mode": "HAND"
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
    return json.load(open(SETTINGS_FILE))

def save_settings(data):
    json.dump(data, open(SETTINGS_FILE, "w"), indent=4)
