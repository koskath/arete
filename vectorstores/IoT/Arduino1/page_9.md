<a id='44eaa3c0-be9a-49f6-a90d-c573ee8656e4'></a>

12/4/25, 2:50 PM

<a id='fc904177-8e7e-4d1a-9e57-9186314171cb'></a>

ArduinoBLE | Arduino Documentation

<a id='9e11a09f-0497-44c4-9b6d-1fdd133ea0d1'></a>

ARDUINODOCS

<a id='e0d8000f-554e-4718-9f39-94c884f77519'></a>



<a id='e38ccc0a-99ea-4f17-ac9c-f50cb6b18031'></a>

Example

```
1 byte value = 0;
2
3 // get the value, descriptor is 1 byte so use by
4 descriptor.readValue(value);
```

<a id='261cc339-f71a-47bd-84bc-bb517174bfcd'></a>

v bleDescriptor.read()
> Perform a read request for the descriptor.

<a id='3303034f-e96f-4716-a9fb-ae02e72c595c'></a>

## Syntax

```
1 bleDescriptor.read()
```

<a id='802a9eda-b2a9-464f-b0f5-31ada463fc68'></a>

**Parameters**

None

<a id='c9daaf86-b003-4285-8400-432bb751cffb'></a>

Returns

**true**, if successful,
**false** on failure

<a id='28ac1cfd-0802-49eb-8fdd-9ab872b64dd7'></a>

Example

```
1 if (descriptor.read()) {
2   Serial.println("descriptor value read");
3
4   // ...
5 } else {
6   Serial.println("error reading descriptor value");
7 }
```

<a id='3dac71ea-3cfe-49c7-90b2-38f9b51098e7'></a>

Was this article helpful?

---



See more related articles

<a id='fefaf83b-4cfd-4891-95e0-384dff27f383'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='2df2b138-cb11-48f4-8e3a-8e78aee32db2'></a>

9/10

<a id='9ae0c459-3fd3-4d62-8c19-2c23e1cedcea'></a>

Connect and Contribute