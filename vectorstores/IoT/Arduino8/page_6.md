<a id='147e4b32-34ab-4197-9f0c-831a51379318'></a>

12/4/25, 2:52 PM

<a id='ce0e2087-6381-48e6-8949-05887f241e3d'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='24f2cdb9-4daa-42fb-bcc1-a7b34ae04dc2'></a>

ARDUINODOCS

<a id='e3ad485d-106d-44ef-81c5-48021e04d1f2'></a>

# Description

Returns the module ID. When a module is manufactured, a unique SigFox ID is recorded in its permanent memory. It is very important to keep and store the ID tray carefully, as it will be useful to insure the tracability of these devices and to register them on a SigFox Network Operator (SNO).

<a id='f52da79d-d530-48fc-b207-6c108afbc2f7'></a>

## Syntax

```
1 SigFox.ID();
```

<a id='c464a330-8702-4834-9174-7e1616d0c19b'></a>

# Returns

A String that contains the 4 bytes ID.

<a id='5a307330-9166-41e2-bba7-abbebee617f0'></a>

SigFox.PAC()

<a id='956f202d-f02e-4d6d-afe8-1743ffe1dfce'></a>

# Description

Returns the module PAC. For each module, a PAC key is a secret key corresponding to the Sigfox ID. The PAC key will be useful to register a device on a SigFox Network Operator (SNO). As opposed to the SigFox ID, a PAC key is not transferable and must be re-generated if the module's ownership is changed.

<a id='6cfbdccd-1bdd-4768-8ca7-2ce52b6643de'></a>

## Syntax

```
1 SigFox.PAC();
```

<a id='3159d5f0-cc09-4a42-b55c-e13eb9c7fbe2'></a>

## Returns

A String that contains the 16 bytes PAC.

<a id='6cf1ee6f-78d0-4840-8583-b0c219d5178e'></a>

SigFox.reset()

<a id='fb3a319c-f181-41f5-b883-0b31b11b9aa3'></a>

Description

<a id='d4ca0e7c-1edc-4b43-a462-c77ceb2f0599'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='bd06cd9d-8c7d-48ee-8cb8-1a176541e55d'></a>

8/13