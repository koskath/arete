<a id='a3332959-f0eb-4853-9844-15eb6a4983b3'></a>

Example for line 3:

Portrait Up Front

<a id='226f77fe-082d-4686-8b90-372af7565630'></a>

This is the output of the orientation detection inside the chip. Since inexpensive accelerometers are often used to detect orientation and tilt, this sensor has it built in. The orientation can be Portrait or Landscape, then Up/Down or Left/Right and finally tilted forward or tilted back. Note that if the sensor is tilted less than 30 degrees it cannot determine the forward/back orientation. If you play with twisting the board around you'll get the hang of it.

<a id='d0860328-60cf-47cb-bbe3-9268b3df9888'></a>

Library Reference
The library we have is simple and easy to use

<a id='ed4eac47-8378-4f01-85a1-4519c0b3217d'></a>

You can create the **Adafruit_MMA8451** object with:
```
Adafruit_MMA8451 mma = Adafruit_MMA8451();
```
There are no pins to set since you must use the I2C bus!

<a id='22a284c3-fea0-4cdf-a5dc-b2609b1560d5'></a>

Then initialize the sensor with:

```
mma.begin()
```

<a id='1369a757-ed36-41dc-9e41-bfe92d344685'></a>

this function returns **True** if the sensor was found and responded correctly and **False** if it was not found. We suggest something like this:

```
if (! mma.begin()) {
Serial.println("Couldnt start")
while (1);
}
Serial.println("MMA8451 found!");
```

<a id='6e39bee1-f0ef-4eec-9cc2-ddbf2c24b20e'></a>

Set & Get Range
You can set the accelerometer max range to 2g, 4g or 8g with

<a id='69e5c8c8-408a-4a0a-a63e-e093fee3c3bf'></a>

<table id="12-1">
<tr><td id="12-2">mma.setRange(MMA8451 RANGE 2 G);</td><td id="12-3"></td></tr>
<tr><td id="12-4">mma.setRange(MMA8451 RANGE 4 G);</td><td id="12-5"></td></tr>
<tr><td id="12-6">mma.setRange(MMA8451 RANGE 8 G);</td><td id="12-7"></td></tr>
</table>

<a id='51def107-119d-4b9b-961f-70fc86fffeb7'></a>

And read what the current range is with

<a id='32708e44-6774-472c-a6ba-1aa761a3d693'></a>

© Adafruit Industries

<a id='bb9ada82-640b-4c17-af71-5220f6d0d6f7'></a>

Page 13 of 21