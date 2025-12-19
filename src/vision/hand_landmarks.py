import cv2
import mediapipe as mp


class HandLandmarkDetector:
    def __init__(self,
                 static_image_mode=False,
                 max_num_hands=1,
                 detection_confidence=0.7,
                 tracking_confidence=0.7):

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=static_image_mode,
            max_num_hands=max_num_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def draw(self, frame, hand_landmarks):
         self.drawer.draw_landmarks(
          frame,
          hand_landmarks,
          self.mp_hands.HAND_CONNECTIONS,
          self.drawer.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
        self.drawer.DrawingSpec(color=(255, 0, 0), thickness=2)
)

