from typing import List, Dict, Any
from hotto.modules.survey.domain.entities.patient import Patient
from hotto.modules.timestamp.domain.timestamp_helper import TimestampHelper
from hotto.modules.database.mysql import MySQLDatabase

class InvalidPatientAnalyticsRequest(Exception):
    pass

class PatientAnalyticsModel:
    def __init__(self):
        self.db = MySQLDatabase()

    def get_patients_without_insurance(self) -> List[Patient]:
        query = '''
            SELECT DISTINCT patients.id
            FROM patients
            LEFT JOIN submissions ON patients.id = submissions.patient_id
            LEFT JOIN answers ON answers.submission_id = submissions.id
            WHERE answers.question_id = 'Has Insurance?' AND LOWER(answers.value) NOT IN ('yes', 'true', '1')
        '''
        rows = self.db.fetch_all(query)
        patient_ids = [row['id'] for row in rows]
        patients = [Patient(id=pid) for pid in patient_ids]
        if not patients:
            raise InvalidPatientAnalyticsRequest("No patient data available.")
        return patients

    def get_clinical_data_for_patient(self, patient_id: str) -> List[Dict[str, Any]]:
        if not patient_id:
            raise InvalidPatientAnalyticsRequest("Missing patient_id.")
        query = '''
            SELECT
                answers.id AS answer_id,
                submissions.form_id,
                answers.question_id,
                answers.submission_id,
                submissions.patient_id,
                submissions.submitted_at,
                answers.value,
                questions.is_clinical
            FROM submissions
            LEFT JOIN answers ON answers.submission_id = submissions.id
            LEFT JOIN questions ON answers.question_id = questions.id
            WHERE submissions.patient_id = %s AND questions.is_clinical = TRUE
            ORDER BY submissions.submitted_at DESC, submissions.id DESC
        '''
        data = self.db.fetch_all(query, (patient_id,))
        for item in data:
            if "submitted_at" in item and item["submitted_at"] is not None:
                item["submitted_at"] = TimestampHelper.unix_to_iso8601(item["submitted_at"])
            if "is_clinical" in item:
                item["is_clinical"] = bool(item["is_clinical"])
        if not data:
            raise InvalidPatientAnalyticsRequest(f"No clinical data for patient_id: {patient_id}")
        return data
