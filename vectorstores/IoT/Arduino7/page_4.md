<a id='fc58b8fc-c18d-48df-b654-5b8addacedd9'></a>

12/4/25, 2:52 PM

<a id='360af965-6e2a-46b1-917d-8a766b2d51f7'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='f43f2bab-62c8-4665-9080-dc398b7f5b33'></a>

ARDUINO DOCS

<a id='296a02d1-fd92-4347-9308-e556efbe8520'></a>

____________________________________________________________________________________________________

<a id='fcb86be0-9870-464a-a542-fe725fef459f'></a>

for Arduino_MKRGPS and install it.

3. Here are some of the core functions of this sketch:

`GPS.begin` - initializes the GPS library.

`GPS.available()` - checks for available GPS data from the module.

`GPS.latitude()` - records latitude.

`GPS.longitude()` - records longitude.

`GPS.altitude()` - records altitude.

`GPS.speed()` - records speed in km/h.

<a id='89539a78-e74c-43f8-9c02-ba0708ddda8a'></a>

The sketch can be found in the
snippet below. Upload the sketch
to the board.

<a id='d4fdad71-c86b-4ce4-8cb9-8a81e4b04b3b'></a>

```cpp
1 #include <Arduino_MKR
2 
3 void setup() {
4   // initialize seria
5   Serial.begin(9600);
6   while (!Serial) {
7     ; // wait for ser
8   }
9 
10   // If you are using
11   // the GPS_MODE_SHI
12   if (!GPS.begin()) {
13     Serial.println("F
14     while (1);
15   }
16 }
17 
18 void loop() {
19   // check if there i
20   if (GPS.available()
21   // read GPS value
22   float latitude
23   float longitude
24   float altitude
25   float speed
26   int satellites
27 
28   // print GPS valu
```

<a id='b74026de-de5d-4a83-97c6-a49634cb520e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='33d50d10-6738-484c-8a58-7a78e1b14cf3'></a>

4/7

<a id='0abb6ab0-0331-401e-bbf6-9105417905bf'></a>

Manage libraries.., and search