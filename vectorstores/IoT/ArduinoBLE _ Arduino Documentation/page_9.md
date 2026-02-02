<a id='c570851c-d85a-4bdf-81c4-cd767881632c'></a>

12/4/25, 2:49 PM

<a id='42fb27c0-c051-476f-b969-18d9f77dcae5'></a>

ArduinoBLE | Arduino Documentation

<a id='9c0f4e88-ce86-4538-8636-a19a2aaeec68'></a>

ARDUINODOCS

<a id='7554cb30-a6c0-4e1a-aadb-882f889bbb36'></a>

An empty input field.

<a id='57610e10-f63f-484b-8f6b-e640d4b9a765'></a>

## Returns
The **RSSI** of the connected Bluetooth® Low Energy device, 127 if no Bluetooth® Low Energy device is connected.

<a id='434c716e-db26-4c4a-a759-ff3b0f72b49b'></a>

# Example

```
1 if (BLE.connected()) {
2    Serial.print("RSSI = ");
3    Serial.println(BLE.rssi());
4 }
```

<a id='1b8f30d5-6b38-4a0b-8728-b9cafeb24b5c'></a>

BLE.setAdvertisedServiceUuid()
Set the advertised service UUID used when advertising.

# Syntax

```
1 BLE.setAdvertisedServiceUuid(uuid)
```

<a id='3f98910a-44a2-4fc0-9cbb-8a28c4c73e88'></a>

## Parameters

**uuid**: 16-bit or 128-bit Bluetooth® Low Energy UUID in **String** format

<a id='d468c20b-2ada-48fc-996f-dc0a6d1aef42'></a>

Returns
Nothing

<a id='14ca31eb-19d5-480e-8174-cf8ec9589334'></a>

Example

```
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy");
  while (1);
}

BLE.setAdvertisedServiceUuid("19B10000-E8F2-537");

// ...

// start advertising
BLE.advertise();
```

<a id='22f0f0dd-6df2-42d4-823e-2c9193232a0f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='97135ad1-3ac8-4070-b646-8b676cd803c5'></a>

10/26