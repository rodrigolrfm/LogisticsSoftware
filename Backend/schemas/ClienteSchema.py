from pydantic import BaseModel
from typing import Optional, List

class Cliente(BaseModel):
    id: Optional[int]
    razonSocial: Optional[str]