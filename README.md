 

---

Touchless AI Reader

Touchless AI Reader is a multimodal Human–Computer Interaction system that enables touch-free computer control using hand gestures, eye gestures, face movement, and a virtual pen.

The system is designed for smooth, stable, and safe interaction, focusing on accessibility, hygiene, and futuristic user experience.


---

Key Features

Real-time hand gesture based mouse control

Smooth cursor movement using index finger

Pinch gesture for click, drag, and selection

Two-finger scrolling (up & down with motion-based logic)

Pause & resume controls using palm and fist

Face gesture integration (zoom in / zoom out)

Eye gesture interaction (blink, left wink, right wink)

Mode switching: Hand Mode, Face Mode, Pen Mode

Virtual air-pen drawing with pinch

Gesture smoothing & cooldown logic

Safe interaction (anti-flicker, action gating)

HUD overlay showing current mode

Designed for accessibility and hands-free use



---

Development Timeline & Progress

Day 1 – Project Setup

Objective:
Initialize environment and test camera access.

Completed:

Project structure created

Python virtual environment configured

OpenCV camera tested successfully



---

Day 2 – Hand Tracking

Objective:
Detect hand landmarks in real-time.

Completed:

Integrated MediaPipe Hands

Detected 21 hand landmarks

Displayed hand skeleton overlay

Created reusable hand detector module



---

Day 3 – Hand Feature Engineering

Objective:
Convert landmarks into reliable gesture states.

Completed:

Finger up/down detection

Pinch distance calculation

Palm, fist, index-only, two-finger, three-finger logic

Scale & position invariant hand state



---

Day 4 – Mouse Control Using Hand Gestures

Objective:
Control mouse smoothly using gestures.

Completed:

Index finger → Mouse movement

Pinch → Click & drag

Two fingers → Scroll up & down

Added motion-based scroll logic



---

Day 5 – Stability & Safety

Objective:
Prevent accidental triggers.

Completed:

Pause using palm

Resume using fist

Cooldown timers

Gesture gating & smoothing



---

Day 6 – Face Detection

Objective:
Add face tracking support.

Completed:

Integrated MediaPipe Face Mesh

Stable face landmark detection

Modular face tracker created



---

Day 7 – Eye Gesture Recognition

Objective:
Enable eye-based interaction.

Completed:

Blink → Pause / Resume

Left wink → Left click

Right wink → Right click

Cooldown logic added



---

Day 8 – Face-Based Zoom Control

Objective:
Enable zoom without hands.

Completed:

Head forward → Zoom in

Head backward → Zoom out

Motion thresholds & cooldown



---

Day 9 – Mode Switching

Objective:
Avoid gesture conflicts.

Modes Implemented:

HAND Mode

FACE Mode

PEN Mode


Switching Gestures:

Palm → Face mode

Three fingers → Pen mode

Fist → Hand mode



---

Day 10 – Pen Mode

Objective:
Enable air drawing.

Completed:

Pinch → Pen down

Release → Pen up

Persistent drawing overlay

Clean separation from mouse control



---

Day 11 – Final Stability Improvements

Completed:

Anti-flicker logic

Gesture memory

Motion smoothing

Reliable mode isolation



---

Gesture Mapping

Hand Mode

Gesture	Action

Index finger	Move mouse
Pinch	Click / Drag
Index + Middle	Scroll
Palm	Pause / Switch mode
Fist	Resume



---

Face & Eye Mode

Gesture	Action

Blink	Pause / Resume
Left wink	Left click
Right wink	Right click
Head forward	Zoom in
Head backward	Zoom out



---

Pen Mode

Gesture	Action

Pinch	Draw
Release	Stop drawing
Palm	Exit pen mode



---

Installation & Running

Clone Repository

git clone <repo-url>
cd touchless-ai-reader

Create Virtual Environment

python -m venv venv
venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Application

python app.py


---

EXE Build Instructions

pip install pyinstaller
pyinstaller --onefile app.py

The EXE will be available in the dist folder.


---

Troubleshooting

Camera not opening

Close other apps using camera

Restart system

Try changing camera index


Gestures flickering

Improve lighting

Reduce background movement

Adjust cooldown thresholds


Face / Eye gestures not detected

Ensure full face visibility

Avoid strong backlight

Avoid glasses during testing



---

Gesture Demo (Add GIFs)

Add demo GIFs here:

hand_mouse.gif

scroll.gif

blink_click.gif

pen_draw.gif



---

Purpose of This Project

This project demonstrates:

Real-time computer vision

Accessibility-first design

Gesture-based HCI systems

Stability-focused AI engineering

End-to-end application development



---

Resume / LinkedIn Description

Developed a touchless computer interaction system using hand, face, and eye gestures. Implemented smooth mouse control, scrolling, zoom, click, and air-pen drawing with gesture smoothing and safety mechanisms. Focused on accessibility and real-world stability.


---

Author

Manidhar Bheempadu
AI & Computer Vision Developer


---

License

This project is intended for educational, research, and demonstration purposes.


---