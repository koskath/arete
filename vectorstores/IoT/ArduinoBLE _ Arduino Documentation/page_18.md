<a id='598e2eb4-fedc-43e0-a462-149924678bb4'></a>

12/4/25, 2:49 PM

<a id='a1bdc9be-9c24-4d72-9172-b04f59c6d041'></a>

ArduinoBLE | Arduino Documentation

<a id='87d0ca35-f8be-4131-af2b-11ea3b5597f8'></a>

ARDUINODOCS

<a id='d7e5a6d7-14c6-42dd-8967-6d2ec56bc5d4'></a>



<a id='6332eb83-17c5-40f0-9acd-ff5220340e47'></a>

```
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energ");
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...
}
```

<a id='6790fd3c-1561-4292-8b89-e0cb6afc66f0'></a>

Was this article helpful?

---

option Like: [ ]
option Dislike: [ ]

<a id='71873b81-f1b8-45d4-8421-c6f6f8b2bcd4'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='f8cacc53-c4f2-41da-aa5f-1e0b6bbea715'></a>

 2025 Arduino

<a id='36cfbbdf-b6e6-46d1-819c-c3e2ea029e08'></a>

Terms Of Service Privacy Policy Security Cookie Settings

<a id='87b97e58-d420-422d-8b75-be84125218af'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='46a096c7-3076-4bba-baa5-abb893d3680b'></a>

26/26