<a id='12297ffa-acf1-41ca-84ec-b892c5e181cf'></a>

12/4/25, 2:52 PM

<a id='00e6090b-6953-4089-a84e-d378c8067e1e'></a>

WiFiNINA | Arduino Documentation

<a id='a76c9f9b-0398-4748-8e13-a2c8866d4e77'></a>

ARDUINODOCS

<a id='181f7a91-c7ce-461e-bff8-0d6636849e83'></a>

WiFi.setHostname()

# Description

Sets the hostname of the module, the
hostname is sent in WiFi.begin(...) when an
IP address is requested from a DHCP server.

<a id='3da4d025-2997-4478-8afa-80c4af5ac6ad'></a>

## Syntax

```
1 WiFi.setHostname(hostname)
```

<a id='a08aafce-799a-4431-90a0-119baaa2d9aa'></a>

## Parameters

hostname - new hostname to use

<a id='6cf84426-dfc7-405c-b709-5cbb757fada2'></a>

Returns
Nothing

<a id='bc11976d-7901-4e8e-affb-eb0fe88cf176'></a>

Example

```arduino
1   ...
2   WiFi.setHostname("MyArduino"
3   
4   // attempt to connect to WiF
5   while (status != WL_CONNECTE
6       Serial.print("Attempting t
7       Serial.println(ssid);
8   // Connect to WPA/WPA2 net
9   status = WiFi.begin(ssid, 
10  
11  // wait 10 seconds for con
12  delay(10000);
13  }
14  ...
```

<a id='3b489754-32c2-46b1-bfc8-feaf187f3ecf'></a>

WiFi.setTimeout()

### Description
Sets the connection timeout value in milliseconds for WiFi.begin(...).

### Syntax


<a id='d3cdce8b-f99e-4a18-9b38-33b0181b2b83'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='95c68263-b61e-4ad9-95e4-4de7f72e8a08'></a>

9/30