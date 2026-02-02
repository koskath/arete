<a id='e378eb63-bc6d-4af6-b1b3-7bfd470712f8'></a>

12/4/25, 2:49 PM

<a id='fc0b8636-e3c2-4b55-832a-b184084898d7'></a>

ArduinoBLE | Arduino Documentation

<a id='bc6e83ee-cabf-408d-b41d-1179e3c0b813'></a>

ARDUINODOCS

<a id='2f6ca508-3357-403a-a47e-e43e3b4d177e'></a>

An empty rectangular box.

<a id='de72cb4b-a4fb-4fae-a358-71058e9950ba'></a>

### Syntax

```
1 BLE.setAdvertisingInterval(advertisingInterval)
```

<a id='a78304a6-7037-4a4b-9ac7-ba023ce405c6'></a>

## Parameters

**advertisingInterval**: advertising interval in units of 0.625 ms

<a id='bce68962-b8b1-4859-85dd-ab92c9ab4240'></a>

Returns

<a id='99cd7ad4-549e-4083-bb27-a9ffd1b8038f'></a>

Nothing.

<a id='15805274-9e72-48cd-b4a8-7f003f1cd0d5'></a>

Example

```
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energ
  while (1);
}

// ...

BLE.setAdvertisingInterval(320); // 200 * 0.625
BLE.advertise();
```

<a id='f998d4b8-4cb0-47fd-9af3-bb98c857e539'></a>

BLE.setConnectionInterval()

<a id='6c641e39-6234-40e1-9cae-e5a047607bb7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='9ff76e12-6329-4ad4-877c-5479e182e5e8'></a>

18/26