<a id='d139f0b1-282e-4631-8c98-eb8b9fb0ed3c'></a>

12/4/25, 2:50 PM

<a id='ad91adff-f367-4d70-9c45-54ee3a074d88'></a>

ArduinoBLE | Arduino Documentation

<a id='188fb5a4-b6ce-4eca-bea2-e5e96e421a3c'></a>

ARDUINODOCS

<a id='fd57bc26-814f-4633-93a4-eb1699a92e7b'></a>

Search on Docs /

<a id='aa337ae4-d7b1-4efe-a621-b66f7bcb1b17'></a>

← Go Back

## Library

<a id='f582dda6-9c05-4d82-a146-29e61199f285'></a>

Recents viewed

<a id='980bebc4-16b5-43cd-b606-f14155f7d567'></a>

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

<a id='7e65a48a-0740-45f0-a0d1-6de6ed07db75'></a>

Home / Programming / Library / ArduinoBLE

<a id='01915786-ddd6-4951-8f14-7abfa2e282e6'></a>

COMMUNICATION

# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>

https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='d31c79f3-c1cf-4150-b682-bad5bad8963c'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='18d0f3f4-032a-419d-9950-3bcc74dc109b'></a>

GO TO REPOSITORY

<a id='291c07b7-38cd-4fd2-9a47-5527fcdc0d24'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='b2b53c9f-15f4-4942-a0c1-62dead893760'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='a3a8d1b0-61e5-4b6e-bf38-125eaa4f6055'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled
"Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low
Energy is optimized for low power use at low data rates, and was
designed to operate from simple lithium coin cell batteries.

<a id='fc805117-9f4d-471b-b7be-d4b47b9d5093'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='1a7df304-7244-4a16-aab2-5a694fdaac0e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='6a26eaaf-3282-47ad-9ca2-786857858eae'></a>

Help

<a id='8a886a8c-2906-4236-87ca-a533e43bd183'></a>

1/22

<a id='1b9182d7-f752-4152-b0e2-bbd068a4fa74'></a>

ON THIS PAGE

*   Usage/Examples
*   Compatibility
*   Releases
*   BLE class
*   BLEDevice Class
*   BLEService Class
*   BLECharacteristic
*   BLEDescriptor Clas