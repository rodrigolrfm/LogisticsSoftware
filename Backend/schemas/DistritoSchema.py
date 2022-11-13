#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class Distrito(BaseModel):
    id: Optional[int]
    nombreDistrito: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    idProvincia: Optional[int] = Field(default=None, example=1)