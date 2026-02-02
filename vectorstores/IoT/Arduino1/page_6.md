<a id='333a5b80-1737-46a0-9445-1f3a32dd9509'></a>

12/4/25, 2:50 PM

<a id='4ab19179-4d8a-4275-90ed-4a033f11a02c'></a>

ArduinoBLE | Arduino Documentation

<a id='1e210d06-458e-4916-b821-fef76fa4070c'></a>

ARDUINODOCS

<a id='48030e5f-566b-4b64-b9ea-8a8c182cc8c4'></a>



<a id='cfa5c3db-23c5-4273-965b-025f6f9d1ca5'></a>

Query the UUID of the specified BLEDescriptor.

# Syntax

```
1 bleDescriptor.uuid()
```

<a id='99c9cf59-5454-4ee4-ad25-e49cd2444c76'></a>

**Parameters**

None

<a id='906fe3a1-a867-4ed1-a4fa-6ea11ef51b96'></a>

## Returns

**UUID** of the Bluetooth® Low Energy descriptor (as a String).

<a id='08ea4f7e-5dd4-42b5-a656-aaf356ca701c'></a>

# Example

```cpp
1 BLEDescriptor millisLabelDescriptor("2901", "mill:
2
3
4 Serial.print("millis label descriptor UUID = ");
5 Serial.println(millisLabelDescriptor.uuid());
```

<a id='d14d8934-aeba-48d4-af4b-7563dfa991b1'></a>

bleDescriptor.valueSize()
Query the value size of the specified BLEDescriptor.

<a id='617a86f4-2bc1-4262-a7c5-1a17f651b967'></a>

## Syntax

```
1 bleDescriptor.valueSize()
```

<a id='2cf82898-af76-4bdf-9415-01f098d014c7'></a>

**Parameters**

None

<a id='c3c25f9e-01e6-40d0-855b-5b54227675a2'></a>

## Returns

**Value size** (in bytes) of the Bluetooth® Low Energy descriptor.

<a id='1c232784-d86a-4de7-87b1-d93397d924bd'></a>

Example

________________________________________________________________________________

<a id='14cab879-2d02-40b0-b3fc-904c6952c3fa'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='c5f12234-ca08-4b11-99a5-be9fbfd6a19b'></a>

6/10