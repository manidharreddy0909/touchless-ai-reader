import tkinter as tk
from src.settings import load_settings, save_settings

def launch_settings():
    s = load_settings()
    root = tk.Tk()
    root.title("Touchless AI Reader Settings")
    root.geometry("350x320")

    hud_var = tk.BooleanVar(value=s["hud"])
    sound_var = tk.BooleanVar(value=s["sounds"])
    stab_var = tk.IntVar(value=s["gesture_stability"])
    mode_var = tk.StringVar(value=s["mode"])

    def save_and_close():
        s["hud"] = hud_var.get()
        s["sounds"] = sound_var.get()
        s["gesture_stability"] = stab_var.get()
        s["mode"] = mode_var.get()
        save_settings(s)
        root.destroy()

    tk.Checkbutton(root, text="HUD Overlay", variable=hud_var).pack(pady=5)
    tk.Checkbutton(root, text="Sound Effects", variable=sound_var).pack(pady=5)

    tk.Label(root, text="Gesture Stability (1–8)").pack()
    tk.Scale(root, from_=1, to=8, orient="horizontal", variable=stab_var).pack()

    tk.Label(root, text="Default Mode").pack()
    tk.OptionMenu(root, mode_var, "HAND", "EYE", "PEN").pack()

    tk.Button(root, text="Save", command=save_and_close).pack(pady=20)

    root.mainloop()
