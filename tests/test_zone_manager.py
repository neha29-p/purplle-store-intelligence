# PROMPT:
# I need a validation suite for the zone management component used to monitor customer activity within specific store areas.
#
# The objective is to verify that visitors are assigned to the correct zones and that occupancy metrics remain accurate.
#
# The test should validate:
# - Zone entry detection
# - Zone exit detection
# - Occupancy calculations per zone
# - Multiple zone handling
# - Consistent zone analytics generation
#
# These validations are important because retailers use zone-level insights to understand customer engagement and optimize store layouts.
#
# CHANGES MADE:
# Added retail-focused zone analytics scenarios and aligned outputs with the dashboard reporting requirements.
#
from pipeline.zone_manager import ZoneManager

manager = ZoneManager()

previous = manager.assign_zone("VIS_001", "ENTRANCE")
print(previous)

previous = manager.assign_zone("VIS_001", "CHECKOUT")
print(previous)

print(manager.get_zone("VIS_001"))
