
sensor_dummy_data = [
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


def get_temp_sensors(query: str = None):
    return sensor_dummy_data
