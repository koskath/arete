<a id='e7eead98-3007-4dd6-b54c-02fa722c2c04'></a>

12/4/25, 2:52 PM

<a id='868a7987-6eb7-4617-a1fa-451cda1f5bbd'></a>

WiFiNINA | Arduino Documentation

<a id='cad5c783-c5a8-4418-8f25-af9739195019'></a>

ARDUINODOCS

<a id='5f216f59-5a7e-4dda-b4ee-01de4d0b4160'></a>

Ping a remote device on the network.

<a id='c3714269-2cc6-4ec6-8b3f-7c53a94b5295'></a>

# Syntax

```
1 WiFi.ping(ip);
2 WiFi.ping(ip, ttl);
3 WiFi.ping(host);
4 WiFi.ping(host, ttl);
```

<a id='3f4d81ac-7dfb-40f3-beb6-fa59e8343306'></a>

## Parameters

ip: the IP address to ping (array of 4 bytes)
host: the host to ping (string)
ttl: Time of live (optional, defaults to 128). Maximum number of routers the request can be forwarded to.

<a id='ec685e79-2686-4b22-9362-5960aebbe1e6'></a>

## Returns

WL_PING_SUCCESS when the ping was successful

WL_PING_DEST_UNREACHABLE when the destination (IP or host is unreachable)

WL_PING_TIMEOUT when the ping times out

WL_PING_UNKNOWN_HOST when the host cannot be resolved via DNS

WL_PING_ERROR when an error occurs

<a id='146e15b6-78fc-4e06-b651-2792f815eb0d'></a>

Example

________________________________________________________________________________

<a id='4da2f4c8-fee1-405c-bb8f-60d54cf938d7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='67f2efe9-8545-4ea0-a6f3-245d0e3c03b6'></a>

18/30