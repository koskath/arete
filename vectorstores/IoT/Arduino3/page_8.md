<a id='60cc001d-8311-4ecb-b380-9f9b06b9a9be'></a>

12/4/25, 2:51 PM

<a id='a291cb01-cca6-4ebf-93f5-c483f240a391'></a>

ArduinoBLE | Arduino Documentation

<a id='841149bf-51ca-4f9f-a4c3-8593dbbf1766'></a>

ARDUINODOCS

<a id='505b4c7f-376f-420a-9245-0aff4749beda'></a>

___

<a id='c6047601-724b-4e3b-9bc6-bcc4dc078f7d'></a>

index: optional, index of characteristic to check if the device provides more than on. Defaults to 0, if not provided.

<a id='e35d10c2-f7cc-4eb8-87f5-30050ca29314'></a>

## Returns

**true**, if the service provides the characteristic,
**false** otherwise.

<a id='5c513e8f-6b8e-4d7a-ac0b-2b7c9946fef2'></a>

Example

```
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy");
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

  // discover peripheral attributes
  Serial.println("Discovering attributes ...");
  // ... (rest of code is cut off)
```

<a id='4abffbc8-e710-4186-af77-b468aeca8e46'></a>

- bleService.characteristic()
  Get a BLECharacteristic representing a Bluetooth® Low Energy characteristic the service provides.

<a id='9209d578-5c61-4a6b-ba91-4e01aadda733'></a>

Syntax

```
1 bleService.characteristic(index)
2 bleService.characteristic(uuid)
3 bleService.characteristic(uuid, index)
```

<a id='1dce9e07-6213-49e7-9b9f-94bd630cffd4'></a>

Parameters

<a id='2986fae7-bd9b-4aae-822d-2d785c5b1448'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='58a618c1-2951-4bda-8a1d-f810b451cbfc'></a>

8/9