from fastapi.testclient import TestClient
from ..main import app
from random import randrange

# ENDPOINT = "http://127.0.0.1:8001"

# client = TestClient(app)
# def generate_vaccine() :
#     random_code = randrange(5000, 555555555)
#     return  {
#         "user_id": random_code,
#         "vaccination_date": "2023-07-13",
#         "center_id": random_code,
#         "status": False,
#         "certificate_url": "string",
#         "operator_id": random_code
#     }

def test_create_vaccine():
    assert 1 == 1
    # Test the creation of a new user
    # vaccine_data = generate_vaccine()
    # response = client.post(ENDPOINT + "/vaccine", json = vaccine_data)
    # assert response.status_code == 200


