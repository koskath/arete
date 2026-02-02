<a id='3273760a-c799-45cb-a2db-d9d2f2fb9310'></a>

12/4/25, 2:52 PM

<a id='ba3497f5-d776-4390-836b-6335270771af'></a>

WiFiNINA | Arduino Documentation

<a id='ba61cb0e-71c2-477c-bae9-44c34405560d'></a>

ARDUINODOCS

<a id='bcb78b8d-8870-44bd-8f33-825e89c4d848'></a>

Description

Gets the MAC Address of your WiFi NINA
module

<a id='b14ade21-e8dc-40fb-9b76-76e660783e4d'></a>

## Syntax

```
1 WiFi.macAddress(mac)
```

<a id='246206c4-4098-4ee8-9c84-e57909c8257e'></a>

## Parameters

mac: a 6 byte array to hold the MAC address

<a id='dbff5cd1-2801-471a-9c78-f6e36574effc'></a>

## Returns

byte array : 6 bytes representing the MAC address of your module

<a id='7430f287-fdbd-4b7c-b464-10643c10c342'></a>

Example

```
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3
4 char ssid[] = "yourNetwork";
5 int status = WL_IDLE_STATUS;
6
7 byte mac[6];
8
9
10 void setup()
11 {
12   Serial.begin(9600);
13
14   status = WiFi.begin(ssid);
15
16   if (status != WL_CONNECTED)
17     Serial.println("Couldn't
18     while(true);
19   }
20   // if you are connected, pr
21   else {
22     WiFi.macAddress(mac);
23     Serial.print("MAC: ");
24     Serial.print(mac[5], HEX);
25     Serial.print(":");
26     Serial.print(mac[4], HEX);
27     Serial.print(":");
28     Serial.print(mac[3], HEX);
30
```

<a id='9b7d5576-6d9f-48dc-92df-d0a705001a3d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='ec4a2813-8731-4d43-9996-1a1f69993d07'></a>

21/30