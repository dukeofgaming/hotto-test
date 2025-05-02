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
            "forms": [asdict(f) for f in self.forms],
            "questions": [asdict(q) for q in self.questions],
            "submissions": [asdict(s) for s in self.submissions]
        }
