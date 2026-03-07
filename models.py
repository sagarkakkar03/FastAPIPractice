from pydantic import BaseModel
import datetime

class Employee(BaseModel):
    id: str
    name: str
    department: str
    age: int 


class Items(BaseModel):
    id: str 
    name: str 
    category: str 
    date: datetime.date
    