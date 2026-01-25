import cv2
import mediapipe as mp

mp_face = mp.solutions.face_mesh

class FaceTracker:
    def __init__(self):
        self.face = mp_face.FaceMesh(
            refine_landmarks=True,
            max_num_faces=1
        )

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.face.process(rgb)