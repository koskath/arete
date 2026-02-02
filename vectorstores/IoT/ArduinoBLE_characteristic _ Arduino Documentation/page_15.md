<a id='82f166e4-af8d-45e8-8f37-3cdd51a22efe'></a>

12/4/25, 2:50 PM

<a id='2714c5e2-5d5c-4d0e-8afe-0c14f926b6ca'></a>

ArduinoBLE | Arduino Documentation

<a id='05d84afc-c457-4d93-a2b5-0f7409d63816'></a>

ARDUINODOCS

<a id='9a7f992e-e2be-456a-9bd4-7d592cdee56f'></a>



<a id='bcd4ff74-9205-4c0f-91e5-c126e0d52ac1'></a>

## Syntax

```
1 bleCharacteristic.descriptorCount()
```

<a id='cb0ab12e-8566-4e80-9f40-0158d77f83bf'></a>

**Parameters**

None

<a id='3db11c92-756f-4a32-931c-2af1e8c1d954'></a>

## Returns

The **number of Bluetooth® Low Energy descriptors** discovered for the characteristic

<a id='a2bbedf0-328d-45fb-b90d-6f9c2c8ee48e'></a>

Example
```java
1 // loop the descriptors of the characteristic and
2 for (int i = 0; i < characteristic.descriptorCo
3     BLEDescriptor descriptor = characteristic.desc
4 
5     // ...
6 }
```

<a id='5fdb25b4-6bde-466e-ad78-e8ae842f528b'></a>

bleCharacteristic.hasDescriptor()
Check if a characteristic has a particular descriptor.

<a id='05353db3-19ff-44be-8569-279a402b8ccb'></a>

## Syntax

```
1 bleCharacteristic.hasDescriptor(uuid)
2 bleCharacteristic.hasDescriptor(uuid, index)
```

<a id='795eef76-bf4e-4994-926e-7f866f487e34'></a>

# Parameters

**index**: index of descriptor
**uuid**: uuid (as a String)

<a id='768ea601-8edd-47e4-8a42-42ae906d35a5'></a>

## Returns

**true**, if the characteristic has a matching descriptor,
otherwise **false**.

<a id='44a662b0-14f9-4e58-9636-c4a46b58f91b'></a>

Example

<a id='93026086-4a6b-4a7f-81f7-98319700c2d4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='e4647313-ede8-4ae3-a78d-f75bdccd5db0'></a>

15/22