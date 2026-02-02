<a id='d2edda40-bbae-48ca-9dd1-2936e3eb1a65'></a>

12/4/25, 2:49 PM

<a id='37aa6aec-b087-45d9-bd80-94bded749fd8'></a>

ArduinoBLE | Arduino Documentation

<a id='8134b098-3beb-4613-af08-cf934a3e9473'></a>

ARDUINODOCS

<a id='0138df83-7625-4730-b233-c67aabba4ef4'></a>

Search on Docs /

<a id='a4462f9a-01a9-4eb6-97b6-f49f854fa7a1'></a>

← Go Back

## Library

<a id='e3b9fda0-0c22-4beb-9f55-9375b96ce46f'></a>

Recents viewed

<a id='b0602277-c118-46e3-af74-e575c979b66d'></a>

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

<a id='760c3196-e5c4-46d8-ab2d-9bdb741c55ff'></a>

Home / Programming / Library / ArduinoBLE

<a id='1f2e8980-f883-4667-ad99-d73fd9e8b22e'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='d4341be7-d647-42b9-8ca0-7a47dd4f392e'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='1432ae16-071f-4308-9bcc-dac135ded397'></a>

GO TO REPOSITORY

<a id='619adb39-e92c-430d-91cd-4afb7ea5583e'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='c15b4ad9-28ac-402b-8e53-c905d05be89b'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='034d2b5d-45bd-49a7-9645-36631c8c1ad1'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled "Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low Energy is optimized for low power use at low data rates, and was designed to operate from simple lithium coin cell batteries.

<a id='4eb04877-65d7-40bb-8ddb-75fd72f5c6a0'></a>

Unlike standard Bluetooth® communication basically based on an an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='77be8dc8-d5fe-4e74-86c9-5e80de74e84b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='1c85ea63-b86a-40bc-9755-bfcf9688d45b'></a>

Help

<a id='e481b41b-a56d-4e72-b0bd-d5d258b6c5c7'></a>

1/26

<a id='c2efce69-07d6-4878-9c81-27b668648399'></a>

ON THIS PAGE

* Usage/Examples
* Compatibility
* Releases
* BLE class
* BLEDevice Class
* BLEService Class
* BLECharacteristic
* BLEDescriptor Clas