<a id='e2704209-e8f8-4c3e-a200-95afe4e41db6'></a>

12/4/25, 2:51 PM

<a id='1bdcc652-b88a-4e5f-b9c1-214602b221d1'></a>

ArduinoBLE | Arduino Documentation

<a id='ce1c51ec-e287-461a-9bb9-a7031b5920c3'></a>

ARDUINODOCS

<a id='cd28836d-5666-4cb1-9484-4c28d3fc0342'></a>

Search on Docs /

<a id='f771097d-fec5-434c-9b85-518a8441db9c'></a>

← Go Back

## Library

<a id='87c182eb-aabb-4d32-9955-0d3d452d6d30'></a>

Recents viewed

<a id='116e3272-e842-4e32-b99e-5b64815e3bb6'></a>

option ArduinoBLE: [x]
option ArduinoMqttClient: [ ]
option WiFiNINA: [ ]
option Arduino SigFox for MKRFox1200: [ ]
option autowp-mcp2515: [ ]
option Arduino_MKRENV: [ ]
option Arduino_MKRGPS: [ ]
option Arduino_APDS9960: [ ]
option Arduino_MKRIoTCarrier: [ ]

<a id='99e29aa4-5bc4-4fa4-83b0-9be3323323c5'></a>

Home / Programming / Library / ArduinoBLE

<a id='14143782-8570-4162-aa8c-4f489f94786f'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='919833c3-f293-4b06-8d73-666ade0ef524'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='5fa51426-0a60-4516-b1e8-543ba7339bb5'></a>

GO TO REPOSITORY

<a id='7a72381f-5069-42ae-9c1c-38cd4506bfd8'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='96f99b12-45cd-4065-805b-e5821a931be2'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='4c6090c6-b789-4b2d-bc89-db555ad0ecbb'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled "Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low Energy is optimized for low power use at low data rates, and was designed to operate from simple lithium coin cell batteries.

<a id='a89f8326-ed49-4b6d-ab5f-23a6a186db85'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='64f8ce01-64de-4242-a90f-d8c46beec97b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='4ce2d9ad-fbdd-400b-85ea-be3b24bc1a52'></a>

Help

<a id='35de5ece-036d-40cf-ab40-9a6b6e5cea17'></a>

1/24

<a id='48666032-422b-4213-973c-429e9c03e894'></a>

ON THIS PAGE

* Usage/Examples
* Compatibility
* Releases
* BLE class
* BLEDevice Class
* BLEService Class
* BLECharacteristic
* BLEDescriptor Clas