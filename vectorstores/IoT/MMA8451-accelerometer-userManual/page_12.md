<a id='7458bfba-dbbc-47a1-a19b-23420682f7fa'></a>

COM70
Send

Adafruit MMA8451 test!
MMA8451 found!
Range = 8G
X: 45 Y: -672 Z: 734
X: 0.05 Y: -0.65 Z: 0.71 m/s^2
Portrait Up Front

X: 86 Y: -807 Z: 646
X: 0.07 Y: -0.77 Z: 0.62 m/s^2
Portrait Up Front

X: -767 Y: 75 Z: 656
X: -0.75 Y: 0.07 Z: 0.64 m/s^2
Landscape Left Front

X: -862 Y: 266 Z: 545
X: -0.85 Y: 0.26 Z: 0.54 m/s^2
Landscape Left Front

X: -880 Y: -268 Z: 10
X: -0.88 Y: -0.25 Z: 0.01 m/s^2
Landscape Left Front

X: 136 Y: -171 Z: -881
X: 0.14 Y: -0.17 Z: -0.88 m/s^2
Landscape Left Back

X: 536 Y: -96 Z: -805
X: 0.53 Y: -0.10 Z: -0.79 m/s^2
Landscape Right Back

X: 732 Y: 1107 Z: -161
X: 0.70 Y: 1.19 Z: -0.13 m/s^2
Portrait Down Back

option Autoscroll: [x]
option No line ending: [x]
option 9600 baud: [x]

<a id='eb0a1157-e310-4318-a218-7c173a5705c6'></a>

There's three lines of output from the sensor.

<a id='d0d89f7c-c02c-45ef-a6ef-abffa79ce4c0'></a>

Example for line 1:

<a id='6cc6b37a-670c-4e78-8af4-c2a55272f8ab'></a>

X: 45 Y: -672 Z: 734

<a id='8a754178-c418-434d-ab72-8efcf3efd0e7'></a>

This is the "raw count" data from the sensor, its a number from -8192 to 8191 (14 bits)
that measures over the set range. The range can be set to 2G, 4G or 8G

<a id='e74f65cb-7cdc-4180-ae38-10459f86e7d9'></a>

Example for line 2:
X: -0.07 Y: 0.09 Z: 9.8 m/s^2

<a id='4ea06c18-a0fb-4b9c-84a8-0d61c92b6a47'></a>

This is the Adafruit_Sensor'ified nice output which is in m/s*s, the SI units for measuring acceleration. No matter what the range is set to, it will give you the same units, so its nice to use this instead of mucking with the raw counts. (Note that the screenshot above has the m/s^2 divided by 10, you can ignore that typo :)

<a id='1d897519-4040-44f5-81f2-a0dc47de4535'></a>

 Adafruit Industries

<a id='4403bc10-d7d6-4f13-b748-5e3aef678a4f'></a>

Page 12 of 21