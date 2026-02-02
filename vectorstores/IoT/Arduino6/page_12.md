<a id='d3d31586-f528-433b-a77e-a7eee74494a7'></a>

12/4/25, 2:51 PM

<a id='efe86ef5-4ac8-4ab4-b83d-3f1dd0b9b4a8'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='b689a70c-37df-43c7-b3b3-f3dcedb3326b'></a>

ARDUINODOCS

<a id='8dc5d394-3390-4693-8405-779793c0fd66'></a>

## Parameters

None.

<a id='684d9e21-7f63-427a-8a94-076b32f9f147'></a>

## Returns

The current epoch time from the GPS.

<a id='d20dbcfd-a308-46c3-9d1e-cfaa7fa3b2cd'></a>

Example

```
1 // Check if there is new GPS d
2 if (GPS.available()) {
3   // Read GPS values
4   unsigned long epochTime = 
5
6   // ...
7
8   // Print GPS data
9   Serial.print("Epoch time: ");
10  Serial.println(epochTime);
11 }
```

<a id='a777d53e-e822-431a-a54b-81f9de28bc78'></a>

## See also

begin()

end()

available()

latitude()

longitude()

speed()

course()

variation()

altitude()

satellites()

standby()

wakeup()

<a id='88bb0f09-7ed5-4c61-9a0c-9c11a5ce52ff'></a>

v standby()

<a id='bbe01bfe-e6b5-4ec0-ae69-055102e50f23'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='2aa29b77-d65b-4be8-964c-5a514094dad1'></a>

12/15