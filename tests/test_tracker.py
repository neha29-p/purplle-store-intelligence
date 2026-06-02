import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.tracker import VisitorTracker

tracker = VisitorTracker()

frame1 = [
    (100, 100, 200, 300),
    (300, 120, 420, 350),
]

print("Frame 1:", tracker.update(frame1))

frame2 = [
    (110, 110, 210, 310),
    (305, 125, 425, 355),
]

print("Frame 2:", tracker.update(frame2))