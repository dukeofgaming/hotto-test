from hotto.slices.patient_analytics.application.patient_analytics_repository import PatientAnalyticsRepository
from hotto.slices.patient_analytics.application.patient_analytics_gateway import PatientAnalyticsGateway

class PatientAnalyticsUseCase:
    def __init__(self, repository: PatientAnalyticsRepository, gateway: PatientAnalyticsGateway):
        self.repository = repository
        self.gateway = gateway

    def get_patients_without_insurance(self):
        return self.repository.get_patients_without_insurance()

    def get_clinical_data_for_patient(self, patient_id):
        return self.repository.get_clinical_data_for_patient(patient_id)
