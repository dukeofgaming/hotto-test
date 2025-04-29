from hotto.modules.survey.domain.entities.submission import Submission
from hotto.modules.survey.domain.repositories.submission_repository import SubmissionRepository
from hotto.modules.survey.infrastructure.gateways.mysql_answer_gateway import MySQLAnswerGateway
from hotto.modules.survey.infrastructure.gateways.mysql_submission_gateway import MySQLSubmissionGateway

class MySQLSubmissionRepository(SubmissionRepository):
    def __init__(self, conn):
        self.conn = conn
        self.submission_gateway = MySQLSubmissionGateway(conn)
        self.answer_gateway = MySQLAnswerGateway(conn)

    def save(self, submission: Submission):
        self.submission_gateway.save(submission)
        self.answer_gateway.save(submission.answers)
