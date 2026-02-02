<a id='79c9770a-f417-4cb4-9b87-7b6cbc70df7c'></a>

12/4/25, 2:51 PM

<a id='848f5f41-de59-410d-93f8-064c5e44b8ad'></a>

ArduinoBLE | Arduino Documentation

<a id='12807490-63fb-4cd1-9c76-8b5e4f74da44'></a>

ARDUINODOCS

<a id='38e75ef5-7fe0-4c0a-baf5-72d4a9317441'></a>



<a id='c3ea867f-8ea2-4d3a-8b20-ceab654c791c'></a>

// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy...");
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
// ...

<a id='866ea623-84c2-4813-8608-cc708e9589a7'></a>

Was this article helpful?

---

option Thumbs up: [ ]
option Thumbs down: [ ]

<a id='87ab46fa-7209-4a27-8809-9bc828d82882'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='f068e882-cbc4-495d-af32-165345d83dc2'></a>

© 2025 Arduino

<a id='053b0c9a-9408-48e1-9f71-28c183f36c8a'></a>

Terms Of Service

Privacy Policy

Security

Cookie Settings

<a id='8eb4d830-0c32-4425-be12-f40816e3ce7f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='172fd2d5-4997-4b56-968a-b2cd1107bf35'></a>

24/24