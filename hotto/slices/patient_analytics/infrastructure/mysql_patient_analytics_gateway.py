from typing import List, Dict, Any
from hotto.slices.patient_analytics.application.patient_analytics_gateway import PatientAnalyticsGateway
import mysql.connector
import os

class MySQLPatientAnalyticsGateway(PatientAnalyticsGateway):
    def __init__(self, db_config=None):
        if db_config is None:
            db_config = {
                'host': os.getenv('DB_HOST', 'localhost'),
                'user': os.getenv('DB_USER', 'root'),
                'password': os.getenv('DB_PASSWORD', 'password'),
                'database': os.getenv('DB_NAME', 'submissions_db'),
            }
        self.db_config = db_config

    def get_patients_without_insurance(self) -> List[str]:
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor(dictionary=True)
        query = '''
            SELECT DISTINCT patients.id
            FROM patients
            LEFT JOIN submissions ON patients.id = submissions.patient_id
            LEFT JOIN answers ON answers.submission_id = submissions.id
            WHERE answers.question_id = 'Has Insurance?' AND LOWER(answers.value) NOT IN ('yes', 'true', '1')
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        patient_ids = [row['id'] for row in rows]
        cursor.close()
        conn.close()
        return patient_ids

    def get_clinical_data_for_patient(self, patient_id: str) -> List[Dict[str, Any]]:
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor(dictionary=True)
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
        cursor.execute(query, (patient_id,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
