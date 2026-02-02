<a id='b612d708-cc86-45c8-b7c9-a5ddc56b73f9'></a>

12/4/25, 2:51 PM

<a id='81a28c42-a0c1-4a0d-b490-b784b4b895e0'></a>

ArduinoBLE | Arduino Documentation

<a id='c79f951e-bcd0-4818-9526-bbb6b143af28'></a>

ARDUINODOCS

<a id='94c84597-ca1c-49b5-ad97-32aaa553c715'></a>



<a id='403aae55-df21-4613-85de-b6b5a3438d51'></a>

```cpp
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy setup failed!");
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

<a id='d3b4950f-8625-4d16-893a-c48eea1fcaf4'></a>

bleDevice.serviceCount()

Query the number of services discovered for the Bluetooth® Low Energy device.

### Syntax

```
1 bleDevice.serviceCount()
```

<a id='5e647eee-c7ea-495a-a6c6-3a9bd281ec43'></a>

Parameters

None

<a id='84ff523d-6f03-46b5-81b7-49da6ff104df'></a>

### Returns

The number of **services discovered** for the Bluetooth® Low Energy device.

<a id='29ad44ff-b6d7-49a5-83d3-305f7174ff2e'></a>

Example

<::text: empty input box::>

<a id='1f094404-b91a-4cb1-96c8-30252b4664a3'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='df611c91-d0d4-4097-9be3-c9620e113376'></a>

13/24