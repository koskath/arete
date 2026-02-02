<a id='f1f59aa4-9f55-473b-95f3-dd437644046c'></a>

12/4/25, 2:51 PM

<a id='204ce839-a63d-4cc5-a981-df2c8c7ee26d'></a>

ArduinoBLE | Arduino Documentation

<a id='1cc26f81-69fd-45b4-80d2-ed3c845b325a'></a>

ARDUINODOCS

<a id='a4e4338a-fcaa-4915-9880-099d38779e43'></a>

Used to get information about the devices connected or discovered while scanning

<a id='9d176bf9-270f-44a4-b318-0ac6fdc5850a'></a>

bleDevice.poll()
Poll for Bluetooth® Low Energy radio events for the specified Bluetooth® Low Energy device and handle them.

### Syntax

```
bleDevice.poll()
bleDevice.poll(timeout)
```

### Parameters

timeout: optional timeout in ms, to wait for event. If not specified defaults to 0 ms.

### Returns

Nothing

### Example

```
// listen for Bluetooth® Low Energy centrals to co
BLEDevice central = BLE.central();

// if a central is connected to peripheral:
if (central) {
  central.poll();
}

// ...
```

<a id='0a52f717-105b-4874-9a01-4d11bf47ee6e'></a>

bleDevice.connected()

<a id='723aac76-6f2a-4241-928b-dc52bae5403c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='0e9debf5-077d-4b44-9a8a-828692e585eb'></a>

5/24