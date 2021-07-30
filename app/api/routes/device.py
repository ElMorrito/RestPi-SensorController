from flask import Blueprint
from flask import json, request
from flask.json import jsonify
from app.api.controller.network_service import get_local_ip_address, hostname

api_device_bp = Blueprint(
    name="device_api", import_name=__name__, url_prefix='/device')


@api_device_bp.route('/', methods=['GET', 'PATCH'])
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
