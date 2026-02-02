<a id='0bf07a9d-abfe-44ce-aecc-8c058fba5bc5'></a>

12/4/25, 2:51 PM

<a id='e0412349-5820-436c-a6f1-123229b7787d'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='9c6ccbf1-b4d8-4232-9113-a3cc8920fbab'></a>

ARDUINODOCS

<a id='8f3aa3ad-0baf-41fa-87cd-a2839e8307ed'></a>



<a id='db1b8c45-d4fc-4c26-b146-ea34dc309101'></a>

wakeup()
Wake up the GPS from standby mode.

## Syntax

```
1 GPS.wakeup()
```

<a id='1712363e-f895-4546-8cb1-da4e8714d787'></a>

**Parameters**

None.

<a id='b0772166-f813-4afe-a3de-41259c110e97'></a>

Returns

<a id='5e9f3245-ee91-451b-8b03-ffbecbf3de18'></a>

None.

<a id='3cfdb655-ff69-459d-beaf-900434c3a026'></a>

Example

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

<a id='e823729a-80d9-40f5-b67f-38b508a639ea'></a>

## See also
* begin()
* end()
* available()
* latitude()
* longitude()
* speed()
* course()
* variation()
* altitude()
* satellites()
* getTime()
* standby()

<a id='e57eabb0-6938-4777-bbb3-ad66eb3f8a10'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='53a59063-d2a5-48fc-a47d-df763e00c0d5'></a>

14/15