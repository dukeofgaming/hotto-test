import mysql.connector
from hotto.modules.survey.domain.entities.submission import Submission
from hotto.modules.survey.domain.repositories.submission_repository import SubmissionRepository
from hotto.modules.survey.infrastructure.gateways.mysql_answer_gateway import MySQLAnswerGateway
from hotto.modules.survey.infrastructure.gateways.mysql_submission_gateway import MySQLSubmissionGateway

class MySQLSubmissionRepository(SubmissionRepository):
    def __init__(self, db_config):
        self.db_config = db_config

    def save(self, submission: Submission):
        conn = mysql.connector.connect(**self.db_config)
        try:
            submission_gateway = MySQLSubmissionGateway(conn)
            answer_gateway = MySQLAnswerGateway(conn)
            submission_gateway.save(submission)
            answer_gateway.save(submission.answers)
        finally:
            conn.close()
