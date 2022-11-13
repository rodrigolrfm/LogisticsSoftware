#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class Provincia(BaseModel):
    id: Optional[int]
    nombreProvincia: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    idDepartamento: Optional[int] = Field(default=None, example=1)