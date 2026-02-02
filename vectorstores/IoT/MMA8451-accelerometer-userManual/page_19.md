<a id='14a61527-a503-44a7-9561-946e08129e0c'></a>

The following is a complete example that will print the orientation and acceleration of the sensor every second. Save this as **code.py** on your board and open the REPL to see the output.

<a id='ac3fb886-d1b3-47ec-94df-afe687ce83cc'></a>

Full Example Code

<a id='422eb9e8-c566-4ddf-afb9-79590243df7e'></a>

# SPDX-FileCopyrightText: 2018 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

<a id='933d3b4f-ee65-4243-966f-1459526aa43b'></a>

# Simple demo of reading the MMA8451 orientation every second.import timeimport boardimport adafruit_mma8451

<a id='ef5bb1ce-1391-4edd-a61f-7700f229e8dc'></a>

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a
microcontroller

# Initialize MMA8451 module.
sensor = adafruit_mma8451.MMA8451(i2c)
# Optionally change the address if it's not the default:
# sensor = adafruit_mma8451.MMA8451(i2c, address=0x1C)

# Optionally change the range from its default of +/-4G:
# sensor.range = adafruit_mma8451.RANGE_2G # +/- 2G
# sensor.range = adafruit_mma8451.RANGE_4G # +/- 4G (default)
# sensor.range = adafruit_mma8451.RANGE_8G # +/- 8G

# Optionally change the data rate from its default of 800hz:
# sensor.data_rate = adafruit_mma8451.DATARATE_800HZ # 800Hz (default)
# sensor.data_rate = adafruit_mma8451.DATARATE_400HZ # 400Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_200HZ # 200Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_100HZ # 100Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_50HZ # 50Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_12_5HZ # 12.5Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_6_25HZ # 6.25Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_1_56HZ # 1.56Hz

<a id='4d4d4872-54b9-4795-a8b9-41d1ca10d924'></a>

```python
# Main loop to print the acceleration and orientation every second.
while True:
    x, y, z = sensor.acceleration
    print(
        "Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2".format(x, y,
        z)
    )
```

<a id='d9ed96ed-0b41-4796-ac58-1168a20bedda'></a>

orientation = sensor.orientation
# Orientation is one of these values:
# - PL_PUF: Portrait, up, front
# - PL_PUB: Portrait, up, back
# - PL_PDF: Portrait, down, front
# - PL_PDB: Portrait, down, back
# - PL_LRF: Landscape, right, front
# - PL_LRB: Landscape, right, back
# - PL_LLF: Landscape, left, front
# - PL_LLB: Landscape, left, back
print("Orientation: ", end="")
if orientation == adafruit_mma8451.PL_PUF:
    print("Portrait, up, front")
elif orientation == adafruit_mma8451.PL_PUB:
    print("Portrait, up, back")
elif orientation == adafruit_mma8451.PL_PDF:

<a id='77018818-3958-4ad5-9b27-00383319e64a'></a>

Adafruit Industries

<a id='0cc896fc-cd3a-4e4a-922d-d455fc9364a5'></a>

Page 19 of 21