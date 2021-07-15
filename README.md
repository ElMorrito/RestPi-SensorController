# RestPi-SensorController
Use a Raspberry-Pi as a RestAPI-Webserver to retrieve data from its connected sensors.

## Models
All Models are represented as JSON.

### Sensor Model

```JSON
{
  "id": "int -> representing the unique Id of a sensor",
  "type": "string -> representing the device type (Temprature, Lux, Huminidty, ...)",
  "loc": "string -> location of the Device",
  "data": {
      "value_": "Sensor specific data e.g. temprature" 
      }
}
```

### Device Model


## Get all connected Sensors
Retrieve a list of all connected Sensors.
 
Method:`GET`

Route: http://{device-ip}:{port}/sensors

Responses:
+ `200 Success` -> On Succees
+ `404 Not Found` -> If device is not found

## Get Sensor by id

