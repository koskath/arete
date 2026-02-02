<a id='02768c68-21f0-4fea-ba1d-1037a5164984'></a>

12/4/25, 2:50 PM

<a id='b4d28ce9-78dc-4dad-858c-6a89a362b83a'></a>

ArduinoBLE | Arduino Documentation

<a id='70d23533-4cee-4087-806d-16b9e5996b2c'></a>

ARDUINODOCS

<a id='548e4d05-0eb2-430d-8a5b-8e83ad311f0a'></a>

// Bluetooth® Low Energy Battery Level Characteristic
BLEUnsignedCharCharacteristic batteryLevelChar("2
BLERead | BLENotify); // remote clients will





if (batteryLevelChar.subscribed()) {
  // set a new value , that will be pushed to
  batteryLevelChar.writeValue(0xab);
}

<a id='3960b986-420e-4da7-8f5f-4ce079489697'></a>

bleCharacteristic.addDescriptor()
Add a BLEDescriptor to the characteristic.

## Syntax
```
bleCharacteristic.addDescriptor(bleDescriptor)
```

## Parameters
bleDescriptor: descriptor to add to the characteristic

## Returns
Nothing

## Example
```
// Bluetooth® Low Energy Battery Level Characteristic
BLEUnsignedCharCharacteristic batteryLevelChar("2
BLERead | BLENotify); // remote clients will
BLEDescriptor batteryLevelDescriptor("2901", "mi]
batteryLevelChar.addDescriptor(batteryLevelDesc
```

<a id='7a4a5c13-f797-4838-a4a5-d9dfcf6e9868'></a>

bleCharacteristic.descriptorCount()

Query the number of Bluetooth® Low Energy descriptors
discovered for the characteristic

<a id='aed51ade-3960-41f0-a4c8-8f96979c5dfb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='17e8181c-e04b-416b-a684-5b2fef72a33b'></a>

14/22