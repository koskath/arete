<a id='b0fbbb67-d0eb-4429-9a8b-3db2c9858199'></a>

12/4/25, 2:52 PM

<a id='96e90d48-9c04-45da-b030-864c26c88ec2'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='c8b1213e-3ab6-4f17-a654-bf9dcd56cb0e'></a>

ARDUINODOCS

<a id='785874a7-69d9-4d6c-b56a-f65d8226d992'></a>

## Syntax

```
1 SigFox.begin();
```

<a id='8c6f92cc-9e24-46c9-87d3-fad10c89fa83'></a>

Parameters

None

<a id='841d28e6-6c30-4cd4-8e46-9e93923b5211'></a>

## Returns
true if correctly configured, false otherwise

<a id='17402491-3c2d-4ff0-ba2f-5ac250d2aba0'></a>

# Example

```
1 #include <SigFox.h>
2 #include <ArduinoLowPower.h>
3 
4 void setup() {
5   Serial.begin(115200);
6   while (!Serial) {};
7 
8   if (!SigFox.begin()) {
9     Serial.println("Shield error");
10    return;
11  }
12 
13 void loop() {
14 }
```

<a id='1165aeca-5c25-4d61-9eb4-d86f844f75d9'></a>

SigFox.beginPacket()

<a id='065fa427-2b3e-4915-a743-9bd028dbf7bd'></a>

**Description**

Begins the process of sending a packet

<a id='9445a51f-c7ca-44c7-a383-093ba1fe7cdb'></a>

## Syntax

```
1 SigFox.beginPacket();
```

<a id='b87d5e6f-9283-45cc-b849-2d77726f19a9'></a>

**Parameters**
None

<a id='bef4712c-d679-4d6c-935f-45993e556e65'></a>

Example

<a id='b3821720-4c66-4a17-b434-8ede59098355'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='23f3eb6e-367a-4adc-a787-f7562fe909c7'></a>

2/13