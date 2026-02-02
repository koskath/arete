<a id='a3bef749-1a62-4116-a78d-a31ffc387761'></a>

12/4/25, 2:51 PM

<a id='9979ac99-35d1-446a-998f-f00629d8fa4f'></a>

ArduinoBLE | Arduino Documentation

<a id='b34d2cce-c74c-440c-b3ff-675081c538cc'></a>

ARDUINODOCS

<a id='1ee54206-a012-46c3-8883-7dea89c1aa61'></a>

## Parameters

None

## Returns

**true**, if successful,
**false** on failure.

<a id='beab9954-0cb5-4201-9478-316663eae6b8'></a>

Example

```c
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
}

// discover peripheral attributes
Serial.println("Discovering attributes...");
```

<a id='5a8adcec-167c-4bb2-b048-a8d66b965447'></a>

### bleDevice.discoverService()

Discover the attributes of a particular service on the Bluetooth® Low Energy device.

## Syntax

```
1 bleDevice.discoverService(serviceUuid)
```

<a id='f4a4aeca-144a-4ec2-a8cd-37ececb06d27'></a>

Parameters

<a id='4d9daced-bf31-4ab5-96b8-d655cc394a9b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='32e04844-c7f7-49b8-817f-a0034c0dd19f'></a>

10/24