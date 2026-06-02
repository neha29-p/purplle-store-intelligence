from pipeline.event_generator import create_entry_event
from pipeline.event_client import send_event

# 1. Create an event using our generator (Micro-Step 7)
event = create_entry_event(
    visitor_id="VIS_001",
    store_id="STORE_001",
    camera_id="CAM_001"
)

# 2. Send it to the FastAPI server
result = send_event(event)

# 3. Print the result to confirm it worked
print(result)