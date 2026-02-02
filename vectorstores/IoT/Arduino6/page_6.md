<a id='f8825bd0-ba92-42c5-a25a-4d18cd90af04'></a>

12/4/25, 2:51 PM

<a id='185b771c-a5ba-40a2-a970-309d1cfb7c64'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='2d86dccc-b82c-4896-b8fb-cda2086663f3'></a>

ARDUINODOCS

<a id='a51de67e-caa6-4dce-bcf7-322c800e71c4'></a>



<a id='ff89c27d-603e-4bd0-b6f2-d328c006bdb9'></a>

Read the ground speed of the GPS.

## Syntax

```
1 GPS.speed()
```

<a id='91fc810d-2147-43dd-822b-f78c9dc0374f'></a>

**Parameters**

None.

<a id='5e769ba6-88ff-4ccb-85d9-d73bb57b8105'></a>

## Returns

GPS ground speed in km/h.

<a id='48d4d01b-8ee6-49c7-b1e9-d5f05f12e1d4'></a>

Example

```
1 // Check if there is new GPS data
2 if (GPS.available()) {
3   // Read GPS data
4   float speed = GPS.speed();
5 
6   // ...
7 
8   // Print GPS data
9   Serial.print("Ground speed ");
10  Serial.print(speed);
11  Serial.println(" km/h");
12 }
```

<a id='edffe3fd-7d42-443e-8bbd-4274e7913ae2'></a>

## See also

begin()
end()
available()
latitude()
longitude()
course()
variation()
altitude()
satellites()
getTime()
standby()
wakeup()

<a id='6aa296a6-c58e-4461-98f2-60b9eec3ad71'></a>

course()

<a id='ef0924c6-ae91-431f-8f33-5433d7b8d991'></a>

Read the source of the GDS

<a id='e0bc4173-1b47-4357-a663-6c8b21ada248'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='4c5545b0-f9f4-4261-abd0-20b9266865e5'></a>

6/15