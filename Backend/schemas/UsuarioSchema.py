#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class Usuario(BaseModel):
    id: Optional[int]
    nombreUsuario: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    password: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    nombres: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    apellidos: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )


class UsuarioIniciarSesionIN(BaseModel):
    nombreUsuario: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    password: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )

class UsuarioOUT(BaseModel):
    id: Optional[int]
    nombreUsuario: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Lima"
    )
    nombres: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )
    apellidos: Optional[str] = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Lima"
    )