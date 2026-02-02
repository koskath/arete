<a id='2957bcaa-3084-4111-894b-7e1fbe7a8d56'></a>

12/4/25, 2:52 PM

<a id='2369f2bb-93b6-4585-920a-559e9069124a'></a>

WiFiNINA | Arduino Documentation

<a id='42b0c0eb-dafc-4181-8993-bf76eb90ba0c'></a>

ARDUINODOCS

<a id='dd9f946b-7c9f-470c-833d-e740d429e185'></a>

WiFi.disconnect()

## Description
Disconnects the WiFi from the current
network.

## Syntax
```
1 WiFi.disconnect()
```

## Parameters
None

## Returns
Nothing

<a id='9f1b598f-ef27-4d61-bbed-01c596484244'></a>

WiFi.config()

<a id='82c50c3f-c78a-4100-999c-7767bd296199'></a>

## Description
WiFi.config() allows you to configure a static IP address as well as change the DNS, gateway, and subnet addresses on the WiFi shield.

<a id='2d6bbeff-7efe-4d63-a281-267ad4f64e54'></a>

Unlike WiFi.begin() which automatically
configures the WiFi shield to use DHCP,
WiFi.config() allows you to manually set the
network address of the shield.

<a id='2cb7e9f5-8695-4927-9038-99c6a7263325'></a>

Calling WiFi.config() before WiFi.begin()
forces begin() to configure the WiFi shield
with the network addresses specified in
config().

<a id='a429c007-77a1-4a9d-9b12-1f81d7bdaf6d'></a>

You can call WiFi.config() after WiFi.begin(),
but the shield will initialize with begin() in
the default DHCP mode. Once the config()
method is called, it will change the network
address as requested.

<a id='cc7ecb47-d578-42d9-8b67-64fc85593fa1'></a>

Syntax

<a id='18472d8b-a457-49b4-9c97-177dd92d2cb4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='d879b97e-31cc-4328-854d-c5c910dc5356'></a>

6/30