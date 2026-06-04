from enum import Enum


class ModType(str, Enum):
    ENGINE = "Engine"
    SUSPENSION = "Suspension"
    EXHAUST = "Exhaust"
    TURBO = "Turbo"
    AERODYNAMICS = "Aerodynamics"
    WHEELS = "Wheels"
    BRAKES = "Brakes"
    INTERIOR = "Interior"
    ELECTRONICS = "Electronics"