<a id='c5a7ef41-390b-4028-a1d5-84933699f37d'></a>

12/4/25, 2:51 PM

<a id='3491cde2-8433-447c-a812-37b840d29254'></a>

ArduinoBLE | Arduino Documentation

<a id='7d67bc2f-aadc-403d-8d6a-bae5435d242b'></a>

ARDUINODOCS

<a id='4a656b02-749b-4d6e-aa8f-b5f3df9eed68'></a>

<::transcription of the content
: empty text box::>

<a id='1c0ded36-3c50-4793-b5ba-a89626266f91'></a>

Disconnect the Bluetooth® Low Energy device, if connected

## Syntax

```
1 bleDevice.disconnect()
```

<a id='651fa749-0855-4bcc-b83c-9642595d4299'></a>

**Parameters**

None

<a id='ab692a25-0193-4fe7-b528-00e81b08a397'></a>

## Returns

**true** if the Bluetooth® Low Energy device was disconnected,
otherwise **false**.

<a id='0ea13d79-422f-4227-8592-afa0279fde34'></a>

Example

```
1 // listen for Bluetooth® Low Energy centrals to co
2 BLEDevice central = BLE.central();
3 
4 
5 central.disconnect();
```

<a id='fa6708c9-657d-44a0-b886-c1828aa4653e'></a>

✓ bleDevice.address()
Query the Bluetooth® address of the Bluetooth® Low Energy device.

<a id='bd0b8376-1d8e-43ad-9d57-0f5d012a5fe2'></a>

## Syntax

```
1 bleDevice.address()
```

<a id='0657d562-df6f-4bb9-8dd0-2353e6f25755'></a>

Parameters

None

<a id='edc3ee1c-b402-4466-89d8-2d5c0abf7527'></a>

## Returns

**Bluetooth® address** of the Bluetooth® Low Energy device (as a String).

<a id='6e16a248-b0e7-43b1-bb61-b859b77d3789'></a>

Example

<a id='71045ca0-3779-4aba-a3f7-7a36586c59b9'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='d933d4ed-1cd9-47e0-a306-ceaa38d3ca91'></a>

7/24