<a id='5b2cfce9-b6f2-4647-8057-99c7e22ef54c'></a>

12/4/25, 2:52 PM

<a id='0cd6cc90-673a-472d-a63d-a14b0658cf67'></a>

WiFiNINA | Arduino Documentation

<a id='be5f4cd8-176e-4c66-af92-58dcb34692f2'></a>

ARDUINODOCS

<a id='e1377ab5-044c-435f-a84c-878c176f44df'></a>

# Parameters

None

# Returns

The client connection status

# Example

```
1
2
3 void setup() {
4
5     Serial.begin(9600);
6     while (!Serial) {
7         ;
8     }
9     if (WiFi.status() == WL_NO_SOC) {
10         Serial.println("Communication with WiFi module failed!");
11         while (true);
12     }
13
14     while (status != WL_CONNECTED) {
15         Serial.print("Attempting to connect to SSID: ");
16         Serial.println(ssid);
17         status = WiFi.begin(ssid, pass);
18         delay(10000);
19     }
20     Serial.println("Connected to WiFi");
21     printWifiStatus();
22
23     Serial.println("\nStarting connection to \"www.google.com\"");
24     IPAddress result;
25     int err = WiFi.hostByName("www.google.com", result);
26     if (err == 1) {
27         Serial.print("IP address for google.com: ");
28         Serial.println(result);
29     } else {
30         Serial.print("Failed to resolve google.com: ");
```

<a id='d66b2807-59cc-4785-82a3-57e3efd08fb8'></a>

client.write()

# Description

Write data to all the clients connected to a server.

# Syntax

```
1 client.write(data)
2 client.write(buffer, size);
```

<a id='62bf3bb8-fe6e-4db4-a09c-696e86aa4089'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='1586b323-af2d-4f6e-835a-1ce4d7ca2377'></a>

9/16