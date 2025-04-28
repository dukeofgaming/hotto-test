from hotto.slices.save_submission.adapters.abstract_save_submission_controller import AbstractSaveSubmissionController
from hotto.slices.save_submission.usecases.save_submission_usecase import SaveSubmissionUseCase
from hotto.domain.entities.submission import Submission

class SaveSubmissionController(AbstractSaveSubmissionController):
    def __init__(self, use_case: SaveSubmissionUseCase):
        self.use_case = use_case

    def save_submission(self, request):
        data = request.get_json()
        submission = Submission.from_dict(data)
        return self.use_case.save_submission(submission, data['answers'])
