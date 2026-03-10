from typing import Annotated

from pydantic import BaseModel, Field, computed_field
from uuid import UUID, uuid4

MIN_LENGTH_SHIP_NAME = 5
MIN_LENGTH_LOCATION = 1


class Ship(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: Annotated[str, Field(min_length=MIN_LENGTH_SHIP_NAME)]
    # model: ShipModel todo (maybe for now we should have one type , in diffetent file Model for the ShipTYpe)
    fuel: Annotated[float, Field(ge=0)]
    fuel_capacity: Annotated[float, Field(gt=0)]
    cargo_capacity: Annotated[
        int, Field(ge=0)
    ]  ## also depends on the Model of the ship type so it should take the value from there
    cargo_used: Annotated[int, Field(ge=0)]
    credits: Annotated[int, Field(ge=0)]
    location: Annotated[str, Field(min_length=MIN_LENGTH_LOCATION)]
    inventory: list[str]

    # if cargo_used > cargo_capacity:
    #     raise ValueError("Cargo exceeds capacity")

    # if fuel > fuel_capacity:
    #     raise ValueError("Fuel exceeds capacity")

    # @computed_field
    # def fuel_remaining(self) -> float:
    #     return self.fuel_capacity - self.fuel

    @computed_field
    def remaining_cargo_space(self) -> int:
        return self.cargo_capacity - self.cargo_used

    @computed_field
    def cargo_full(self) -> bool:
        return self.cargo_used == self.cargo_capacity
