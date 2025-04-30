from hotto.modules.survey.domain.entities.submission import Submission
from hotto.modules.survey.domain.repositories.submission_repository import SubmissionRepository

ALLOWED_QUESTION_TYPES = {'text', 'date', 'boolean', 'object', 'array', 'number'}

class SaveSubmissionUseCase:
    def __init__(self, submission_repository: SubmissionRepository):
        self.submission_repository = submission_repository

    def save_submission(self, submission: Submission, raw_answers: dict):
        """
        Args:
            submission (Submission): The Submission entity to save.
            raw_answers (dict): The original answers dict from the incoming JSON (to get question type info).

        Returns:
            tuple: (response_dict, status_code)
                - On success: ({"message": "Submission saved successfully"}, 201)
                - On validation error: ({"error": f"Invalid question type: ..."}, 400)
        """
        question_text_to_answer = {
            ans['question']: ans
            for ans in raw_answers.values()
        }
        for answer_obj in submission.answers:
            answer_dict = question_text_to_answer[answer_obj.question_id]
            question_type = answer_dict.get('type')
            if question_type not in ALLOWED_QUESTION_TYPES:
                return {"error": f"Invalid question type: {question_type}"}, 400

        # Save submission and answers using repository
        self.submission_repository.save(submission)
        return {"message": "Submission saved successfully"}, 201
