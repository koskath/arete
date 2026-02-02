<a id='b9c9543c-7175-4d92-a503-afe7fb5bc0e5'></a>

12/4/25, 2:52 PM

<a id='b41db34d-c70f-4211-a7aa-6e75e1583f3e'></a>

WiFiNINA | Arduino Documentation

<a id='831af1c5-f071-4a41-a07b-e58b27998f80'></a>

ARDUINODOCS

<a id='ba28cc91-c0c8-4827-ad18-13127d1b9761'></a>

```
1 ...
2 
3 while (status != WL_CONNECTED) {
4     Serial.print("Attempting to connect to SSID: ");
5     Serial.println(ssid);
6     // Connect to WPA/WPA2
7     status = WiFi.begin(ssid, password);
8     if (status != WL_CONNECTED) {
9 
10         Serial.print("Connection failed, retrying...");
11         Serial.println();
12     }
13 }
14 // wait 10 seconds for
15 delay(10000);
16 }
17 
18 ...
```

<a id='e4a1693d-a78c-4460-ae35-47fdbad439d0'></a>

WiFi.hostByName()

<a id='358060fb-a530-45fd-9dae-b728bd925d48'></a>

## Description

Resolve the given hostname to an IP
address

<a id='69c71c01-6fa4-46ee-9b3b-f02bbbd552c0'></a>

# Syntax

```
1 WiFi.hostByName(hostname, resul
```

<a id='6fbfbad1-edad-4876-a034-954955073447'></a>

# Parameters

hostname: Name to be resolved

result: IPAddress structure to store the
returned IP address

<a id='883e545a-b44d-4805-97cc-2c726328323f'></a>

# Returns

1 if hostname was successfully
converted to an IP address, else the
error code

<a id='7ae30a0b-6492-44ec-8488-98d5174ef148'></a>

Example

[ ]

<a id='e23e6cfc-92a3-4a84-b862-461c89a9aff5'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='de601b82-131e-4af7-a98f-e15b66c97d09'></a>

24/30