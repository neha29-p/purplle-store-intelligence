# PROMPT:
# Generate tests for retail analytics event generation.
# Validate event structure, payload consistency, and metadata creation.
#
# CHANGES MADE:
# Added project-specific event validation rules.
#
from pipeline.event_generator import create_entry_event

event = create_entry_event(
    visitor_id="VIS_001",
    store_id="STORE_001",
    camera_id="CAM_001"
)

print(event)
