from flask import jsonify, request
from http import HTTPStatus
from hotto.features.patient_analytics.model import PatientAnalyticsModel, InvalidPatientAnalyticsRequest

class PatientAnalyticsApiController:
    def __init__(self):
        self.model = PatientAnalyticsModel()

    def get_patients_without_insurance(self, incoming_request):
        try:
            patients = self.model.get_patients_without_insurance()
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

            clinical_data = self.model.get_clinical_data_for_patient(patient_id)
            return jsonify(clinical_data), HTTPStatus.OK
        except InvalidPatientAnalyticsRequest as error:
            return jsonify({"error": str(error)}), HTTPStatus.BAD_REQUEST
        except Exception as error:
            return jsonify({"error": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR
