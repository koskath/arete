<a id='eec32a84-731e-4f64-b95f-bba3637de7d4'></a>

12/4/25, 2:51 PM

<a id='20abcde3-d678-4eed-8fa2-d04503d4b913'></a>

ArduinoBLE | Arduino Documentation

<a id='e92c5f37-9567-45ef-bfe5-179e804c49d7'></a>

ARDUINODOCS

<a id='f458ff77-68fe-42e0-88dc-cf7bb3eefeb4'></a>



<a id='f98bd20e-626d-4541-be27-0a45b16347d5'></a>

```cpp
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Ene
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...

  // print the advertised service UUIDs, if p
  if (peripheral.hasAdvertisedServiceUuid())
    Serial.print("Service UUIDs: ");
    for (int i = 0; i < peripheral.advertised:
      Serial.print(peripheral.advertisedServi
      Serial.print(" ");
    }
    Serial.println();
}
//
```

<a id='97420243-2ba1-4105-8cd9-f7ab9e8e770a'></a>

## bleDevice.localName()
Query the local name a discovered Bluetooth® Low Energy device is advertising with.

### Syntax
```
1 bleDevice.localName()
```

### Parameters
Nothing

### Returns
Advertised local name (as a String).

### Example

<a id='9cd11ebb-1ea9-43af-a5bb-a7dfc3329e0c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='0e4b41da-cbe9-477c-884c-2571b2aed96b'></a>

21/24