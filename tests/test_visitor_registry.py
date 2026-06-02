from pipeline.visitor_registry import VisitorRegistry

registry = VisitorRegistry()

registry.register("VIS_001")
registry.register("VIS_002")

print(registry.count())
print(registry.get("VIS_001"))