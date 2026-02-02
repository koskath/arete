<a id='b3dd1a07-d130-4699-a730-94c67dfd4574'></a>

12/4/25, 2:51 PM

<a id='ba010a78-f713-41c5-bbb8-7400137b975b'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='6bddbc51-be0d-4861-a36e-3a7bb7941906'></a>

ARDUINODOCS

<a id='1f72ab7f-22f6-4bc2-8409-f85a7f7bf3a9'></a>



<a id='01aec831-06ad-45b2-9ce1-4e4d23d0d4b8'></a>

1 GPS.satellites()

<a id='6d37f06d-ae4b-4195-be54-9a649e699097'></a>

Parameters

None.

<a id='375dc2f7-25ad-439d-a2f8-16dc311f2db4'></a>

# Returns

The number of satellites being tracked by
the GPS.

<a id='f2dbefc8-2a86-415b-9abb-82410ac5d97e'></a>

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

<a id='c93e5259-ca8f-4fc3-8e1a-048a17069e0b'></a>

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
* getTime()
* standby()
* wakeup()

<a id='f2b44760-bcd1-44ab-9e80-7ae987e07eb4'></a>

### satellites()

Read the number of satellites being tracked by the GPS.

### Syntax

<a id='93b0d42f-d412-4470-bd95-0f66cd0097be'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='58a69ba0-7509-4936-b13d-d47ba4308f44'></a>

10/15