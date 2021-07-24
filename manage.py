import api
import os
from flask import Flask
import markdown

from api.main import api_blueprint
from app.views import app_blueprint

app = Flask("__name__")

app.register_blueprint(app_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(debug=True)


# Get Hostname and Ip Address.
# gethostbyname funtion does only return 127.0.1.1 if platfrom is linux,
# so check for platfrom first.
# hostname = socket.gethostname()

# if platform == "linux" or platform == "linux2":
#     output = check_output(
#         ['hostname', '-s', '-I']).decode('utf-8')[:-1]
#     local_ip_address = output.split(" ")[0]
# else:
    # local_ip_address = socket.gethostbyname(hostname)

# print(platform)
# print(hostname)
# print(local_ip_address)


# @app.route('/api/info', methods=['GET'])
# def device_settings():
#     return {
#         'external_id': 1,
#         'host_name': hostname,
#         'ipv4_address': local_ip_address.split(" ")[0],
#         'name': 'Rpi',
#         'location': 'Main Store'
#     }
