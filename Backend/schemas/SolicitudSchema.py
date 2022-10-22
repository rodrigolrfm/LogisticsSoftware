from pydantic import BaseModel
from typing import Optional, List

class Solicitud(BaseModel):
    id: Optional[int]
    nombre: Optional[str]
    numeroDocumento: Optional[str]