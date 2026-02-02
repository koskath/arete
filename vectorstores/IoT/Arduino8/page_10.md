<a id='4016af1f-1b7d-4779-8097-85e92bbf1788'></a>

12/4/25, 2:52 PM

<a id='6cdc9ce7-7b8e-4fc5-a75a-0da7ef52a91c'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='5ab6016a-36fd-4e4f-9092-12bf43669ac1'></a>

ARDUINODOCS

<a id='3a914906-e348-47c0-9f27-b29568f24286'></a>

```c
/*
 SigFox First Configuration

 This sketch demonstrates the
 Since the board is designed

 This example code is in the
*/

#include <SigFox.h>
#include <ArduinoLowPower.h>

void setup() {
 Serial.begin(9600);
 while (!Serial) {};

 // Uncomment this line and
 //if (!SigFox.begin(SPI1, 3))
 if (!SigFox.begin()) {
 Serial.println("Shield error");
 return;
 }
 // Enable debug led and disable
 // Comment this line when shipping
 SigFox.debug();

 String version = SigFox.SigfoxVersion();
 String ID = SigFox.ID();
```

<a id='e323c98a-36fd-4c8d-ad7d-c6e641f1883c'></a>

Was this article helpful?
---
option Thumbs up: [ ]
option Thumbs down: [ ]

<a id='d063b06e-77d2-4497-8de4-5e772022df50'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='6eedbb39-805e-4812-b050-d8670fed9f33'></a>

 2025 Arduino

<a id='d611ad4c-ba35-4852-b2c6-79e288fc1451'></a>

Terms Of Service Privacy Policy Security Cookie Settings

<a id='9325da7f-a1fc-453d-98bd-2bf5f62c3f0d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='c18562bc-84bf-4d44-8992-9073d073dcf8'></a>

13/13