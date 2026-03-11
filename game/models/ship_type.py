from pydantic import BaseModel, Field
from typing import Annotated

MIN_SHIP_NAME_TYPE_LENGTH = 3
MAX_SHIP_NAME_TYPE_LENGTH = 50


class ShipType(BaseModel):
    name: Annotated[
        str,
        Field(
            min_length=MIN_SHIP_NAME_TYPE_LENGTH, max_length=MAX_SHIP_NAME_TYPE_LENGTH
        ),
    ]
    cargo_capacity: Annotated[int, Field(gt=0)]
    fuel_capacity: Annotated[float, Field(gt=0)]
    fuel_efficiency: Annotated[float, Field(gt=0)]
    speed: Annotated[float, Field(gt=0)]
