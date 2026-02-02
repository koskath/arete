<a id='9bf4ef27-6da3-4049-a6ed-41d11d04202a'></a>

12/4/25, 2:51 PM

<a id='07596732-8bce-4ba3-9390-1687f4e8759a'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='0a73ef79-4190-48ce-abcb-39a0cd1c655a'></a>

ARDUINODOCS

<a id='4907ef6c-d445-4169-92bb-655ccdaff30c'></a>



<a id='d4b9f9c9-845a-4119-bafe-de05c5f52362'></a>

## Syntax

```
1 GPS.course()
```

<a id='3b9da3fe-49b8-4eda-8f7a-8572aab05e4c'></a>

**Parameters**

None.

<a id='dc755fa4-930a-4011-a0fa-59836e4d32c5'></a>

**Returns**

GPS course in degrees.

<a id='b5055f7c-a054-4499-b122-5af04c961091'></a>

Example

```
1 // Check if there is new GPS d
2 if (GPS.available()) {
3   // Read GPS data
4   float course = GPS.course(
5 
6   // ...
7 
8   // Print GPS data
9   Serial.print("Course: ");
10  Serial.print(course);
11  Serial.println(" degrees")
12 }
```

<a id='f0c718a1-5535-44ff-ac4d-b11ff6dd960a'></a>

## See also

begin()
end()
available()
latitude()
longitude()
speed()
variation()
altitude()
satellites()
getTime()
standby()
wakeup()

<a id='370b4ef7-f96b-498f-abec-7fbd50086da9'></a>

v variation()
Read the magnetic variation of the GPS.

<a id='0ddc5090-6f9c-4ed2-8eee-ab758ca77034'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='df288b93-a812-4eb3-ba00-7aa899df9550'></a>

7/15