<a id='836a95bd-baae-45a2-ae93-69109d443497'></a>

12/4/25, 2:51 PM

<a id='794744d9-05a8-40e9-94d9-555d35b2be9e'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='e9083aa1-ff3c-4512-8c69-c205f8bf1da9'></a>

ARDUINODOCS

<a id='27f77521-6e2d-4142-aa32-c81bf4b77a83'></a>

```cpp
1 #include <Arduino_MKRENV.h>
2 
3 void setup() {
4   Serial.begin(9600);
5   while (!Serial);
6 
7   if (!ENV.begin()) {
8     Serial.println("Failed to initialize ENV sensor!");
9     while (1);
10   }
11 }
12 
13 void loop() {
14   // read all the sensor value
15   float temperature = ENV.readTemperature();
16   float humidity    = ENV.readHumidity();
17   float pressure    = ENV.readPressure();
18   float illuminance = ENV.readIlluminance();
19   float uva         = ENV.readUVA();
20   float uvb         = ENV.readUVB();
21   float uvIndex     = ENV.readUVIndex();
22 
23   // print each of the sensor
24   Serial.print("Temperature = ");
25   Serial.print(temperature);
26   Serial.println(" °C");
27 
28   Serial.print("Humidity    = ");
29   Serial.print(humidity);
```

<a id='419760e7-0063-456c-a68f-1282daa147d5'></a>

> Note: If you are using a newer version of
> the MKR ENV shield, you will not be able to
> use the
> `readUVA()`, `readUVB()` and
> `readUVindex()` commands.

<a id='46e43495-55d6-4c14-a879-a6898ede03e1'></a>

# Testing It Out

The code that we have now uploaded is very simple. First, we do a reading of all the sensors, then we simply print them in the Serial Monitor, with an interval of one second.

<a id='1eeb1e05-6db4-4dd0-95e5-9ed8f709ab49'></a>

We can test that it is working, by opening the
Serial Monitor. If everything is working
properly, we should now see the values
being printed in the Serial Monitor.

<a id='cfb5e9c5-b6a6-4343-a244-6fb172361284'></a>

<::Arduino IDE window and Serial Monitor window: figure::>
<::Arduino IDE window titled "Arduino.ino - Arduino 1.8.19">
Menu: File, Edit, Sketch, Tools, Help
Toolbar icons: Verify, Upload, New, Open, Save, Serial Monitor
Code editor content:
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  float hif = dht.computeHeatIndex(f, h);
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(f);
  Serial.print(" *F\t");
  Serial.print("Heat index: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F");
  delay(2000);
}
```
<::Serial Monitor window titled "Serial Monitor">
Output content:
```
Temperature = 25.17 %
Humidity = 75.99 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24

Temperature = 25.43 %
Humidity = 76.24 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24

Temperature = 25.64 %
Humidity = 76.45 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24

Temperature = 25.93 %
Humidity = 76.71 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24
```

<a id='a32b2671-8155-4bc0-a845-9acdaea1ba83'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='18f40449-da01-46f5-bb94-aead746248ef'></a>

7/8