<a id='ebb7658c-68dc-4bfb-b719-41fd98492492'></a>

12/4/25, 2:50 PM

<a id='92e095bd-ecad-4fe1-9686-f3d0781eb7ba'></a>

ArduinoBLE | Arduino Documentation

<a id='fffc93e0-5217-4a62-bb14-6ade2207508c'></a>

ARDUINODOCS

<a id='e7721738-7176-47a9-90cf-be4d7afbdc03'></a>

```
// Bluetooth® Low Energy LED Switch Characteristic
BLEByteCharacteristic switchCharacteristic("19B100



Serial.print("value length = ");
Serial.println(switchCharacteristic.valueLength())
```

<a id='7559374e-4792-494f-9cd7-c5e9509f982b'></a>

✓ bleCharacteristic.readValue()
Read the current value of the characteristic. If the characteristic is on a remote device, a read request will be sent.

<a id='2cc9c132-da4c-4d84-973a-6ba9e59d7d79'></a>

## Syntax

```
1 bleCharacteristic.readValue(buffer, length)
2 bleCharacteristic.readValue(value)
```

<a id='23674157-b50a-468c-b668-d33905c0a418'></a>

## Parameters

**buffer**: byte array to read value into length: size of buffer
argument in bytes

**value**: variable to read value into (by reference)

<a id='5caff8db-7c65-4541-b512-a46d0111b7fb'></a>

Returns

Number of bytes read

<a id='b2ce3f63-5d38-4a1e-98ce-dfa19021f6b9'></a>

Example

```
while (peripheral.connected()) {
  // while the peripheral is connected

  // check if the value of the simple key chara
  if (simpleKeyCharacteristic.valueUpdated()) {
    // yes, get the value, characteristic is 1
    byte value = 0;
    simpleKeyCharacteristic.readValue(value);

    if (value & 0x01) {
      // first bit corresponds to the right but
      Serial.println("Right button pressed");
    }

    if (value & 0x02) {
      // second bit corresponds to the left but
      Serial.println("Left button pressed");
    }
  }
}
```

<a id='f5896af8-7d7e-4576-a27b-44c41bf35872'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='c90ac188-c440-474e-add9-d274e3d2814b'></a>

9/22