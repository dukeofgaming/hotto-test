import pytest
from flask import Flask
from hotto.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_patients_without_insurance_returns_200(client):
    response = client.get('/api/patients/without-insurance')
    assert response.status_code == 200
    assert response.get_json() == {}

def test_get_clinical_data_returns_200(client):
    response = client.get('/api/patients/clinical-data')
    assert response.status_code == 200
    assert response.get_json() == {}
