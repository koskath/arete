<a id='d7a26b4f-bdc9-4c49-9e07-e921e03aed18'></a>

12/4/25, 2:50 PM

<a id='ebf42978-302f-4db5-bdfd-6953b19b7b7c'></a>

ArduinoBLE | Arduino Documentation

<a id='29f91fde-86cf-4cc1-891b-762b3a91ee4e'></a>

ARDUINODOCS

<a id='4326a875-ac79-493a-9478-46e652841366'></a>

```c
1 while (peripheral.connected()) {
2   // while the peripheral is connected
3
4   // check if the value of the simple key characteristic
5   if (simpleKeyCharacteristic.valueUpdated()) {
6     // yes, get the value, characteristic is 1
7     byte value = 0;
8
9     simpleKeyCharacteristic.readValue(value);
10
11    if (value & 0x01) {
12      // first bit corresponds to the right button
13      Serial.println("Right button pressed");
14    }
15
16    if (value & 0x02) {
17      // second bit corresponds to the left button
18      Serial.println("Left button pressed");
19    }
20  }
21 }
```

<a id='4489552a-43ac-4956-aace-29b2c055f61a'></a>

Was this article helpful?

option Thumbs Up: [ ]
option Thumbs Down: [ ]

<a id='cc45b29d-85b0-4948-94d0-724cedd07e96'></a>

Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='d787c582-c43d-456c-94c9-434d5c04fff9'></a>

© 2025 Arduino

Terms Of Service Privacy Policy Security Cookie Settings

<a id='300e5d8b-0def-4bde-b9e9-0b43ead751a0'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='4bccb0ca-c80e-4909-a561-1d40f07407a2'></a>

22/22