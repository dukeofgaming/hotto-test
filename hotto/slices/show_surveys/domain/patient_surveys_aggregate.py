from dataclasses import dataclass, asdict
from typing import List
from hotto.modules.survey.domain.entities.form import Form
from hotto.modules.survey.domain.entities.question import Question
from hotto.modules.survey.domain.entities.submission import Submission

@dataclass
class PatientSurveysAggregate:
    forms: List[Form]
    questions: List[Question]
    submissions: List[Submission]

    def to_dict(self):
        return {
            "forms": [asdict(form) for form in self.forms],
            "questions": [asdict(question) for question in self.questions],
            "submissions": [asdict(submission) for submission in self.submissions]
        }
