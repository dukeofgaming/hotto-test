from hotto.modules.survey.adapters.gateways.submission_gateway import SubmissionGateway
from hotto.modules.survey.domain.entities.submission import Submission

class MySQLSubmissionGateway(SubmissionGateway):
    def __init__(self, conn):
        self.conn = conn

    def save(self, submission: Submission):
        cursor = self.conn.cursor()
        submission_query = """
        INSERT INTO submissions (id, form_id, patient_id, submitted_at)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(submission_query, (
            submission.id,
            submission.form_id,
            submission.patient_id,
            submission.submitted_at
        ))
        self.conn.commit()
        cursor.close()
