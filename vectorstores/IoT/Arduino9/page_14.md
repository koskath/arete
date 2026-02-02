<a id='ac639f16-09ca-4e37-898a-f189ccd251f6'></a>

12/4/25, 2:52 PM

<a id='d10f6253-2135-479e-834a-0d8af2974dc6'></a>

WiFiNINA | Arduino Documentation

<a id='d7121856-cdbd-4f91-afd9-f87013a13921'></a>

ARDUINODOCS

<a id='30d6ef3b-b024-42eb-ae25-bb64024bc019'></a>

```
1 ...
2 // scan for nearby networks
3 Serial.println("** Scan Net
4 int numSsid = WiFi.scanNetw
5 if (numSsid == -1)
6 {
7   Serial.println("Couldn't
8   while (true);
9 }
10 
11 // print the list of networ
12 Serial.print("number of ava
13 Serial.println(numSsid);
14 
15 // print the network number
16 for (int thisNet = 0; thisN
17   Serial.print(thisNet + 1)
18   Serial.print(") ");
19   Serial.print("Signal: ");
20   Serial.print(WiFi.RSSI(th
21   Serial.print(" dBm");
22   Serial.print("\tChannel:
23   Serial.print(WiFi.channel
24   byte bssid[6];
25   Serial.print("\t\tBSSID:
26   printMacAddress(WiFi.BSSI
27   Serial.print("\tEncryptio
28   printEncryptionType(WiFi.
```

<a id='d3ac184a-ba74-4509-b25c-1d613adea86a'></a>

WiFi.encryptionType()

<a id='5962878b-02fa-4661-b0d5-4533529b17a1'></a>

## Description

Gets the encryption type of the current network

<a id='6f593ada-228a-4320-9834-2cf92e481a31'></a>

## Syntax

```
1 WiFi.encryptionType();
2 WiFi.encryptionType(wifiAccessP
```

<a id='a76378e4-273e-4eef-bc9d-958e98b7a81a'></a>

## Parameters

wifiAccessPoint: specifies which network to get information from

<a id='936969b5-a36e-4a1f-a721-198620bd19c1'></a>

## Returns

byte : value represents the type of encryption

<a id='65222850-2fa7-4f08-b38b-9744b79331c2'></a>

TKIP (WPA) = 2

WEP = 5

<a id='d0933840-a4b8-4f60-a526-9de198f6816c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='54529465-8d9b-472f-93ac-a57f300633fc'></a>

15/30