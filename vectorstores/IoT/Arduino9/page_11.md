<a id='47ab4cd2-eae4-4f6f-89bc-301865dd7c61'></a>

12/4/25, 2:52 PM

<a id='50801420-1841-47b2-afa8-b48c3055cc66'></a>

WiFiNINA | Arduino Documentation

<a id='b94c09e0-7020-4d9d-933e-11c0eea7e057'></a>

ARDUINODOCS

<a id='6a103cc6-fe29-4cb4-b054-f21d6f4df7c9'></a>

### Description

Gets the SSID of the current network

<a id='887b042d-b460-4be1-a660-4fc11343309b'></a>

## Syntax

```
1 WiFi.SSID();
2 WiFi.SSID(wifiAccessPoint)
```

<a id='8472ea0a-8b9a-46d8-9747-39df89688f31'></a>

## Parameters

wifiAccessPoint: specifies from which network to get the information

<a id='31d0bbc0-0562-467d-b2fb-0d6787d11b19'></a>

# Returns
A string containing the SSID the WiFi is currently connected to.
A string containing name of network requested.

<a id='40d5350a-ee36-4bcf-b6b6-131208d12308'></a>

Example

```c
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 //SSID of your network
5 char ssid[] = "yourNetwork";
6 int status = WL_IDLE_STATUS;
7 
8 void setup()
9 {
10   // initialize serial:
11   Serial.begin(9600);
12 
13   // scan for existing networks
14   Serial.println("Scanning available networks");
15   scanNetworks();
16 
17   // attempt to connect using ssid as target
18   Serial.println("Attempting to connect to SSID: ");
19   status = WiFi.begin(ssid);
20 
21   Serial.print("SSID: ");
22   Serial.println(ssid);
23 }
24 
25 void loop() {}
26 
27 void scanNetworks() {
28   // code for scanning networks
```

<a id='98270af8-37a0-4263-8b72-d1f4b390644c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='065b12ad-b461-4294-ab68-16d776b3c691'></a>

11/30