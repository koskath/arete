<a id='818b6629-ccd6-469b-8682-b8fc6fba71fb'></a>

12/4/25, 2:51 PM

<a id='30d03dcf-6bfb-415d-8390-dc1edfe93f42'></a>

ArduinoBLE | Arduino Documentation

<a id='793b31fb-9726-4ade-882b-9d0cba532d1b'></a>

ARDUINODOCS

<a id='947f9359-1991-4343-8a87-c82fb2a1728b'></a>



<a id='4736489c-2a6a-4c17-b37a-16cf34fe2063'></a>

Query if a Bluetooth® Low Energy device is connected

## Syntax

```
bleDevice.connected()
```

<a id='6616d54e-2d15-4f5d-b72b-51db1f5f1bd7'></a>

Parameters

None

<a id='68394d2d-8071-4495-a724-1825fd30aad4'></a>

## Returns

**true** if the Bluetooth® Low Energy device is connected,
otherwise **false**.

<a id='12a5cce3-10b9-4757-a83d-9dbb1b1bbc60'></a>

## Example

```
// listen for Bluetooth® Low Energy centrals to connect
BLEDevice central = BLE.central();

// while the central is still connected
while (central.connected()) {

  // ...
}
```

<a id='ee0c3b5b-cd69-4a56-9503-46d744247567'></a>

bleDevice.disconnect()

<a id='edc44ddf-e8f8-4950-928d-e0852d740b75'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='ad750222-795f-4b72-abd7-47e9dc9dde20'></a>

6/24