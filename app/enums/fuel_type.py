from enum import Enum


class FuelType(str, Enum):
    GASOLINE = "Gasoline"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"
    ETHANOL = "Ethanol"
    LPG = "LPG"