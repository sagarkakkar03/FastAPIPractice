from fastapi.testclient import TestClient
from UnitTesting.app.main import app

client = TestClient(app)

def test_eligibilty_api_pass():
    payload = {
        'income': 6000000,
        'age': 21
    }

    response = client.post('/loan_eligibility', json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligibility': True}


def test_eligibility_api_fail():
    payload = {
        'income': 600,
        'age':10
    }

    response = client.post('/loan_eligibility', json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligibility': False}
