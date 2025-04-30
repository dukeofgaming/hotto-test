from hotto.modules.survey.domain.repositories.submission_repository import SubmissionRepository

class ShowSurveysUseCase:
    def __init__(self, submission_repository: SubmissionRepository):
        self.submission_repository = submission_repository

    def get_surveys_for_patient(self, patient_id: str):
        if not patient_id:
            raise ValueError("Missing patient_id")
        return self.submission_repository.get_by_patient_id(patient_id)
