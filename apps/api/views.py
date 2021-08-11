import markdown
from flask import jsonify, Blueprint, request, abort
from models import Sensor
from apps.api.schema import SensorSchema
from apps.utils import get_local_ip_address, get_temperature_data, hostname
from pathlib import Path

api_bp = Blueprint(name='api', import_name=__name__, url_prefix='/api/v1')


@api_bp.app_errorhandler(500)
@api_bp.app_errorhandler(400)
def bad_api_reguest(error):

    message, detail = str(error).split(":")
    print(message)
    print(detail)

    return jsonify(message=message, detail=detail), error.code


@api_bp.route("/docs")
def index():
    """Route for API documentation

    This Route provides a simple documantation about how to use the api,
    by rendering the README.md
     file to HTML.
    """
    base_path = Path().absolute()

    with open(base_path / 'README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


@api_bp.route('/device', methods=['GET', 'PATCH'])
def device_info():

    device_json = {
        "name": "RestPi",
        "location": "Main Store A456",
        "station": "DUS",
        "ipv4_address": get_local_ip_address(),
        "hostname": hostname,
    }

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
                      f'Key <{key}> is not a valid atrribute. Make sure only valid keys are used and no spelling mistakes are present')

        device_json[key] = request.get_json()[key]

        return jsonify(device_json), 201


@api_bp.get('/sensors')
def sensor_list():

    sensors = Sensor.query.all()
    sensors_json = SensorSchema().dump(sensors, many=True)

    if not sensors:
        return jsonify(sensors_json), 200

    # add data to the sensors
    for s in sensors_json:
        s['data'] = get_temperature_data()
        s['status_code'] = "OK"

    return jsonify(sensors_json), 200
