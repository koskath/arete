<a id='15eedcd6-5145-463e-9a14-a136005fd088'></a>

12/4/25, 2:52 PM

<a id='b1b8791f-9758-4b4e-b30a-6e13007a7eb2'></a>

WiFiNINA | Arduino Documentation

<a id='ac8183f0-7906-469f-a0cb-626cbbaf757f'></a>

ARDUINODOCS

<a id='9b8d78e0-4b57-4e2b-baaf-2cbf249d76cc'></a>

```c
#include <SPI.h>
#include <WiFiNINA.h>

//SSID of your network
char ssid[] = "yourNetwork";
//password of your WPA Network
char pass[] = "secretPassword";

void setup() {
  WiFi.begin(ssid, pass);

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Couldn't get connected");
    while(true);
  }
  // if you are connected, print
  else {
    // print the received signal
    long rssi = WiFi.RSSI();
    Serial.print("RSSI:");
    Serial.println(rssi);
  }
}

void loop () {}
```

<a id='82aaed40-1442-4f7c-90e8-c77d5c55edd6'></a>

option WiFi.channel(): [ ]

<a id='0232e4c7-7065-433a-8b21-1cb3eaf9888f'></a>

## Description
Gets the WiFi channel of a network that was scanned.

<a id='c40cfd80-aeb5-46c6-b4dc-356e03c35abf'></a>

## Syntax

```
1 WiFi.channel(wifiAccessPoint)
```

<a id='10fe7650-41d8-4ec3-bfe5-a068d3688ec7'></a>

## Parameters

wifiAccessPoint - specifies from which
network to get the information

<a id='129be353-2781-4b79-8294-2d565055c43a'></a>

Returns

WiFi channel of scanned network

<a id='6fdf75e9-9cf6-49ce-b0bc-f9cf0eba4a1a'></a>

Example

________________________________________________________________________________

<a id='7fd9a584-fd3d-4df3-b4b1-b02bc18d2892'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='fbc82e3b-9db5-41fc-9219-4a588cbb1e7b'></a>

14/30