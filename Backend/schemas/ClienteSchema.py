from pydantic import BaseModel
from typing import Optional, List

class Cliente(BaseModel):
    razonSocial: Optional[str]