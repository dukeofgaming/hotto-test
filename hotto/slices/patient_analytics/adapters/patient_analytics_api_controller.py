from flask import jsonify, request
from hotto.slices.patient_analytics.application.patient_analytics_usecase import PatientAnalyticsUseCase
from hotto.slices.patient_analytics.application.patient_analytics_repository import PatientAnalyticsRepository
from hotto.slices.patient_analytics.application.patient_analytics_gateway import PatientAnalyticsGateway
from hotto.slices.patient_analytics.infrastructure.mysql_patient_analytics_gateway import MySQLPatientAnalyticsGateway

class PatientAnalyticsApiController:
    def __init__(self):
        gateway = MySQLPatientAnalyticsGateway()
        repository = PatientAnalyticsRepository(gateway)
        self.usecase = PatientAnalyticsUseCase(repository, gateway)

    def get_patients_without_insurance(self, request):
        patients = self.usecase.get_patients_without_insurance()
        # Serialize each Patient entity (assumes Patient has an id attribute)
        return jsonify([p.id for p in patients]), 200

    def get_clinical_data(self, request):
        patient_id = request.args.get("patient_id")
        if not patient_id:
            return jsonify({"error": "Missing patient_id"}), 400
        data = self.usecase.get_clinical_data_for_patient(patient_id)
        return jsonify({"clinical_data": data}), 200
