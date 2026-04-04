from app.logic import loan_eligibility


def test_low_income():
    assert loan_eligibility(60000, 25) == False

def test_age_eligible():
    assert loan_eligibility(600000000, 17) == False

def test_boundary_case():
    assert loan_eligibility(income=1000000, age=21) == True