import tkinter as tk
from tkinter import ttk
from src.settings import load_settings, save_settings

def open_settings_ui():
    settings = load_settings()

    root = tk.Tk()
    root.title("Touchless AI Reader - Settings")
    root.geometry("420x420")
    root.resizable(False, False)

    def save_and_close():
        settings["enable_hand"] = hand_var.get()
        settings["enable_face"] = face_var.get()
        settings["enable_eye"] = eye_var.get()
        settings["hud"] = hud_var.get()
        settings["gesture_stability"] = stability_var.get()
        settings["mode"] = mode_var.get()
        save_settings(settings)
        root.destroy()

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Control Modules", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=8)

    hand_var = tk.BooleanVar(value=settings["enable_hand"])
    face_var = tk.BooleanVar(value=settings["enable_face"])
    eye_var = tk.BooleanVar(value=settings["enable_eye"])
    hud_var = tk.BooleanVar(value=settings["hud"])

    ttk.Checkbutton(frame, text="Enable Hand Gestures", variable=hand_var).pack(anchor="w")
    ttk.Checkbutton(frame, text="Enable Face Gestures", variable=face_var).pack(anchor="w")
    ttk.Checkbutton(frame, text="Enable Eye Control", variable=eye_var).pack(anchor="w")
    ttk.Checkbutton(frame, text="Show HUD Overlay", variable=hud_var).pack(anchor="w")

    ttk.Separator(frame).pack(fill="x", pady=10)

    ttk.Label(frame, text="Gesture Stability").pack(anchor="w")
    stability_var = tk.IntVar(value=settings["gesture_stability"])
    ttk.Scale(frame, from_=3, to=8, variable=stability_var, orient="horizontal").pack(fill="x")

    ttk.Separator(frame).pack(fill="x", pady=10)

    ttk.Label(frame, text="Default Mode").pack(anchor="w")
    mode_var = tk.StringVar(value=settings["mode"])
    ttk.Combobox(
        frame,
        textvariable=mode_var,
        values=["HAND", "PEN", "EYE"],
        state="readonly"
    ).pack(fill="x")

    ttk.Button(frame, text="Save & Close", command=save_and_close).pack(pady=20)

    root.mainloop()
