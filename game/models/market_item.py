from pydantic import BaseModel, Field
from typing import Annotated
from game.models.cargo import Cargo


class MarketItem(BaseModel):
    cargo: Cargo
    price: Annotated[float, Field(ge=0)]
    stock: Annotated[int, Field(geg=0)]
