<a id='ecb9a44a-16d9-44f9-991b-cc0d8515241c'></a>

ARDUINODOCS

<a id='0c598019-e1b5-48c1-91c8-373d7e1da2cb'></a>

____________________________________________________________________________________________________

<a id='51eccad5-44b4-4414-ab4d-19d9f73a0f86'></a>

```c
1 #include <DHT.h>
2 #include <DHT_U.h>
3 #include <Wire.h>
4 #include <SeeedOLED.h>
5 
6 DHT dht(0, DHT22);
7 
8 void setup() {
9 
10   Wire.begin();
11 
12   SeeedOled.init();
13 
14   SeeedOled.clearDisp();
15 
16   SeeedOled.setNormal();
17 
18   SeeedOled.setPageMo();
19 }
20 
21 void loop() {
22 
23   float temp, hum;
24 
25   //Read temperature
26 
27   do {
28 
29     hum = dht.readHum();
30 
    temp = dht.readTemp();
   } while (isnan(hum) || isnan(temp));

   SeeedOled.clearDisplay();
   SeeedOled.setTextXY(0,0);
   SeeedOled.putString("Temp: ");
   SeeedOled.putFloat(temp);
   SeeedOled.putString(" C");

   SeeedOled.setTextXY(1,0);
   SeeedOled.putString("Hum: ");
   SeeedOled.putFloat(hum);
   SeeedOled.putString(" %");

   delay(2000);
}
```

<a id='be79899f-3d8f-4e2c-8483-297d554ff021'></a>

## Suggest changes
The content on [docs.arduino.cc](docs.arduino.cc) is facilitated through a public [GitHub repository](repository.). If you see anything wrong, you can edit this page [here](here.).

## Need support?
*   [Help Center](Help%20Center)
*   [Ask the Arduino Forum](Ask%20the%20Arduino%20Forum)
*   [Discover Arduino](Discover%20Arduino)
*   [Discord](Discord)

## License
The Arduino documentation is licensed under the [Creative Commons Attribution-Share Alike 4.0 license](Creative%20Commons%20Attribution-Share%20Alike%204.0%20license.).

<a id='1c2c542a-0694-4efb-93d3-f2ecbdc4e58c'></a>

Was this article helpful?