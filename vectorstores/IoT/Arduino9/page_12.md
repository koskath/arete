<a id='ab3daf86-820b-4108-a396-8be10aa80336'></a>

12/4/25, 2:52 PM

<a id='ce3b4385-6a7b-472c-be73-e9f830ced2b2'></a>

WiFiNINA | Arduino Documentation

<a id='935eaf7c-e823-44a7-9bb9-e76e139f1ebf'></a>

ARDUINODOCS

<a id='6adbd65d-d0d8-4c1a-b786-66faf82ef279'></a>

WiFi.BSSID()

# Description

Gets the MAC address of the router you are
connected to or the MAC address of a
network that was scanned.

<a id='af63b505-654a-4604-9181-2c45860e9a22'></a>

## Syntax

```
1 WiFi.BSSID(bssid)
2 WiFi.BSSID(wifiAccessPoint, bss
```

<a id='1ab12277-be84-4d36-91b5-cce852adb012'></a>

## Parameters

bssid - 6 byte array
wifiAccessPoint - specifies from which network to get the information (optional), only needed after a scan

<a id='d56ccbe0-be23-4092-b603-990e419ecfbb'></a>

# Returns
A byte array containing the MAC address of the router the WiFi shield is currently connected to or the MAC address of a network that was scanned. The first array index contains the last byte of the MAC address.

<a id='db0a0b7a-93a4-4c93-a2cc-0f69078b3e94'></a>

Example

___

<a id='8055a135-1024-46dc-a10f-238e5be6f660'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='f76ff872-0a9d-4022-9ebb-34ce66b5f106'></a>

12/30