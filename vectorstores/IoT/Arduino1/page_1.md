<a id='cf5b4aed-64c8-4c0a-b915-97ed338a432d'></a>

12/4/25, 2:50 PM

<a id='80773bf3-ad5a-4916-94b7-7b0633c91517'></a>

ArduinoBLE | Arduino Documentation

<a id='17e3db92-7ccf-435b-bc44-3a036ddf6909'></a>

ARDUINODOCS

<a id='23481b9f-7bba-4809-8a0c-dd7b22f5e16c'></a>

Search on Docs /

<a id='e1474826-0de3-432e-b8ae-71366f58c78b'></a>

← Go Back

## Library

<a id='1b9294c8-c670-4548-ae28-18559dfd9d6b'></a>

Recents viewed

<a id='3d2bdb82-a363-4a3d-ab3b-5e75337b5258'></a>

ArduinoBLE

ArduinoMqttClient

WiFiNINA

Arduino SigFox for
MKRFox1200

autowp-mcp2515

Arduino_MKRENV

Arduino_MKRGPS

Arduino_APDS9960

Arduino_MKRIoTCarrier

<a id='f56ba910-8d1d-46b5-96e7-ab5d6e8e4c78'></a>

Home / Programming / Library / ArduinoBLE

<a id='63d7128d-4523-452e-9e58-4f314d4145b9'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='eaa0fd10-37c4-4043-a493-eb3a55680e19'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='27bb371f-2410-4352-b118-dd2ed078c401'></a>

GO TO REPOSITORY

<a id='5275f48a-4412-4179-9214-44e8649746d8'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='3ffef8de-6609-4375-81f1-3bee10edd3ce'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='67a44623-3bd4-4aba-af84-19088c13dc9c'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled
"Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low
Energy is optimized for low power use at low data rates, and was
designed to operate from simple lithium coin cell batteries.

<a id='3e7bc3d7-b55d-406e-a3d7-44185f31d502'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='62fa04cb-16a7-4054-a72d-e4f93440dd12'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='e4b5634c-fb09-4088-892d-96b6073cee0f'></a>

Help

<a id='b5b8f95f-a6c2-40e0-861b-dc21801eb187'></a>

1/10

<a id='d6dff80b-f353-41d6-a8ba-7ea7449b8845'></a>

ON THIS PAGE

* Usage/Examples
* Compatibility
* Releases
* BLE class
* BLEDevice Class
* BLEService Class
* BLECharacteristic
* BLEDescriptor Clas