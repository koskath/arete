<a id='6936260c-567b-44a7-b3f0-efc46d234773'></a>

12/4/25, 2:51 PM

<a id='f78e0292-2f26-4e4f-8e07-69a0ad5fc1e8'></a>

ArduinoBLE | Arduino Documentation

<a id='fb22d90d-2215-4fd6-a2c5-f2af4a1f386d'></a>

ARDUINODOCS

<a id='0d676843-6f39-4426-8b8c-c995fc692ee1'></a>

```c
// listen for Bluetooth® Low Energy peripherals to
BLEDevice central = BLE.central();

// if a central is connected to peripheral:
if (central) {
  Serial.print("Connected to central: ");
  // print the central's MAC address:
  Serial.println(central.address());
}
```

<a id='bc19d891-45f3-489f-b355-bceb6c17a25c'></a>

bleDevice.rssi()
Query the RSSI (Received signal strength indication) of the Bluetooth® Low Energy device.

<a id='dd7a15a4-38c7-41de-ab93-1240e8c08eab'></a>

## Syntax

```
1 bleDevice.rssi()
```

<a id='3da0a5ff-7ca8-40d3-b567-83f819bf49c4'></a>

Parameters

None

<a id='e69203d4-1b06-4413-8106-c7d2b53268d1'></a>

Returns

**RSSI** of the connected Bluetooth® Low Energy device, 127 if
the Bluetooth® Low Energy device is not connected.

<a id='65be3d43-87a0-4a84-ad6e-37522530bd32'></a>

# Example

```
1 if (bleDevice.connected()) {
2   Serial.print("RSSI = ");
3   Serial.println(bleDevice.rssi());
4 }
```

<a id='20765b72-a14c-41bd-8369-1e7c6cf7d19a'></a>

v bleDevice.characteristic()
  Get a BLECharacteristic representing a Bluetooth® Low Energy
  characteristic the device provides.

<a id='a6f3d58d-3d16-4d15-87af-c51dd9d4ab77'></a>

Syntax

```

```

<a id='5668a19d-2096-4a72-aef8-c957194de6ba'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='0e0379dc-bc8f-4591-b3e5-50ce2ad0fc83'></a>

8/24