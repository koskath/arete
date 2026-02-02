<a id='890f8c31-d1a6-44f2-9a18-60509ed04649'></a>

12/4/25, 2:51 PM

<a id='49e2e818-e982-4a34-932b-16ed5e5aefc1'></a>

ArduinoBLE | Arduino Documentation

<a id='294c1e09-cf8f-4309-910e-caff9ed019bd'></a>

ARDUINODOCS

<a id='15b5005a-94ae-4ad1-8af7-5fb6ec4a8223'></a>

Used to enable the services board provides or interact with services a remote board
provides.

<a id='6fc835a9-5b96-4b84-ab13-64b0cf0ea1ec'></a>

BLEService()
Create a new Bluetooth® Low Energy service.

### Syntax
```
BLEService(uuid)
```

### Parameters

uuid: 16-bit or 128-bit UUID in String format

### Returns

New BLEService with the specified UUID

### Example
```
BLEService ledService("19B10000-E8F2-537E-4F6C-D16
```

<a id='81e452f3-9ba2-45bc-873e-fd3e66f84004'></a>

### bleService.uuid()
Query the UUID of the specified BLEService.

## Syntax
```
1 bleService.uuid()
```

## Parameters
None

## Returns
UUID of the Bluetooth® Low Energy service as a **String**.

## Example

<a id='62b934b0-595f-43da-992f-400afda462e7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='f0a4ebbb-8b2a-4799-b824-8134ca7e1aff'></a>

5/9