<a id='e1b11806-0e98-49c0-a84b-5c8b1e9e165f'></a>

12/4/25, 2:49 PM

<a id='800bf829-ab48-44c1-8cb7-16dbdc61b7fb'></a>

ArduinoBLE | Arduino Documentation

<a id='95e47a89-7dfe-4494-aae6-dd47a4778685'></a>

ARDUINODOCS

<a id='bcddf7dc-0f94-49b4-a311-08ea7aa4b173'></a>

Add a BLEService to the set of services the Bluetooth® Low Energy device provides

## Syntax
```
BLE.addService(service)
```

## Parameters
service: BLEService to add

## Returns
Nothing

## Example
```
BLEService ledService("19B10000-E8F2-537E-4F6C-D1

// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energ
  while (1);
}
// ...
BLE.addService(ledService);
```

<a id='e3c26872-d5eb-4f51-9da8-d21b80061595'></a>

### BLE.advertise()

Start advertising.

## Syntax

```
1 BLE.advertise()
```

## Parameters

None

<a id='204a3574-38d0-415e-b533-c7f84c888bfd'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='0d60c841-b5cd-4a17-a4c4-a135d5d63f91'></a>

15/26

<a id='a9d50be3-cfa8-4a73-966a-aa333ada1d0f'></a>

15
16 // ...