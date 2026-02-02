<a id='306d0856-ff5a-4678-bced-2cd90253cc1c'></a>

12/4/25, 2:52 PM

<a id='e34a0abc-96d3-4c87-82c1-8b0a4e60684e'></a>

WiFiNINA | Arduino Documentation

<a id='54937263-c765-41af-b2d0-8b8baa356dc1'></a>

ARDUINODOCS

<a id='8593600d-d09c-4b8a-b2fd-6ac84d8af302'></a>

# Parameters
timeout - the connection timeout value
in milliseconds

# Returns
Nothing

# Example
```
1   ...
2   WiFi.setTimeout(120 * 1000);
3
4   // attempt to connect to WiFi
5   while (status != WL_CONNECTED) {
6     Serial.print("Attempting to connect to SSID: ");
7     Serial.println(ssid);
8     // Connect to WPA/WPA2 network. Change this to your WiFi name and password
9     status = WiFi.begin(ssid, password);
10
11    // wait 10 seconds for connection
12    delay(10000);
13  }
14
15  ...
```

<a id='6bdcc00c-e91a-416a-ac8a-1be7f5ca202f'></a>

WiFi.SSID()

<a id='153444d9-89e0-4952-8a28-c94bb63bbe46'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='a0861e9c-1586-4810-805e-639400f0b622'></a>

10/30