<a id='0c84d4c7-91a6-4447-a491-a3b2c2612cb9'></a>

ARDUINODOCS

<a id='d9bff3bc-a39a-4913-86b0-cb6587269a5f'></a>

Empty input field.

<a id='81aec2c2-ffbc-412f-8ca1-fedfb5e246be'></a>

MKR Connector Carrier that follows this pin mapping:

<a id='86ea08db-d832-4940-842a-56f646977af7'></a>

PinFunctrionNotespin1SCLI2C
Clockpin2SDAI2C
Datapin3VCCPower to module
5V/3.3Vpin4GNDGround

<a id='e405aa0a-67a2-4bac-bdf3-99cac6d4a390'></a>

# CodeTo drive the modules you need to load four separate libraries:```cpp1 #include <DHT.h>2 #include <DHT_U.h>3 #include <Wire.h>4 #include <SeeedOLED.h>```

<a id='0b690440-217f-4790-8fb7-c9ca61069812'></a>

The DHT module is mapped on
D0 when the object dht is
instantiated:

<a id='a03e6ad8-34ad-4db2-a570-b5bbeeed6640'></a>

1 DHT dht(0, DHT22);

<a id='504a97cf-0087-4909-8604-32a0e47e6630'></a>

The rest of the code is
straightforward and keeps
reading the `hum` and `temp`
values to be printed on the OLED
screen.

<a id='2e1a23b5-3618-4faa-9ff6-1a2af8de8d34'></a>

Here is the complete sketch:

<::transcription of the content
: An empty, rounded rectangular box representing a sketch.::>