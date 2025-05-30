from hotto.slices.patient_analytics.application.patient_analytics_repository import PatientAnalyticsRepository
from hotto.slices.patient_analytics.application.patient_analytics_gateway import PatientAnalyticsGateway

class InvalidPatientAnalyticsRequest(Exception):
    pass

class PatientAnalyticsUseCase:
    def __init__(self, repository: PatientAnalyticsRepository):
        self.repository = repository

    def get_patients_without_insurance(self):
        patients = self.repository.get_patients_without_insurance()
        if patients is None:
            raise InvalidPatientAnalyticsRequest("No patient data available.")
        return patients

    def get_clinical_data_for_patient(self, patient_id):
        if not patient_id:
            raise InvalidPatientAnalyticsRequest("Missing patient_id.")
        data = self.repository.get_clinical_data_for_patient(patient_id)
        if data is None:
            raise InvalidPatientAnalyticsRequest(f"No clinical data for patient_id: {patient_id}")
        return data
