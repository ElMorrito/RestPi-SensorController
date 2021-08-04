from socket import gethostbyname, gethostname
from sys import platform
from subprocess import check_output
import random

hostname = gethostname()


def get_local_ip_address():
    '''Get IPv4-Adress of device .

    This function can be used for OSX, LINUX and WINDOWS.'''
    # Ggethostbyname funtion does only return 127.0.1.1 if platfrom is linux,
    # so check for platfrom first.
    if platform == "linux" or platform == "linux2":
        output = check_output(
            ['hostname', '-s', '-I']).decode('utf-8')[:-1]
        return output.split(" ")[0]
    else:
        return gethostbyname(hostname)


def get_temperature_data(sensor_id: str = None) -> dict:

    dummy_temp = random.uniform(10.1, 25.9)

    data = {
        'value': f'{dummy_temp:.4f}',
        'unit': '°C'
    }
    return data
