import pytest
from hotto.app import app
from dotenv import load_dotenv

# Load test environment variables
def setup_module(module):
    load_dotenv(dotenv_path='test.env')


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_given_patient_without_insurance_when_getting_patients_without_insurance_then_returns_200(client):
    # Arrange
    # (No setup needed, using existing patient data)

    # Act
    response = client.get('/api/patients/without-insurance')

    # Assert
    assert response.status_code == 200
    assert 'abc321' in response.get_json()

def test_given_patient_with_clinical_data_when_getting_clinical_data_then_returns_expected_contract(client):
    # Arrange
    patient_id = "abc321"

    # Act
    response = client.get(f'/api/patients/clinical-data?patient_id={patient_id}')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert all(bool(item["is_clinical"]) for item in data)
    assert all(item["patient_id"] == patient_id for item in data)
    assert all("answer_id" in item for item in data)
