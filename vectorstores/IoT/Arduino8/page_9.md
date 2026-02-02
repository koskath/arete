<a id='e5d47319-4b70-4bf2-a82b-83a92dc1ef3e'></a>

12/4/25, 2:52 PM

<a id='54a64f5a-6f16-4c35-8f1b-82661de29cae'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='ebd738fe-8e33-4b91-a761-3a7b66a2fd83'></a>

ARDUINODOCS

<a id='3dcf5904-90e2-46ff-b333-14b5c2e635cb'></a>

buffer (which holds 8 bytes). available()
inherits from the Stream utility class.

## Syntax

```
1 SigFox.available()
```

## Parameters

none

## Returns

the number of bytes available to read

<a id='a8944df7-f411-4db2-9352-eabeaddf1d14'></a>

read()

<a id='2e5b8daa-5aeb-4250-a500-a183a8ce3baf'></a>

# Description
Reads incoming SigFox data. read() inherits
from the Stream utility class.

<a id='6dacc00d-5242-45c5-8103-33a51cf7cd85'></a>

## Syntax

```
1 SigFox.read()
```

<a id='54f79565-83d2-400c-90fb-8b64762a1e73'></a>

**Parameters**

None

<a id='668d75d2-bfda-40dc-a4ff-12aefb3ba773'></a>

Returns
the first byte of incoming SigFox data
available (or -1 if no data is available) - int

<a id='2b867b2f-4656-4497-b3cc-658f24e13bc2'></a>

Example

[ ]

<a id='7663f6cb-e74c-4915-9e2c-942ae0636e14'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='97b4f15a-e612-4883-9580-a92a2f977869'></a>

12/13