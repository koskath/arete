<a id='f357885c-56cf-405f-b266-64e04b879947'></a>

12/4/25, 2:52 PM

<a id='ea7b49a1-01fe-4041-af05-9548563418e4'></a>

WiFiNINA | Arduino Documentation

<a id='4e4eb69f-1d10-406b-b581-b0d075ee4db3'></a>

ARDUINODOCS

<a id='48d4afb8-f3d3-4966-9483-483d786137e2'></a>

```cpp
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 int status = WL_IDLE_STATUS;
5 
6 //SSID of your network
7 char ssid[] = "yourNetwork";
8 //password of your WPA Network
9 char pass[] = "secretPassword";
10 
11 IPAddress gateway;
12 
13 void setup()
14 {
15   Serial.begin(9600);
16 
17   WiFi.begin(ssid, pass);
18 
19   if ( status != WL_CONNECTED ) {
20     Serial.println("Couldn't");
21     while(true);
22   }
23   // if you are connected, print
24   else {
25 
26     // print your gateway address
27     gateway = WiFi.gatewayIP();
28     Serial.print("GATEWAY: ");
29     Serial.println(gateway);
30   }
```

<a id='687cb252-9f60-4e75-aca5-7ed134224fb5'></a>

WiFi.dnsIP()

# Description
Returns the DNS server IP address for the device.

# Syntax
```
1 WiFi.dnsIP()
2 WiFi.dnsIP(n)
```

# Parameters
optional parameter n for the number of the DNS server to get the second DNS serverv

# Returns
the DNS server IP address for the device (IPAddress).

# Example

<a id='d4963e22-0165-4be0-9188-d5a257a8687e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='1b66043b-65c8-4e79-a609-e5dd6f9890c6'></a>

28/30