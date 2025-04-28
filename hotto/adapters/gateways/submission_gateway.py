from abc import ABC, abstractmethod
from hotto.domain.entities.submission import Submission

class SubmissionGateway(ABC):
    @abstractmethod
    def save(self, submission: Submission):
        pass
