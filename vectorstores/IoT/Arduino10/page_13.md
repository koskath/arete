<a id='b8b5d425-0cf0-49dd-9a8d-3ff050d1ce5a'></a>

12/4/25, 2:52 PM

<a id='cd90b600-b744-4895-bc3c-0be0b0f48afe'></a>

WiFiNINA | Arduino Documentation

<a id='1df0594b-06fd-4829-ae13-4a30794da769'></a>

ARDUINODOCS

<a id='d054ecc2-11ed-4134-9b91-33f1b3f09ad7'></a>

Example
```c
...
#include <SPI.h>
#include <WiFiNINA.h>

#include "arduino_secrets.h"
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int keyIndex = 0;

int status = WL_IDLE_STATUS;
char server[] = "www.google.c


WiFiClient client;

void setup() {
  //Initialize serial and wai
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  if (WiFi.status() == WL_NO_
    Serial.println("Commu
    while (true);
  }
}
while (status != WL_CONNECT
```

<a id='0ac6a2fb-e5ea-454f-95a2-0459bd13b4f4'></a>

<::A dropdown icon followed by the text "client.read()": figure::>

<a id='06189fcf-15a9-433b-bab8-ad529f8cc890'></a>

## Description
Reads data from the client. If no arguments are given, it will return the next character in the buffer.

<a id='5bd79469-6d2d-4dba-bdd6-827d56b823f4'></a>

## Syntax

```
1 client.read()
2 client.read(buffer, size);
```

<a id='2ae3322d-05da-4ac1-9482-e51ec9f50c39'></a>

## Parameters

buffer: buffer to hold incoming
packets (char*)

len: maximum size of the buffer (int)

<a id='bdac6792-8cfa-416e-9fbe-e0c1e39dc428'></a>

Returns

<a id='2554f6ca-cb98-4da3-8813-c48a43226f57'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='48d5cfdf-ca4e-4bdc-882b-aad48983090d'></a>

13/16