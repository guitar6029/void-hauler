from enum import Enum


class EconomyType(str, Enum):
    MINING = "MINING"
    AGRICULTURE = "AGRICULTURE"
    INDUSTRIAL = "INDUSTRIAL"
    TECH = "TECH"
    MILITARY = "MILITARY"
    TRADE_HUB = "TRADE_HUB"
