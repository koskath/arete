<a id='eb05be8d-72f1-4ee7-adf9-fbba85932217'></a>

* adafruit_mma8451.PL_LLF: Landscape, left, front
* adafruit_mma8451.PL_LLB: Landscape, left, back

<a id='46252fc0-4a26-4f32-baa8-11d3190a662c'></a>

```
x, y, z = sensor.acceleration
print('Acceleration: x={0:0.3f} m/s^2 y={1:0.3f} m/s^2 z={2:0.3f} m/s^2'.format(x,
y, z))
orientation = sensor.orientation
print('Orientation: {0}'.format(orientation))
```

<a id='90638ca5-6aa9-471c-ab77-e2349628baf5'></a>

```
>>> x, y, z = sensor.acceleration
>>> print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
Acceleration: x=-1.475m/s^2 y=-1.820m/s^2 z=9.357m/s^2
>>> orientation = sensor.orientation
>>> print('Orientation: {0}'.format(orientation))
Orientation: 0
>>>
```

<a id='54f4399f-7274-4c49-b509-43c6089c658d'></a>

In addition there are a few properties you can read and write to change the behavior of the sensor:

<a id='7c51c616-95a5-45e5-b0a9-5455091239fa'></a>

- range - The range of the accelerometer measurements. This must be a value of:
  * adafruit_mma8451.RANGE_2G: +/- 2G range
  * adafruit_mma8451.RANGE_4G: +/- 4G range (the default)
  * adafruit_mma8451.RANGE_8G: +/- 8G range
- data_rate - The rate at which the sensor measures acceleration data. This must be a value of:
  * adafruit_mma8451.DATARATE_800HZ: 800hz
  * adafruit_mma8451.DATARATE_400HZ: 400hz
  * adafruit_mma8451.DATARATE_200HZ: 200hz
  * adafruit_mma8451.DATARATE_100HZ: 100hz
  * adafruit_mma8451.DATARATE_50HZ: 50hz
  * adafruit_mma8451.DATARATE_12_5HZ: 12.5hz
  * adafruit_mma8451.DATARATE_6_25HZ: 6.25hz
  * adafruit_mma8451.DATARATE_1_56HZ: 1.56hz

<a id='047ee490-df08-4400-9abd-788143193270'></a>

sensor.range = adafruit_mma8451.RANGE_8G
sensor.data_rate = adafruit_mma8451.DATARATE_400HZ

<a id='30075db3-7b28-4402-9da1-74548893c6e1'></a>

>>> sensor.range = adafruit_mma8451.RANGE_8G
>>> sensor.data_rate = adafruit_mma8451.DATARATE_400HZ
>>> x, y, z = sensor.acceleration
>>> print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
Acceleration: x=-1.456m/s^2 y=-1.810m/s^2 z=9.385m/s^2
>>> orientation = sensor.orientation
>>> print('Orientation: {0}'.format(orientation))
Orientation: 0
>>>

<a id='43938730-72bc-40ff-9d36-f640cc607da2'></a>

That's all there is to using the MMA8451 with CircuitPython!

<a id='700704f1-2540-4f0c-ae70-a101d28f9cb3'></a>

© Adafruit Industries

<a id='7013d550-f2a5-4927-a7c2-15239ff938f0'></a>

Page 18 of 21