<a id='c187269b-f8ae-4a40-a4f2-daced8df4003'></a>

MKR IoT Carrier User Manual\nLearn how to get started with your MKR IoT Carrier, including hardware, compatible boards, and libraries.\n\nOVERVIEW GET STARTED FEATURES REFERENCE COMMUNITY\n\n<::\nTwo top-down views of the MKR IoT Carrier board. The left image shows the top of the board with components like a display, joystick, buttons, sensors, and connectors. The right image shows the bottom of the board, primarily the solder pads and connections.\nThe MKR IoT Carrier.\n: figure::>\nThe MKR IoT Carrier is designed as an all-in-one platform, including a display, a joystick, buttons, sensors, and a buzzer, to allow you to get started developing your next IoT projects. The carrier does not come equipped with a microcontroller, meaning it only acts as a breakout board for other boards. The MKR IoT Carrier comes equipped with a RGB, IMU, Humidity & Temperature, and Pressure sensor, as well as a range of Grove connectors. It also features a joystick, five LED buttons, a buzzer, an SD card holder, and two Grove connectors.\n\nCompatible Boards\nThe MKR IoT Carrier supports different boards, meaning that they are all physically compatible. The MKR IoT Carrier supports any board from the MKR family.\n\n- MKR ZERO\n- MKR WiFi 1010\n- MKR 1000 WiFi\n- MKR NB 1500\n- MKR GSM 1400\n- MKR WAN 1300\n- MKR FOX 1200\n- MKR VIDOR 4000\n\nThe MKR IoT Carrier is a useful tool that will help you kickstart your projects. You can browse through the Arduino IoT Cloud examples to see a complete list of programs.\n\nPinout\n<::\nAn exploded view diagram of the MKR IoT Carrier. The diagram shows the main circular board, with a rectangular MKR board plugged into the central header, and the circular display module sitting on top of the main board.\nThe MKR IoT Carrier in exploded view.\n: figure::>\n\nDatasheet\nFor more information about the technical specifications of the MKR IoT Carrier, see the following:\n\n- Product documentation (PDF)\n- Schematic (PDF)\n\nArduino Cloud\nThe MKR IoT Carrier can be easily integrated with the Arduino IoT Cloud, allowing you to monitor and control your projects from anywhere in the world. It comes with pre-built examples that you can easily upload to your board.\nThe following MKR boards are compatible with the Arduino IoT Cloud:\n\n- MKR WiFi 1010\n- MKR 1000 WiFi\n- MKR NB 1500\n- MKR GSM 1400\n- MKR WAN 1300\n\n<::\n**Note:** These boards are compatible with the Arduino IoT Cloud, and the MKR IoT Carrier supports both the Arduino IoT Cloud and the Arduino IoT Cloud examples. However, other boards can be used with the Arduino IoT Cloud.\n: not_figure::>\nYou can find the Arduino IoT Cloud examples through the Arduino Web Editor.\n\nPinout\n<::\nA detailed pinout diagram of the MKR IoT Carrier. The circular board is shown with various components and connectors labeled, including power pins (VCC, GND), analog pins (A0, A1), digital pins (D0-D7), I2C (SDA, SCL), UART (RX, TX), SPI (MOSI, MISO, SCK, CS), and control pins (DC, RST, BL).\nThe MKR IoT Carrier pinout.\n: figure::>\n<::\nA table listing the pinout of the MKR IoT Carrier.\n\n| Pin   | Function         | Description                                    |\n| :---- | :--------------- | :--------------------------------------------- |\n| VCC   | Power            | 5V power supply.                               |\n| GND   | Ground           | Ground reference.                              |\n| A0    | Analog Input     | Analog input pin 0.                            |\n| A1    | Analog Input     | Analog input pin 1.                            |\n| D0    | Digital I/O      | Digital input/output pin 0.                    |\n| D1    | Digital I/O      | Digital input/output pin 1.                    |\n| D2    | Digital I/O      | Digital input/output pin 2.                    |\n| D3    | Digital I/O      | Digital input/output pin 3.                    |\n| D4    | Digital I/O      | Digital input/output pin 4.                    |\n| D5    | Digital I/O      | Digital input/output pin 5.                    |\n| D6    | Digital I/O      | Digital input/output pin 6 (Buzzer).           |\n| D7    | Digital I/O      | Digital input/output pin 7.                    |\n| SDA   | I2C              | I2C Serial Data Line.                          |\n| SCL   | I2C              | I2C Serial Clock Line.                         |\n| RX    | UART             | UART Receive pin.                              |\n| TX    | UART             | UART Transmit pin.                             |\n| MOSI  | SPI              | SPI Master Out Slave In.                       |\n| MISO  | SPI              | SPI Master In Slave Out.                       |\n| SCK   | SPI              | SPI Serial Clock.                              |\n| CS    | SPI              | SPI Chip Select for SD card.                   |\n| DC    | Control          | Display Data/Command pin.                      |\n| RST   | Control          | Display Reset pin.                             |\n| BL    | Backlight        | Display Backlight control pin.                 |\n| 3V3   | Power            | 3.3V power supply.                             |\n| 5V    | Power            | 5V power supply.                               |\n: figure::>\nTo see the full pinout, you can download the PDF from the link below.\n\n- MKR IoT Carrier pinout (PDF)\n\nGrove Connectors\n<::\nA top-down view of the MKR IoT Carrier board highlighting the three Grove connectors. Two analog Grove connectors (A0-A1) and one digital Grove connector (D0-D1) are clearly visible and labeled.\nGrove connectors on the MKR IoT Carrier.\n: figure::>\nThe MKR IoT Carrier comes with three Grove connectors, two analog (A0-A1) and one digital (D0-D1). In addition, you can use the Grove connector to expand the functionality of your projects. The Grove connectors make it easy to connect external sensors and actuators to the carrier.\n\nCarrier Library\nTo simplify the development of applications, the Arduino team has made a dedicated library, the Arduino_MKR_IoT_Carrier library, which abstracts the hardware features of the MKR IoT Carrier and provides an easy-to-use API for interacting with the sensors, actuators, and other components. The library provides functions to read sensor data, control the display, and interact with the buttons and joystick.\n\nHumidity & Temperature Sensor\nThe MKR IoT Carrier is equipped with a humidity and temperature sensor. The sensor is used to measure the ambient humidity and temperature. The sensor is connected to the I2C bus and can be accessed through the Carrier library.\n\nYou can read the humidity and temperature sensor data through the following functions:\n\n<::\n```cpp\ncarrier_temperature_c()\n```\n: figure::>\n\nReturns the temperature in Celsius.\n\n<::\n```cpp\ncarrier_temperature_f()\n```\n: figure::>\n\nReturns the temperature in Fahrenheit.\n\n<::\n```cpp\ncarrier_humidity()\n```\n: figure::>\n\nReturns the relative humidity in percentage.\n\nHumidity & Temperature Sensor\n<::\nA top-down view of the MKR IoT Carrier board with the BME680 Humidity & Temperature sensor highlighted. The sensor is a small square component located near the center of the board, labeled \"BME680 Humidity & Temperature sensor\".\nThe BME680 Humidity & Temperature sensor.\n: figure::>\nThe BME680 Humidity & Temperature sensor is connected to the I2C bus and can be accessed through the Carrier library. The sensor provides accurate measurements of humidity and temperature. It is a low-power sensor that can be used in a variety of applications. The sensor measures humidity from 0% to 100% with an accuracy of ±3% and temperature from -40°C to 85°C with an accuracy of ±1°C.\n\nCode\nYou can read the temperature and humidity sensor data through a simple example sketch:\n\n<::\n```cpp\n#include <Arduino_MKR_IoT_Carrier.h>\n\nvoid setup() {\n  Serial.begin(9600);\n  if (!CARRIER_BME680.begin()) {\n    Serial.println(\"Failed to initialize BME680!\");\n    while (1);\n  }\n}\n\nvoid loop() {\n  Serial.print(\"Temperature: \");\n  Serial.print(CARRIER_BME680.readTemperature());\n  Serial.println(\" °C\");\n\n  Serial.print(\"Humidity: \");\n  Serial.print(CARRIER_BME680.readHumidity());\n  Serial.println(\" %\");\n\n  delay(1000);\n}\n```\n: figure::>\n\nTemperature and humidity sensor values are often used in environmental monitoring, weather stations, and smart home applications.\nThe underlying library used to read the sensor is the Adafruit BME680 library.\n\nPressure Sensor\n<::\nA top-down view of the MKR IoT Carrier board with the BMP280 Pressure sensor highlighted. The sensor is a small square component located near the edge of the board, labeled \"BMP280 Pressure sensor\".\nThe BMP280 Pressure sensor.\n: figure::>\nThe BMP280 Pressure sensor is connected to the I2C bus and can be accessed through the Carrier library. The sensor provides accurate measurements of pressure. It is a low-power sensor that can be used in a variety of applications. The sensor measures pressure from 300 hPa to 1100 hPa with an accuracy of ±1 hPa.\n\nCode\nYou can read the pressure sensor data through a simple example sketch:\n\n<::\n```cpp\n#include <Arduino_MKR_IoT_Carrier.h>\n\nvoid setup() {\n  Serial.begin(9600);\n  if (!CARRIER_BMP280.begin()) {\n    Serial.println(\"Failed to initialize BMP280!\");\n    while (1);\n  }\n}\n\nvoid loop() {\n  Serial.print(\"Pressure: \");\n  Serial.print(CARRIER_BMP280.readPressure());\n  Serial.println(\" Pa\");\n\n  delay(1000);\n}\n```\n: figure::>\nThe underlying library used to read the sensor is the Adafruit BMP280 library.\n\nIMU Accelerometer & Gyroscope Sensors\n<::\nA top-down view of the MKR IoT Carrier board with the LSM6DS3TR-C IMU sensor highlighted. The sensor is a small square component located near the center of the board, labeled \"LSM6DS3TR-C IMU sensor\".\nThe LSM6DS3TR-C IMU sensor.\n: figure::>\nThe LSM6DS3TR-C IMU sensor is connected to the I2C bus and can be accessed through the Carrier library. The sensor provides accurate measurements of acceleration and angular velocity. It is a low-power sensor that can be used in a variety of applications. The sensor measures acceleration from ±2 g to ±16 g and angular velocity from ±125 dps to ±2000 dps.\n\nCode\nThe data from the accelerometer and gyroscope sensors can be accessed and read through functions defined in the Carrier library.\n\n<::\n```cpp\n#include <Arduino_MKR_IoT_Carrier.h>\n\nvoid setup() {\n  Serial.begin(9600);\n  if (!CARRIER_LSM6DS3TR_C.begin()) {\n    Serial.println(\"Failed to initialize LSM6DS3TR-C!\");\n    while (1);\n  }\n}\n\nvoid loop() {\n  float accX, accY, accZ;\n  CARRIER_LSM6DS3TR_C.readAcceleration(accX, accY, accZ);\n  Serial.print(\"Acceleration: \");\n  Serial.print(accX);\n  Serial.print(\", \");\n  Serial.print(accY);\n  Serial.print(\", \");\n  Serial.print(accZ);\n  Serial.println(\" m/s^2\");\n\n  float gyroX, gyroY, gyroZ;\n  CARRIER_LSM6DS3TR_C.readGyroscope(gyroX, gyroY, gyroZ);\n  Serial.print(\"Gyroscope: \");\n  Serial.print(gyroX);\n  Serial.print(\", \");\n  Serial.print(gyroY);\n  Serial.print(\", \");\n  Serial.print(gyroZ);\n  Serial.println(\" dps\");\n\n  delay(1000);\n}\n```\n: figure::>\nThe following methods can be used to read the acceleration:\n\n<::\n```cpp\ncarrier_acceleration_x()\n```\n: figure::>\n\nReturns the acceleration data sample in g (gravity) for the X-axis in m/s^2.\n\n<::\n```cpp\ncarrier_acceleration_y()\n```\n: figure::>\n\nReturns the acceleration data sample in g (gravity) for the Y-axis in m/s^2.\n\n<::\n```cpp\ncarrier_acceleration_z()\n```\n: figure::>\n\nReturns the acceleration data sample in g (gravity) for the Z-axis in m

<a id='215d34cc-e10d-4d6c-b9ed-3bc4784c2331'></a>

LEDS

<::transcription of the content
: figure::>

RGB(255,0,0) RGB(0,255,0) RGB(0,0,255)
The LEDs on the MKR IoT Carrier

The MKR IoT Carrier comes with 5 **digital RGB LEDs** placed on the top side of the carrier in front of the buttons.

Code

The LEDs are controlled with the Adafruit® DotStar library, which is included in the `MKRIoTCarrier` library.
The `carrier.leds.show();` method is necessary for updating the new state of the LEDs and needs to be called after any change of the state of the LEDs (turning on & off or change of color).
Here are some of the useful methods used to control the LEDs on the MKR IoT Carrier:

```
1 carrier.leds.setPixelColor (index, red, green, blue);
```
Sets the color of the index's LED.

```
1 carrier.leds.setBrightness(255);
```
Set the overall brightness, from 0 (no brightness) to 255 (maximum brightness).

```
1 carrier.leds.clear();
```
Clear the buffer of the LEDs.

```
1 carrier.leds.fill(color, firstLedToCount, count);
```
Fill X amount of the LEDs with the same color.

```
1 uint32_t myColor = carrier.leds.Color(red, green, blue)
```
Saves a custom color.

The code example below shows how to light up all 5 LEDs with our customized color.

```
1 #include <Arduino_MKRIoTCarrier.h>
2 MKRIoTCarrier carrier;
3 uint32_t myCustomColor = carrier.leds.Color(255,100,50);
4 void setup(){
5   carrier.noCase();
6   carrier.begin();
7   carrier.leds.fill(myCustomColor, 0, 5);
8   carrier.leds.show();
9 }
```

Buzzer

<::transcription of the content
: figure::>

BUZZER
FCCE
The buzzer on the MKR IoT Carrier

The MKR IoT Carrier is equipped with a **sound buzzer** on the bottom side of the carrier, under the MKR board.

<a id='df088f42-119d-4db7-aba5-3bc30b809acb'></a>

The SD class initialized in the main `carrier.begin()` so you don't need to do it yourself. The code below demonstrates how to save data on a file on a SD card.

```
#include <Arduino_MKRIoTCarrier.h>
MKRIoTCarrier carrier;

File myFile;

void setup() {
  carrier.noCase();
  carrier.begin(); //SD card initialized here

  myFile = SD.open("test.txt", FILE_WRITE);
}
```

In order to learn more, check any of the many tutorials about using the SD library on Arduino.

# Power

<::An illustration of the MKR IoT Carrier circuit board, highlighting the JST BATTERY CONNECTOR. The board has markings like FC CE, ROHS COMPLIANT, DESIGNED AND ASSEMBLED IN ITALY.
: figure::>

JST battery connector on the MKR IoT Carrier.

The MKR IoT Carrier can be either powered through a USB cable connected to the mounted MKR board, or through a battery. The battery used should be a LI-ION 18650 3.7v battery, which can be mounted to the carrier via the battery holder on the bottom side.

In order to use the USB power to charge the battery, a little cable with JST connectors on both ends is needed between the MKR IoT Carrier and the MKR board. The bBattery can then be recharged via a USB connection through the MKR Board (runs up to 48h with a 3.7v 2500mAh).

<a id='9f9a5a20-de70-4fa7-a0bf-a7a8d6788306'></a>

through the MKR Board (runs up to 48h with a 3.7v 2500mAh).

<::3D model of a circuit board within a video player with time controls (0:00 / 0:25)
: figure::>

Suggest changes
The content on docs.arduino.cc is
facilitated through a public GitHub

Need support?
Help Center
Ask the Arduino Forum

License
The Arduino documentation is licensed
under the Creative Commons Attribution-

<a id='5b5f4a88-5eb6-4a69-9f26-044104450d29'></a>

ON THIS PAGE

Compatible Boards
Assembly
Datasheet
Arduino Cloud
Pinout
Grove Connectors
Carrier Library
Initialization
Setup
Humidity & Temperature
Sensor
Code
Pressure Sensor
Code
IMU Accelerometer &
Gyroscope Sensors
Code
RGB and Gesture Sensor
Code
Relays
Code
Peripherals
Display +
Buttons -
Code
LEDs
Code
Buzzer
Code
Memory
Code
Power