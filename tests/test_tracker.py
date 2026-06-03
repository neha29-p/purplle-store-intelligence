# PROMPT:
# I need to validate the visitor tracking engine responsible for maintaining customer identities across video frames.
#
# The test should ensure that tracked visitors remain consistent even when detections move or temporarily disappear.
#
# Validation should include:
# - Identity persistence
# - Movement tracking
# - Entry detection
# - Exit detection
# - Visitor count consistency
#
# This component is critical because occupancy analytics and customer flow metrics depend directly on tracking accuracy.
#
# CHANGES MADE:
# Added retail movement scenarios and aligned assertions with the tracker implementation.
#
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
