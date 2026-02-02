<a id='bef74c83-7928-4aec-8adf-a17bad4ae902'></a>

12/4/25, 2:52 PM

<a id='8be368e7-b4f3-4fe2-9a77-561efab87f8d'></a>

WiFiNINA | Arduino Documentation

<a id='0891a047-b75c-4615-ad05-d075a0ec391c'></a>

ARDUINODOCS

<a id='2219a809-8a4e-42d3-a7a4-db73bb35bd8c'></a>

```
/*
This example connects to an
Then it prints the MAC address and
the IP address obtained, and
Then it continuously pings

Circuit:
* Board with NINA module (Arduino

created 13 July 2010
by dlf (Metodo2 srl)
modified 09 June 2016
by Petar Georgiev
*/
#include <SPI.h>
#include <WiFiNINA.h>

#include "arduino_secrets.h"
//////// please enter your credentials in arduino_secrets.h
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int status = WL_IDLE_STATUS;

// Specify IP address or host
String hostName = "www.google.com";
int pingResult;

void setup() {
  // Initialize serial and wait for port to open:
```

<a id='40775030-5bde-4b7b-8d50-fc275ed0829f'></a>

v WiFi.status()

<a id='c2156440-bc23-4f16-b01c-d4c979d92b0f'></a>

### Description

Return the connection status.

<a id='1b449024-f863-4520-93d9-f23de9d8e58e'></a>

Syntax

```
1 WiFi.status()
```

<a id='5cfdb222-8bb2-4be8-921e-ed359f752660'></a>

Parameters

None

<a id='6b7c0af0-8100-4286-852d-7b1fa3f4b09c'></a>

Returns

WL_CONNECTED: assigned when
connected to a WiFi network;

WL_AP_CONNECTED: assigned when a
device is connected in Access Point
mode;

WL_AP_LISTENING : assigned when the
listening for connections in Access
Point mode;

<a id='80986064-760a-4ef3-81b0-4b24f05ee47f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='7e6a2bad-41af-4b3e-9b86-4f5e83caf0e0'></a>

19/30