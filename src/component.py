from dataclasses import dataclass


@dataclass(frozen=True)
class ComponentType:
    name: str
    mass: int
    cost: int
    requires: str = ""
    remarks: str = ""


PROBE = ComponentType("Probe", 1, 2)
SUPPLIES = ComponentType("Supplies", 1, 1, "Life Support")
SAMPLE = ComponentType("Sample", 1, 0)

BASIC_TYPES = {
    "probe": PROBE,
    "supplies": SUPPLIES,
    "sample": SAMPLE,
}


@dataclass(frozen=True)
class EngineType(ComponentType):
    thrust: int = 0


JUNO = EngineType("Juno", 1, 1, "Juno", thrust=4)
ATLAS = EngineType("Atlas", 4, 5, "Atlas", thrust=27)
SOYUZ = EngineType("Soyuz", 9, 8, "Soyuz", thrust=80)
SATURN = EngineType("Saturn", 20, 15, "Saturn", thrust=200)
ION_THRUSTER = EngineType(
    "Ion Thruster",
    1,
    10,
    "Ion Thruster",
    remarks="Multiply thrust by voyage years",
    thrust=5,
)

ENGINE_TYPES = {
    "juno": JUNO,
    "atlas": ATLAS,
    "soyuz": SOYUZ,
    "saturn": SATURN,
    "ion": ION_THRUSTER,
}


@dataclass(frozen=True)
class CapsuleType(ComponentType):
    seats: int = 0


VOSTOK = CapsuleType("Vostok", 2, 2, "Reentry", "Can attempt reentry", seats=1)
EAGLE = CapsuleType("Eagle", 1, 4, "Landing", seats=2)
APOLLO = CapsuleType("Apollo", 3, 4, "Reentry", "Can attempt reentry", seats=3)
ALDRIN = CapsuleType("Aldrin", 3, 4, "Life Support", "Radiation level -1", seats=8)

CAPSULE_TYPES = {
    "vostok": VOSTOK,
    "eagle": EAGLE,
    "apollo": APOLLO,
    "aldrin": ALDRIN,
}

TYPE_LOOKUP = dict(
    **BASIC_TYPES,
    **ENGINE_TYPES,
    **CAPSULE_TYPES,
)


def parse_components(component_string):
    result = []
    for group in component_string.split(","):
        name, _, num = group.partition(" x")
        try:
            num = int(num)
        except ValueError:
            num = 1
        component = TYPE_LOOKUP[name.lower().strip()]
        result.extend([component] * num)
    return result
