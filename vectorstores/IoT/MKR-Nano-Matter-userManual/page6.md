<a id='c5397c2f-6ae6-46bf-914e-d574e7376165'></a>

ARDUINODOCS

<a id='b4154bee-bed1-4f01-965d-aab2cbc67ac7'></a>

<::logo: [Unknown] [No readable text] A teal circuit board with various black and white electronic components and silver pins on the edges::>

<a id='1aeac189-df3d-4d97-b954-cf1730bed6f0'></a>

<::logo: matter
matter
A dark blue abstract symbol resembling three interconnected arrows or spokes is positioned to the left of the company name.::>

<a id='ef092f93-309a-405d-a967-252f5dfe93d7'></a>

Nano Matter

<a id='1b5239ad-cbec-4a1c-b570-9756b00ed1df'></a>

The Nano Matter can communicate with Matter hubs through a Thread® network, so the hubs used must be **Thread® border routers**.

<a id='7d305241-d323-4204-9d97-5842eab6ec71'></a>

The Silicon Labs core in the Arduino IDE comes with several Matter examples ready to be tested with the Nano Matter and works as a starting point for almost any IoT device we can imagine building.

<a id='493cda5e-e663-4019-a3e1-ba857e2b89a5'></a>

sketch_ino231 | Arduino IDE 2.3.1
File Edit Sketch Tools Help
New Sketch Ctrl+N
New Cloud Sketch Alt+Ctrl+N
Open... Ctrl+O
Open Recent
Sketchbook
Examples
Blink
Digital
Analog
Communication
Control
Sensors
Display
Strings
USB
WiFi
Bluetooth
FirmwareUpdater
Adafruit GFX Library
Adafruit HT16K33
Adafruit ILI9341
Adafruit LIS3MDL Library
Adafruit MPU6050 Library
Adafruit PWM Servo Driver Library
Adafruit SSD1306
Adafruit TFTLCD
Adafruit Unified Sensor Library
Adafruit VS1053 Library
Adafruit WaveShield
Adafruit PN532
Adafruit NeoPixel
Adafruit LSM303DLHC
Adafruit HMC5883L
Adafruit BME280 Library
Adafruit BMP280
Adafruit BMP085
Adafruit SHT31
Adafruit VEML6070
Adafruit VEML6075
Adafruit APDS9960
Adafruit LSM6DS3
Adafruit LTR390
Adafruit MPL3115A2
Adafruit MPU6050
Adafruit MSA301
Adafruit SGP30
Adafruit SI1145
Adafruit TCS34725
Adafruit TSL2591
Adafruit VL53L0X
Adafruit AMG88XX
Adafruit CCS811
Adafruit BNO055
Adafruit AS726X
Adafruit ICM20649
Adafruit VL6180X
Adafruit LSM9DS0
Adafruit LSM9DS1
Adafruit MPU9250
Adafruit BMP3XX
Adafruit ADXL343
Adafruit LSM6DSOX
Adafruit ADXL375
Adafruit ADXL34X
Adafruit AHTX0
Adafruit Circuit Playground Express Library
Adafruit GFX Library
matter_air_quality_sensor
matter_contact_sensor
matter_decommissioning
matter_door_lock
matter_fan
matter_flow_sensor
matter_humidity_sensor
matter_illuminance_sensor
matter_lightbulb
matter_lightbulb_callback
matter_lightbulb_color
matter_lightbulb_custom_name
matter_lightbulb_dimmable
matter_lightbulb_dimmable_multiple
matter_lightbulb_identify
matter_lightbulb_multiple
matter_lightbulb_multiple_color
matter_lightbulb_with_button
matter_occupancy_sensor
matter_on_off_outlet
matter_pressure_sensor
matter_sensor_and_bulb
matter_sensor_multiple
matter_switch
matter_temp_sensor
matter_thermostat
matter_window_covering
matter_lightbulb_color
Matter examples

<a id='a7c89c64-3043-4adb-9cd9-e42319b77ad6'></a>

ⓘ The _matter_lightbulb_ example is the only officially Matter-certified profile for the Nano Matter. Consequently, while running any of the other available profile examples, it is expected to get an _Uncertified device_ message in the different Matter-compatible apps. This does not prevent the user from prototyping a solution with different configurations.

First, to start creating Matter-enabled solutions, we need to select the Matter protocol in **Tools > Protocol stack > Matter**:

<a id='0a392824-7ef8-4f79-a020-b2fc5b57bd20'></a>

File Edit Sketch Tools Help

Auto Format Ctrl+T
Archive Sketch
Manage Libraries... Ctrl+Shift+I
Serial Monitor Ctrl+Shift+M
Serial Plotter
Firmware Updater
Upload SSL Root Certificates
Board: "Arduino Nano Matter"
Port: "COM5"
Get Board Info

Protocol stack: "Matter"
  option Matter: [x]
  option BLE (Arduino): [ ]
  option BLE (Slabs): [ ]
  option None: [ ]

Programmer
Burn Bootloader

<a id='6ce2d0e8-656a-44e3-be45-622fb8200a55'></a>

Matter Protocol stack selected

<a id='41ff58a3-6957-4fcd-b80c-c4d612c697c1'></a>

In the example below, we are going to use the Nano Matter as a *RGB Lightbulb*. For this,
navigate to **File** > **Examples** > **Matter** and open the built-in sketch called
**nano_matter_lightbulb_color**.