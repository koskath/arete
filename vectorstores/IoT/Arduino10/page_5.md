<a id='37a6bdf2-a050-42c3-a570-14f2261f122c'></a>

12/4/25, 2:52 PM

<a id='9bcce4b0-209a-4f04-907d-15a7f70fbee8'></a>

WiFiNINA | Arduino Documentation

<a id='d7d4e1b8-d5a2-486b-bf07-6e087ff5eea1'></a>

ARDUINODOCS

<a id='04f3fb68-2a73-41e0-a1be-8f9d62617209'></a>



<a id='9227a3ee-ed54-4b73-802e-7171d08001e6'></a>

Example

```
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 char ssid[] = "myNetwork";
5 char pass[] = "myPassword";
6 
7 int status = WL_IDLE_STATUS;
8 IPAddress server(74, 125, 115, 1;
9 
10 // Initialize the client libr
11 WiFiClient client;
12 
13 void setup() {
14   Serial.begin(9600);
15   Serial.println("Attempting to connect...");
16   Serial.print("SSID: ");
17   Serial.println(ssid);
18 
19   status = WiFi.begin(ssid, pass);
20   if ( status != WL_CONNECTED) {
21     Serial.println("Couldn't connect to WiFi");
22     // don't do anything else
23     while(true);
24   } else {
25     Serial.println("Connected to WiFi");
26     Serial.println("\nStarting web server...");
27     // if you get a connectio
28     // client connect/server...
```

<a id='e4272bb7-cb85-464e-8c62-401e04edf2e7'></a>

client.connect()

<a id='bf600d8d-2bb6-42da-a483-746211db308e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='5e595790-e4da-42a7-b0e9-248acb7a805c'></a>

5/16