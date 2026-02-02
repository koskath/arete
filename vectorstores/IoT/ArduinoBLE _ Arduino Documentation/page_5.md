<a id='75e2eddc-88b8-49b0-85db-499716f0b4a6'></a>

12/4/25, 2:49 PM

<a id='599b2167-4b3f-4435-8154-7753a73d65ee'></a>

ArduinoBLE | Arduino Documentation

<a id='3c6e70c3-ef90-4f20-89d0-1b9d41459fe8'></a>

ARDUINODOCS

<a id='12bf651d-11b1-412a-8406-cd02919728a0'></a>

<::An empty rectangular box
: figure::>

<a id='aa05fa40-d081-4414-96ba-a94246a0160a'></a>

Used to enable the Bluetooth® Low Energy module.

<a id='bb307528-aaf2-4e69-aa05-05f2346d2b26'></a>

## BLE.begin()
Initializes the Bluetooth® Low Energy device.

### Syntax
```
BLE.begin()
```

### Parameters
None

### Returns
1 on success
0 on failure

### Example
```c
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy");
  while (1);
}
```

<a id='212cb315-620d-4285-8293-99caf94ee258'></a>

### BLE.end()
Stops the Bluetooth® Low Energy device.

### Syntax
```
1 BLE.end()
```

### Parameters
None

### Returns
Nothing

<a id='122647de-d672-43e9-a68c-3bce5dd62b3b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='0da38d62-c20d-40ed-ac06-f8ff3b968c5a'></a>

5/26