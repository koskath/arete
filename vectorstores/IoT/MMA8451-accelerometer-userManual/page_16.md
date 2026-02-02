<a id='0525d496-cd15-4933-ba3a-511d276d8305'></a>

<::A diagram illustrating the wiring connections between a Raspberry Pi and a sensor module on a breadboard. The green Raspberry Pi board is on the left, featuring various ports such as Power, DSI (Display), HDMI, CSI (Camera), Audio, Ethernet, and two USB 2x ports. A 40-pin GPIO header is visible on the right side of the Raspberry Pi. On the right, a blue sensor module, labeled "MMA8453", is plugged into a white breadboard. Four jumper wires connect the Raspberry Pi's GPIO pins to the sensor module:
Pi 3V3 to sensor VIN
Pi GND to sensor GND
Pi SCL to sensor SCL
Pi SDA to sensor SDA
: figure::>

<a id='396069a4-8751-48d0-9fd9-a429193ef937'></a>

Older versions of the Raspberry Pi firmware do not have I2C clock stretching support so they don't work well with the MMA. Please ensure your firmware is updated to the latest version before continuing and slow down the I2C as explained here https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/i2c-clock-stretching

<a id='7c3e1bea-f3f0-4468-a8ad-369e4992c530'></a>

# CircuitPython Installation of MMA8451 Library

Next you'll need to install the [Adafruit CircuitPython MMA8451](https://adafru.it/C5g) library on your CircuitPython board.

<a id='591b005f-226b-4428-b693-e766c886b489'></a>

First make sure you are running the [latest version of Adafruit CircuitPython](https://adafru.it/Amd) for your board.

<a id='b5389689-8ff9-4bf5-9953-e606487ccd4b'></a>

Next you'll need to install the necessary libraries to use the hardware--carefully follow the steps to find and install these libraries from [Adafruit's CircuitPython library bundle](https://adafru.it/zdx). Our introduction guide has a [great page on how to install the library bundle](https://adafru.it/ABU) for both express and non-express boards.

<a id='aebc4452-7a80-47a3-a2ab-d929c59dbb0b'></a>

Remember for non-express boards like the, you'll need to manually install the necessary libraries from the bundle:

<a id='265dab5a-a066-4d12-87b2-980959d43ddb'></a>

* adafruit_mma8451.mpy
* adafruit_bus_device

<a id='2fdcf8e3-7989-4959-8760-13d77a006d92'></a>

Before continuing make sure your board's lib folder or root filesystem has the `adafruit_mma8451.mpy`, and `adafruit_bus_device` files and folders copied over.

<a id='37566a7d-88e7-4f22-b683-7c6341ee9c2d'></a>

© Adafruit Industries

<a id='a71e1d96-252d-4ef8-9695-16bc88866b1c'></a>

Page 16 of 21