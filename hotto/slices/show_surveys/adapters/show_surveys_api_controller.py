from flask import jsonify, request
from http import HTTPStatus
from hotto.modules.survey.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository
from hotto.slices.show_surveys.application.show_surveys_usecase import ShowSurveysUseCase
from hotto.slices.show_surveys.domain.patient_surveys_aggregate import PatientSurveysAggregate

class ShowSurveysApiController:
    def __init__(self):
        submission_repository = MySQLSubmissionRepository()
        self.use_case = ShowSurveysUseCase(submission_repository)

    def get_surveys_for_patient(self, request):
        patient_id = request.args.get("patient_id")
        try:
            aggregate = self.use_case.get_surveys_for_patient(patient_id)
            # Convert aggregate to dict for JSON
            return jsonify(self.aggregate_to_dict(aggregate)), HTTPStatus.OK
        except ValueError as err:
            return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST
        except Exception as err:
            return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR

    def aggregate_to_dict(self, aggregate):
        return {
            "forms": [self.form_to_dict(f) for f in aggregate.forms],
            "questions": [self.question_to_dict(q) for q in aggregate.questions],
            "submissions": [self.submission_to_dict(s) for s in aggregate.submissions]
        }

    def form_to_dict(self, form):
        return {
            "id": form.id,
            **({"name": form.name} if hasattr(form, "name") else {})
        }

    def question_to_dict(self, question):
        return {
            "id": question.id,
            "question_text": question.question_text,
            "type": question.type,
            "is_clinical": bool(question.is_clinical)
        }

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
