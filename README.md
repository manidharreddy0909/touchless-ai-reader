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
  


## Progress
- [x] Camera module
- [x] Hand landmark detection
- [x] Hand feature extraction (distance + angle based)
---

## 📅 Day 3: Hand Feature Engineering

### 🎯 Objective
Convert raw hand landmark coordinates into **stable, machine-learning-ready features**
that accurately represent hand gestures regardless of scale or orientation.

---

### 🧠 What Was Accomplished

- Designed **geometric feature extraction** pipeline
- Computed:
  - Wrist-to-fingertip **Euclidean distances**
  - Finger joint **angles** for gesture articulation
- Ensured:
  - Scale normalization
  - Rotation invariance
  - Smooth temporal behavior
- Generated **compact feature vectors** suitable for ML models

---

### 🧩 Feature Types

| Feature Type | Description |
|------------|-------------|
| Distance | Wrist → fingertip distances |
| Angle | Joint bending angles for fingers |

---

### 🛠 Technologies Used
- NumPy
- Python math utilities

---

## 📅 Day 4: Custom Gesture Dataset Creation

### 🎯 Objective
Create a **self-collected, labeled dataset** for hand gestures to enable
accurate and personalized machine learning.

---

### 🧠 What Was Accomplished

- Designed gesture labeling scheme
- Built **real-time dataset collection pipeline**
- Captured hand features + gesture labels via webcam
- Stored samples in **CSV format**
- Collected ~900 labeled samples across gestures

---

### ✋ Supported Gestures

| Label | Gesture | Intended Action |
|------|--------|----------------|
| 0 | Open Palm | Next Page |
| 1 | Fist | Previous Page |
| 2 | Index Point | Scroll |
| 3 | Two Fingers | Zoom |
| 4 | Pinch | Select |

---

### 🗂 Dataset Format

Each row in `dataset.csv`:



---

## 📅 Day 5: Machine Learning Model Training

### 🎯 Objective
Train a robust machine-learning classifier capable of recognizing hand gestures
from extracted features.

---

### 🧠 What Was Accomplished

- Loaded custom gesture dataset
- Performed stratified train-test split
- Trained **Random Forest Classifier**
- Evaluated model using precision, recall, and F1-score
- Achieved **~90% classification accuracy**
- Saved trained model for real-time inference

---

### 📊 Model Performance (Summary)

- Accuracy: ~90%
- Balanced performance across gesture classes
- Robust to real-time variations

---

### 🛠 Technologies Used
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📅 Day 6: Real-Time Gesture Recognition

### 🎯 Objective
Deploy the trained ML model for **live gesture prediction** using a webcam feed.

---

### 🧠 What Was Accomplished

- Loaded trained gesture classification model
- Integrated feature extraction with ML inference
- Displayed predicted gesture labels in real time
- Achieved stable, low-latency predictions

---

### 🖥 System Flow


---

## 🚀 Project Status

- [x] Hand tracking
- [x] Feature engineering
- [x] Dataset creation
- [x] Model training
- [x] Real-time gesture prediction
- [ ] Gesture smoothing
- [ ] Page control integration
- [ ] Facial gesture module

---

## 🔮 Next Steps

- Temporal smoothing for gesture stability
- Integration with PDF / e-book reader
- Facial expression-based control
- Research paper & demo deployment

---

## 👨‍💻 Author
**Manidhar Bheempadu**  
Computer Vision & AI Developer




