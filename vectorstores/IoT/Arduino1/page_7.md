<a id='e03cfa17-b036-4899-aa92-9fdea24412f7'></a>

12/4/25, 2:50 PM

<a id='757fbf44-1deb-4a2f-b932-84ee84a3a0a4'></a>

ArduinoBLE | Arduino Documentation

<a id='15866406-a89d-4a55-9a84-13a03c057b81'></a>

ARDUINODOCS

<a id='291f3108-c532-45d8-bc41-a95e8b60dde4'></a>

1 BLEDescriptor millisLabelDescriptor("2901", "mill:
2
3
4 Serial.print("millis label descriptor value size :
5 Serial.println(millisLabelDescriptor.valueSize())

<a id='666d8886-1a54-47fc-936b-a82d3dc1b664'></a>

✓ bleDescriptor.valueLength()

Query the length, in bytes, of the descriptor current value.

## Syntax

```
bleDescriptor.valueLength()
```

## Parameters

None

## Returns

Length of descriptor value in bytes.

## Example

```cpp
1 // read the descriptor value
2 descriptor.read();
3
4 // print out the value of the descriptor
5 Serial.print(", value 0x");
6 printData(descriptor.value(), descriptor.valuel
7 // ...
8
9 void printData(const unsigned char data[], int
10 for (int i = 0; i < length; i++) {
11 unsigned char b = data[i];
12
13 if (b < 16) {
14 Serial.print("0");
15 }
16
17 Serial.print(b, HEX);
18 }
19 }
```

<a id='36087d70-e1ce-40f3-8e25-27823a9fb809'></a>

bleDescriptor.value()

<a id='56d39cb6-9c95-49a9-81bc-af58106b7de6'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='7d27c6a4-9729-453a-8fd1-545e4fbbfeec'></a>

7/10