from enum import Enum


class CargoCategory(str, Enum):
    FOOD = "FOOD"
    WATER = "WATER"
    MEDICAL = "MEDICAL"
    MINERALS = "MINERALS"
    INDUSTRIAL = "INDUSTRIAL"
    TECHNOLOGY = "TECHNOLOGY"
    LUXURY = "LUXURY"
