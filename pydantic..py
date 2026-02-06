from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    email: EmailStr
    age: int 
    weight: float = Field(gt=0, lt=60)
    married: Optional[bool] = None 
    allergies: List[str] = Field(max_length=5)
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)

patient1_info = {'name': 'sagar', 'email':'abc@gmail.com', 'age': '30', 'weight':55.1, 'allergies':['a', 'b'], 'contact_details': {'number': '9779772164'}}

patient1 = Patient(**patient1_info)

insert_patient_data(patient1)


