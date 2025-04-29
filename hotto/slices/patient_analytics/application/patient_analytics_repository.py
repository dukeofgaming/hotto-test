from typing import List, Dict, Any
from hotto.domain.entities.patient import Patient
from hotto.slices.patient_analytics.application.patient_analytics_gateway import PatientAnalyticsGateway
from hotto.modules.Timestamp.timestamp_helper import TimestampHelper

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
        data = self.gateway.get_clinical_data_for_patient(patient_id)
        for item in data:
            if "submitted_at" in item and item["submitted_at"] is not None:
                item["submitted_at"] = TimestampHelper.unix_to_iso8601(item["submitted_at"])
            if "is_clinical" in item:
                item["is_clinical"] = bool(item["is_clinical"])
        return data
