<a id='87d84770-f8aa-4f61-9c84-191292c30b6a'></a>

12/4/25, 2:51 PM

<a id='6276abd1-5a04-4f70-9e8a-b25236ae5b7a'></a>

ArduinoBLE | Arduino Documentation

<a id='96749d7e-4193-40ea-836a-d9cb1c3af0e0'></a>

ARDUINODOCS

<a id='ff79b52d-32ae-4e78-8653-bcc875298000'></a>

A very faint, light grey rectangular outline is visible in the center of the image, appearing empty.

<a id='238a0857-e618-41ed-9761-49a88b5d5720'></a>

// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy...");
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...

  Serial.println("Connecting ...");

  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }
}

// discover peripheral attributes

<a id='1108230d-6f74-4552-a434-c2ee54fecec4'></a>

v bleDevice.hasCharacteristic()
Query if the Bluetooth® Low Energy device has a particular characteristic.

<a id='eed2ae10-8bf1-4712-8235-7375e76633aa'></a>

## Syntax

```
1 bleDevice.hasCharacteristic(uuid)
2 bleDevice.hasCharacteristic(uuid, index)
```

<a id='034686ef-2088-4ec8-a9a7-cd2cf6839b7e'></a>

## Parameters

**uuid**: uuid to check (as a **String**)

**index**: optional, index of characteristic to check if the device
provides more than on. Defaults to 0, if not provided.

<a id='37c4fb5a-84a2-4948-a197-aa12b1cac396'></a>

## Returns

**true**, if the device provides the characteristic,
**false** otherwise.

<a id='3d30bfbd-6436-4e87-879d-a6e2cdaae062'></a>

Example

<a id='f4e692e6-08d3-448e-b48e-df98ec25a42d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='8cd2d6a0-79be-4ce5-8abc-5becb4e03d6d'></a>

17/24