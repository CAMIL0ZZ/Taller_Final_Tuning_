from enum import Enum


class ChassisType(str, Enum):
    SEDAN = "Sedan"
    COUPE = "Coupe"
    HATCHBACK = "Hatchback"
    SUV = "SUV"
    PICKUP = "Pickup"
    CONVERTIBLE = "Convertible"
    WAGON = "Wagon"