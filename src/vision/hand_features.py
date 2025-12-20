import numpy as np
import math

def euclidean(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 +
                     (p1.y - p2.y)**2 +
                     (p1.z - p2.z)**2)

def angle(a, b, c):
    """Angle at point b formed by points a-b-c"""
    ba = np.array([a.x - b.x, a.y - b.y, a.z - b.z])
    bc = np.array([c.x - b.x, c.y - b.y, c.z - b.z])

    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    return np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0)))
def extract_distances(landmarks):
    wrist = landmarks[0]

    fingertips = [4, 8, 12, 16, 20]
    features = []

    for idx in fingertips:
        features.append(euclidean(wrist, landmarks[idx]))

    return features
def extract_angles(landmarks):
    finger_joints = {
        "index": (5,6,8),
        "middle":(9,10,12),
        "ring":(13,14,16),
        "pinky":(17,18,20)

    }

    features = []
    for _, (a,b,c) in finger_joints.items():
        features.append(angle(landmarks[a],landmarks[b],landmarks[c]))
    return features
def extract_hand_features(hand_landmarks):
    landmarks = hand_landmarks.landmark

    distance_features = extract_distances(landmarks)
    angle_features = extract_angles(landmarks)

    return distance_features + angle_features
