from flask import Blueprint
from flask import jsonify

from service import sensor_service


api_sensor_bp = Blueprint(
    'api_sensor_bp', import_name=__name__, url_prefix='/sensors')


@api_sensor_bp.get('/')
def sensor_list():
    sensors = sensor_service.get_temp_sensors()
    return jsonify(*sensors)
