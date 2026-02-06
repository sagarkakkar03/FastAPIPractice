from fastapi import FastAPI, Path, HTTPException, Query 
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

app = FastAPI()


class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient', examples=['Sagar'])]
    city: Annotated[str, Field(..., description='City of the patient', examples=['Sirsa'])] 
    age: Annotated[int, Field(..., description='Age of the patient', examples=[23], gt=0, lt=100)] 
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient', examples=['Male'])]
    height: Annotated[float, Field(..., description='Height of the patient in mts', examples=['1.75'], gt=0)] 
    weight: Annotated[float, Field(..., description='Weight of the patient in kgs', examples=[60], gt=0)] 

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi 
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'  
        elif self.bmi < 30:
            return 'Overweight'   
        else:
            return 'Obese'


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description='Name of the patient')]
    city: Annotated[Optional[str], Field(default=None, description='City of the patient')] 
    age: Annotated[Optional[int], Field(default=None, description='Age of the patient')] 
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None, description='Gender of the patient')]
    height: Annotated[Optional[float], Field(default=None, description='Height of the patient in mts')] 
    weight: Annotated[Optional[float], Field(default=None, description='Weight of the patient in kgs')] 


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def HelloWorld():
    return {'message': 'Patient management system API'}

@app.get("/about")
def about():
    return {'message': "This is the about section for the patient management API"}

@app.get("/view")
def view():
   data = load_data()
   return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
    
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='Sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field selected from {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order selected from asc or desc')
    data = load_data()
    sort_order = True
    if order == 'asc':
        sort_order = False
    return sorted(data.values(), key= lambda person: person[sort_by], reverse=sort_order)

@app.post('/create')
def create_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')
    
    data[patient.id] = patient.model_dump(exclude=['id']) 
    save_data(data)
    
    return JSONResponse(status_code=201, content={'message': 'patient created successfully'})
    

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    existing_patient_details = data[patient_id]
    updated_patient_details = patient_update.model_dump(exclude_unset=True)
    for key, value in updated_patient_details.items():
        existing_patient_details[key] = value
    existing_patient_details['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_details)
    existing_patient_details = patient_pydantic_obj.model_dump(exclude='id')
    data[patient_id] = existing_patient_details

    save_data(data)

    return JSONResponse(status_code=200, content="Patient Updated")

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content="Patient deleted")