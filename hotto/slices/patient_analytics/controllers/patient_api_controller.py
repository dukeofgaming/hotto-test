from flask import jsonify

class PatientApiController:
    def get_patients_without_insurance(self, request):
        return jsonify({}), 501  # 501 Not Implemented

    def get_clinical_data(self, request):
        return jsonify({}), 501  # 501 Not Implemented
