import logging
logging.basicConfig(filename='flask_app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
import json
import os
import re
from hotto.bootloader import bootloader
from hotto.slices.save_submission.adapters.save_submission_api_controller import SaveSubmissionApiController
from hotto.slices.patient_analytics.adapters.patient_analytics_api_controller import PatientAnalyticsApiController
from hotto.slices.show_surveys.adapters.show_surveys_api_controller import ShowSurveysApiController

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
    manifest_path = os.path.join(app.static_folder, 'react', '.vite', 'manifest.json')
    with open(manifest_path) as f:
        manifest = json.load(f)
    js_file = manifest['index.html']['file']

    # Find the latest CSS file in the static/react/assets directory
    assets_dir = os.path.join(app.static_folder, 'react', 'assets')
    logging.debug(f"[DEBUG] assets_dir: {assets_dir}")
    print(f"[DEBUG] assets_dir: {assets_dir}")
    css_file = None
    if os.path.isdir(assets_dir):
        all_files = os.listdir(assets_dir)
        logging.debug(f"[DEBUG] Files in assets_dir: {all_files}")
        print(f"[DEBUG] Files in assets_dir: {all_files}")
        css_files = [f for f in all_files if f.startswith('index-') and f.endswith('.css')]
        logging.debug(f"[DEBUG] Matched CSS files: {css_files}")
        print(f"[DEBUG] Matched CSS files: {css_files}")
        if css_files:
            css_file = sorted(css_files)[-1]  # Use the latest by name
            logging.debug(f"[DEBUG] Selected css_file: {css_file}")
            print(f"[DEBUG] Selected css_file: {css_file}")
        else:
            logging.debug("[DEBUG] No CSS files matched.")
            print("[DEBUG] No CSS files matched.")
    else:
        logging.debug("[DEBUG] assets_dir does not exist.")
        print("[DEBUG] assets_dir does not exist.")

    # Get patient_id from querystring, default to False if not provided
    patient_id = request.args.get('patient_id', False)
    return render_template('index.html', react_name=patient_id, react_js_file=js_file, react_css_file=css_file)

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