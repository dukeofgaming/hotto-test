from abc import ABC, abstractmethod
from hotto.modules.survey.domain.entities.submission import Submission

class SubmissionGateway(ABC):
    @abstractmethod
    def save(self, submission: Submission):
        pass
