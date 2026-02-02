<a id='7276bd2a-062f-4c37-b31a-16cf44dbac62'></a>

12/4/25, 2:51 PM

<a id='ae742f09-b1eb-4b52-89cc-31e3cf6cb71a'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='799a61d5-318c-421e-a376-0242e2653f5c'></a>

ARDUINODOCS

<a id='60ca78d5-0cd2-422c-8654-2eaa30aa9875'></a>



<a id='57b7f184-ffd4-4140-89d8-9a42da6c234b'></a>

1 GPS.altitude()

<a id='a8d0089c-b7e6-489c-aee0-78bcb4275138'></a>

**Parameters**

None.

<a id='3af7b3af-f60e-4a4a-9cc9-41400af86ea3'></a>

## Returns
GPS altitude in meters.

<a id='dd96a02f-7662-45d7-ba08-c469551a1424'></a>

Example

```
1 // Check if there is new GPS data
2 if (GPS.available()) {
3   // Read GPS data
4   float altitude = GPS.altitude();
5 
6   // ...
7 
8   // Print GPS data
9   Serial.print("Altitude: ");
10  Serial.print(altitude);
11  Serial.println("m");
12 }
```

<a id='ba15ea25-3e20-4ca0-8fcb-62aad44a026e'></a>

See also

begin()
end()
available()
latitude()
longitude()
speed()
course()
variation()
satellites()
getTime()
standby()
wakeup()

<a id='075b0eea-dee8-4e87-8290-82168420ac93'></a>

satellites()
Read the number of satellites being tracked
by the GPS.

## Syntax



<a id='1eedd7ea-76ec-44d8-975e-06f482b7a611'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='d1c7dc84-e385-407e-bb55-d0cf72ca4085'></a>

9/15