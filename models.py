from pydantic import BaseModel, Field
import datetime
from typing import Optional

class Employee(BaseModel):
    id: str = Field(..., gt=0)
    name: str = Field(..., min_length=3, max_length=50)
    department: str = Field(...)
    age: Optional[int] = Field(..., gt=0, lt=101)


class Items(BaseModel):
    id: str 
    name: str 
    category: str 
    date: datetime.date
 