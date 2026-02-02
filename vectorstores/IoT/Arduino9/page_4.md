<a id='c5d93a0c-be5c-4d63-a1f9-57423b27f7c6'></a>

12/4/25, 2:52 PM

<a id='3680016f-f8a9-4eb3-bc16-84d507e05f42'></a>

WiFiNINA | Arduino Documentation

<a id='e8c61eb3-e6c7-4e7f-ac92-0d0ff9eb862d'></a>

ARDUINODOCS

<a id='6f992d19-c77d-470a-b90b-1b2d671d786b'></a>

channel 1;

## Returns

WL_AP_LISTENING when creating
access point succeeds
WL_CONNECT_FAILED when creating
access point fails

<a id='0f485ec3-5111-4cf3-8d69-8ce02f7d01d8'></a>

Example

```
1 /*
2
3 WiFi Web Server LED Blink
4
5 A simple web server that le
6 This sketch will create a n
7 It will then launch a new s
8 to the Serial Monitor. From
9 to turn on and off the LED
10
11 If the IP address of your b
12 http://yourAddress/H turn
13 http://yourAddress/L turn
14
15 created 25 Nov 2012
16 by Tom Igoe
17 adapted to WiFi AP by Adafr
18 */
19 #include <SPI.h>
20 #include <WiFiNINA.h>
21 #include "arduino_secrets.h"
22 /////please enter your sens
23 char ssid [] = SECRET_SSID;
24 char pass [] = SECRET_PASS;
25 int keyIndex = 0;
26
27 int led = LED_BUILTIN;
28 int status = WL_IDLE_STATUS;
```

<a id='b54b9a53-6cf5-4115-8f0c-518566b4d566'></a>

v WiFi.beginEnterprise()

<a id='cacecd1c-c483-40e2-a41e-7f415171fc44'></a>

# Description
Initializes the WiFININA library's network settings for a common WPA2 Enterprise network with username and password authentication (PEAP/MSCHAPv2).

<a id='459062f4-fb9a-46a3-96cd-26fd49504a9e'></a>

Note: this feature requires NINA firmware
version 1.3.0 or later. All string parameter
supplied must have a combined length of
under 4000 bytes.

<a id='e5171a18-e2a1-4ac8-94aa-58e540d8f2b6'></a>

Syntax

<a id='8146a189-8d61-4229-8fc1-89d65095850f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='db8b764c-2e93-41e3-afb4-f72875326ae8'></a>

4/30