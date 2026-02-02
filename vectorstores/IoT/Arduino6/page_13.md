<a id='1aa25bc7-4ef9-4013-bdbb-59ec0e732f4c'></a>

12/4/25, 2:51 PM

<a id='916e149e-b2d6-4341-abea-fef27476755a'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='71bf7b73-5af5-44a9-8037-f2d808f4fd27'></a>

ARDUINODOCS

<a id='17fe145b-5b61-4b5a-8a52-61fdd1bc79a4'></a>



<a id='18d32ee4-2c7d-4b4e-a7ff-4d229faf5081'></a>

Put the GPS in standby mode.

## Syntax

```
1 GPS.standby()
```

<a id='481d8586-35bd-41ed-8ba3-b7fb46540783'></a>

Parameters

None.

<a id='ed2de2a1-0640-491f-90be-96e5f6023b54'></a>

Returns

<a id='403e6c40-4f8d-4719-b498-c41c733819df'></a>

None.

<a id='c5438a30-c740-42f9-b8c2-951f09f0fc52'></a>

# Example
```
1 // Put the GPS in standby mode
2 Serial.println("Standby mode")
3 GPS.standby();
4
5 // Wait for 10 seconds
6 delay(10000);
7
8 // Wake up the GPS
9 Serial.println("Wakeup");
10 GPS.wakeup();
11
12 // Wait for new GPS data to be
13 Serial.print("Waiting new loca
14 while (!GPS.available());
15
16 // ...
```

<a id='353bac2f-0200-47fd-95ea-d81a6e25762a'></a>

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
satellites()
getTime()
wakeup()

<a id='b4d42565-f65f-472e-95ef-226a4eacafaa'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='ee9677a9-b356-48b0-8c70-2c00a641ca42'></a>

13/15