from flask import Flask, request, jsonify, render_template
import mysql.connector
from dotenv import load_dotenv
import os
from bootloader import bootloader
import hashlib
import secrets

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Database configuration
db_config = {
    'host'      : os.getenv('DB_HOST', 'localhost'),
    'user'      : os.getenv('DB_USER', 'root'),
    'password'  : os.getenv('DB_PASSWORD', 'password'),
    'database'  : os.getenv('DB_NAME', 'submissions_db')
}

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

        # Insert submission into the database
        submission_query = """
        INSERT INTO submissions (id, form_id, patient_id, submitted_at)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(submission_query, (
            data['submission_id'],
            data['form_id'],
            data['patient_id'],
            iso8601_to_unix(data['submitted_at'])
        ))

        # Insert answers into the database
        for key, answer in data['answers'].items():
            # Use the question text as question_id
            question_id = answer['question']
            # Compose a unique, non-reversible hash for the answer id
            id_source = f"{data['submission_id']}|{question_id}|{str(answer['answer'])}"
            # Use SHA-256 and then encode as hex, but truncate to 64 chars to ensure <255
            answer_id = hashlib.sha256(id_source.encode('utf-8') + secrets.token_bytes(8)).hexdigest()[:64]
            answer_query = """
            INSERT INTO answers (id, submission_id, question_id, value)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(answer_query, (
                answer_id,
                data['submission_id'],
                question_id,
                str(answer['answer'])
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
    return render_template('index.html')

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