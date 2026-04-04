from fastapi import FastAPI
from pydantic import BaseModel
from .logic import loan_eligibility

app = FastAPI()


class Applicant(BaseModel):
    income: int
    age: int


@app.post('/loan_eligibility')
def check_eligibilty(applicant: Applicant):

    income = applicant.income
    age = applicant.age 

    eligibility = loan_eligibility(income=income, age=age)

    return {'eligibility': eligibility}




