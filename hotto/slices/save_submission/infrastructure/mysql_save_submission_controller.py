from hotto.slices.save_submission.adapters.save_submission_controller import SaveSubmissionController
from hotto.slices.save_submission.usecases.save_submission_usecase import SaveSubmissionUseCase
from hotto.infrastructure.repositories.mysql_submission_repository import MySQLSubmissionRepository

class MySQLSaveSubmissionController(SaveSubmissionController):
    def __init__(self, conn):
        submission_repository = MySQLSubmissionRepository(conn)
        use_case = SaveSubmissionUseCase(submission_repository)
        super().__init__(use_case)
