<a id='07be0d24-d03e-4c29-88bf-9d8059426a05'></a>

12/4/25, 2:52 PM

<a id='127c28f9-6858-491d-8438-87717a443fe2'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='e3bf6c8f-642d-439b-bdd3-f6f3ce64b089'></a>

ARDUINODOCS

<a id='31d14393-924c-4e5e-bb26-17cdf88e604a'></a>

[ ]

<a id='c94fb2cb-e9d8-4c5d-8e3b-1c6c65f4a45a'></a>

## Syntax

```
1 SigFox.statusCode(protocol);
```

<a id='2093a134-6016-4ca9-bd38-5f535ff857cb'></a>

## Parameters

protocol: can be one of either:
- SSM
- ATMEL
- SIGFOX

<a id='f3e93206-6fd9-4bc4-86c4-d0c4c032a7ef'></a>

**Returns**
the status code of the chosen protocol:

<a id='b532a5cf-d912-41b8-a531-f859b78a619a'></a>

SSM

TBD

<a id='f077ddc7-ca56-4fd8-9449-d52dab291752'></a>

**Atmel**

Bit0: PA on/off indication Bit6: System ready
to operate (system ready event) Bit5: Frame
sent (frame ready event) Bit4 to Bit1: Error
code

<a id='7939c9d9-cf6b-4c42-bdd4-f447d1ba0d05'></a>

0000: no error
0001: command error / not supported
0010: generic error
0011: frequency error
0100: usage error
0101: opening error
0110: closing error
0111: send error

<a id='a89b37f2-7dd0-4885-870e-107a2e632bc2'></a>

SIGFOX
<table id="5-1">
<tr><td id="5-2">0x00</td></tr>
<tr><td id="5-3">No error</td></tr>
<tr><td id="5-4">0x01</td></tr>
<tr><td id="5-5">Manufacturer error</td></tr>
<tr><td id="5-6">0x02</td></tr>
<tr><td id="5-7">ID or key error</td></tr>
<tr><td id="5-8">0x03</td></tr>
<tr><td id="5-9">State machine error</td></tr>
<tr><td id="5-a">0x04</td></tr>
<tr><td id="5-b">Frame size error</td></tr>
<tr><td id="5-c">0x05</td></tr>
<tr><td id="5-d">Manufacturer send error</td></tr>
<tr><td id="5-e">0x06</td></tr>
<tr><td id="5-f">Get voltage/temperature error</td></tr>
<tr><td id="5-g">0x07</td></tr>
<tr><td id="5-h">Close issues encountered</td></tr>
<tr><td id="5-i">0x08</td></tr>
<tr><td id="5-j">API error indication</td></tr>
</table>

<a id='bf6d93a8-b481-43af-8210-a46e1989a809'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='eff8fa5e-123e-437d-9580-d5d3638479d9'></a>

6/13