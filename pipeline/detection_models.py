from dataclasses import dataclass

@dataclass
class Detection:
    track_id: int
    x1: float
    y1: float
    x2: float
    y2: float
    confidence: float