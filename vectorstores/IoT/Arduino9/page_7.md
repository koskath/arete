<a id='4fdb7e6c-fc3b-4c1f-b83d-16b044f0c940'></a>

12/4/25, 2:52 PM

<a id='f785b77f-1382-467c-b444-a6aae7880af4'></a>

WiFiNINA | Arduino Documentation

<a id='19f2c342-e6d5-4ecb-8ec5-8d957642cfc6'></a>

ARDUINODOCS

<a id='046f7115-33a1-441a-a5ea-782a4f7ba9ad'></a>



<a id='01c3df0b-8a4e-4639-95b9-85e0b5444208'></a>

```
1 WiFi.config(ip);
2 WiFi.config(ip, dns);
3 WiFi.config(ip, dns, gateway);
4 WiFi.config(ip, dns, gateway, s
```

<a id='9f093069-9373-4054-9641-25ee1e73f54e'></a>

# Parameters

ip: the IP address of the device (array of 4 bytes)

dns: the address for a DNS server.

gateway: the IP address of the network gateway (array of 4 bytes). - optional: defaults to the device IP address with the last octet set to 1

subnet: the subnet mask of the network (array of 4 bytes). optional: defaults to 255.255.255.0

<a id='f957cfd6-253a-4395-a092-f53c9c980f7f'></a>

Returns

Nothing

<a id='733d71b6-262c-4d22-9604-a3a0b2d95f9b'></a>

Example
```c
1 This example shows how to set
2
3 #include <SPI.h>
4 #include <WiFiNINA.h>
5
6 // the IP address for the shield
7 IPAddress ip(192, 168, 0, 177);
8
9 char ssid[] = "yourNetwork";
10 char pass[] = "secretPassword";
11
12 int status = WL_IDLE_STATUS;
13
14 void setup()
15 {
16   // Initialize serial and wait for port to open:
17   Serial.begin(9600);
18   while (!Serial) {
19     ;
20   }
21
22   WiFi.config(ip);
23
24   // attempt to connect to WiFi network
25   while (status != WL_CONNECTED) {
26     Serial.print("Attempting to connect to SSID: ");
27     Serial.println(ssid);
28     // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
29     status = WiFi.begin(ssid, pass);
```

<a id='26db6748-7ad5-4f28-85d6-3a3d831611c1'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='ae00bd30-965a-4b4d-9d50-f456c6d21a79'></a>

7/30