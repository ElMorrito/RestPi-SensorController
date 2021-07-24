from flask import Blueprint
from flask import json, request
from flask.json import jsonify
from socket import gethostbyname, gethostname
from sys import platform
from subprocess import check_output


api_device_bp = Blueprint(
    name="device_api", import_name=__name__, url_prefix='/device')

# Get Hostname and Ip Address.
# gethostbyname funtion does only return 127.0.1.1 if platfrom is linux,
# so check for platfrom first.
hostname = gethostname()

if platform == "linux" or platform == "linux2":
    output = check_output(
        ['hostname', '-s', '-I']).decode('utf-8')[:-1]
    local_ip_address = output.split(" ")[0]
else:
    local_ip_address = gethostbyname(hostname)

# print(platform)
# print(hostname)
# print(local_ip_address)


@api_device_bp.route('/', methods=['GET', 'PATCH'])
def device_settings():

    if request.method == 'GET':
        return {
            "name": "Restpi raspberry",
            "location": "Main Store A456",
            "Station": "DUS",
            "ipv4_address": local_ip_address,
            "hostname": hostname,
        }
    else:
        pass
