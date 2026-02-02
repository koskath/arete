<a id='fc20df37-e9cc-489a-983d-f656cc794924'></a>

12/4/25, 2:51 PM

<a id='26e1f7b3-c17d-4c27-bb56-9b25776a7f1b'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='3b28fafa-a7f3-4ff4-9de7-a6e71bba0467'></a>

ARDUINODOCS

<a id='14780e8b-6dd8-4da4-8d8c-4855f1aacf44'></a>

[ ]

<a id='ca3d5fd9-cd80-4e01-aeb5-4f1e318d6b41'></a>

1 GPS.satellites()

<a id='ef637d1d-85a9-4ffe-8b65-a34142c21cf3'></a>

Parameters

None.

<a id='19d67639-988f-49b3-8b82-724a28472236'></a>

# Returns

The number of satellites being tracked by
the GPS.

<a id='581e645f-b238-4447-a7f1-8e253e6e6f1e'></a>

Example

```
1 // Check if there is new GPS d
2 if (GPS.available()) {
3   // Read GPS values
4   int satellites = GPS.satel
5 
6   // ...
7 
8   // Print GPS data
9   Serial.print("Number of sa
10  Serial.println(satellites)
11 }
```

<a id='9a85247c-d550-4222-b939-73d91f783e95'></a>

See also

begin()
end()
available()
latitude()
longitude()
speed()
course()
variation()
altitude()
getTime()
standby()
wakeup()

<a id='4b6af1d9-1f0c-462b-b225-2f2a29408a97'></a>

v getTime()
Read the current epoch time from the GPS.

## Syntax

```

```

<a id='45f06728-c84c-4928-8e20-fc4a14f6b7ba'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='0047ad89-f304-4902-aaa0-c2c5b079410f'></a>

11/15