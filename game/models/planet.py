from pydantic import BaseModel, Field
from typing import Annotated, Optional
from uuid import UUID, uuid4

MIN_LENGTH_PLANET_NAME = 2
MIN_LENGTH_DESCRIPTION = 2


class Planet(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: Annotated[str, Field(min_length=MIN_LENGTH_PLANET_NAME)]
    system: str
    economy_type: str  # later could be a model or enum ?
    danger_level: Annotated[
        int, Field(ge=0, le=4)
    ]  # maybe a scale , hghest , ran by pirates (kind of like in No Man's Sky)
    population: Annotated[int, Field(ge=0)]
    distance_index: Annotated[int, Field(ge=0)]
    description: Optional[Annotated[str, Field(min_length=MIN_LENGTH_DESCRIPTION)]]
