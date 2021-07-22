# RestPi-SensorController

Use a Raspberry-Pi as a RestAPI-Webserver to retrieve data from its connected sensors.

## Usage of the API

### Get Controller Status

`GET {controller-ip}:{port}/api/Status`

Reponses:

* `200 OK` -> returns a Device Model in Json
* `404 NOT FOUND` -> Device is not reachable

```json
{
  "name": "Restpi raspberry",
  "location": "Main Store A456",
  "Station": "DUS",
  "ipv4_address": "192.168.0.1",
  "hostname": "raspberry",
}
```

#### Retrieve a List of connected Sensors

`GET {controller-ip}:{port}/api/sensors`

Responses:

* `200 OK` -> returns al List of Sensors.
* `404 Not Found` -> If device is not found.

Example:
```JSON
[
  {
    
      "id": "int -> representing the unique Id of a sensor",
      "internal_id": "string -> id give by the manufacturer",
      "name": "strin -> meaningful name for the Sensor",
      "type": "string -> representing the device type",
      "description": "string -> optional",
      "data": {
          "value": "Sensor specific data e.g. temprature",
          "unit": "Unit of the value e.g. Degrees C"
          }
}

  },
  {

  }
]
```
### Retrieve Sensordata by id

`GET http://{device-ip}:{port:int}/sensors/{id:int}`

```JSON
{
  "id": "int -> representing the unique Id of a sensor",
  "internal_id": "string -> id give by the manufacturer",
  "name": "strin -> meaningful name for the Sensor",
  "type": "string -> representing the device type",
  "description": "string -> optional",
  "data": {
      "value": "Sensor specific data e.g. temprature",
      "unit": "Unit of the value e.g. Degrees C"
      }
}
```

Responses:

* `200 OK` -> On Succees
* `404 Not Found` -> If Sensor is not found
