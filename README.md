# RestPi-SensorController

Use a Raspberry-Pi as a RestAPI-Webserver to retrieve data from its connected sensors.

## Before first use


1. Install image on SD-Card.
2. Power up the device and Connect rpi and establish a Ethernet connection inside the network.
3. SSH via Terminal or Power shell and enter password

```shell
ssh pi@raspberrypi.local
 ```

4.Setup a static IP address.

## Usage of the API

All Errors will have the form:

```json
{
    "message" : " ' Short error descritpion ': 'A detailed message about the error and possible causes.'"
}
```

### Get device status

`GET /api/device`

Responses:

* `200 OK` -> Returns basic device in Json
* `404 NOT FOUND` -> Device is not reachable

Example:

```json
{
  "name": "Restpi raspberry",
  "location": "Main Store A456",
  "Station": "DUS",
  "ipv4_address": "192.168.0.1",
  "hostname": "raspberry",
}
```

### Modify Device Info

`PATCH /api/device`

Allowed values:

* `string`: station
* `string`: location
* `string`: name


Responses:

* `201 UPDATED` -> Returns nothing but the response Code
* `400 NOT FOUND` -> Device is not reachable



### Retrieve Sensor data

`GET /api/sensors/{id:int}`

Example:

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

#### Retrieve a list of connected Sensors

`GET /api/sensors`

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
