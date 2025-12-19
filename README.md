# Touchless AI Reader

An advanced multimodal AI system that enables touchless book navigation using
hand gestures, facial expressions, and intelligent perception.

## Status
- [x] Project structure initialized
- [x] Virtual environment setup
- [x] Camera module tested

## Next Step
Hand landmark detection using MediaPipe.
    




## 📅 Day 2: Hand Tracking Module (MediaPipe)

### 🎯 Objective
Implement reliable real-time hand landmark detection using a webcam as the foundation for touchless interaction (page turning, gesture control).

---

### 🧠 What Was Accomplished

- Integrated **MediaPipe Hands** with OpenCV
- Detected and tracked **21 hand landmarks** in real time
- Visualized:
  - Full hand skeleton
  - Index finger tip (used for future gesture logic)
- Built a **modular HandLandmarkDetector class**
- Verified stable performance on live webcam feed

---

### 🧩 Key Components

#### 1. `HandLandmarkDetector`
- Encapsulates MediaPipe initialization
- Converts frames from BGR → RGB
- Provides reusable `detect()` and `draw()` methods

#### 2. Real-Time Tracking
- Webcam feed using OpenCV
- Hand skeleton overlay
- Index finger tip coordinates extracted for gesture math

---

### 🛠 Technologies Used

- Python 3.11
- OpenCV
- MediaPipe (Hands solution)

---

### 🧪 How to Run

Activate virtual environment:
```bash
venv\Scripts\activate   # Windows
  