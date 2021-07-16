from flask import Flask, request
import socket


app = Flask("__name__")


@app.route("/")
def index():
    return "Hello User"


# Get Hostname and Ip Address
hostname = socket.gethostname()
local_ip_address = socket.gethostbyname(hostname)


@app.route('/api/settings', methods=['GET', 'PATCH'])
def device_settings():
    if request.method == 'PATCH':
        return "not implemented"
    else:
        return {
            'id': 1,
            'host_name': hostname,
            'ip_address': local_ip_address,
            'logging': False,
            'status': 'ok',
            'location': 'Main Store'
        }


if __name__ == "__main__":
    app.run(debug=True)
