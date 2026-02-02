<a id='0512a948-52de-4cbf-8d32-d736e7bbb1ce'></a>

12/4/25, 2:52 PM

<a id='42fa9f6c-362d-4a36-8665-a4088fa1df5f'></a>

WiFiNINA | Arduino Documentation

<a id='f478c1f3-e7fb-4791-acc5-a45f776b401b'></a>

ARDUINODOCS

<a id='2e930f36-8762-4184-b720-59551d42f9d1'></a>

```cpp
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 char ssid[] = "myNetwork";
5 char pass[] = "myPassword";
6 
7 int status = WL_IDLE_STATUS;
8 char servername[]="google.com";
9 
10 WiFiClient client;
11 
12 void setup() {
13   Serial.begin(9600);
14   Serial.println("Attempting to connect to WiFi...");
15   Serial.print("SSID: ");
16   Serial.println(ssid);
17 
18   status = WiFi.begin(ssid, pass);
19   if ( status != WL_CONNECTED) {
20     Serial.println("Couldn't connect to WiFi");
21     // don't do anything else
22     while(true);
23   }
24   else {
25     Serial.println("Connected to WiFi");
26     Serial.println("\nStarting connection to server...");
27     // if you get a connection, report back via serial:
28     if (client.connect(servername, 80)) {
29       Serial.println("connected to server");
```

<a id='4e12c2a8-f1b6-4f45-9034-61950ee4b4fa'></a>

client.peek()

<a id='a2f67a0f-4a6f-4aac-ab1d-8f3156ef1edb'></a>

## Description

Read a byte from the file without advancing to the next one. That is, successive calls to peek() will return the same value, as will the next call to read().

<a id='51124554-5095-459e-98b6-ed2c6723c35e'></a>

This function inherited from the Stream
class. See the Stream class main page for
more information.

<a id='6f7d4c59-ccad-4beb-9a5e-e9f6dcc608ab'></a>

# Syntax

```
1 client.peek()
```

<a id='af73cb32-b123-4493-8ab3-4f3abd9cca6a'></a>

Parameters

None

<a id='1d1bdc13-059a-408b-a452-c073f8dcaa1c'></a>

## Returns

b: the next byte or character

<a id='ed4ebc0a-44c3-4f0a-9f28-61703c0460b5'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e22a2339-f5a2-4434-91f2-f6b9a6ece576'></a>

12/16