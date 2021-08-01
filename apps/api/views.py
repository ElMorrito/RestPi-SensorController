import markdown
import os
import random
from flask import jsonify, Blueprint, request

from database.models import Sensor
from apps.api.models import SensorSchema

from apps.utils import get_local_ip_address, hostname

api_bp = Blueprint(name='apiV1', import_name=__name__, url_prefix='/api')


@api_bp.route("/docs")
def index():
    with open(os.path.dirname(api_bp.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


@api_bp.route('/device', methods=['GET', 'PATCH'])
def device_info():

    if request.method == 'GET':
        return jsonify({
            "name": "Restpi raspberry",
            "location": "Main Store A456",
            "Station": "DUS",
            "ipv4_address": get_local_ip_address(),
            "hostname": hostname,
        }), 200

    else:
        pass


@api_bp.get('/sensors')
def sensor_list():

    sensors = Sensor.query.all()

    if not sensors:
        return jsonify({'message': 'No sensors in list'}), 204

    sensors_json = SensorSchema().dump(sensors, many=True)

    for s in sensors_json:
        dummy_temp = random.randrange(17, 24)
        s['data'] = {
            'value': dummy_temp,
            'unit': '°C'
        }
        s['status_code'] = 'OK'

    return jsonify(sensors_json), 200
