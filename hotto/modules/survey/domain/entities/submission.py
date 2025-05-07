from dataclasses import dataclass, field
from typing import List
from hotto.modules.survey.domain.entities.answer import Answer
from hotto.modules.timestamp.domain.timestamp_helper import TimestampHelper

@dataclass(frozen=True)
class Submission:
    id: str
    form_id: str
    patient_id: str
    submitted_at: int
    answers: List[Answer] = field(default_factory=list)

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
        # Use TimestampHelper for conversion
        submitted_at = TimestampHelper.iso8601_to_unix(data['submitted_at']) if 'submitted_at' in data else None
        return cls(
            id=data['submission_id'],
            form_id=data['form_id'],
            patient_id=data['patient_id'],
            submitted_at=submitted_at,
            answers=answers
        )
