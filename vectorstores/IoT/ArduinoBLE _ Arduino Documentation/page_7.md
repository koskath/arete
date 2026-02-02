<a id='876a9fbd-d5a7-4361-854f-de587cdbbf59'></a>

12/4/25, 2:49 PM

<a id='cb23d359-a7ba-40fe-a0aa-e4d836108923'></a>

ArduinoBLE | Arduino Documentation

<a id='a644278f-8099-4869-bd65-0b9e1c70534a'></a>

ARDUINODOCS

<a id='1916ec78-03c2-4410-b301-8096c60b2737'></a>

[Empty Field]

<a id='2a975653-3edf-4f62-93ff-7d632739be76'></a>

1 BLE.connected()

<a id='58d02138-342e-4540-b267-0f1930f46117'></a>

Parameters

None

<a id='39ecd40b-be17-44d3-a2f0-aff093387c97'></a>

## Returns

**true** if another Bluetooth® Low Energy device is connected, otherwise **false**.

<a id='8d1b1f84-ecf1-45fd-b277-3fcea1f2deac'></a>

Example

```
1 // while the central is still connected to periphe
2 while (BLE.connected()) {
3 
4     // ...
5 }
```

<a id='2247ab1d-4ca0-4b34-9ca3-70bb4d2271b1'></a>

## BLE.disconnect()
Disconnect any Bluetooth® Low Energy devices that are connected

### Syntax
```
1 BLE.disconnect()
```

### Parameters
None

### Returns
**true** if any Bluetooth® Low Energy device that was previously connected was disconnected,
otherwise **false**.

<a id='7582058f-8480-41ca-b874-5c1cc55c993c'></a>

Example

____________________________________________________________________________________________________

<a id='caf558d9-9dbb-42a5-ad0c-b0584db3da61'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='7b2c1bfe-2c64-4864-92ef-9293b0043512'></a>

8/26