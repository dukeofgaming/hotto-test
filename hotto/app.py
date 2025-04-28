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
from hotto.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository

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

ALLOWED_QUESTION_TYPES = {'text', 'date', 'boolean', 'object', 'array', 'number'}

# Removed iso8601_to_unix helper; now encapsulated in Submission

# Endpoint to handle submissions
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    conn = None  # Initialize conn to None
    try:
        conn = mysql.connector.connect(**db_config)
        # Use repository instead of direct gateways
        submission_repository = MySQLSubmissionRepository(conn)

        # Create Submission object from JSON
        submission = Submission.from_dict(data)

        # Validate question types before saving
        question_text_to_answer = {
            ans['question']: ans
            for ans in data['answers'].values()
        }
        for answer_obj in submission.answers:
            answer_dict = question_text_to_answer[answer_obj.question_id]
            question_type = answer_dict.get('type')
            if question_type not in ALLOWED_QUESTION_TYPES:
                return jsonify({"error": f"Invalid question type: {question_type}"}), 400

        # Save submission and answers using repository
        submission_repository.save(submission)

        conn.commit()
        return jsonify({"message": "Submission saved successfully"}), 201

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