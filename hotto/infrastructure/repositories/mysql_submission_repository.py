from hotto.domain.repositories.submission_repository import SubmissionRepository
from hotto.domain.entities.submission import Submission
from hotto.infrastructure.gateways.mysql_submission_gateway import MySQLSubmissionGateway
from hotto.infrastructure.gateways.mysql_answer_gateway import MySQLAnswerGateway

class MySQLSubmissionRepository(SubmissionRepository):
    def __init__(self, conn):
        self.conn = conn
        self.submission_gateway = MySQLSubmissionGateway(conn)
        self.answer_gateway = MySQLAnswerGateway(conn)

    def save(self, submission: Submission):
        self.submission_gateway.save(submission)
        self.answer_gateway.save(submission.answers)
