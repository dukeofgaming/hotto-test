from hotto.modules.survey.adapters.gateways.answer_gateway import AnswerGateway
from hotto.modules.survey.domain.entities.answer import Answer

class MySQLAnswerGateway(AnswerGateway):
    def __init__(self, conn):
        self.conn = conn

    def save(self, answer_or_answers):
        # Accept either a single Answer or a list of Answers
        if isinstance(answer_or_answers, Answer):
            answers = [answer_or_answers]
        else:
            answers = list(answer_or_answers)
        cursor = self.conn.cursor()
        answer_query = """
        INSERT INTO answers (id, submission_id, question_id, value)
        VALUES (%s, %s, %s, %s)
        """
        data = [
            (answer.id, answer.submission_id, answer.question_id, answer.value)
            for answer in answers
        ]
        cursor.executemany(answer_query, data)
        self.conn.commit()
        cursor.close()

    def get_by_submission_id(self, submission_id: str):
        cursor = self.conn.cursor(dictionary=True)
        query = """
        SELECT submission_id, question_id, value
        FROM answers
        WHERE submission_id = %s
        ORDER BY question_id
        """
        cursor.execute(query, (submission_id,))
        rows = cursor.fetchall()
        cursor.close()
        from hotto.modules.survey.domain.entities.answer import Answer
        return [Answer(**row) for row in rows]
