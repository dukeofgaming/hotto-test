from typing import List, Dict, Any
from hotto.domain.entities.patient import Patient
from hotto.slices.patient_analytics.application.patient_analytics_gateway import PatientAnalyticsGateway

class PatientAnalyticsRepository:
    """
    Application-layer repository for patient analytics. Always returns entities.
    Calls the abstracted patient analytics gateway.
    """
    def __init__(self, gateway: PatientAnalyticsGateway):
        self.gateway = gateway

    def get_patients_without_insurance(self) -> List[Patient]:
        patient_ids = self.gateway.get_patients_without_insurance()
        return [Patient(id=pid) for pid in patient_ids]

    def get_clinical_data_for_patient(self, patient_id: str) -> List[Dict[str, Any]]:
        return self.gateway.get_clinical_data_for_patient(patient_id)
