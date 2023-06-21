from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from enum import Enum


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []  # opcionalno, chto b ne lezli oshibki - optional[...] = []<- po defoltu, otday putoy spisok ili tam prosto budet null


class Trade(BaseModel):
    user_id: int
    currency: str = Field(max_length=10)
    date: float
