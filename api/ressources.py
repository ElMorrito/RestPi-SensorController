from flask import Blueprint
from flask import json, request
from flask.json import jsonify
from socket import gethostbyname, gethostname
from sys import platform
from subprocess import check_output
import markdown
import os

api_blueprint = Blueprint(name='api', import_name=__name__, url_prefix='/api')

hostname = gethostname()

if platform == "linux" or platform == "linux2":
    output = check_output(
        ['hostname', '-s', '-I']).decode('utf-8')[:-1]
    local_ip_address = output.split(" ")[0]
else:
    local_ip_address = gethostbyname(hostname)


@api_blueprint.route("/")
def index():
    with open(os.path.dirname(api_blueprint.root_path) + '/README.md', 'r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


@api_blueprint.route('/settings', methods=['GET', 'PATCH'])
def device_settings():

    if request.method == 'GET':
        return {
            "name": "Restpi raspberry",
            "location": "Main Store A456",
            "Station": "DUS",
            "ipv4_address": "192.168.0.1",
            "hostname": "raspberry",
        }
    else:
        pass


@api_blueprint.route('/sensors', methods=['GET'])
def sensor_list():
    return jsonify(
        [
            {
                "internal_id": "azd345fff",
                "name": "AZd8222",
                "type": "temp",
                "description": "Sensor 1",
                "data": {
                    "value": "21.0",
                    "unit": "°C"
                }
            },
            {
                "internal_id": "azd345sdir",
                "name": "AZd8222",
                "type": "temp",
                "description": "Sensor 2",
                "data": {
                    "value": "21.1",
                    "unit": "°C"
                }
            }
        ]

    )
