<a id='3d8495ab-d1e9-4f88-aba6-f6d2fcd02fb6'></a>

12/4/25, 2:52 PM

<a id='14a5ed11-ba61-4fdb-832b-a8cde24fe630'></a>

WiFiNINA | Arduino Documentation

<a id='b2d861af-74fb-4be9-82ec-566512e5aae8'></a>

ARDUINODOCS

<a id='012ab823-bc34-4a68-bcd6-2bd33d32eb93'></a>

```c
1 #include <WiFiNINA.h>
2 
3 char ssid[] = "yourNetwork";
4 
5 int status = WL_IDLE_STATUS;
6 
7 IPAddress ip;
8 
9 void setup()
10 {
11   // initialize serial:
12   Serial.begin(9600);
13 
14   WiFi.begin(ssid);
15 
16   if ( status != WL_CONNECTED ) {
17     Serial.println("Couldn't");
18     while(true);
19   }
20   // if you are connected, pr
21   else {
22     //print the local IP address
23     ip = WiFi.localIP();
24     Serial.println(ip);
25   }
26 }
27 }
28 
29 // void loop() {
```

<a id='c5d238fc-2ee4-4469-957d-5fdc5515e0ed'></a>

WiFi.subnetMask()

<a id='35de8c9a-8ee2-4544-b8df-0653c5555279'></a>

### Description

Gets the WiFi's subnet mask

<a id='2b72a433-a8d7-4ea4-9313-8acf657b820c'></a>

## Syntax

```
1 WiFi.subnet()
```

<a id='6c7c1434-6c37-4627-ac9e-e8e27d8125fc'></a>

Parameters

None

<a id='93add709-6064-4712-9655-51979bd68b77'></a>

Returns

the subnet mask of the board

<a id='21c8b18b-0a36-4d90-a3ca-7e5d285739e8'></a>

Example

____________________________________________________________________

<a id='f5231257-f302-4c23-bb67-8826af39d58d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='271dde9e-6508-4001-b3d0-d059400300fb'></a>

26/30