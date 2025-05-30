from abc import ABC, abstractmethod
from hotto.modules.survey.domain.entities.submission import Submission

class SubmissionGateway(ABC):
    @abstractmethod
    def save(self, submission: Submission):
        pass

    def get_by_patient_id(self, patient_id: str):
        raise NotImplementedError()
