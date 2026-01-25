import math

# Face landmark indices (MediaPipe)
LEFT_CHEEK = 234
RIGHT_CHEEK = 454

prev_distance = None


def detect_face_zoom(face_landmarks):
    """
    Detect zoom-in / zoom-out based on face distance change.
    Returns:
        "ZOOM_IN" | "ZOOM_OUT" | None
    """
    global prev_distance

    lm = face_landmarks.landmark

    left = lm[LEFT_CHEEK]
    right = lm[RIGHT_CHEEK]

    distance = math.sqrt(
        (left.x - right.x) ** 2 +
        (left.y - right.y) ** 2
    )

    if prev_distance is None:
        prev_distance = distance
        return None

    delta = distance - prev_distance
    prev_distance = distance

    if abs(delta) < 0.003:
        return None

    if delta > 0:
        return "ZOOM_IN"
    else:
        return "ZOOM_OUT"