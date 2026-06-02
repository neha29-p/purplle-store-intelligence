from pipeline.event_generator import create_entry_event

event = create_entry_event(
    visitor_id="VIS_001",
    store_id="STORE_001",
    camera_id="CAM_001"
)

print(event)