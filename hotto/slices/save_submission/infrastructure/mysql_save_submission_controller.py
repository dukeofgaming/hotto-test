import mysql.connector
from mysql.connector import Error
from hotto.slices.save_submission.adapters.save_submission_controller import SaveSubmissionController
from hotto.slices.save_submission.usecases.save_submission_usecase import SaveSubmissionUseCase
from hotto.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository
import os
from flask import jsonify

class MySQLSaveSubmissionController(SaveSubmissionController):
    def __init__(self, db_config=None):
        if db_config is None:
            db_config = {
                'host'      : os.getenv('DB_HOST', 'localhost'),
                'user'      : os.getenv('DB_USER', 'root'),
                'password'  : os.getenv('DB_PASSWORD', 'password'),
                'database'  : os.getenv('DB_NAME', 'submissions_db')
            }
        self.db_config = db_config
        super().__init__(None)  # use_case will be created per request

    def save_submission(self, request):
        conn = None
        try:
            conn = mysql.connector.connect(**self.db_config)
            submission_repository = MySQLSubmissionRepository(conn)
            use_case = SaveSubmissionUseCase(submission_repository)
            data = request.get_json()
            if not data:
                return {"error": "Invalid or missing JSON payload."}, 400

            # Use the domain entity's from_dict method, not a repository method
            from hotto.domain.entities.submission import Submission
            submission = Submission.from_dict(data)

            response, status_code = use_case.save_submission(submission, data['answers'])
            if status_code == 201:
                conn.commit()
            return response, status_code
        except Error as err:
            return {"error": str(err)}, 500
        except Exception as err:
            return {"error": str(err)}, 500
        finally:
            if conn and conn.is_connected():
                conn.close()
