<a id='cb09f4a7-64c0-4d54-ba7c-b83a88ed84f2'></a>

12/4/25, 2:49 PM

<a id='4270cdb9-75e8-4807-811c-3821f7358b91'></a>

ArduinoBLE | Arduino Documentation

<a id='716785b4-58cf-4639-b96b-006bfccffbd8'></a>

ARDUINODOCS

<a id='636d2f97-d12b-46b2-b6fe-6065f5d8c030'></a>

Set the appearance in the built in appearance characteristic. If not set, the value defaults to 0x0000.

### Syntax
```
BLE.setAppearance(appearance)
```

### Parameters
appearance: appearance value

### Returns
Nothing

### Example
```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ
4 while (1);
5 }
6 
7 BLE.setAppearance(0x8000);
8 
9 // ...
10 
11 // start advertising
12 BLE.advertise();
```

<a id='d2bd51dc-8a58-49e9-8304-b8940f54d051'></a>

BLE.addService()

<a id='81d33b0b-a126-49e2-b4e9-959e12159307'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='7a47e104-74f9-48ba-9e5b-805b6c7dc2b5'></a>

14/26