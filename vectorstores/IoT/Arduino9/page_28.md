<a id='4f29e42c-7c9f-4f0b-b687-a3570caedbfe'></a>

12/4/25, 2:52 PM

<a id='d10a5a39-0c14-4362-9fba-6a826456e265'></a>

WiFiNINA | Arduino Documentation

<a id='d4363d70-c98a-4ae3-a614-06795f1d10c3'></a>

ARDUINODOCS

<a id='29aab0ff-35a9-45af-b0cf-e22f99c8cc98'></a>

```cpp
#include <WiFiNINA.h>

#include "arduino_secrets.h"
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;

IPAddress emptyIP;

void setup() {
  Serial.begin(115200);
  while (!Serial) {}

  Serial.print("Attempting to ");
  Serial.println(ssid);
  int status = WiFi.begin(ssid, pass);
  if (status != WL_CONNECTED) {
    Serial.println("Couldn't connect");
    while(true);
  }

  Serial.print("DHCP assigned ");
  IPAddress dns1 = WiFi.dnsIP();
  if (dns1 == emptyIP) {
    Serial.println("not set");
  } else {
    dns1.printTo(Serial);
    Serial.println();
  }
  // ... code continues
}
```

<a id='22ac221b-9df2-48dc-be4d-e52e4d0652fc'></a>

WiFi.getTime()

<a id='84c5a9b6-f78c-4b3e-a0a6-ba41222f944b'></a>

# Description

Get the time in seconds since January 1st,
1970. The time is retrieved from the WiFi
module which periodically fetches the NTP
time from an NTP server.

<a id='37647c0a-4af0-4ba4-8132-8e9a880975e4'></a>

## Syntax

```
1 WiFi.getTime();
```

<a id='63f5c687-84e0-41da-95b5-a6757663c944'></a>

Parameters

None

<a id='6a4e2d83-bdd1-489b-a099-8bf218507b04'></a>

# Returns

Returns the time in seconds since January 1st, 1970 on success. O on failure.

<a id='56d3f5ff-a268-4ca1-b402-68d0d8cf0c7e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='e3a675c0-a0df-44ef-a7f1-cd193a16b5bd'></a>

29/30