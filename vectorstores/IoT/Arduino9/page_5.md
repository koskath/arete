<a id='d7ba6eb1-e923-4ec3-9b7c-b4c4d29b4ee6'></a>

12/4/25, 2:52 PM

<a id='4208d3ed-b89d-4b64-8367-7c35f331e56a'></a>

WiFiNINA | Arduino Documentation

<a id='dfd74369-2f41-4dbc-8245-ccb3be647df2'></a>

ARDUINODOCS

<a id='7aab82a2-59b4-42dc-bd53-bc68ba05b039'></a>

1 WiFi.beginEnterprise(ssid, user
2 WiFi.beginEnterprise(ssid, user
3 WiFi.beginEnterprise(ssid, user

<a id='83b4b58f-4867-41fe-bba5-78b21b2e61d3'></a>

# Parameters

ssid: the SSID (Service Set Identifier) is
the name of the WiFi network you
want to connect to.

username: username part of WPA2
Enterprise (RADIUS) credentials

password: password part of WPA2
Enterprise (RADIUS) credentials

identity: WPA2 enterprise identity
(optional)

ca: root certificate (string) to validate
against (optional)

<a id='1946dc07-13c1-411e-a768-8c945b7d5b25'></a>

# Returns

WL_CONNECTED when connected to a
network
WL_IDLE_STATUS when not connected
to a network, but powered on

<a id='b71993e4-44a7-4015-afb7-9d0afaa5eae3'></a>

Example
1 /*
2 This example connects to a
3 Then it prints the MAC addr
4 the IP address obtained, an
5 
6 Based on ConnectWithWPA.ino
7 */
8 #include <SPI.h>
9 #include <WiFiNINA.h>
10 
11 #include "arduino_secrets.h"
12 ///////please enter your sens
13 char ssid [] = SECRET_SSID; /
14 char user[] = SECRET_USER; /
15 char pass[] = SECRET_PASS; /
16 int status = WL_IDLE_STATUS;
17 
18 void setup() {
19 //Initialize serial and wai
20 Serial.begin(9600);
21 while (!Serial) {
22 ; // wait for serial port
23 }
24 
25 // check for the WiFi modul
26 if (WiFi.status() == WL_NO_
27 Serial.println("Communica
28 // don't continue

<a id='fd8a4565-8c36-4c13-8fe2-06a0aa3ef95d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='f85b184e-df3c-4976-9286-59bed2a280d8'></a>

5/30