<a id='fa242a42-06c7-4e9c-b451-5ab9655888df'></a>

12/4/25, 2:50 PM

<a id='a97cda28-7e8c-4e0b-9f27-7501175b2969'></a>

ArduinoBLE | Arduino Documentation

<a id='dd76e6a2-03a6-4959-bbca-388ed5580af6'></a>

ARDUINODOCS

<a id='ea6d3e72-4eca-4f23-b54e-834794e37adb'></a>

// ...

// retrieve the simple key characteristic
BLECharacteristic simpleKeyCharacteristic = per

// subscribe to the simple key characteristic
Serial.println("Subscribing to simple key chara
if (!simpleKeyCharacteristic) {
    Serial.println("no simple key characteristic
    peripheral.disconnect();
    return;
} else if (!simpleKeyCharacteristic.canSubscrib
    Serial.println("simple key characteristic is
    peripheral.disconnect();
    return;
} else if (!simpleKeyCharacteristic.subscribe()
    Serial.println("subscription failed!");
    peripheral.disconnect();
    return;
}

// ...

simpleKeyCharacteristic.unsubscribe();

<a id='961ca291-381a-4d27-b728-f4bd34e98841'></a>

v bleCharacteristic.valueUpdated()
Has the characteristics value been updated via a notification or
indication.

<a id='9299aa0d-ab6c-4199-bf8f-6474d77f0414'></a>

# Syntax

```
1 bleCharacteristic.valueUpdated()
```

<a id='e5f47171-034e-4880-ac73-ab71b83dd50f'></a>

Parameters

None

<a id='89109143-6128-4fef-b570-b16b26bccb2d'></a>

Returns

**true**, if the characteristics value been updated via a notification or indication

<a id='683d0d1e-e7f5-47f3-a2a4-af95336abfef'></a>

Example

________________________________________________________________________________

<a id='b0891781-e563-451b-a149-e7ea94b57ddb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='a2be90fd-6150-41af-bb9b-8c23c6a2b7f8'></a>

21/22