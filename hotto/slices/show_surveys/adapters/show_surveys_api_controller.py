from flask import jsonify, request
from hotto.modules.survey.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository
from hotto.slices.show_surveys.application.show_surveys_usecase import ShowSurveysUseCase

class ShowSurveysApiController:
    def __init__(self):
        submission_repository = MySQLSubmissionRepository()
        self.use_case = ShowSurveysUseCase(submission_repository)

    def get_surveys_for_patient(self, request):
        patient_id = request.args.get("patient_id")
        try:
            surveys = self.use_case.get_surveys_for_patient(patient_id)
            # Convert domain objects to dicts for JSON
            surveys_json = [self.submission_to_dict(s) for s in surveys]
            return jsonify(surveys_json), 200
        except ValueError as err:
            return jsonify({"error": str(err)}), 400
        except Exception as err:
            return jsonify({"error": str(err)}), 500

    def submission_to_dict(self, submission):
        return {
            "submission_id": submission.id,
            "form_id": submission.form_id,
            "patient_id": submission.patient_id,
            "submitted_at": submission.submitted_at,
            "answers": [self.answer_to_dict(a) for a in submission.answers]
        }

    def answer_to_dict(self, answer):
        return {
            "question_id": answer.question_id,
            "value": answer.value
        }
