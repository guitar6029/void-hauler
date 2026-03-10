from pydantic import BaseModel, Field
from typing import Annotated
from uuid import uuid4, UUID
from game.enums.cargo_category import CargoCategory

MIN_LENGTH_CARGO_NAME = 3


class Cargo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: Annotated[str, Field(min_length=MIN_LENGTH_CARGO_NAME)]
    category: CargoCategory
    weight: Annotated[int, Field(gt=0)]
    base_price: Annotated[float, Field(ge=0.0)]
    illegal: bool = False
