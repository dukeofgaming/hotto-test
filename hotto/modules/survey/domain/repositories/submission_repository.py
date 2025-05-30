from abc import ABC, abstractmethod
from hotto.modules.survey.domain.entities.submission import Submission
from typing import List

class SubmissionRepository(ABC):
    @abstractmethod
    def save(self, submission: Submission):
        pass

    @abstractmethod
    def get_by_patient_id(self, patient_id: str) -> List[Submission]:
        pass
