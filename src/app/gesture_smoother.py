from collections import deque
from statistics import mode

class GestureSmoother:
    def __init__(self, window_size=7):
        self.window = deque(maxlen=window_size)

    def smooth(self, prediction):
        self.window.append(prediction)
        if len(self.window) < self.window.maxlen:
            return None
        return mode(self.window)
