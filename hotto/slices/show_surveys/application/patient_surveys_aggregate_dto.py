class PatientSurveysAggregateDTO:
    def __init__(self, aggregate_asdict):
        self.data = self._process_aggregate(aggregate_asdict)

    def _process_aggregate(self, aggregate):
        return {
            "forms": [self._rename_form(form) for form in aggregate.get("forms", [])],
            "questions": [self._rename_question(question) for question in aggregate.get("questions", [])],
            "submissions": [self._rename_submission(submission) for submission in aggregate.get("submissions", [])],
        }

    def _rename_form(self, form):
        # No renaming needed for forms, but can add here if needed
        return form

    def _rename_question(self, question):
        # No renaming needed for questions, but can add here if needed
        return question

    def _rename_submission(self, submission):
        submission_dict = dict(submission)
        submission_dict['submission_id'] = submission_dict.pop('id', None)
        if 'answers' in submission_dict:
            submission_dict['answers'] = [self._rename_answer(answer) for answer in submission_dict['answers']]
        return submission_dict

    def _rename_answer(self, answer):
        # Only keep 'question_id' and 'value', do not try to rename 'id'
        return {
            "question_id": answer.get("question_id"),
            "value": answer.get("value")
        }

    def to_dict(self):
        return self.data
