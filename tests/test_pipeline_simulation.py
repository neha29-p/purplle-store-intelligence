from pipeline.visitor_registry import VisitorRegistry
from pipeline.zone_manager import ZoneManager
from pipeline.event_router import EventRouter

# Initialize the components
registry = VisitorRegistry()
zones = ZoneManager()
router = EventRouter()

visitor_id = "VIS_001"

# Simulate the workflow
registry.register(visitor_id)

previous_zone = zones.assign_zone(
    visitor_id,
    "ENTRANCE"
)

event = router.route_zone_change(
    visitor_id=visitor_id,
    store_id="STORE_001",
    camera_id="CAM_001",
    zone_id="ENTRANCE"
)

# Print results to verify
print("Visitors:", registry.count())
print("Previous Zone:", previous_zone)
print("Current Zone:", zones.get_zone(visitor_id))
print(event)