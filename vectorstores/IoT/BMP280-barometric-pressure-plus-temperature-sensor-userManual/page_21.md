<a id='d2f7a562-a012-4057-a25e-6acdcc30473c'></a>

Or if you're using a SPI connection run this code instead to setup the SPI connection
and sensor:

```
import board
import digitalio
import adafruit_bmp280
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
sensor = adafruit_bmp280.Adafruit_BMP280_SPI(spi, cs)
```

<a id='73a58dc7-65ee-4ecf-99bb-e1da3728b44e'></a>

Now you're ready to read values from the sensor using any of these properties:

<a id='d7d367c0-d735-43c4-966d-def094ee2dcc'></a>

* **temperature** - The sensor temperature in degrees Celsius.
* **pressure** - The pressure in hPa.
* **altitude** - The altitude in meters.

<a id='07edf083-883d-467a-885f-4ed58c33773a'></a>

For example to print temperature and pressure:

<a id='b3b93fba-44d3-43e9-b119-3505d91e98ff'></a>

```python
print('Temperature: {} degrees C'.format(sensor.temperature))
print('Pressure: {}hPa'.format(sensor.pressure))
```

<a id='c239f983-e00b-4af8-851b-a96e3b0cedde'></a>

```
>>> print('Temperature: {} degrees C'.format(sensor.temperature))
Temperature: 21.0874 degrees C
>>> print('Pressure: {}hPa'.format(sensor.pressure))
Pressure: 1012.32hPa
>>>
```

<a id='381b2af2-0069-4cf2-9e73-816fef1c042c'></a>

For altitude you'll want to set the pressure at sea level for your location to get the most accurate measure (remember these sensors can only infer altitude based on pressure and need a set calibration point). Look at your local weather report for a pressure at sea level reading and set the **seaLevelhPA** property:

<a id='00d764b5-8ebb-4f60-b6f8-6ce613c38268'></a>

```
sensor.sea_level_pressure = 1013.25
```

<a id='456a272e-6b22-4074-9c10-6f51a2a84bb1'></a>

Then read the altitude property for a more accurate altitude reading (but remember this altitude will fluctuate based on atmospheric pressure changes!):

<a id='f2031896-f1e5-497f-a400-dc703bcfa12c'></a>

```python
print('Altitude: {} meters'.format(sensor.altitude))
```

<a id='784ac68f-e7aa-4ffb-af4c-add35ff18efd'></a>

<::A screenshot of a PuTTY terminal window titled "COM11 - PuTTY". The terminal displays Python code execution and its output. The content shown is:

>>>
>>> sensor.sea_level_pressure = 1013.25
>>> print('Altitude: {} meters'.format(sensor.altitude))
Altitude: 65.8983 meters
>>>
: terminal::>

<a id='5725a28d-ef58-4621-802f-4e112e03afc4'></a>

That's all there is to using the BMP280 sensor with CircuitPython!

<a id='852be16f-505f-4528-a599-84277e33bc34'></a>

© Adafruit Industries

<a id='f4b5dec2-4379-41c6-ba33-dd1933eae22b'></a>

Page 22 of 34