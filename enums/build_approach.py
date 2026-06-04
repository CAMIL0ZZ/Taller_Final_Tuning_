from enum import Enum


class BuildApproach(str, Enum):
    STREET = "Street"
    TRACK = "Track"
    DRIFT = "Drift"
    DRAG = "Drag"
    OFFROAD = "Offroad"
    SHOW = "Show"