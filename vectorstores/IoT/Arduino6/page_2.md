<a id='00fd4d8a-9d41-488c-bd6f-c268131a6d16'></a>

12/4/25, 2:51 PM

<a id='a3eaeebe-32b0-4935-8d62-f02852ab18cb'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='92f0ed4f-0e45-470a-81dd-526dbc731494'></a>

ARDUINODOCS

<a id='30af456e-dac1-4356-84d1-39364b80b623'></a>

ARDUINODOCS [ ]

<a id='897e6520-a690-4222-ba3c-62a7d9fab3f8'></a>

1 GPS.begin()
2 GPS.begin(mode)

<a id='7065eeaf-8589-41b5-8745-233ee5a5efa5'></a>

# Parameters

`GPS_MODE_I2C`
to use the MKR GPS with the I2C cable
(default setting),

`GPS_MODE_SHIELD`
if using the MKR GPS as a shield.

<a id='2cf18585-f931-420f-88b0-c20b4b8ca36e'></a>

**Returns**

1 on success, 0 on failure.

<a id='b7045360-b05a-4d71-912a-90feb0ea6d8b'></a>

Example

```
1 if (!GPS.begin()) {
2   Serial.println("Failed to i[illegible]");
3   while(1);
4 }
```

<a id='b4ff59fe-25f4-4f84-88de-e0a9194a550b'></a>

## See also

*   end()
*   available()
*   latitude()
*   longitude()
*   speed()
*   course()
*   variation()
*   altitude()
*   satellites()
*   getTime()
*   standby()
*   wakeup()

<a id='c89dcff7-26c4-44dd-9535-d1db4a6f3551'></a>

## end()
De-initialize the GPS.

### Syntax

```
1 GPS.end()
```

<a id='b22292cc-47df-4bc8-90f7-39096e9fc192'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='ecb10119-77fc-4906-9ca4-a59fd2982a80'></a>

2/15