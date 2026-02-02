<a id='62f26bdb-17e5-4db3-8459-698da5bd21ff'></a>

12/4/25, 2:52 PM

<a id='86610b17-ca0f-4a7e-a2c9-89ceb09fea6b'></a>

WiFiNINA | Arduino Documentation

<a id='8381096e-2ae4-45a2-9a66-f4407d7f16e0'></a>

ARDUINODOCS

<a id='5784ad36-6d78-4d88-80ca-a2769dbbf2e8'></a>

ip: the IP address that the client will connect to (array of 4 bytes)

URL: the domain name the client will connect to (string e.g., "arduino.cc")

port: the port that the client will connect to (int)

<a id='ad0d0a80-f917-417a-8194-85e1295dd7ae'></a>

## Returns

Returns true if the connection succeeds,
false if not.

<a id='5f99b9b7-b6f0-4f26-8b14-b4c87f04c383'></a>

Example

1 ...
2
3 /*
4   Web client
5
6   This sketch connects to a web client
7   using a WiFi board.
8
9   This example is written for a network with
10  WEP or WPA, change the WiFi.h library.
11
12 Circuit:
13  * WiFiNINA supported board
14
15  created 13 July 2010
16  by dlf (Metodo2 srl)
17  modified 31 May 2012
18  by Tom Igoe
19 */
20
21
22 #include <SPI.h>
23 #include <WiFiNINA.h>
24
25 char ssid[] = "yourNetwork";
26 char pass[] = "secretPassword";
27 int keyIndex = 0;
28
29 int status = WL_IDLE_STATUS;

<a id='cad0a6f5-962c-489a-8718-613831f72d9d'></a>

client.status()

## Description

Return Connection status.

<a id='2e3fa71e-8b05-454d-82ac-c04ff4784ca4'></a>

Syntax

```
client.status()
```

<a id='9f1d726b-0923-4868-a985-b503e7e11e73'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e312c4c8-df08-4eb1-a2a0-53d2f57f679a'></a>

8/16