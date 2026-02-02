<a id='0d0e6d4a-ac61-4628-bc30-f4270122bc43'></a>

12/4/25, 2:51 PM

<a id='738fa74e-853c-4440-beea-825aee1c8f30'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='189f1872-85c6-4067-8ba6-57374dc3abc4'></a>

ARDUINODOCS

<a id='f006778d-5dc7-4559-87d9-bdd6420d0a1c'></a>



<a id='6ce32e72-0d51-422b-bc67-5b292686a833'></a>

Read the latitude of the GPS.

## Syntax

```
1 GPS.latitude()
```

<a id='6144331c-5ea4-4c1f-9db4-f524c1f7858b'></a>

**Parameters**

None.

<a id='9a1049d8-8dd7-4cc8-a4e3-77bd464a8e90'></a>

Returns

GPS longitude in degrees.

<a id='c5eabcf9-4a86-4626-a48b-c322109b5d88'></a>

# Example

```
1 // Check if there is new GPS data
2 if (GPS.available()) {
3   // Read GPS data
4   float latitude = GPS.latitude;
5   float longitude = GPS.longitude;
6
7   // ...
8
9   // Print GPS data
10  Serial.print("Location: ");
11  Serial.print(latitude, 7);
12  Serial.print(", ");
13  Serial.println(longitude, 7);
14}
```

<a id='4a2c9274-17d9-4255-b7cb-2339d7005e84'></a>

## See also

* begin()
* end()
* available()
* latitude()
* speed()
* course()
* variation()
* altitude()
* satellites()
* getTime()
* standby()
* wakeup()

<a id='270e9302-4263-44e3-be11-9c96a555b04f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='d5aabf28-531c-4f24-a652-45c9e02b96cf'></a>

5/15