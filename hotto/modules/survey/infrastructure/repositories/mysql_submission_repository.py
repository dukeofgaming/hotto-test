import mysql.connector
from flask import current_app
from hotto.modules.survey.domain.entities.submission import Submission
from hotto.modules.survey.domain.repositories.submission_repository import SubmissionRepository
from hotto.modules.survey.infrastructure.gateways.mysql_answer_gateway import MySQLAnswerGateway
from hotto.modules.survey.infrastructure.gateways.mysql_submission_gateway import MySQLSubmissionGateway

class MySQLSubmissionRepository(SubmissionRepository):
    def __init__(self):
        pass

    def save(self, submission: Submission):
        db_config = current_app.config['DB_CONFIG']
        conn = mysql.connector.connect(**db_config)
        try:
            submission_gateway = MySQLSubmissionGateway(conn)
            answer_gateway = MySQLAnswerGateway(conn)
            submission_gateway.save(submission)
            answer_gateway.save(submission.answers)
        finally:
            conn.close()
