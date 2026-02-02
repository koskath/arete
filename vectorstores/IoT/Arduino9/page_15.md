<a id='6b5948d7-4dd0-470d-941e-7fddaa84771c'></a>

12/4/25, 2:52 PM

<a id='7cd20707-2af3-4771-ab3a-6e4cc767c460'></a>

WiFiNINA | Arduino Documentation

<a id='02b97c4f-46a3-4565-b911-893003b04de2'></a>

ARDUINODOCS

<a id='8be127b5-1458-42c8-9a1f-84bf554a3eba'></a>

AUTO = 8

# Example

```c
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 //SSID of your network
5 char ssid[] = "yourNetwork";
6 //password of your WPA Network
7 char pass[] = "secretPassword";
8 
9 void setup() {
10   WiFi.begin(ssid, pass);
11 
12   if (status != WL_CONNECTED) {
13     Serial.println("Couldn't get connected");
14     while(true);
15   }
16   // if you are connected, print the encryption type
17   else {
18     byte encryption = WiFi.encryptionType();
19     Serial.print("Encryption Type: ");
20     Serial.println(encryption, HEX);
21   }
22 }
23 
24 void loop () {}
```

<a id='f15abd79-fdda-40da-bf43-a261b20f767f'></a>

WiFi.scanNetworks()

<a id='b5d2a90e-398a-4814-9bbd-8459962c37eb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='beb17267-65b9-4925-beac-196ac32a3c60'></a>

16/30