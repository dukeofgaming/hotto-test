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

    def get_by_patient_id(self, patient_id: str) -> list[Submission]:
        db_config = current_app.config['DB_CONFIG']
        conn = mysql.connector.connect(**db_config)
        try:
            submission_gateway = MySQLSubmissionGateway(conn)
            submissions_data = submission_gateway.get_by_patient_id(patient_id)
            submissions = []
            for data in submissions_data:
                answers = MySQLAnswerGateway(conn).get_by_submission_id(data['submission_id'])
                submission = Submission(
                    id=data['submission_id'],
                    form_id=data['form_id'],
                    patient_id=data['patient_id'],
                    submitted_at=data['submitted_at'],
                    answers=answers
                )
                submissions.append(submission)
            return submissions
        finally:
            conn.close()
