from pipeline.zone_manager import ZoneManager

manager = ZoneManager()

previous = manager.assign_zone("VIS_001", "ENTRANCE")
print(previous)

previous = manager.assign_zone("VIS_001", "CHECKOUT")
print(previous)

print(manager.get_zone("VIS_001"))