from flask import Flask, request
import socket
from sys import platform
from subprocess import check_output


app = Flask("__name__")


@app.route("/")
def index():
    return "Hello User"



# Get Hostname and Ip Address.
# gethostbyname funtion does only return 127.0.1.1 if platfrom is linux,
# so check for platfrom first.
hostname = socket.gethostname()

if platform == "linux" or platform == "linux2":
    output = check_output(
        ['hostname', '-s', '-I']).decode('utf-8')[:-1]
    local_ip_address = output.split(" ")[0]
else:
    local_ip_address = socket.gethostbyname(hostname)

# print(platform)
# print(hostname)
# print(local_ip_address)


@app.route('/api/info', methods=['GET'])
def device_settings():
    return {
        'external_id': 1,
        'host_name': hostname,
        'ipv4_address': local_ip_address.split(" ")[0],
        'name': 'Rpi',
        'location': 'Main Store'
    }


if __name__ == "__main__":
    app.run( debug=True)
