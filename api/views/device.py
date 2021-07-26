from flask import Blueprint
from flask import json, request
from flask.json import jsonify
from service.network_service import hostname, get_local_ip_address

api_device_bp = Blueprint(
    name="device_api", import_name=__name__, url_prefix='/device')


@api_device_bp.route('/', methods=['GET', 'PATCH'])
def device_settings():

    if request.method == 'GET':
        return {
            "name": "Restpi raspberry",
            "location": "Main Store A456",
            "Station": "DUS",
            "ipv4_address": get_local_ip_address(),
            "hostname": hostname,
        }
    else:
        pass
