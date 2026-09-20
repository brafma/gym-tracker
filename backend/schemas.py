from typing import Literal

from pydantic import BaseModel, Field


class WorkoutItemCreate(BaseModel):
    type: Literal["muscle_group", "exercise"]
    id: int
    rank: int = Field(ge=1)


class WorkoutCreate(BaseModel):
    name: str = Field(min_length=1, max_length=25)
    items: list[WorkoutItemCreate]