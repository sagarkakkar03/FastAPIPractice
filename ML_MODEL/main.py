from fastapi import FastAPI
from .schemas import InputSchema, OutputSchema
from .predict import make_prediction, make_batch_predictions
from typing import List

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Welcome to our website'}

@app.post('/predict', response_model=OutputSchema)
def prediction(data_input: InputSchema):
    result = make_prediction(data=data_input.model_dump())
    return OutputSchema(predicted_price=result)

@app.post('/batch_presict', response_model=List[OutputSchema])
def batch_prediction(data_input: List[InputSchema]):
    results = make_batch_predictions(data_inputs = [data.model_dump() for data in data_input])
    return [OutputSchema(predicted_price=prediction) for prediction in results]