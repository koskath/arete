<a id='14ac22f7-1277-4e4e-8003-8f63b503d5ae'></a>

12/4/25, 2:52 PM

<a id='3a7751cb-4d00-40fe-b104-0df5153d542d'></a>

WiFiNINA | Arduino Documentation

<a id='3f834fbd-7ca9-419b-8182-4c442fbb2220'></a>

ARDUINODOCS

<a id='2611c8bd-2b95-464a-986b-4dde819e8895'></a>

# Description

Returns the firmware version running on the module as a string.

<a id='f252d268-6ad5-4fb1-b476-5621eb56d9b7'></a>

## Syntax

```
1 WiFi.firmwareVersion()
```

<a id='2ac0f700-f3d4-4671-8440-023f404943b9'></a>

Parameters

None

<a id='1cc67f62-1341-4e15-b95d-0ec4d3721de3'></a>

**Returns**

The firmware version running on the module as a string

<a id='2b0f3296-3595-40a3-b352-65b64dc57fb5'></a>

Example

```
1 ...
2 String fv = WiFi.firmwareVersio
3 if (fv < "1.0.0") {
4     Serial.println("Please upgrad
5 }
6 ...
```

<a id='d7c6c412-fa19-4f18-ad57-c41a17a12b67'></a>

⌄ WiFi.lowPowerMode()

<a id='1e6f1f5f-a55c-48c9-9635-8605d3e7d68e'></a>

# Description

Enable low power mode. This is an automatically managed mode where the WiFi NINA Module reduces its power drain bringing the overall power consumption to 30 mA. Any incoming data is received and the device sends out regularly the beacon signal each 100 ms to keep the AP connection alive.

<a id='2f3854c5-b426-4fb1-b727-0065d54ea002'></a>

## Syntax

```
1 WiFi.lowPowerMode()
```

<a id='c2cddecb-5443-4d53-b492-0cdc68607d1c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='5570462a-8bc6-43ae-a393-a3473a860048'></a>

22/30