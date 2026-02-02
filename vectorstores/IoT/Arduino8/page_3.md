<a id='fdeeeff5-0844-4028-947e-bc86c7e7bad4'></a>

12/4/25, 2:52 PM

<a id='59139d85-255d-4448-b153-2901d895556c'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='2e1a1199-5735-434d-a783-1d46e1e1a92c'></a>

ARDUINODOCS

<a id='4527386b-e9fa-4dc0-be65-88fba45cd156'></a>

#include <SigFox.h>
#include <ArduinoLowPower.h>

void setup() {
 Serial.begin(115200);
 while (!Serial) {};

 if (!SigFox.begin()) {
  Serial.println("Shield error");
  return;
 }
}

void loop() {
 SigFox.begin();
 SigFox.beginPacket();
 SigFox.print("123456789012");
 int ret = SigFox.endPacket();
 if (ret == 0)
  Serial.println("OK");
 else
  Serial.println("KO");
 while (1);
}

<a id='c6a3ff46-3d98-40b6-b573-2abfbe2774cf'></a>

SigFox.parsePacket()

<a id='5991b3bc-80e5-4412-9607-e46ee983fa8e'></a>

## Description
Checks for the presence of a SigFox packet, and reports the size. parsePacket() must be called before reading the buffer with SigFox.read().

<a id='e74e33ff-34e9-42de-8f3c-99f3f4561a24'></a>

## Syntax

```
1 SigFox.parsePacket()
```

<a id='6f96e4ce-6433-4a1e-9e4d-ba52b02309c4'></a>

**Parameters**

None

<a id='999ae2d4-7aa1-44d7-9b29-0df0e340914d'></a>

## Returns

int: the size of a received SigFox packet

<a id='a4d03f03-c8ed-4de7-8efb-1d8acd1b6b11'></a>

v SigFox.statusCode()

# Description

Returns the protocol status code

<a id='4e3ccda2-9c68-4495-b403-67f51dbb8d89'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='02aaa3cb-5ab0-4cab-980f-2516a1349df6'></a>

5/13