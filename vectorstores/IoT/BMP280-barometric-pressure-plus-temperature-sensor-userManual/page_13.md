<a id='af7d61c0-ebe9-4e59-aae3-dd2d468361fb'></a>

#define BMP_MOSI 11
#define BMP_CS 10
Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO, BMP_SCK);

<a id='28303d48-81be-4b45-93aa-e0ac8ff85580'></a>

Once uploaded to your Arduino, open up the serial console at 9600 baud speed to see data being printed out

<a id='5f0ee925-7d0c-44e3-b850-e77235c2ee50'></a>

COM55

[ ] Send

BMP280 test
Temperature = 25.53 *C
Pressure = 100935.02 Pa
Approx altitude = 32.52 m

Temperature = 25.54 *C
Pressure = 100937.41 Pa
Approx altitude = 32.32 m

Temperature = 25.54 *C
Pressure = 100935.35 Pa
Approx altitude = 32.49 m

Temperature = 25.65 *C
Pressure = 100939.53 Pa
Approx altitude = 32.14 m

Temperature = 26.91 *C
Pressure = 101698.37 Pa
Approx altitude = -31.04 m

Temperature = 26.73 *C
Pressure = 100944.21 Pa
Approx altitude = 31.75 m

option Autoscroll: [x]
Both NL & CR
9600 baud

<a id='872f08c8-1b60-438d-814d-b23fb887126c'></a>

**Temperature** is calculated in degrees C, you can convert this to F by using the classic
F = C * 9/5 + 32 equation.

<a id='b06b1551-dc93-41df-b5d4-3390009803f5'></a>

Pressure is returned in the SI units of **Pascals**. 100 Pascals = 1 hPa = 1 millibar. Often times barometric pressure is reported in millibar or inches-mercury. For future reference 1 pascal =0.000295333727 inches of mercury, or 1 inch Hg = 3386.39 Pascal. So if you take the pascal value of say 100734 and divide by 3389.39 you'll get

<a id='6f5f14c3-c036-40d9-ab74-11417ba7a4c8'></a>

Adafruit Industries

<a id='9e273871-6003-4aaa-98bf-22b21e15fe40'></a>

Page 14 of 34