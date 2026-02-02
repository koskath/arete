<a id='24bf044d-9b67-4f35-8b98-f3eb298dc9ed'></a>

12/4/25, 2:52 PM

<a id='2a04abbb-ee56-4e8f-8a70-20a7a9731293'></a>

WiFiNINA | Arduino Documentation

<a id='d2b1890c-6c96-451a-adb2-71d5be4e1fc3'></a>

ARDUINODOCS

<a id='a4a208dd-55f6-4e82-adb1-4c4598cc3f1d'></a>



<a id='93ca6ab2-17ca-49fb-a668-ec8b8210250a'></a>

### Description

WiFi.setDNS() allows you to configure the DNS (Domain Name System) server.

<a id='45000e56-e35a-43f7-867e-7ca7eef453df'></a>

## Syntax

```
1 WiFi.setDNS(dns_server1)
2 WiFi.setDNS(dns_server1, dns_se
```

<a id='418ad3c5-3450-42d8-b874-b6a6e99cada8'></a>

## Parameters

dns_server1: the IP address of the primary DNS server

dns_server2: the IP address of the secondary DNS server

<a id='3c577834-6b45-42da-9df4-0bf6f459a9f7'></a>

Returns
Nothing

<a id='9b089c30-4183-4399-b79d-a0e8be73bce4'></a>

Example
```c
1 This example shows how to set
2
3 #include <SPI.h>
4 #include <WiFiNINA.h>
5
6 // the IP address for the shi
7 IPAddress dns(8, 8, 8, 8); /
8
9 char ssid[] = "yourNetwork";
10 char pass[] = "secretPassword";
11
12 int status = WL_IDLE_STATUS;
13
14 void setup()
15 {
16   // Initialize serial and wa
17   Serial.begin(9600);
18   while (!Serial) {
19     ; // wait for serial port
20   }
21
22   // attempt to connect to Wi
23   while (status != WL_CONNEC
24   Serial.print("Attempting");
25   Serial.println(ssid);
26   // Connect to WPA/WPA2 ne
27   status = WiFi.begin(ssid,
28   // wait 10 seconds for --
```

<a id='a4e624b2-fd1f-4b97-994d-ae1bde4e330d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='249b5037-6bf4-476a-90e3-8a8ea270cb46'></a>

8/30