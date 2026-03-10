# Installation Guide - Touchless AI Reader

Complete step-by-step instructions for setting up Touchless AI Reader on your system.

## Table of Contents
- [System Requirements](#system-requirements)
- [Installation Steps](#installation-steps)
- [Troubleshooting](#troubleshooting)
- [Verifying Installation](#verifying-installation)

## System Requirements

### Hardware
- **Processor**: Intel i5 / AMD Ryzen 5 or better (for smooth 30+ FPS)
- **RAM**: 4GB minimum (8GB recommended)
- **Webcam**: USB 2.0 or higher (1080p recommended)
- **Storage**: 2GB free space for dependencies

### Software
- **OS**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **Python**: 3.9, 3.10, or 3.11
- **Git**: For cloning the repository

### Supported Cameras
- Built-in laptop webcams
- USB external webcams
- Any camera supported by OpenCV

## Installation Steps

### 1. Install Python

#### Windows
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer and **CHECK** "Add Python to PATH"
3. Click "Install Now"

Verify installation:
```bash
python --version
```

#### macOS
```bash
# Using Homebrew
brew install python@3.11

# Or download from python.org
```

Verify:
```bash
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3.11 python3.11-venv python3.11-dev
```

Verify:
```bash
python3.11 --version
```

### 2. Clone Repository

```bash
git clone https://github.com/manidharreddy0909/touchless-ai-reader.git
cd touchless-ai-reader
```

### 3. Create Virtual Environment

This isolates dependencies for this project.

#### Windows
```powershell
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **OpenCV** - Computer vision
- **MediaPipe** - Hand/Face detection
- **NumPy** - Numerical computing
- **Pillow** - Image processing
- **PyAutoGUI** - Mouse/keyboard control
- And more...

### 6. Verify Installation

```bash
# Test if all packages imported correctly
python -c "import cv2, mediapipe, numpy; print('✓ All packages imported successfully')"
```

### 7. Test Camera Access

```bash
python -c "import cv2; cap = cv2.VideoCapture(0); print(f'Camera accessible: {cap.isOpened()}')"
```

If it shows `False`, your camera isn't accessible. See [Troubleshooting](#troubleshooting).

## Running the Application

### Start the Application

```bash
python app.py
```

### Expected Output
```
Touchless AI Reader Started
Initializing Camera...
Loading MediaPipe Models...
Ready! Start making gestures...
```

### Stop the Application
- Press `Q` to quit gracefully
- Or `Ctrl+C` in terminal

## Building Standalone Executable

Create a single `.exe` or app file without needing Python installed:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile app.py

# Built file will be in: dist/app.exe
```

## Troubleshooting

### Camera Not Detected

**Problem**: Application can't find camera

**Solutions**:
1. **Check if camera is in use**
   ```bash
   # Windows
   # Check Task Manager > Performance > Camera
   
   # macOS
   # System Preferences > Security & Privacy > Camera
   ```

2. **Try different camera index**
   - Open `settings.json`
   - Change `"camera_index": 0` to `1` or `2`
   - Save and restart

3. **Check camera permissions**
   - **Windows**: Settings > Privacy > Camera > Allow apps
   - **macOS**: System Preferences > Security & Privacy > Camera
   - **Linux**: `sudo usermod -a -G video $USER`

4. **Restart camera driver**
   - Windows: Device Manager > Cameras > Right-click > Restart
   - macOS/Linux: Restart system

### Low Performance / Lag

**Solutions**:
1. **Close other applications** using camera
2. **Reduce resolution** in `settings.json`
3. **Upgrade hardware** (especially GPU)
4. **Improve lighting**
5. **Reduce background complexity**

### Module Not Found Errors

**Problem**: `ModuleNotFoundError: No module named 'xyz'`

**Solutions**:
```bash
# Make sure virtual environment is activated
# (should see (venv) in terminal)

# Reinstall all requirements
pip install -r requirements.txt

# Or specific module
pip install mediapipe
```

### MediaPipe Installation Issues

**Problem**: MediaPipe fails to install

**Solutions**:
```bash
# Update pip first
python -m pip install --upgrade pip

# Try installing specific version
pip install mediapipe==0.8.11

# Or check system requirements
# Make sure you have C++ build tools installed
```

### Permissions Error (Linux)

**Problem**: `Permission denied` when accessing camera

**Solution**:
```bash
# Add user to video group
sudo usermod -a -G video $USER

# Apply group changes
newgrp video

# Reboot (or log out and back in)
```

## Verifying Installation

Run the test suite to verify everything works:

```bash
# Test hand detection
python debugfiles/test_hand_gestures.py

# Test face detection
python debugfiles/test_face_debug.py

# Test index finger position
python debugfiles/test_index_position.py

# Test gesture model
python debugfiles/test_hand_features.py
```

All tests should run without errors.

## Common Issues Checklist

- [ ] Python 3.9+ installed
- [ ] Virtual environment activated (see `(venv)` in terminal)
- [ ] All requirements installed (`pip list` | grep mediapipe)
- [ ] Camera detected and accessible
- [ ] Good lighting conditions
- [ ] Latest video drivers installed
- [ ] No permission errors

## Next Steps

1. **Read the README** for feature overview
2. **Check settings.json** for configuration options
3. **Run the application** - `python app.py`
4. **Explore debugfiles/** for testing individual features
5. **Read CONTRIBUTING.md** if you want to contribute

## Still Having Issues?

1. Check [GitHub Issues](https://github.com/manidharreddy0909/touchless-ai-reader/issues)
2. Search for your error message
3. Create a new issue with:
   - Your OS and Python version
   - Full error message
   - Steps you took
   - Screenshot if applicable

---

**Installation Complete!** 🎉

You're now ready to use Touchless AI Reader. Happy gesturing!
