import tkinter as tk
from tkinter import ttk
from src.settings import load_settings, save_settings


def open_settings_window(on_close=None):
    settings = load_settings()

    root = tk.Toplevel()
    root.title("Touchless AI Reader Settings")
    root.geometry("340x330")
    root.resizable(False, False)

    root.grab_set()

    hud_var = tk.BooleanVar(value=settings.get("hud", True))
    sound_var = tk.BooleanVar(value=settings.get("sounds", True))
    hand_var = tk.BooleanVar(value=settings.get("enable_hand", True))
    face_var = tk.BooleanVar(value=settings.get("enable_face", True))
    eye_var = tk.BooleanVar(value=settings.get("enable_eye", True))

    stability_var = tk.IntVar(value=settings.get("gesture_stability", 5))

    ttk.Label(root, text="General Settings", font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=15, pady=(10, 5))

    ttk.Checkbutton(root, text="Enable HUD Overlay", variable=hud_var).pack(anchor="w", padx=25, pady=3)
    ttk.Checkbutton(root, text="Enable Sounds", variable=sound_var).pack(anchor="w", padx=25, pady=3)

    ttk.Separator(root).pack(fill="x", padx=10, pady=10)

    ttk.Label(root, text="Control Modules", font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=15)

    ttk.Checkbutton(root, text="Hand Control", variable=hand_var).pack(anchor="w", padx=25, pady=3)
    ttk.Checkbutton(root, text="Face Control", variable=face_var).pack(anchor="w", padx=25, pady=3)
    ttk.Checkbutton(root, text="Eye Control", variable=eye_var).pack(anchor="w", padx=25, pady=3)

    ttk.Separator(root).pack(fill="x", padx=10, pady=10)

    ttk.Label(root, text="Gesture Stability", font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=15)

    stability_label = ttk.Label(root, text=f"Frames Required: {stability_var.get()}")
    stability_label.pack(anchor="w", padx=25)

    def update_label(value):
        stability_label.config(text=f"Frames Required: {int(float(value))}")

    ttk.Scale(
        root,
        from_=3,
        to=10,
        orient="horizontal",
        variable=stability_var,
        command=update_label
    ).pack(fill="x", padx=25, pady=5)

    def save_and_close():
        save_settings({
            "hud": hud_var.get(),
            "sounds": sound_var.get(),
            "gesture_stability": int(stability_var.get()),
            "mode": settings.get("mode", "HAND"),
            "enable_hand": hand_var.get(),
            "enable_face": face_var.get(),
            "enable_eye": eye_var.get()
        })
        root.destroy()
        if on_close:
            on_close()

    ttk.Button(root, text="Save & Launch", command=save_and_close).pack(pady=15)

    root.protocol("WM_DELETE_WINDOW", save_and_close)
