<a id='fec4cfb6-83f4-4544-8656-ccdb72bbb4b5'></a>

12/4/25, 2:50 PM

<a id='baa5b6ea-c05c-4cdd-a9e1-64908b9e708d'></a>

ArduinoBLE | Arduino Documentation

<a id='50988b83-f7ca-4874-937d-078aaa22308e'></a>

ARDUINODOCS

<a id='cf610da1-5837-402a-a8da-efaf0dac7cea'></a>



<a id='385f4419-d609-4f90-b085-5d6a96148cb7'></a>

## Syntax

```
1 bleDescriptor.value()
```

<a id='a9df6cc9-4d12-42b7-925c-6fd3d30f18a6'></a>

Parameters

None

<a id='5d59a9d4-fe77-40bb-950a-4259caa18156'></a>

## Returns

Value byte array of the **BLE descriptor**.

<a id='6583effc-d50b-4aac-a45c-61e3b768b49b'></a>

Example

```
1 BLEDescriptor millisLabelDescriptor("2901", "mil]
2
3
4
5   int descriptorValueSize = millisLabelDescriptor
6   byte descriptorValue[descriptorValueSize];
7
8   for (int i = 0; i < descriptorValueSize; i++) {
9     descriptorValue[i] = millisLabelDescriptor.va
10  }
```

<a id='c64535d3-8d22-4ea4-80b3-553fd087137e'></a>

bleDescriptor.readValue()

Read the current value of the descriptor. If the descriptor is on a remote device, a read request will be sent.

### Syntax

```
1 bleDescriptor.readValue(buffer, length)
2 bleDescriptor.readValue(value)
```

<a id='933c8ad2-51a8-4f0a-924f-c4ade665a97d'></a>

## Parameters

**buffer**: byte array to read value into
**length**: size of buffer argument in bytes
**value**: variable to read value into (by reference)

<a id='26a80ff6-ab8a-435f-8f42-b68d259621b0'></a>

Returns

<a id='b83c384f-47dc-420d-9d7a-194a3e3a60d2'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='32301cda-e487-4b91-ae12-510a73e568f9'></a>

8/10