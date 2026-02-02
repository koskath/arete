<a id='6414ec06-1f93-40f3-9f52-318884642d36'></a>

12/4/25, 2:51 PM

<a id='9192db90-7938-418b-b24e-b3f43327dc3a'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='f32c8a72-a57b-4d7e-914e-50c4c9aa1945'></a>

ARDUINODOCS

<a id='0d412e8d-c027-4c38-b193-4dd5a905026d'></a>



<a id='239bc35f-db95-461a-9346-89e1ba189517'></a>

None.

## Returns

GPS latitude in degrees.

<a id='f01c6e8a-8123-4426-a5ef-1b5bfa0cad4d'></a>

Example

```
1 // Check if there is new GPS data
2 if (GPS.available()) {
3   // Read GPS data
4   float latitude = GPS.latitude();
5   float longitude = GPS.longitude();
6
7   // ...
8
9   // Print GPS data
10  Serial.print("Location: ");
11  Serial.print(latitude, 7);
12  Serial.print(", ");
13  Serial.println(longitude, 7);
14 }
```

<a id='14d857a9-b06e-4e1b-b7de-61e38e400b5e'></a>

See also

begin()
end()
available()
longitude()
speed()
course()
variation()
altitude()
satellites()
getTime()
standby()
wakeup()

<a id='84919c6a-54ca-4549-8bbb-d6071a35458e'></a>

longitude()

<a id='ac147c88-564b-445b-8782-8b8da39d087a'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='ddf19f2b-b623-4605-891a-e4f3fcfd08fb'></a>

4/15