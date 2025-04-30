import mysql.connector
from mysql.connector import Error
from flask import jsonify, current_app
from hotto.modules.survey.domain.entities.submission import Submission
from hotto.modules.survey.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository
from hotto.slices.save_submission.application.save_submission_usecase import SaveSubmissionUseCase, InvalidQuestionTypeError

class SaveSubmissionApiController:
    def __init__(self):
        submission_repository = MySQLSubmissionRepository()
        self.use_case = SaveSubmissionUseCase(submission_repository)

    def save_submission(self, request):
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Invalid or missing JSON payload."}), 400

            submission = Submission.from_dict(data)
            self.use_case.save_submission(submission, data['answers'])
            return jsonify({"message": "Submission saved successfully"}), 201
        except InvalidQuestionTypeError as err:
            return jsonify({"error": str(err)}), 400
        except Error as err:
            return jsonify({"error": str(err)}), 500
        except Exception as err:
            return jsonify({"error": str(err)}), 500
