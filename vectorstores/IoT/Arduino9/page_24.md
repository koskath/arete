<a id='3e6bed45-6c44-473d-9f0e-1e75fae44e54'></a>

12/4/25, 2:52 PM

<a id='26ec5d5f-6b08-461e-91f7-4be0b2c38676'></a>

WiFiNINA | Arduino Documentation

<a id='65be345a-7231-47dc-96bf-a0d6d597ebb2'></a>

ARDUINODOCS

<a id='622b3db3-16b9-4ce4-8dc4-9f513a72c40f'></a>

1
...
3 while (status != WL_CONNECTED) {
4     Serial.print("Attempting to connect to ");
5     Serial.println(ssid);
6     status = WiFi.begin(ssid, password);
7     delay(10000);
8 }
9 Serial.println("Connected to WiFi");
10 printWifiStatus();
11
12 Serial.println("\nStarting connection to host");
13 IPAddress result;
14 int err = WiFi.hostByName(serverName, result);
15 if(err == 1){
16     Serial.print("IP address of ");
17     Serial.println(result);
18 } else {
19     Serial.print("Error code: ");
20     Serial.println(err);
21 }
22
23 ...

<a id='17297675-fa8b-47ad-ab5a-8b4300d8c604'></a>

WiFi.localIP()

<a id='3017ae07-dce7-4161-92a0-e252956f15c8'></a>

**Description**

Gets the WiFi's IP address

<a id='ca285ccb-53c4-4157-8ef4-b076a0d947f9'></a>

## Syntax

```
1 WiFi.localIP()
```

<a id='59dfe946-f5b2-41b3-bb2a-581dc4886a8f'></a>

Parameters

None

<a id='149c9244-171e-48c8-9754-df5c69b58e55'></a>

Returns

the IP address of the board

<a id='41942b27-6acd-4119-b834-dfc3ec867615'></a>

Example

___

<a id='4186f2ce-5bbc-4c5f-96b4-58fccd10ce99'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='e22ffa3c-d2d8-4157-8624-565633a157e6'></a>

25/30