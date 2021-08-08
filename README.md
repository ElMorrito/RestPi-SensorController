# RestPi-SensorController

Use a Raspberry-Pi as a RestAPI-Webserver to retrieve data from its connected sensors.


## Usage of the API

### API errors


Response errors will have the form:

```json
{
    "message" : "Short error description",
    "detail:": "A detailed message about the error."
}
```

### Get device status

Use this route to get information about the SensorController itself.

`GET /api/v1/device`

Responses:

* `200 OK` -> Returns basic device in Json
* `404 NOT FOUND` -> Device is not reachable

Example:

```json
{
  "name": "Restpi Controller 1",
  "location": "Main Store A456",
  "station": "DUS",
  "ipv4_address": "192.168.0.1",
  "hostname": "raspberry",
}
```

### Modify Device Info

`PATCH /api/v1/device`

Values:

* `string`: station
* `string`: location
* `string`: name


Responses:

* `201 UPDATED` -> Returns nothing but the response Code
* `400 NOT FOUND` -> Device is not reachable



### Retrieve Sensor data

`GET /api/v1/sensors/{id:int}`

Example:

```JSON
{
  "id": "int(representing the unique Id of a sensor)",
  "internal_id": "string(id give by the manufacturer)",
  "name": "string(meaningful name for the Sensor)",
  "type": "string(representing the device type)",
  "description": "string(optional description)",
  "status": "string(information of Sensor Status. Default is OK)",
  "data": {
      "value": "float(Sensor specific data e.g. temperature. 2 digits)",
      "unit": "string(Unit of the value e.g. Degrees C)"
      }
}
```

Responses:

* `200 OK` -> On Succees
* `404 Not Found` -> If Sensor is not found

#### Retrieve a list of connected Sensors

`GET /api/v1/sensors`

Responses:

* `200 OK` -> Returns a list of Sensors.
* `404 Not Found` -> If device is not found.

Example:

```JSON
[
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
```
