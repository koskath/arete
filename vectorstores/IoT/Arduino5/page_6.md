<a id='664d646c-672f-4c78-bacf-60af8e9c0c6c'></a>

12/4/25, 2:51 PM

<a id='fdec619b-d5dd-4574-9d97-56714b8c0320'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='22709aed-1af0-4176-b3ef-2c67f59f98b4'></a>

ARDUINODOCS

<a id='9410bd0c-a306-4a1d-82e6-0689cb7665fc'></a>

the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it.

2. Now, we need to install the libraries needed. If we are using the Cloud Editor, there is no need to install anything. If we are using an offline editor, simply go to **Tools** > **Manage libraries**.., and search for **Arduino_MKRENV** and install it.

<a id='dc31e536-43ea-48f5-9005-0ef143b02dbb'></a>

3. We can now take a look at some of the core functions of this sketch:
`ENV.begin()` - initializes the library.
`ENV.readTemperature()` - returns temperature.
`ENV.readHumidity()` - returns relative humidity.
`ENV.readPressure()` - returns atmospheric pressure.
`ENV.readIlluminance()` - returns LUX.
`ENV.readUVA()` - returns UVA (only for older versions).
`ENV.readUVB()` - returns UVB (only for older versions).
`ENV.readUVIndex()` - calculates UV index (only for older versions).

<a id='49a54d30-c309-4471-99a6-7f8992235ba6'></a>

The sketch can be found in the snippet
below, or in the **Arduino_MKRENV** library, in
**File > Examples > Arduino_MKRENV >
ReadSensors**. Then, upload the code to the
board.

<a id='f72db4db-deb3-49cb-bb1f-1d2f76392c3e'></a>

Note: If you are using imperial units, e.g.
Fahrenheit, there is a sketch called
ReadSensorsImperial that is better suited.

<a id='22ab5578-f640-42be-b582-de35b2c88117'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='5d37a173-60fe-4f90-b202-2fec83a7dd72'></a>

6/8