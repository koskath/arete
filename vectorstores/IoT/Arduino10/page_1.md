<a id='0579fcdc-0ded-4a5e-a638-8d2f22020f97'></a>

12/4/25, 2:52 PM

<a id='1f47efa0-8344-4440-aa4f-2053be98d6ab'></a>

WiFiNINA | Arduino Documentation

<a id='bfdf50c9-ed82-4c20-bfec-923f9c790ac4'></a>

ARDUINODOCS

<a id='d6a77d2e-71bb-4673-a28d-b2824ecb8692'></a>

Search on Docs /

<a id='bddbc484-848a-4d5c-a4fd-8a75e3dd7ddc'></a>

← Go Back

Library

<a id='66b5a1e1-946f-4568-8bc1-884436a3c698'></a>

Recents viewed

<a id='8c4eabf8-5c95-4581-8ea8-03946b7e4eab'></a>

- WiFiNINA
- Arduino SigFox for
  MKRFox1200
- autowp-mcp2515
- Arduino_MKRENV
- Arduino_MKRGPS
- Arduino_APDS9960
- Arduino_MKRIoTCarrier

<a id='59723ef1-42ee-4b12-bcee-e6e39d4f1c80'></a>

Home / Programming / Library / WiFiNINA

<a id='a77241f3-6ded-45a3-a141-cc7d89cccd7f'></a>

COMMUNICATION
# WiFiNINA

ARDUINO LGPL-2.1 V1.9.1 Arduino 20/03/2025

<a id='a9e7e3f2-5f01-4cc2-84a4-3d4167182d45'></a>

Arduino <info@arduino.cc>
http://www.arduino.cc/en/Ref... info@arduino.cc

<a id='9606fa83-d7c4-49cb-8281-3ae9d8fcad81'></a>

Enables network connection (local and Internet) with the
Arduino MKR WiFi 1010, Arduino MKR VIDOR 4000,
Arduino Uno WiFi Rev.2 and Nano 33 IoT.

<a id='d095e902-9d72-40f3-9fca-d8a62e17a127'></a>

With this library you can instantiate Servers, Clients
and send/receive UDP packets through WiFi. The
board can connect either to open or encrypted
networks (WEP, WPA). The IP address can be
assigned statically or through a DHCP. The library
can also manage DNS.

<a id='14418d04-0aee-4cc6-9d07-5ab6921846c6'></a>

GO TO REPOSITORY

<a id='2ea28c5b-a6c6-407f-b25c-52d1d010024c'></a>

Usage/Examples Compatibility Releases

This library allows you to use the Arduino Uno WiFi Rev.2, Arduino Nano 33 IoT, Arduino MKR 1010 and Arduino MKR VIDOR 4000 WiFi capabilities. It can serve as either a server accepting incoming connections or a client making outgoing ones. The library supports WEP, WPA2 Personal and WPA2 Enterprise encryptions. This library supports all the same methods of the original WiFi library plus the connectSSL(). The WiFININA library is very similar to the Ethernet and the WiFi library, and many of the function calls are the same.

<a id='fa7f9a72-e698-4031-b4fd-284a344f3936'></a>

To use this library:

```
1 #include <SPI.h>
2 #include <WiFiNINA.h>
```

<a id='7badc199-7322-40a1-8072-13f7b4995877'></a>

# Examples

Several examples for the **WiFiNINA** library are available from the **Examples from Libraries** page.

<a id='1eae9b8b-3888-4cb4-b97e-86e680be48aa'></a>

ON THIS PAGE

- Usage/Examples
- Compatibility
- Releases
  - WiFi Class +
  - Client Class +
  - Server Class +
  - UDP Class +

<a id='aeaac052-2138-47d7-8814-2d62d7e7354e'></a>

WiFi Class Client Class Server Class

UDP Class

<a id='c2280105-f065-4304-a4b8-07ab92c01125'></a>

Help

<a id='79f9a855-2f56-46e6-984c-10e9827654c9'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='dbb7e04f-3d33-4d2d-b1c4-6e87b0deade9'></a>

1/16