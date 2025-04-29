import mysql.connector
from mysql.connector import Error
from flask import jsonify, current_app
from hotto.modules.survey.domain.entities.submission import Submission
from hotto.modules.survey.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository
from hotto.slices.save_submission.usecases.save_submission_usecase import SaveSubmissionUseCase

class SaveSubmissionApiController:
    def __init__(self, db_config=None):
        if db_config is None:
            db_config = current_app.config['DB_CONFIG']
        self.db_config = db_config

    def save_submission(self, request):
        try:
            # Let the repository handle DB connection management internally
            submission_repository = MySQLSubmissionRepository(self.db_config)
            use_case = SaveSubmissionUseCase(submission_repository)
            data = request.get_json()
            if not data:
                return {"error": "Invalid or missing JSON payload."}, 400

            submission = Submission.from_dict(data)
            response, status_code = use_case.save_submission(submission, data['answers'])
            return response, status_code
        except Error as err:
            return {"error": str(err)}, 500
        except Exception as err:
            return {"error": str(err)}, 500
