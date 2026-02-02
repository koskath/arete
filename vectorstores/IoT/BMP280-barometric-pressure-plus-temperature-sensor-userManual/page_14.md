<a id='30e0b3a0-fbfe-40de-be7b-ef7596f3e402'></a>

29.72 inches-Hg.

<a id='8a3a1aaa-025e-4107-82db-2bf7d26e2562'></a>

You can also calculate Altitude. However, you can only really do a good accurate job of calculating altitude if you know the hPa pressure at sea level for your location and day! The sensor is quite precise but if you do not have the data updated for the current day then it can be difficult to get more accurate than 10 meters.

<a id='7cbdf584-6217-424e-8f40-9f3281436d7f'></a>

# Library Reference
You can start out by creating a BMP280 object with either software SPI (where all four pins can be any I/O) using

<a id='eab208a6-7ab4-492f-a134-fe98a1a7fe3a'></a>

Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO, BMP_SCK);

<a id='f931c0a1-abef-468a-8ec7-e8d6fb818ccf'></a>

Or you can use hardware SPI. With hardware SPI you must use the hardware SPI pins for your Arduino - and each arduino type has different pins! Check the [SPI reference to see what pins to use.](https://adafru.it/d5h)
In this case, you can use any CS pin, but the other three pins are fixed

```
Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
```

<a id='37eadafd-7f67-4029-b7d1-9da9e0eb6064'></a>

or I2C using the default I2C bus, no pins are assigned

```
Adafruit_BMP280 bmp; // I2C
```

<a id='9fd8f84b-d90f-4142-8ebe-3138c703eb8a'></a>

Once started, you can initialize the sensor with

```
if (!bmp.begin()) {
Serial.println("Could not find a valid BMP280 sensor, check wiring!");
while (1);
}
```

<a id='aff2f052-32b8-4311-bddc-926d99973f47'></a>

begin() will return True if the sensor was found, and False if not. If you get a False value back, check your wiring!

<a id='d52f1f27-12c1-4dd8-9ff0-4b9fcd137d8b'></a>

Reading temperature and pressure is easy, just call:

```
bmp.readTemperature()
bmp.readPressure()
```

<a id='0bcf86af-905f-4801-8cd6-d523ec505fe9'></a>

© Adafruit Industries

<a id='7d944b79-f040-4a08-9b44-8dbbfa881271'></a>

Page 15 of 34