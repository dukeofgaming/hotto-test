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

def iso8601_to_unix(value):
    """
    Converts an ISO8601 string (e.g., '2025-04-10T16:30:45Z') to a Unix timestamp (int).
    Accepts both string and int input; returns int.
    """
    from datetime import datetime, timezone
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
            return int(dt.timestamp())
        except Exception:
            pass
    raise ValueError(f"Cannot convert {value} to Unix timestamp")

# Endpoint to handle submissions
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    conn = None  # Initialize conn to None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create Submission object from JSON
        submission = Submission.from_dict(data)

        # Insert submission into the database
        submission_query = """
        INSERT INTO submissions (id, form_id, patient_id, submitted_at)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(submission_query, (
            submission.id,
            submission.form_id,
            submission.patient_id,
            submission.submitted_at
        ))

        # Build a mapping from question text to the answer dict for reliable lookups
        question_text_to_answer = {
            ans['question']: ans
            for ans in data['answers'].values()
        }

        # Insert answers into the database
        for answer_obj in submission.answers:
            # Get the answer dict by question text
            answer_dict = question_text_to_answer[answer_obj.question_id]
            question_type = answer_dict.get('type')
            if question_type not in ALLOWED_QUESTION_TYPES:
                return jsonify({"error": f"Invalid question type: {question_type}"}), 400
            answer_query = """
            INSERT INTO answers (id, submission_id, question_id, value)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(answer_query, (
                answer_obj.id,
                answer_obj.submission_id,
                answer_obj.question_id,
                answer_obj.value
            ))

        conn.commit()
        return jsonify({"message": "Submission saved successfully"}), 201

    except Exception as err:  # Catch all exceptions
        return jsonify({"error": str(err)}), 500

    finally:
        if conn and conn.is_connected():
            cursor.close()
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