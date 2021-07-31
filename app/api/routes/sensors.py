
from flask import jsonify, Blueprint, request
from app.database.models import Sensor
from app.api.schemas import SensorSchema

api_sensor_bp = Blueprint(
    'api_sensor_bp', import_name=__name__, url_prefix='/sensors')


@api_sensor_bp.get('/')
def sensor_list():

    schema = SensorSchema()

    sensors = Sensor.query.all()

    return jsonify(schema.dump(sensors, many=True))
