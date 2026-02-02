<a id='afaa3420-877e-488c-8e09-8b78981f135f'></a>

12/4/25, 2:52 PM

<a id='297511bf-3f0c-4a8d-806c-2621dc0d8188'></a>

WiFiNINA | Arduino Documentation

<a id='1d558dda-218f-49eb-9d9a-80ebac189347'></a>

ARDUINODOCS

<a id='64e08f93-3ed6-4e43-9607-fd7d8b6542f1'></a>

WiFi.end()

# Description

Turns off the WiFi module. If WiFi.begin()
was used to connect to an access point, the
connection will be disconnected. If
WiFi.beginAP() was used before to create an
access point, the WiFi.end() will stop
listening it too.

<a id='6860e942-f14f-4678-8329-886184f3c2b4'></a>

## Syntax

```
1 WiFi.end();
```

<a id='de7bcae8-a167-4a14-af73-9479044595f4'></a>

Parameters

None

<a id='73734f28-61d1-40df-9dff-22392af83987'></a>

Returns

Nothing

<a id='a7ab93d5-5533-409f-ada9-4db09457d2e6'></a>

WiFi.beginAP()

<a id='9b70c9d8-dcb4-4407-aac9-3bb19770ee35'></a>

# Description

Initializes the WiFININA library in Access Point (AP) mode. Other WiFi devices will be able to discover and connect to the created Access Point.

<a id='490a8edf-7e54-4243-8a58-5ea260b8197e'></a>

Syntax

```
1 WiFi.beginAP(ssid);
2 WiFi.beginAP(ssid, channel);
3 WiFi.beginAP(ssid, passphrase);
4 WiFi.beginAP(ssid, passphrase,
```

<a id='e909bfb7-dbb5-44ae-be29-e686062a5385'></a>

## Parameters

ssid: the SSID (Service Set Identifier) of the created Access Point. Must be 8 or more characters.

passphrase: optional, the WPA password of the created Access Point. Must be 8 or more characters.

<a id='638713fd-13a6-4249-b4c0-460019127dd4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='f2943b44-037b-4356-b38e-8b9e4a822bd0'></a>

3/30