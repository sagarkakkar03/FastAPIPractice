import requests

def bodyTemperature(doctorName, diagnosisId):
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"
    temps = []

    first = requests.get(base_url, params={"page": 1}).json()
    total_pages = first["total_pages"]

    for page in range(1, total_pages + 1):
        data = requests.get(base_url, params={"page": page}).json()

        for rec in data.get("data", []):
            doctor = rec.get("doctor", {})
            diagnosis = rec.get("diagnosis", {})
            vitals = rec.get("vitals", {})

            if doctor.get("name") == doctorName and diagnosis.get("id") == diagnosisId:
                temp = vitals.get("bodyTemperature")
                if temp is not None:
                    temps.append(temp)

    return temps

print(bodyTemperature('Dr Allysa Ellis', 1))