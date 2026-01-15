Touchless AI Reader

Touchless AI Reader is an advanced multimodal Human-Computer Interaction system that enables fully touch-free document and computer interaction using hand gestures, facial expressions, head movement, and intelligent perception.

The system allows users to scroll, zoom, click, navigate pages, open keyboard, drag, and control applications using natural movement — improving accessibility, reducing physical effort, and enabling futuristic interaction.

Key Features

Real-time hand gesture recognition (ML-based)

Eye-blink and head-gesture interaction

Pause and safety controls

Scroll, zoom, drag, click, close-window controls

Eye-gesture mouse clicking

Mode switching (Hand, Eye, Pen)

Stable, smooth interaction with gesture-smoothing

Windows keyboard auto-toggle

Full EXE packaging for one-click use

Structured logging system

HUD overlay to show system state

Accessibility friendly design

Development Timeline & Progress

This project was developed step-by-step with daily milestones.

Day 1 – Project Setup

Objective: Initialize the environment and ensure the system can access the camera.

Completed:

Project structure created

Python venv configured

OpenCV camera module tested

Day 2 – Hand Tracking Module

Objective: Detect and track hand landmarks in real-time using MediaPipe.

Completed:

Integrated MediaPipe Hands

Tracked 21 landmarks

Displayed hand skeleton overlay

Built reusable detection module

Day 3 – Hand Feature Engineering

Objective: Convert raw landmarks into geometric features suitable for ML.

Completed:

Extracted wrist-to-fingertip distances

Computed finger joint angles

Achieved gesture-position & scale-invariance

Built compact feature vectors

Day 4 – Custom Gesture Dataset Creation

Objective: Build a labeled dataset using real hand movement.

Dataset Label Scheme:

Label	Gesture	Purpose
0	Open Palm	Scroll Up
1	Fist	Scroll Down
2	Index Finger	Drag Toggle
3	Two Fingers	Zoom In
4	Pinch	Zoom Out

Captured:

~900 labeled samples

CSV storage format

Consistent feature extraction

Day 5 – Model Training

Objective: Train and evaluate a robust classifier.

Completed:

Trained Random Forest model

Achieved ~90% accuracy

Balanced performance across gestures

Saved trained model

Day 6 – Real-Time Gesture Recognition

Objective: Deploy ML-gesture inference live.

Completed:

Live classification

Real-time display overlay

Smooth processing pipeline

Day 7 – Gesture Smoothing & Touchless Page Control

Objective: Convert predictions into usable system actions.

Completed:

Sliding-window smoothing

Action gating to prevent repeats

PyAutoGUI control mapping

Gesture Mapping:

Gesture	Action
Open Palm	Scroll Up
Fist	Scroll Down
Index Finger	Drag Toggle
Two Fingers	Zoom In
Pinch	Zoom Out

Exit:

ESC closes app safely

Day 8 – Face Gesture Integration

Objective: Add eye & head-gesture modules.

Completed Features:

Blink toggle pause

Left wink → Left click

Right wink → Right click

Head left/right → Page navigation

Head up hold → Open on-screen keyboard

Head down hold → Close window (safe-hold)

Cooldown logic to prevent repeat triggers

Day 9–10 – Stability & Reliability Improvements

Enhancements added:

Cooldown timers

Long-hold confirmation

Gesture-state memory

Anti-flicker logic

Safe-mode handling

Confidence stabilization

HUD overlay display

Result:
Smooth, predictable, stable interaction.

Day 11 – Mode Switching System

Objective: Allow dynamic interaction modes.

Modes:

HAND Mode

PEN Mode

EYE Mode

Switching via gesture-hold trigger.

Day 12 – EXE Build & Distribution

Objective: Create standalone Windows app.

Built using:

pyinstaller --onefile app.py


Outcome:

Runs without Python

Portable

Great for demonstrations

Day 13 – Logging System

Objective: Track system events for research & debugging.

Logged:

Detected gestures

Actions executed

Mode changes

System states

Day 14 – User Settings & Config Controls

User-adjustable:

Gesture stability threshold

HUD toggle

Delays

Mode defaults

Safety limits

Day 15 – HUD Overlay

HUD shows:

Current mode

Current gesture

Active / Paused state

This improves interaction clarity.

Day 16 – System Validation

Tested under:

Bright light

Low light

Different backgrounds

With & without glasses

Different movement speeds

Findings:
System remains stable.

Day 17 – Accessibility-First Design

Purpose:
Enable interaction without physical contact or fine-motor effort.

Benefits:

Suitable for limited-mobility users

Minimal movement needed

Natural interaction patterns

Hands-free operation possible

Day 18 – Final Integration & Demo Readiness

Final system supports:

Multimodal control

Real-time response

Smooth operation

Stability under normal use

Installation & Running
Clone Repo
git clone <repo-url>
cd touchless-ai-reader

Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run App
python app.py


OR run the EXE if packaged.

Exit Controls

Press ESC

Or close the camera window

System Pipeline

Camera
→ Hand/Eye/Head Detection
→ Feature Extraction
→ ML Gesture Classification
→ Temporal Filtering
→ Action Mapping
→ Touchless Interaction

Purpose of This Project

This project demonstrates:

Real-world AI system design

Accessibility-focused engineering

Applied computer vision

ML classifier deployment

HCI research development

End-to-end production workflow

Author

Developed by
Manidhar Bheempadu
AI & Computer Vision Developer

Open for collaboration and accessibility research.

License

This project is intended for educational, research, and demonstration use.