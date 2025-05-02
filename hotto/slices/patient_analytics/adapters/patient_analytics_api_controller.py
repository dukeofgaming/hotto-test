from flask import jsonify, request
from http import HTTPStatus
from hotto.slices.patient_analytics.application.patient_analytics_usecase import PatientAnalyticsUseCase, InvalidPatientAnalyticsRequest
from hotto.slices.patient_analytics.application.patient_analytics_repository import PatientAnalyticsRepository
from hotto.slices.patient_analytics.application.patient_analytics_gateway import PatientAnalyticsGateway
from hotto.slices.patient_analytics.infrastructure.mysql_patient_analytics_gateway import MySQLPatientAnalyticsGateway

class PatientAnalyticsApiController:
    def __init__(self):
        gateway = MySQLPatientAnalyticsGateway()
        repository = PatientAnalyticsRepository(gateway)
        self.usecase = PatientAnalyticsUseCase(repository)

    def get_patients_without_insurance(self, request):
        try:
            patients = self.usecase.get_patients_without_insurance()
            return jsonify([p.id for p in patients]), HTTPStatus.OK
        except InvalidPatientAnalyticsRequest as err:
            return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST
        except Exception as err:
            return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR

    def get_clinical_data(self, request):
        try:
            patient_id = request.args.get("patient_id")

            if not patient_id:
                return jsonify({"error": "Missing patient_id"}), HTTPStatus.BAD_REQUEST

            data = self.usecase.get_clinical_data_for_patient(patient_id)
            return jsonify(data), HTTPStatus.OK
        except InvalidPatientAnalyticsRequest as err:
            return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST
        except Exception as err:
            return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
