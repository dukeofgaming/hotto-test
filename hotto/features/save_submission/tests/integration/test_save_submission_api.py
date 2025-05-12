import json
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

@pytest.fixture
def submissions():
    with open('data/data.json') as f:
        return json.load(f)

from hotto.modules.database.mysql import MySQLDatabase
from hotto.app import app

def delete_submission_and_answers(submission_id):
    with app.app_context():
        db = MySQLDatabase()
        conn = db.connect()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM answers WHERE submission_id = %s", (submission_id,))
            cursor.execute("DELETE FROM submissions WHERE id = %s", (submission_id,))
            conn.commit()
            cursor.close()
        finally:
            conn.close()

def test_given_basic_check_submission_when_posted_then_returns_success(client, submissions):
    # Arrange: Use the first submission from data/data.json (real DB integration)
    basic_check_submission = submissions[0]

    # Ensure clean state before test
    delete_submission_and_answers(basic_check_submission["submission_id"])

    # Act: Post the submission to the /api/surveys/submit endpoint
    response = client.post('/api/surveys/submit', json=basic_check_submission)

    # Assert: The response should indicate success
    assert response.status_code == 201
    assert response.get_json()["message"] == "Submission saved successfully"


def test_given_duplicate_submission_when_posted_then_returns_duplicate_error(client, submissions):
    # Arrange: Use the first submission from data/data.json
    basic_check_submission = submissions[0]

    # Ensure clean state
    delete_submission_and_answers(basic_check_submission["submission_id"])

    # Act: Post the submission twice
    response1 = client.post('/api/surveys/submit', json=basic_check_submission)
    response2 = client.post('/api/surveys/submit', json=basic_check_submission)

    # Assert: First should succeed, second should return duplicate error
    assert response1.status_code == 201
    assert response1.get_json()["message"] == "Submission saved successfully"
    assert response2.status_code == 500
    assert "Duplicate entry" in response2.get_json().get("error", "")

    # Cleanup: Remove the test submission and answers
    delete_submission_and_answers(basic_check_submission["submission_id"])
