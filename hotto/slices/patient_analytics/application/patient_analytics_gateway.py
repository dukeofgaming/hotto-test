from abc import ABC, abstractmethod
from typing import List, Dict, Any

class PatientAnalyticsGateway(ABC):
    """
    Gateway for patient analytics queries. Only returns data (IDs, dicts, DTOs), never entities.
    """
    @abstractmethod
    def get_patients_without_insurance(self) -> List[str]:
        pass

    @abstractmethod
    def get_clinical_data_for_patient(self, patient_id: str) -> List[Dict[str, Any]]:
        pass
