from pipeline.occupancy_analyzer import OccupancyAnalyzer


class CameraAnalyzer:

    def __init__(self):
        self.analyzer = OccupancyAnalyzer()

    def summarize(self, video_path):

        samples = self.analyzer.analyze_video(video_path)

        if not samples:
            return {
                "samples": 0,
                "average_occupancy": 0,
                "max_occupancy": 0,
            }

        return {
            "samples": len(samples),
            "average_occupancy": round(
                sum(samples) / len(samples), 2
            ),
            "max_occupancy": max(samples),
        }