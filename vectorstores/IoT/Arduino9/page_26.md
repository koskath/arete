<a id='cfcced9d-9215-4fc0-bd10-c5ba51206ec6'></a>

12/4/25, 2:52 PM

<a id='74248961-8432-441f-98fc-1ae697076fe6'></a>

WiFiNINA | Arduino Documentation

<a id='30721c3a-9813-4e2f-8e5d-ada498cd5d3b'></a>

ARDUINODOCS

<a id='d0ebae58-e9b8-4abc-ac82-76179d7bba33'></a>

```cpp
1 #include <WiFiNINA.h>
2 int status = WL_IDLE_STATUS;
3 
4 //SSID of your network
5 char ssid[] = "yourNetwork";
6 //password of your WPA Networ
7 char pass[] = "secretPassword";
8 
9 IPAddress ip;
10 IPAddress subnet;
11 IPAddress gateway;
12 
13 void setup()
14 {
15   WiFi.begin(ssid, pass);
16 
17   if ( status != WL_CONNECTED ) {
18     Serial.println("Couldn't");
19     while(true);
20   }
21   // if you are connected, pr
22   else {
23 
24     // print your subnet mask
25     subnet = WiFi.subnetMask();
26     Serial.print("NETMASK: ");
27     Serial.println();
28   }
29 }
```

<a id='7a598e5e-c1da-415b-84a8-8c39296ad448'></a>

# WiFi.gatewayIP()

## Description
Gets the WiFi's gateway IP address.

## Syntax
```
1 WiFi.gatewayIP()
```

## Parameters
None

## Returns
An array containing the board's gateway IP address

## Example

<a id='53ba1878-43cf-48b8-8779-fac5ab0fd998'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='8f76b906-1293-45bf-844c-f11fecb5b555'></a>

27/30