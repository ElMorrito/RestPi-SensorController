from flask import Flask, request
import socket
from sys import platform
from subprocess import check_output


app = Flask("__name__")


@app.route("/")
def index():
    return "Hello User"


print(platform)
# Get Hostname and Ip Address
hostname = socket.gethostname()

if platform == "linux" or platform == "linux2":
    local_ip_address = check_output("hostname", "-I")
else:
    local_ip_address = socket.gethostbyname(hostname)


print(hostname)
print('IP on platform "{}" is : {}'.format(platform, local_ip_address))


@app.route('/api/info', methods=['GET'])
def device_settings():
    return {
        'id': 1,
        'host_name': hostname,
        'ip_address': local_ip_address,
        'status': 'ok',
        'location': 'Main Store'
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
