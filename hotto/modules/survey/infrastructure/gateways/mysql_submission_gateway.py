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
        SELECT s.id as submission_id, s.form_id, s.patient_id, s.submitted_at,
               fq.question_id, fq.position,
               q.question_text, q.type as question_type, q.is_clinical,
               a.id as answer_id, a.value as answer_value
        FROM submissions s
        JOIN form_questions fq ON s.form_id = fq.form_id
        JOIN questions q ON fq.question_id = q.id
        LEFT JOIN answers a ON a.submission_id = s.id AND a.question_id = q.id
        WHERE s.patient_id = %s
        ORDER BY s.submitted_at DESC, fq.position ASC
        """
        cursor.execute(query, (patient_id,))
        result = cursor.fetchall()
        cursor.close()
        return result
