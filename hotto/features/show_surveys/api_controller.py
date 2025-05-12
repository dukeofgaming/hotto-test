from flask import jsonify

from http import HTTPStatus

from hotto.features.show_surveys.model import ShowSurveysModel


class ShowSurveysApiController:
    def __init__(self):
        self.model = ShowSurveysModel()

    def get_surveys_for_patient(self, request):
        patient_id = request.args.get("patient_id")
        try:
            result = self.model.get_surveys_for_patient(patient_id)
            return jsonify(result), HTTPStatus.OK
        except ValueError as err:
            return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST
        except Exception as err:
            return jsonify({"error": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR
