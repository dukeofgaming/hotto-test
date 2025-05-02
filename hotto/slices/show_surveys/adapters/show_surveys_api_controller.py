from flask import jsonify
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
            dto = self.use_case.get_surveys_for_patient(patient_id)
            return jsonify(dto.to_dict()), HTTPStatus.OK
        except ValueError as err:
            return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST
        except Exception as err:
            return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
