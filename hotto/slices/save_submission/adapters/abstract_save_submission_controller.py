from abc import ABC, abstractmethod
from flask import Request

class AbstractSaveSubmissionController(ABC):
    @abstractmethod
    def save_submission(self, request: 'Request'):
        """
        Args:
            request: The incoming Flask request object.
        Returns:
            tuple: (response_dict, status_code)
        """
        pass
