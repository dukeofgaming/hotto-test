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

    def get_patients_without_insurance(self, incoming_request):
        try:
            patients = self.usecase.get_patients_without_insurance()
            return jsonify([patient.id for patient in patients]), HTTPStatus.OK
        except InvalidPatientAnalyticsRequest as error:
            return jsonify({"error": str(error)}), HTTPStatus.BAD_REQUEST
        except Exception as error:
            return jsonify({"error": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR

    def get_clinical_data(self, incoming_request):
        try:
            patient_id = incoming_request.args.get("patient_id")

            if not patient_id:
                return jsonify({"error": "Missing patient_id"}), HTTPStatus.BAD_REQUEST

            clinical_data = self.usecase.get_clinical_data_for_patient(patient_id)
            return jsonify(clinical_data), HTTPStatus.OK
        except InvalidPatientAnalyticsRequest as error:
            return jsonify({"error": str(error)}), HTTPStatus.BAD_REQUEST
        except Exception as error:
            return jsonify({"error": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR
