<a id='452c7d33-93af-458d-886b-9fb357371ff3'></a>

12/4/25, 2:52 PM

<a id='c15d43ab-9a4b-41b5-a331-d9ff33bc8c54'></a>

WiFiNINA | Arduino Documentation

<a id='e633d4f6-9755-430f-9178-8e8461cdda29'></a>

ARDUINODOCS

<a id='49b060e5-d1b7-4210-adc2-4b986b299086'></a>

```c
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 char ssid[] = "myNetwork";
5 char pass[] = "myPassword";
6 
7 int status = WL_IDLE_STATUS;
8 IPAddress server(74, 125, 115, 1);
9 
10 // Initialize the client libr
11 WiFiClient client;
12 
13 void setup() {
14 Serial.begin(9600);
15 Serial.println("Attempting");
16 Serial.print("SSID: ");
17 Serial.println(ssid);
18 
19 status = WiFi.begin(ssid, pass);
20 if ( status != WL_CONNECTED ) {
21 Serial.println("Couldn't");
22 // don't do anything else
23 while(true);
24 }
25 else {
26 Serial.println("Connected");
27 Serial.println("\nStartin");
28 // if you get a connectio
```

<a id='c5b5550f-5250-4c18-8331-c9280a167fb2'></a>

WiFiSSLClient

<a id='507206e0-c1a9-425c-8fff-cadf190e6830'></a>

## Description

This class allows to create a client that always connects in SSL to the specified IP address and port, even if client.connect() is used instead of client.connectSSL(). This is useful If you have a library that accepts only plain Client, but you want to force it to use SSL, keeping the same method names of the non SSL client.

<a id='586ea1b3-512b-4c01-9219-e5dad22ce67c'></a>

## Syntax

```
1 WiFiNINASSLClient client;
```

<a id='d79b2bfe-eb89-4dcc-939f-878f80089624'></a>

# Parameters

client : the named client to refer to

<a id='a7a41ef8-fa25-4105-81dc-c84215646cc6'></a>

Return

None

<a id='159e7c1d-8db3-4a69-895b-27f2e91c4925'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='b9e1d922-2e58-484c-9cf4-0fc24a0d72fe'></a>

3/16