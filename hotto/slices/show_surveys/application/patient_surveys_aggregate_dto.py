class PatientSurveysAggregateDTO:
    def __init__(self, aggregate_asdict):
        self.data = self._process_aggregate(aggregate_asdict)

    def _process_aggregate(self, agg):
        return {
            "forms": [self._rename_form(f) for f in agg.get("forms", [])],
            "questions": [self._rename_question(q) for q in agg.get("questions", [])],
            "submissions": [self._rename_submission(s) for s in agg.get("submissions", [])],
        }

    def _rename_form(self, form):
        # No renaming needed for forms, but can add here if needed
        return form

    def _rename_question(self, question):
        # No renaming needed for questions, but can add here if needed
        return question

    def _rename_submission(self, submission):
        s = dict(submission)
        s['submission_id'] = s.pop('id', None)
        if 'answers' in s:
            s['answers'] = [self._rename_answer(a) for a in s['answers']]
        return s

    def _rename_answer(self, answer):
        # Only keep 'question_id' and 'value', do not try to rename 'id'
        return {
            "question_id": answer.get("question_id"),
            "value": answer.get("value")
        }

    def to_dict(self):
        return self.data
