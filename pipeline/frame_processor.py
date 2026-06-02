from pipeline.detector import PersonDetector
from pipeline.tracker import PersonTracker

class FrameProcessor:
    def __init__(self):
        self.detector = PersonDetector()
        self.tracker = PersonTracker()

    def process_frame(self, frame):
        detections = self.detector.detect(frame)
        tracked_objects = self.tracker.update(detections)
        return tracked_objects