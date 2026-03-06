from pydantic import BaseModel


class Employee(BaseModel):
    id: str
    name: str
    department: str
    age: int 