<a id='b7765bb5-31f1-4833-906e-9520ca473c6c'></a>

12/4/25, 2:51 PM

<a id='7780079c-54ef-4512-bc6c-a255f00e91b4'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='09e931a9-0a74-47cb-8201-a997959802f2'></a>

ARDUINODOCS

<a id='0693b72b-b9bc-4ed3-953e-a3e62b110c3f'></a>

## Parameters
None.

## Returns
Nothing.

## Example
```
1 if (!GPS.begin()) {
2    Serial.println("Failed to initialize");
3    while(1);
4 }
5
6 // Read GPS data here...
7
8 // Done working with the GPS
9 GPS.end();
```

## See also
begin()
available()
latitude()
longitude()
speed()
course()
variation()
altitude()
satellites()
getTime()
standby()
wakeup()

<a id='3a5bfeb4-4867-451f-a60b-04f5d82ad02e'></a>

> available()

√ latitude()
Read the latitude of the GPS.

### Syntax

```
1 GPS.latitude()
```

<a id='45fcb41b-2f6e-4265-9457-10b162c7124d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='63ee86f0-28c8-40c5-baa8-5cf4c2fdf15b'></a>

3/15