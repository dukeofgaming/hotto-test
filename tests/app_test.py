import json
import pytest
from hotto.app import app
from dotenv import load_dotenv
from hotto.slices.save_submission.adapters.save_submission_api_controller import SaveSubmissionApiController

# Load test environment variables
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

