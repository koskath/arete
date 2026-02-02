<a id='63c7d4c0-43dc-4d42-9259-9fe10caa074f'></a>

12/4/25, 2:51 PM

<a id='c4183200-a30e-472c-b90d-b809a9ba6be1'></a>

ArduinoBLE | Arduino Documentation

<a id='15d166ee-a950-4e38-be19-4845b13dede9'></a>

ARDUINODOCS

<a id='70e8e135-4343-4d94-87a4-dbe7be86f0b0'></a>

1 BLEService ledService("19B10000-E8F2-537E-4F6C-D16
2
3
4 Serial.print("LED service UUID = ");
5 Serial.println(ledService.uuid());

<a id='89240c9d-3664-48d9-ba81-ccfb43ed141f'></a>

## bleService.addCharacteristic()
Add a BLECharacteristic to the Bluetooth® Low Energy service.

### Syntax
```
bleService.addCharacteristic(bleCharacteristic)
```

### Parameters
None

### Returns
Nothing

### Example
```
BLEService ledService("19B10000-E8F2-537E-4F6C-D1

// Bluetooth® Low Energy LED Switch Characteristi
BLECharacteristic switchCharacteristic ("19B10001-




// add the characteristic to the service
ledService.addCharacteristic(switchCharacteristic
```

<a id='f06d2dc8-885f-4131-b131-9b502abd88ac'></a>

bleService.characteristicCount()
Query the number of characteristics discovered for the Bluetooth®
Low Energy service.

<a id='672aa3c1-67ba-4e69-b317-a63a202063da'></a>

Syntax

```
1 bleService.characteristicCount()
```

<a id='171a2820-8adc-4d1d-a652-50a5b1c4a16d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='0cbf0d3c-de86-4ea8-82de-fef668555946'></a>

6/9