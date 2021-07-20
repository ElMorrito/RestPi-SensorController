from flask import Flask, request
import socket
import subprocess

app = Flask("__name__")


@app.route("/")
def index():
    return "Hello User"


# Get Hostname and Ip Address
hostname = socket.gethostname()
try:
    local_ip_address = subprocess.call('hostname', '-I')[0]

except:
    local_ip_address = socket.gethostbyname(hostname)

print(local_ip_address)


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
