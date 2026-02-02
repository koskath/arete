<a id='09c002c3-8b4a-4265-b72d-e65eb00c6359'></a>

12/4/25, 2:52 PM

<a id='8e1040c5-0d33-4d4c-9221-a9c5d5103773'></a>

WiFiNINA | Arduino Documentation

<a id='b15164dc-a07b-41c2-b8de-90cf35f20110'></a>

ARDUINODOCS

<a id='42f2873e-7836-4018-9466-08bc6bf3bdde'></a>

An empty rectangular box.

<a id='1f72e5fd-9008-4952-960d-2fc30783b717'></a>

Example

```
1 /*
2 This example creates a client
3 data using always SSL.
4
5 It is compatible with the met
6 connections, like client.conn
7
8 Written by Arturo Guadalupi
9 last revision November 2015
10
11 */
12
13 #include <SPI.h>
14 #include <WiFiNINA.h>
15
16 #include "arduino_secrets.h"
17 /////please enter your sens
18 char ssid[] = SECRET_SSID;
19 char pass[] = SECRET_PASS;
20 int keyIndex = 0;
21
22 int status = WL_IDLE_STATUS;
23 // if you don't want to use D
24 // use the numeric IP instead
25 //IPAddress server(74,125,232,
26 char server[] = "www.google.c
27
28 // Initialize the Ethernet cl
29 // with the TD address and --
```

<a id='cccdf301-bc43-4d55-869b-bb2a90b22409'></a>

expand client.connected()

<a id='05a2cdcc-86fa-42b3-bfaa-ffe46903d331'></a>

## Description
Whether or not the client is connected. Note that a client is considered connected if the connection has been closed but there is still unread data.

<a id='34da3b2d-ad6e-4a4c-8025-d22b86ddb298'></a>

## Syntax

```
1 client.connected()
```

<a id='93162213-3e0a-4996-a274-0bfd0206c469'></a>

Parameters

None

<a id='d615e0b7-e15f-4e33-bed5-2314c3076f51'></a>

## Returns

Returns true if the client is connected,

<a id='a2d606f6-d4c3-4b66-b45f-4a5d1c0af53a'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='1e0c9bd2-222c-4acc-b659-43da413639a1'></a>

4/16