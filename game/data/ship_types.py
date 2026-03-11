from game.models.ship_type import ShipType

FRONTIER_HAULER = ShipType(
    name="Frontier Hauler",
    cargo_capacity=40,
    fuel_capacity=100,
    fuel_efficiency=1.0,
    speed=1.0,
)

ATLAS_FREIGHTER = ShipType(
    name="Atlas Freighter",
    cargo_capacity=120,
    fuel_capacity=180,
    fuel_efficiency=0.8,
    speed=0.9,
)

AVAILABLE_SHIP_TYPES = [FRONTIER_HAULER, ATLAS_FREIGHTER]
