import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.tracker import VisitorTracker

tracker = VisitorTracker()

# Person below line
frame1 = [
    (100, 350, 200, 450)
]

print(tracker.update(frame1))

# Person crosses upward
frame2 = [
    (100, 250, 200, 350)
]

print(tracker.update(frame2))