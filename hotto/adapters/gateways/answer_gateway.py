from abc import ABC, abstractmethod
from hotto.domain.entities.answer import Answer

class AnswerGateway(ABC):
    @abstractmethod
    def save(self, answer: Answer):
        pass
