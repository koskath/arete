<a id='48e6f1d0-9eb2-41d2-8ca1-e517489cef43'></a>

12/4/25, 2:49 PM

<a id='d3466cb0-896c-4e1c-8fca-6333f8b583d3'></a>

ArduinoBLE | Arduino Documentation

<a id='f9be48f9-bbad-46fe-9389-dd9fe932f39a'></a>

ARDUINODOCS

<a id='5bd1fdbe-8f76-4f3c-9557-9d715d46110e'></a>



<a id='6efa1081-f85b-4212-8c1c-8612de71711b'></a>

Returns

1 on success,
0 on failure.

<a id='dc323bbf-50c6-44e9-8465-b41ec9f26679'></a>

Example

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6 
7 // ...
8 BLE.advertise();
9 // ...
```

<a id='f5fd595c-e98b-4a42-aed9-68ce2ee85b73'></a>

BLE.stopAdvertise()
Stop advertising.

<a id='f2e8bc02-8b39-4daa-b176-657a1dc6a838'></a>

Syntax

```
1 BLE.stopAdvertise()
```

<a id='ed2e4560-73e0-4a32-a43f-9ffe111889c6'></a>

**Parameters**

None

<a id='533d05ab-90f8-46f9-89e8-d49729d71a8e'></a>

Returns

Nothing

<a id='ffc49552-c804-4f4f-aeb5-7a155e5cb8d1'></a>

**Example**

___

<a id='739f7777-e10c-40b7-8726-b18d7adffcf9'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='a0c7f467-0c52-4111-8516-d13d61cd851b'></a>

16/26