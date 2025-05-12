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

def test_show_surveys_returns_surveys_for_patient(client):
    """
    Integration test for GET /api/surveys/show?patient_id=abc321
    Should return a list of submissions with answers for the given patient.
    """
    # Act
    response = client.get('/api/surveys/show?patient_id=abc321')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert "submissions" in data
    submissions = data["submissions"]
    assert isinstance(submissions, list)
    for submission in submissions:
        assert isinstance(submission.get('submission_id'), str)
        assert isinstance(submission.get('form_id'), str)
        assert isinstance(submission.get('patient_id'), str)
        assert isinstance(submission.get('submitted_at'), int)
        assert 'answers' in submission
        assert isinstance(submission['answers'], list)
        for answer in submission['answers']:
            assert isinstance(answer.get('question_id'), str)
            # value can be str, dict, or list (depending on question type)
            assert 'value' in answer
