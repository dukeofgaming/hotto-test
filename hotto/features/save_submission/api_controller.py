from mysql.connector import Error
from flask import jsonify
from http import HTTPStatus
from hotto.modules.survey.domain.entities.submission import Submission
from hotto.features.save_submission.model import SaveSubmissionModel, InvalidQuestionTypeError

class SaveSubmissionApiController:
    def __init__(self):
        self.model = SaveSubmissionModel()

    def save_submission(self, incoming_request):
        try:
            request_data = incoming_request.get_json()
            if not request_data:
                return jsonify({"error": "Invalid or missing JSON payload."}), HTTPStatus.BAD_REQUEST

            submission = Submission.from_dict(request_data)
            self.model.save_submission(submission, request_data['answers'])
            return jsonify({"message": "Submission saved successfully"}), HTTPStatus.CREATED
        except InvalidQuestionTypeError as error:
            return jsonify({"error": str(error)}), HTTPStatus.BAD_REQUEST
        except Error as error:
            return jsonify({"error": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR
        except Exception as error:
            return jsonify({"error": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR
