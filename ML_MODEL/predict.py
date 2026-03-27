import joblib
import numpy as np
from typing import List

saved_model = joblib.load('ML_MODEL/model.joblib')

def make_prediction(data: dict) -> float:
    features = np.array([
        [
        data['latitude'],
        data['longitude'],
        data['housing_median_age'],
        data['total_rooms'],
        data['total_bedrooms'],
        data['population'],
        data['households'],
        data['median_income']
        ]
    ])
    return saved_model.predict(features)[0]


def make_batch_predictions(data_inputs: List[dict]) -> List[float]:
    features = np.array([
        [
        data['latitude'],
        data['longitude'],
        data['housing_median_age'],
        data['total_rooms'],
        data['total_bedrooms'],
        data['population'],
        data['households'],
        data['median_income']
        ] for data in data_inputs
    ])

    return saved_model.predict(features)