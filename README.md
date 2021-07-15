# RestPi-SensorController
Use a Raspberry-Pi as a RestAPI-Webserver to retrieve data from its connected sensors.

## Models
All Models are represented as JSON.

### Controller Model

```json
{
  "id": "int -> representing the unique Id of a Device",
  "controller_name": "string -> default vlaue is Restp+id",
  "Sensors" : "List of Sensors"
}
```

### Sensor Model

```JSON
{
  "id": "int -> representing the unique Id of a sensor",
  "internal_id": "string -> id give by the manufacturer",
  "name": "meaningful name for the Sensor",
  "type": "string -> representing the device type (e.g.TemperatureSensor)",
  "description": "string -> optional",
  "data": {
      "value": "Sensor specific data e.g. temprature" 
      }
}
```

## Usage of the API

### Get Controller Status

`GET {controller-ip}:{port}/api/Status`


Reponses:
* `200 OK` -> returns a Device Model in Json
* `404 NOT FOUND` -> Device is not reachable


#### Retrieve a List of connected Sensors
 
`GET {controller-ip}:{port}/api/sensors`

Responses:
+ `200 OK` -> returns al List of Sensors.
+ `404 Not Found` -> If device is not found

### Retrieve Sensordata by id

`GET http://{device-ip}:{port:int}/sensors/{id:int}`

Responses:
+ `200 OK` -> On Succees
+ `404 Not Found` -> If Sensor is not found
