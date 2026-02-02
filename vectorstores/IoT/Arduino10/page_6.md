<a id='8d7e61bb-0a5a-42c3-a071-3e387e332666'></a>

12/4/25, 2:52 PM

<a id='6b336e6a-f779-4a4f-b41b-6aba3778e5d2'></a>

WiFiNINA | Arduino Documentation

<a id='f2b3e370-1412-4add-ba5d-760adf3e7075'></a>

ARDUINODOCS

<a id='12d4e01e-5b41-439e-9d8e-7ae06abd0b9f'></a>

## Description

Connect to the IP address and port specified in the constructor. The return value indicates success or failure. connect() also supports DNS lookups when using a domain name (e.g., google.com).

<a id='9a6bb942-fafa-4f00-80a6-1e48594c611f'></a>

## Syntax

```
1 client.connect(ip, port)
2 client.connect(URL, port)
```

<a id='d39aa706-f5a1-4935-a2d7-7770030cde5a'></a>

# Parameters

ip: the IP address that the client will connect to (array of 4 bytes)

URL: the domain name the client will connect to (string e.g., "arduino.cc")

port: the port that the client will connect to (int)

<a id='f5a5c851-214c-463e-b1f6-5dfb4d84d3d1'></a>

# Returns

Returns true if the connection succeeds, false if not.

<a id='d92d6e3d-f6d4-4bd1-bb1e-9494a5371ee9'></a>

Example

____________________________________

<a id='a1f9845b-c0e9-4ea5-87e8-f5d0eddfed40'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e548320f-d190-43ce-991a-054db303525e'></a>

6/16