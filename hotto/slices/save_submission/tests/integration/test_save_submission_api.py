import json
import pytest
from hotto.app import app
from dotenv import load_dotenv
from hotto.slices.save_submission.adapters.save_submission_api_controller import SaveSubmissionApiController

# Load test environment variables
def setup_module(module):
    load_dotenv(dotenv_path='test.env')

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

@pytest.fixture
def submissions():
    with open('data/data.json') as f:
        return json.load(f)

def test_given_basic_check_submission_when_posted_then_returns_success(client, mocker, submissions):
    # Arrange: A valid basic_check submission and a mocked database connection
    mocker.patch('mysql.connector.connect')
    basic_check_submission = next(
        submission for submission in submissions
        if submission['form_id'] == 'basic_check' and submission['submission_id'] == 'ghi321'
    )

    # Act: Post the submission to the /api/surveys/submit endpoint
    response = client.post('/api/surveys/submit', json=basic_check_submission)

    # Assert: The response should indicate success
    assert response.status_code == 201
    assert response.get_json()["message"] == "Submission saved successfully"

def test_given_mental_health_followup_submission_when_posted_then_returns_success(client, mocker, submissions):
    # Arrange: A valid mental_health_followup submission and a mocked database connection
    mocker.patch('mysql.connector.connect')
    mental_health_followup_submission = next(
        submission for submission in submissions
        if submission['form_id'] == 'mental_health_followup'
    )

    # Act: Post the submission to the /api/surveys/submit endpoint
    response = client.post('/api/surveys/submit', json=mental_health_followup_submission)

    # Assert: The response should indicate success
    assert response.status_code == 201
    assert response.get_json()["message"] == "Submission saved successfully"

def test_given_failing_submission_when_posted_then_returns_error(client, mocker, submissions):
    # Arrange: A mocked database connection that raises an exception
    mock_connect = mocker.patch('mysql.connector.connect')
    mock_connect.side_effect = Exception("Database connection failed")
    failing_submission = next(
        submission for submission in submissions
        if submission['submission_id'] == 'ghi322'
    )

    # Act: Post the submission to the /api/surveys/submit endpoint
    response = client.post('/api/surveys/submit', json=failing_submission)

    # Assert: The response should indicate a failure with an appropriate error message
    assert response.status_code == 500
    assert "error" in response.get_json()
