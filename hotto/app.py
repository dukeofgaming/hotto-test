from dotenv import load_dotenv
from flask import Flask, request
import os
from hotto.bootloader import bootloader
from hotto.slices.save_submission.api_controller import SaveSubmissionApiController
from hotto.slices.patient_analytics.adapters.patient_analytics_api_controller import PatientAnalyticsApiController
from hotto.slices.show_surveys.api_controller import ShowSurveysApiController
from hotto.slices.show_surveys.page_controller import ShowSurveysPageController

load_dotenv()

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates')
)

# Centralize DB config in app.config
app.config['DB_CONFIG'] = {
    'host'      : os.getenv('DB_HOST', 'localhost'),
    'user'      : os.getenv('DB_USER', 'root'),
    'password'  : os.getenv('DB_PASSWORD', 'password'),
    'database'  : os.getenv('DB_NAME', 'submissions_db'),
}

# Endpoint to handle submissions
@app.route('/api/surveys/submit', methods=['POST'])
def submit():
    controller = SaveSubmissionApiController()
    return controller.save_submission(request)


@app.route('/')
def index():
    controller = ShowSurveysPageController()
    return controller.index(app)

# Update Flask route handlers to use new controller location
@app.route('/api/patients/without-insurance', methods=['GET'])
def get_patients_without_insurance():
    controller = PatientAnalyticsApiController()
    return controller.get_patients_without_insurance(request)

@app.route('/api/patients/clinical-data', methods=['GET'])
def get_clinical_data():
    controller = PatientAnalyticsApiController()
    return controller.get_clinical_data(request)

@app.route('/api/surveys/show', methods=['GET'])
def show_surveys():
    controller = ShowSurveysApiController()
    return controller.get_surveys_for_patient(request)

if __name__ == '__main__':
    # Prepare db_config for bootloader
    bootloader(app.config['DB_CONFIG'])
    flask_env = os.getenv('FLASK_ENV', 'production').strip().lower()
    os.environ['FLASK_ENV'] = flask_env
    debug_env = os.getenv('FLASK_DEBUG', '').strip().lower()
    truthy = {'1', 'true', 'yes', 'on'}
    debug_mode = debug_env in truthy
    app.run(
        debug=debug_mode,
        host='0.0.0.0',
        port=5000
    )