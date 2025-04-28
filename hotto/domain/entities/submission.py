from dataclasses import dataclass, field
from typing import List
from .answer import Answer
from datetime import datetime

@dataclass(frozen=True)
class Submission:
    id: str
    form_id: str
    patient_id: str
    submitted_at: int
    answers: List[Answer] = field(default_factory=list)

    @staticmethod
    def _iso8601_to_unix(value):
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
                return int(dt.timestamp())
            except Exception:
                pass
        raise ValueError(f"Cannot convert {value} to Unix timestamp")

    @classmethod
    def from_dict(cls, data):
        answers = [
            Answer(
                submission_id=data['submission_id'],
                question_id=ans['question'],
                value=str(ans['answer'])
            )
            for ans in data['answers'].values()
        ]
        submitted_at = cls._iso8601_to_unix(data['submitted_at'])
        return cls(
            id=data['submission_id'],
            form_id=data['form_id'],
            patient_id=data['patient_id'],
            submitted_at=submitted_at,
            answers=answers
        )
