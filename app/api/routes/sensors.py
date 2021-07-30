
from flask import jsonify, Blueprint, request
from app.models import Sensor
from app.api.schemas import SensorSchema

# sensor_dummy_data = [
#     {
#         "internal_id": "azd345fff",
#         "name": "AZd8222",
#                 "type": "temp",
#                 "description": "Sensor 1",
#                 "data": {
#                     "value": "21.0",
#                     "unit": "°C"
#                 }
#     },
#     {
#         "internal_id": "azd345sdir",
#         "name": "AZd8222",
#                 "type": "temp",
#                 "description": "Sensor 2",
#                 "data": {
#                     "value": "21.1",
#                     "unit": "°C"
#                 }
#     }
# ]

api_sensor_bp = Blueprint(
    'api_sensor_bp', import_name=__name__, url_prefix='/sensors')


@api_sensor_bp.get('/')
def sensor_list():

    schema = SensorSchema()

    sensors = Sensor.query.all()

    return jsonify(schema.dump(sensors, many=True))
