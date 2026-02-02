<a id='bad69d66-641c-451c-89de-bd562f78c104'></a>

12/4/25, 2:52 PM

<a id='68fa49d9-a129-4b3b-8c5f-6f1132f8f06f'></a>

WiFiNINA | Arduino Documentation

<a id='83583e31-df03-4f1d-a4be-a08feb45b8c9'></a>

ARDUINODOCS

<a id='4afcdfff-c976-4384-ae94-30ee63265b5c'></a>

## Description

Initializes the WiFiNINA library's network settings and provides the current status.

<a id='53e5f66a-d88e-4c6a-8a0c-4db9fc3da0b7'></a>

Syntax

```
1 WiFi.begin(ssid);
2 WiFi.begin(ssid, pass);
3 WiFi.begin(ssid, keyIndex, key)
```

<a id='b11b90c5-a86f-4f62-8b13-4a55ba0949b7'></a>

# Parameters

ssid: the SSID (Service Set Identifier) is
the name of the WiFi network you
want to connect to.

<a id='afde4903-e8eb-4ced-bf00-d15d9a19686e'></a>

keyIndex: WEP encrypted networks can hold up to 4 different keys. This identifies which key you are going to use.

<a id='bd22af35-2e90-4315-aacf-5a8309787e5e'></a>

key: a hexadecimal string used as a security code for WEP encrypted networks.

<a id='d47e54a9-ffe3-4095-a5de-89dd0614d8ed'></a>

pass: WPA encrypted networks use a
password in the form of a string for
security.

<a id='eb7bd3fb-30f3-4970-b551-82abb70089ff'></a>

## Returns

WL_CONNECTED when connected to a network

WL_IDLE_STATUS when not connected to a network, but powered on

<a id='6986567f-8f7d-43f2-98f2-2d966cf7b175'></a>

Example

```
1 #include <WiFiNINA.h>
2
3 //SSID of your network
4 char ssid[] = "yourNetwork";
5 //password of your WPA Network
6 char pass[] = "secretPassword";
7
8 void setup()
9 {
10   WiFi.begin(ssid, pass);
11 }
12
13 void loop () {}
```

<a id='24be27b1-d0ed-4a4e-862b-3550ab21410d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='eba433b7-7e9b-4e40-9da2-4f864986fec4'></a>

2/30