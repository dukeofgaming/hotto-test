from flask import Flask, request, jsonify, render_template
import mysql.connector
from dotenv import load_dotenv
import os
from hotto.bootloader import bootloader
import hashlib
import secrets
import json
from hotto.domain.entities.answer import Answer
from hotto.domain.entities.submission import Submission
from hotto.domain.repositories.submission_repository import SubmissionRepository
from hotto.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository
from hotto.slices.save_submission.usecases.save_submission_usecase import SaveSubmissionUseCase
from hotto.slices.save_submission.infrastructure.mysql_save_submission_controller import MySQLSaveSubmissionController

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates')
)

# Load environment variables
load_dotenv()

# Database configuration
db_config = {
    'host'      : os.getenv('DB_HOST', 'localhost'),
    'user'      : os.getenv('DB_USER', 'root'),
    'password'  : os.getenv('DB_PASSWORD', 'password'),
    'database'  : os.getenv('DB_NAME', 'submissions_db')
}

# Endpoint to handle submissions
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    conn = None  # Initialize conn to None
    try:
        conn = mysql.connector.connect(**db_config)
        controller = MySQLSaveSubmissionController(conn)

        response, status_code = controller.save_submission(request)
        if status_code == 201:
            conn.commit()
        return jsonify(response), status_code

    except Exception as err:  # Catch all exceptions
        return jsonify({"error": str(err)}), 500

    finally:
        if conn and conn.is_connected():
            conn.close()

@app.route('/')
def index():
    manifest_path = os.path.join(app.static_folder, 'react', '.vite', 'manifest.json')
    with open(manifest_path) as f:
        manifest = json.load(f)
    js_file = manifest['index.html']['file']
    return render_template('index.html', react_name="World", react_js_file=js_file)

if __name__ == '__main__':
    # Prepare db_config for bootloader
    bootloader(db_config)
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