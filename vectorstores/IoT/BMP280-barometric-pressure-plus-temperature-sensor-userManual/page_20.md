<a id='3b5548e3-7bb1-46ef-8790-eeb0b4ca3bd6'></a>

For non-express boards like the Trinket MO or Gemma MO, you'll need to manually install the necessary libraries from the bundle:

<a id='6c00bcbb-af74-4fe6-88f2-0d090536ca07'></a>

* adafruit_bmp280.mpy
* adafruit_bus_device

<a id='80b758c9-418d-40f5-b20a-54ec760044e5'></a>

Before continuing make sure your board's lib folder or root filesystem has the `adafruit_bmp280.mpy`, and `adafruit_bus_device` files and folders copied over.

<a id='eb5e6912-e579-4866-b935-61d8340d3f0f'></a>

Next [connect to the board's serial REPL](https://adafru.it/Awz) so you are at the CircuitPython >>> prompt.

<a id='db5e8b52-c047-4501-a2c4-dec43e068b23'></a>

# Python Installation of BMP280 Library
You'll need to install the Adafruit_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready (https://adafru.it/BSN)!

<a id='56c06d12-9164-459f-9b17-34fca9881e1d'></a>

Once that's done, from your command line run the following command:

<a id='6baa7ae1-d4ed-49e0-900a-1a73b6a517c0'></a>

- sudo pip3 install adafruit-circuitpython-bmp280

<a id='f2cf09e1-e466-4137-a272-73a38b3be14b'></a>

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

<a id='4b790296-8a3f-451a-a13c-7493ab76a75d'></a>

CircuitPython & Python Usage

<a id='acdb3112-6441-4dd9-95ce-f5a8ca575d0f'></a>

To demonstrate the usage of the sensor we'll initialize it and read the temperature,
humidity, and more from the board's Python REPL.

<a id='60d82fc5-98e2-44e0-b114-d254d569252b'></a>

If you're using an I2C connection run the following code to import the necessary modules and initialize the I2C connection with the sensor:

<a id='ac3c840f-bd8c-4611-8225-6d38ab9cc751'></a>

```python
import board
import adafruit_bmp280
i2c = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
```

<a id='14d07aa1-a5b5-47cf-a4bc-f42e93b1d829'></a>

© Adafruit Industries

<a id='02c42120-8c76-4934-a229-39bb0b7e3a4d'></a>

Page 21 of 34