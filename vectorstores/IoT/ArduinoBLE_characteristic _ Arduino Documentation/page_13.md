<a id='9d873977-5cf9-41f2-9bd7-d4bf543df5e0'></a>

12/4/25, 2:50 PM

<a id='63e0a693-b14f-4898-a497-6e25b0df2835'></a>

ArduinoBLE | Arduino Documentation

<a id='1d66b59c-d665-45f4-88aa-e3e7f53d645d'></a>

ARDUINODOCS

<a id='bf93bcc4-2853-4c62-9557-3fc6588ad524'></a>

```c
// Bluetooth® Low Energy LED Switch Characteristic
BLEByteCharacteristic switchCharacteristic("19B

// listen for Bluetooth® Low Energy peripheral:
BLEDevice central = BLE.central();

// if a central is connected to peripheral:
if (central) {
  Serial.print("Connected to central: ");
  // print the central's MAC address:
  Serial.println(central.address());
}

// while the central is still connected to |
while (central.connected()) {
  // if the remote device wrote to the characteristic
  // use the value to control the LED:
  if (switchCharacteristic.written()) {
    if (switchCharacteristic.value()) {
      Serial.println("LED on");
      digitalWrite(ledPin, HIGH);
    } else {
      Serial.println(F("LED off"));
      digitalWrite(ledPin, LOW);
    }
  }
}
```

<a id='6472e130-383e-479c-81d5-9bfb451fc7c4'></a>

bleCharacteristic.subscribed()

Query if the characteristic has been subscribed to by another Bluetooth® Low Energy device.

## Syntax

```
1 bleCharacteristic.subscribed()
```

<a id='9d9fa796-d8ea-45ae-ac84-31db756e2927'></a>

Parameters

None

<a id='b5a3860e-10b0-4942-91b0-084e0a843e2e'></a>

## Returns

**true** if the characteristic value has been subscribed to by another Bluetooth® Low Energy device,
**false** otherwise

<a id='b55a7116-d9de-40c4-84d5-9dd904ce00fc'></a>

Example

---

<a id='2c83e347-005a-420b-bb74-5f6369bfde50'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='56e37bb4-95da-480a-a037-978d6210ecf0'></a>

13/22