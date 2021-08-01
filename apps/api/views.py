import markdown
import os
import random
from flask import jsonify, Blueprint, request, abort

from apps.app.models import Sensor
from apps.api.models import SensorSchema

from apps.utils import get_local_ip_address, hostname

api_bp = Blueprint(name='apiV1', import_name=__name__, url_prefix='/api')


@api_bp.app_errorhandler(500)
@api_bp.app_errorhandler(400)
def bad_api_reguest(error):
    return jsonify(message=str(error)), error.code


@api_bp.route("/docs")
def index():
    with open(os.path.dirname(api_bp.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


device_json = {
    "name": "Restpi raspberry",
    "location": "Main Store A456",
    "station": "DUS",
    "ipv4_address": get_local_ip_address(),
    "hostname": hostname,
}


@api_bp.route('/device', methods=['GET', 'PATCH'])
def device_info():
    if request.method == 'GET':
        try:
            return jsonify(device_json), 200
        except:
            abort(500)

    else:
        keys = request.get_json().keys()

        for key in keys:
            if not key in ['name', 'location', 'station']:
                abort(400,
                      'Key <{}> is not a valid atrribute. Make sure only valid keys are used and no spelling mistakes are present'.format(str(key)))

        device_json[key] = request.get_json()[key]

        return jsonify(device_json), 201


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
