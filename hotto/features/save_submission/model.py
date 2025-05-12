from hotto.modules.database.mysql import MySQLDatabase
from hotto.modules.survey.domain.entities.submission import Submission

ALLOWED_QUESTION_TYPES = {'text', 'date', 'boolean', 'object', 'array', 'number'}

class InvalidQuestionTypeError(Exception):
    pass

class SaveSubmissionModel:
    def __init__(self):
        self.db = MySQLDatabase()

    def save_submission(self, submission: Submission, raw_answers: dict):
        # Validate question types
        question_text_to_answer = {
            ans['question']: ans
            for ans in raw_answers.values()
        }
        for answer_obj in submission.answers:
            answer_dict = question_text_to_answer[answer_obj.question_id]
            question_type = answer_dict.get('type')
            if question_type not in ALLOWED_QUESTION_TYPES:
                raise InvalidQuestionTypeError(f"Invalid question type: {question_type}")

        # Save submission and answers directly (no repository/gateway)
        conn = self.db.connect()
        try:
            cursor = conn.cursor()
            # Save submission
            submission_query = (
                "INSERT INTO submissions (id, form_id, patient_id, submitted_at) "
                "VALUES (%s, %s, %s, %s)"
            )
            submission_params = (
                submission.id,
                submission.form_id,
                submission.patient_id,
                submission.submitted_at
            )
            cursor.execute(submission_query, submission_params)

            # Save answers
            answer_query = (
                "INSERT INTO answers (id, submission_id, question_id, value) "
                "VALUES (%s, %s, %s, %s)"
            )
            for answer in submission.answers:
                cursor.execute(answer_query, (answer.id, answer.submission_id, answer.question_id, answer.value))
            conn.commit()
            cursor.close()
        finally:
            conn.close()
