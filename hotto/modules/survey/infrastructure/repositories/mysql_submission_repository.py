import mysql.connector
from flask import current_app
from hotto.modules.survey.domain.entities.submission import Submission
from hotto.modules.survey.domain.entities.answer import Answer
from hotto.modules.survey.domain.entities.form import Form
from hotto.modules.survey.domain.entities.question import Question
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

    def get_by_patient_id(self, patient_id: str) -> dict:
        db_config = current_app.config['DB_CONFIG']
        conn = mysql.connector.connect(**db_config)
        try:
            submission_gateway = MySQLSubmissionGateway(conn)
            rows = submission_gateway.get_by_patient_id(patient_id)
            # Aggregate forms, questions, submissions
            forms = {}
            questions = {}
            submissions = {}
            for row in rows:
                # Forms
                form_id = row['form_id']
                if form_id not in forms:
                    forms[form_id] = Form(id=form_id)
                # Questions
                question_id = row['question_id']
                if question_id and question_id not in questions:
                    questions[question_id] = Question(
                        id=question_id,
                        question_text=row.get('question_text', ''),
                        type=row.get('question_type', ''),
                        is_clinical=row.get('is_clinical', False)
                    )
                # Submissions
                sub_id = row['submission_id']
                if sub_id not in submissions:
                    submissions[sub_id] = {
                        'submission_id': sub_id,
                        'form_id': form_id,
                        'patient_id': row['patient_id'],
                        'submitted_at': row['submitted_at'],
                        'answers': []
                    }
                # Answers
                if row.get('question_id'):
                    value = row.get('answer_value')
                    if value and row.get('question_type') == 'object':
                        try:
                            import ast
                            value = ast.literal_eval(value)
                        except Exception:
                            pass
                    elif value and row.get('question_type') == 'array':
                        try:
                            import ast
                            value = ast.literal_eval(value)
                        except Exception:
                            pass
                    # Only add if not already present
                    if not any(a['question_id'] == question_id for a in submissions[sub_id]['answers']):
                        submissions[sub_id]['answers'].append({
                            'question_id': question_id,
                            'value': value
                        })
            # Convert answers to Answer entities, submissions to Submission entities
            submission_objs = []
            for sub in submissions.values():
                answers = [Answer(submission_id=sub['submission_id'], question_id=a['question_id'], value=a['value']) for a in sub['answers']]
                submission_objs.append(Submission(
                    id=sub['submission_id'],
                    form_id=sub['form_id'],
                    patient_id=sub['patient_id'],
                    submitted_at=sub['submitted_at'],
                    answers=answers
                ))
            return {
                "forms": list(forms.values()),
                "questions": list(questions.values()),
                "submissions": submission_objs
            }
        finally:
            conn.close()
