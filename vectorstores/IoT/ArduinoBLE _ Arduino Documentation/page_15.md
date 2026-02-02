<a id='85541095-2679-443e-8a90-48d51e96508b'></a>

12/4/25, 2:49 PM

<a id='52669e7f-bb6d-4f01-8f22-d3a6e68af1f8'></a>

ArduinoBLE | Arduino Documentation

<a id='cc104fb8-4ebe-4d1e-b868-085f68b97f44'></a>

ARDUINODOCS

<a id='8b49ac5a-eab5-4410-a3c3-8b892d4f248f'></a>

Set if the device is connectable after advertising, defaults to **true**.

### Syntax

```
1 BLE.setConnectable(connectable)
```

<a id='33d76a8c-ad6f-4100-8603-2ee0b54ab5d6'></a>

# Parameters
true: the device will be connectable when advertising
false: the device will NOT be connectable when advertising

<a id='efa33b03-6594-421a-9d1d-86636e654481'></a>

Returns

Nothing.

<a id='29c4fe65-ea47-4eb0-a87d-b51d1f2b1a75'></a>

Example

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ
4 
5   while (1);
6 }
7 
8 // ...
9 
10 BLE.setConnectable(false); // make the device i
```

<a id='4427336f-cd82-42ff-a57e-1854f7351802'></a>

BLE.scan()
Start scanning for Bluetooth® Low Energy devices that are advertising.

## Syntax

```
1 BLE.scan()
2 BLE.scan(withDuplicates)
```

<a id='e67a037f-6bab-4d67-a750-3025cef0ac29'></a>

## Parameters

**withDuplicates**: optional, defaults to **false**. If **true**,
advertisements received more than once will not be filtered

<a id='3c7e5991-7378-440e-83f9-8619de5bd9e1'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='42494768-05fb-48d4-ae6a-01c40ddba371'></a>

20/26