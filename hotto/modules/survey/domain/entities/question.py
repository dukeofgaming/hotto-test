from dataclasses import dataclass

@dataclass
class Question:
    id: str
    question_text: str
    type: str
    is_clinical: bool
