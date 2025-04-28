from dataclasses import dataclass
import hashlib

@dataclass(frozen=True)
class Answer:
    submission_id: str
    question_id: str
    value: str

    @property
    def id(self):
        id_source = f"{self.submission_id}|{self.question_id}|{self.value}"
        return hashlib.sha256(id_source.encode('utf-8')).hexdigest()[:64]
