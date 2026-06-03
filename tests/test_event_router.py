# PROMPT:
# Create tests for routing retail analytics events.
# Ensure events reach the correct processing components.
#
# CHANGES MADE:
# Adapted routing validation for the project's event architecture.
#
from pipeline.event_router import EventRouter

router = EventRouter()

event = router.route_zone_change(
    visitor_id="VIS_001",
    store_id="STORE_001",
    camera_id="CAM_001",
    zone_id="ENTRANCE"
)

print(event)
