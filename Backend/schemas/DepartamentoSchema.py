#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class Departamento(BaseModel):
    id: Optional[int]
    nombreDepartamento: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
