from hotto.modules.database.mysql import MySQLDatabase
from hotto.modules.survey.domain.entities.form import Form
from hotto.modules.survey.domain.entities.question import Question
from hotto.modules.database.mysql import MySQLDatabase

class ShowSurveysModel:
    def __init__(self):
        self.db = MySQLDatabase()

    def get_surveys_for_patient(self, patient_id: str):
        if not patient_id:
            raise ValueError("Missing patient_id")
        rows = self._fetch_rows(patient_id)
        return self._aggregate_surveys(rows)

    def _fetch_rows(self, patient_id: str):
        query = '''
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
        '''
        return self.db.fetch_all(query, (patient_id,))

    def _aggregate_surveys(self, rows):
        forms = self._aggregate_surveys_forms(rows)
        questions = self._aggregate_surveys_questions(rows)
        submissions = self._aggregate_surveys_submissions(rows)
        return {
            'forms': list(forms.values()),
            'questions': list(questions.values()),
            'submissions': submissions
        }

    def _aggregate_surveys_forms(self, rows):
        forms = {}
        for row in rows:
            form_id = row['form_id']
            if form_id not in forms:
                forms[form_id] = Form(id=form_id)
        return forms

    def _aggregate_surveys_questions(self, rows):
        questions = {}
        for row in rows:
            question_id = row['question_id']
            if question_id and question_id not in questions:
                questions[question_id] = Question(
                    id=question_id,
                    question_text=row.get('question_text', ''),
                    type=row.get('question_type', ''),
                    is_clinical=row.get('is_clinical', False)
                )
        return questions

    def _aggregate_surveys_submissions(self, rows):
        submissions = {}
        for row in rows:
            submission_id = row['submission_id']
            form_id = row['form_id']
            if submission_id not in submissions:
                submissions[submission_id] = {
                    'submission_id': submission_id,
                    'form_id': form_id,
                    'patient_id': row['patient_id'],
                    'submitted_at': row['submitted_at'],
                    'answers': []
                }
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
                question_id = row['question_id']
                if not any(a['question_id'] == question_id for a in submissions[submission_id]['answers']):
                    submissions[submission_id]['answers'].append({
                        'question_id': question_id,
                        'value': value
                    })
        # Ensure all submissions have 'submission_id' key (not 'id')
        submission_dicts = []
        for sub in submissions.values():
            if 'id' in sub:
                sub['submission_id'] = sub.pop('id')
            submission_dicts.append(sub)
        return submission_dicts
