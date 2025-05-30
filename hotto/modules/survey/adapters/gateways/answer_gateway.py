from abc import ABC, abstractmethod
from hotto.modules.survey.domain.entities.answer import Answer

class AnswerGateway(ABC):
    @abstractmethod
    def save(self, answer: Answer):
        pass

    @abstractmethod
    def get_by_submission_id(self, submission_id: str):
        pass
