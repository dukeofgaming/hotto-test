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

    def get_by_patient_id(self, patient_id: str):
        cursor = self.conn.cursor(dictionary=True)
        query = """
        SELECT id as submission_id, form_id, patient_id, submitted_at
        FROM submissions
        WHERE patient_id = %s
        ORDER BY submitted_at DESC
        """
        cursor.execute(query, (patient_id,))
        result = cursor.fetchall()
        cursor.close()
        return result
