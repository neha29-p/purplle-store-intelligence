import sys
import os

# Get the absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Force the root to the very front of the search path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now it will find 'pipeline' because the root is at the front of the list
try:
    from pipeline.frame_processor import FrameProcessor
    processor = FrameProcessor()
    result = processor.process_frame(None)
    print(f"Result: {result}")
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    print(f"Current sys.path: {sys.path}")