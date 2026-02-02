<a id='4465869f-bc25-4ab2-880b-59f41f23188c'></a>

12/4/25, 2:52 PM

<a id='570f6c83-95cf-48a9-babc-aa784bef9e3a'></a>

WiFiNINA | Arduino Documentation

<a id='d5fed216-289b-4964-9f6b-d64570c2599a'></a>

ARDUINODOCS

<a id='dfc7b26e-95f6-4eaa-893a-e7efd19e2c88'></a>

## Description

Scans for available WiFi networks and returns the discovered number

<a id='a45fd6ab-e4c7-4769-bd71-5ccd4b01e17d'></a>

## Syntax

```
1 WiFi.scanNetworks()
```

<a id='c613a30b-3f1a-4a26-bf84-7384ffce763e'></a>

Parameters

None

<a id='03b325d5-8694-4c75-af47-cc141db592a8'></a>

## Returns

byte : number of discovered networks

<a id='ae88d1ec-6a6e-45f3-b374-28e5a49d86d8'></a>

# Example
```
/*
This example prints the boar
scans for available WiFi net
Every ten seconds, it scans
connect to any network, so n

Circuit:
* Board with NINA module (Ar

created 13 July 2010
by dlf (Metodo2 srl)
modified 21 Junn 2012
by Tom Igoe and Jaymes Dec
*/

#include <SPI.h>
#include <WiFiNINA.h>

void setup() {
  //Initialize serial and wai
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port
  }

  // check for the WiFi modul
  if (WiFi.status() == WL_NO_
```

<a id='5e863048-30c7-48e2-8637-b1cde58091ea'></a>

v WiFi.ping()

<a id='867b10dc-ac3b-442e-ab09-acd54abad47c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='9fd738b4-8b9b-4e7c-8c8c-f7f6e96e5985'></a>

17/30