<a id='4e303fbe-59a7-4f0d-a50c-d36486a2adba'></a>

12/4/25, 2:50 PM

<a id='4c7c2182-4876-4512-a508-6078de6d9e65'></a>

ArduinoBLE | Arduino Documentation

<a id='2c7caebe-c287-4c80-a385-7e945c5e2f3d'></a>

ARDUINODOCS

<a id='dd780b0a-e87c-4706-a87c-db0febbb0fd9'></a>

Used to describe a characteristic the board offers

<a id='20ca9c3f-b9ab-4fe9-8ef4-72a1dcbc6004'></a>

## BLEDescriptor()
Create a new Bluetooth® Low Energy descriptor.

### Syntax
```
1 BLEDescriptor (uuid, value, valueSize)
2 BLEDescriptor (uuid, stringValue)
```

### Parameters
*   **uuid**: 16-bit or 128-bit UUID in string format
*   **value**: byte array value
*   **valueSize**: size of byte array value
*   **stringValue**: value as a string

### Returns
New **BLEDescriptor** with the specified **UUID** and value

### Example
```
1 BLEDescriptor millisLabelDescriptor("2901", "mill:
```

<a id='9cd59ae7-7790-4b75-8185-eacd08532548'></a>

bleDescriptor.uuid()

<a id='c7f71419-6a1e-4439-8bd7-50d988547825'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='05a35227-6cee-4695-ad0d-ed079315327d'></a>

5/10