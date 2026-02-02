<a id='b0c71285-e5b1-42f1-a5b6-ce8590913a7f'></a>

12/4/25, 2:51 PM

<a id='daa1882f-b289-4f9a-9b4b-00fd02f0c1f7'></a>

ArduinoBLE | Arduino Documentation

<a id='ea20673c-4c74-437a-bbac-900114c7b4ea'></a>

ARDUINODOCS

<a id='ee4af612-d988-4b49-bb26-32aa8a944947'></a>

Search on Docs /

<a id='66b1f426-1c23-4960-9478-c2486e0db584'></a>

← Go Back

## Library

<a id='e35306a4-6f08-4fd4-8096-d81283479573'></a>

Recents viewed

<a id='4803ff6a-d0a4-4a24-9f03-ef0ad49c90b1'></a>

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

<a id='ec4ce92d-c7f6-4d17-9119-1310e18af554'></a>

Home / Programming / Library / ArduinoBLE

<a id='8006e031-3090-4fc9-8d9e-e18cbf21cdb1'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='fc695392-e6c1-4f2a-980e-d9c98b962738'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='ccd15875-a867-4353-9cc2-950ebd6e7392'></a>

GO TO REPOSITORY

<a id='a2c47c8f-9fb1-4f8c-9b71-e51bd929e8e2'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='77f72e37-616e-4be8-96ac-dbf9fef0e48e'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='2ba68331-6208-497b-93ed-512b3018b194'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled "Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low Energy is optimized for low power use at low data rates, and was designed to operate from simple lithium coin cell batteries.

<a id='9e88d0c4-09e1-4c88-91cb-4988f1805375'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='861249d5-7199-46c1-84b8-96729b8279a0'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='45212e04-f0ff-4156-b0e2-3e7ed8c9e11d'></a>

Help

<a id='ef3477ed-939f-41c9-829e-71dc47f8f8e0'></a>

1/9

<a id='b05ae062-93bb-4245-a01a-22271aa499a7'></a>

ON THIS PAGE

* Usage/Examples
* Compatibility
* Releases
* BLE class
* BLEDevice Class
* BLEService Class
* BLECharacteristic
* BLEDescriptor Clas