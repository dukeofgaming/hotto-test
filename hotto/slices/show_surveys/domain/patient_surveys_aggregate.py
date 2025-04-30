from dataclasses import dataclass
from typing import List
from hotto.modules.survey.domain.entities.form import Form
from hotto.modules.survey.domain.entities.question import Question
from hotto.modules.survey.domain.entities.submission import Submission

@dataclass
class PatientSurveysAggregate:
    forms: List[Form]
    questions: List[Question]
    submissions: List[Submission]
