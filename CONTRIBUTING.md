# Contributing to Touchless AI Reader

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the Touchless AI Reader project.

## Code of Conduct

- Be respectful and inclusive
- Focus on the code, not the person
- Help others learn and grow
- Report issues constructively

## How to Contribute

### 1. Fork & Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/touchless-ai-reader.git
cd touchless-ai-reader
git remote add upstream https://github.com/manidharreddy0909/touchless-ai-reader.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b bugfix/issue-description
```

### 3. Make Changes

- Keep commits small and focused
- Write descriptive commit messages
- Add docstrings to new functions
- Test your changes locally

### 4. Test Your Changes

```bash
# Test hand gesture detection
python debugfiles/test_hand_gestures.py

# Test face detection
python debugfiles/test_face_debug.py

# Run the main app
python app.py
```

### 5. Push & Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title describing the change
- Description of what was changed and why
- Reference to related issues (if any)

## Development Setup

### Prerequisites
- Python 3.9+
- Webcam for testing
- Good lighting for gesture detection

### Installation

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# For development with PyInstaller
pip install pyinstaller
```

### Project Structure

```
touchless-ai-reader/
├── src/                    # Main source code
│   ├── app/               # Application logic
│   ├── vision/            # Computer vision modules
│   ├── camera/            # Camera handling
│   ├── control/           # Mouse/action control
│   ├── ui/                # UI components
│   └── ml/                # Machine learning models
├── debugfiles/            # Test and debug scripts
├── data/                  # Data files and datasets
├── models/                # Trained gesture models
├── app.py                 # Main entry point
└── requirements.txt       # Dependencies
```

## Areas for Contribution

### 🐛 Bug Fixes
- Report bugs with reproduction steps
- Test edge cases (different lighting, camera angles)
- Add test cases to prevent regressions

### ✨ New Features
- Multi-hand gesture support
- Voice feedback integration
- Configuration GUI
- Performance optimizations
- Cross-platform testing (Windows, macOS, Linux)

### 📚 Documentation
- Improve README sections
- Add API documentation
- Create tutorials
- Add code comments
- Fix spelling/grammar

### 🧪 Testing
- Write unit tests
- Create integration tests
- Test on different hardware
- Test with different camera types

### 🎨 UI/UX Improvements
- Better settings window
- Real-time gesture preview
- Status notifications
- Gesture calibration tool

## Coding Standards

### Style Guide
- Use PEP 8 for Python code
- Use meaningful variable names
- Add type hints where possible
- Keep functions small and focused

### Example

```python
def detect_pinch(hand_landmarks: List[List[float]]) -> bool:
    """
    Detect if hand is making a pinch gesture.
    
    Args:
        hand_landmarks: List of 21 hand landmark coordinates
        
    Returns:
        True if pinch gesture detected, False otherwise
    """
    # Implementation...
    pass
```

### Comments

```python
# Bad
x = y + 1  # add 1

# Good
# Increment counter for next gesture frame
frame_counter = last_frame_count + 1
```

## Reporting Issues

### Bug Reports

Include:
- Python version
- OS (Windows, macOS, Linux)
- Camera model (if relevant)
- Steps to reproduce
- Expected vs actual behavior
- Error messages/screenshots

### Feature Requests

Include:
- Clear description of feature
- Use cases/why it's needed
- Any related issues
- Suggested implementation (if applicable)

## Pull Request Process

1. **Before submitting:**
   - Rebase on latest `upstream/main`
   - Test all changes locally
   - Update documentation if needed

2. **PR Description should include:**
   - What changed and why
   - Related issue (#issue-number)
   - Testing performed
   - New dependencies (if any)

3. **Review process:**
   - At least one maintainer review required
   - Address feedback and push updates
   - Squash commits if requested
   - PR merged after approval

## Performance Considerations

- Gesture detection should run ~30 FPS
- Minimize CPU usage
- Test on lower-end hardware too
- Profile code for bottlenecks

```python
import time

start = time.time()
# code to measure
elapsed = time.time() - start
print(f"Time: {elapsed:.3f}s")
```

## Need Help?

- Check existing issues and discussions
- Review project documentation
- Ask in issue comments
- Be specific and provide context

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (Educational/Research purposes).

---

**Thank you for contributing to Touchless AI Reader!** 🎉

Your help makes this project better for everyone.
