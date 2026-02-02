<a id='96dd07c5-2a21-4bf4-98d2-8daa3996b512'></a>

Next connect to the board's serial REPL (https://adafru.it/Awz) so you are at the
CircuitPython >>> prompt.

<a id='1c3f95f3-e117-4c0c-aa50-58cbad50ef5e'></a>

# Python Installation of MMA8451 Library

You'll need to install the Adafruit_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready (https://adafru.it/BSN)!

<a id='52c46285-135d-4244-91e5-5b1a75f71656'></a>

Once that's done, from your command line run the following command:

* `sudo pip3 install adafruit-circuitpython-mma8451`

<a id='ac36c891-2fab-4772-bd5a-437bc3659aa4'></a>

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

<a id='f1d922cf-fdef-4718-8263-653233461096'></a>

# CircuitPython & Python Usage
To demonstrate the usage of the sensor we'll initialize it and read the acceleration from the board's Python REPL. Run the following code to import the necessary modules and initialize the I2C connection with the sensor:

<a id='a83be39d-79cf-4a6f-9f1a-6531742c413b'></a>

```python
import board
import adafruit_mma8451
i2c = board.I2C()
sensor = adafruit_mma8451.MMA8451(i2c)
```

<a id='d67de593-97cc-4130-8ed6-b19cf689f960'></a>

Now you're ready to read values from the sensor using any of these properties:

*   **acceleration** - This returns a 3-tuple of X, Y, Z acceleration values in meters per second squared (i.e. 9.8m/s^2 is the force of gravity on the surface of the earth).
*   **orientation** - This is a value the MMA8451 calculates to help you understand what orientation the sensor is in, kind of like how a smartphone detects if its landscape or portrait orientation. This will return one of the following values:
    *   `adafruit_mma8451.PL_PUF`: Portrait, up, front
    *   `adafruit_mma8451.PL_PUB`: Portrait, up, back
    *   `adafruit_mma8451.PL_PDF`: Portrait, down, front
    *   `adafruit_mma8451.PL_PDB`: Portrait, down, back
    *   `adafruit_mma8451.PL_LRF`: Landscape, right, front
    *   `adafruit_mma8451.PL_LRB`: Landscape, right, back

<a id='65c061f7-d9a7-4cf7-9348-f585235a806d'></a>

©Adafruit Industries

<a id='3beb7b44-35f4-4367-aa8b-4ab582cbb0a7'></a>

Page 17 of 21