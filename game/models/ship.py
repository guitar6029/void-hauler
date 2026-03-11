from typing import Annotated

from pydantic import BaseModel, Field, computed_field, model_validator
from uuid import UUID, uuid4
from game.models.ship_type import ShipType

MIN_LENGTH_SHIP_NAME = 5
MIN_LENGTH_LOCATION = 1


class Ship(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: Annotated[str, Field(min_length=MIN_LENGTH_SHIP_NAME)]
    # model: ShipModel todo (maybe for now we should have one type , in diffetent file Model for the ShipTYpe)
    fuel: Annotated[float, Field(ge=0)]
    ship_type: ShipType
    cargo_used: Annotated[int, Field(ge=0)]
    credits: Annotated[int, Field(ge=0)]
    location: Annotated[str, Field(min_length=MIN_LENGTH_LOCATION)]
    inventory: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_ship(self):
        self._validate_cargo()
        self._validate_fuel()
        return self

    def _validate_cargo(self):
        if self.cargo_used > self.ship_type.cargo_capacity:
            raise ValueError("Cargo exceeds capacity")

    def _validate_fuel(self):
        if self.fuel > self.ship_type.fuel_capacity:
            raise ValueError("Fuel exceeds capacity")

    @computed_field
    def remaining_cargo_space(self) -> int:
        return self.ship_type.cargo_capacity - self.cargo_used

    @computed_field
    def cargo_full(self) -> bool:
        return self.cargo_used == self.ship_type.cargo_capacity
