from abc import ABC, abstractmethod
from hotto.modules.survey.domain.entities.submission import Submission

class SubmissionRepository(ABC):
    @abstractmethod
    def save(self, submission: Submission):
        pass
