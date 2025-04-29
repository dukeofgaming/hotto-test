import pytest
from flask import Flask
from hotto.slices.patient_analytics.adapters.patient_analytics_api_controller import PatientAnalyticsApiController
from hotto.app import app

# TODO: Refactor to GWT/AAA

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_patients_without_insurance_returns_200(client):
    response = client.get('/api/patients/without-insurance')
    assert response.status_code == 200
    assert 'abc321' in response.get_json()

def test_get_clinical_data_returns_200(client):
    response = client.get('/api/patients/clinical-data?patient_id=abc321')
    assert response.status_code == 200
    assert response.get_json() == [
        {
            "form_id": "mental_health_followup",
            "id": "e3749bb687bfb5b23ccabdfc1391314aedb56b7c6be65a1a7fd8ff3bd3b10414",
            "patient_id": "abc321",
            "question_id": "Describe your mood over the past week",
            "submission_id": "ghi124",
            "submitted_at": 1744129845,
            "value": "Depressed, occasionally anxious"
        },
        {
            "form_id": "mental_health_followup",
            "id": "d42840a51cb8c33c26f10fe5ff4baaac01585170fd3aebfe7c08c21c67221353",
            "patient_id": "abc321",
            "question_id": "How many hours of sleep did you get last night?",
            "submission_id": "ghi124",
            "submitted_at": 1744129845,
            "value": "8"
        },
        {
            "form_id": "basic_check",
            "id": "df1e07c9e9b40498840308b2de737ade1b5ea28f8e3fb0d3ca70bef31ad234da",
            "patient_id": "abc321",
            "question_id": "Recent Health Events",
            "submission_id": "ghi123",
            "submitted_at": 1744389045,
            "value": "['Hospitalization in 2020', 'Started physical therapy', 'Diagnosed with insomnia']"
        }
    ]
