<a id='920a7e29-e78a-4039-b1a8-ffaa4ae5379e'></a>

Wiring

<a id='e7f4ae3f-f848-4ed9-a48c-f4f7d5412a77'></a>

First, wire up a BMP280 to your board exactly as follows. Here is an example of the
BMP280 wired to an [Adafruit ESP32 Feather V2](http://adafru.it/5400) using I2C with
a [STEMMA QT cable (no soldering required)](http://adafru.it/4210)

<a id='acae752b-3b51-44fe-9eed-82bce3d7157f'></a>

<::logo: fritzing
fritzing
The logo is a stylized wordmark in a sans-serif font.::>

<a id='c1c47490-73a0-495e-b9c0-8bb59c303b84'></a>

<::A Fritzing diagram showing an electronic circuit on a breadboard. A purple Adafruit ESP32 Huzzah v2 microcontroller board is connected to the breadboard. A black BMP280 Pressure Sensor module is also connected to the breadboard. Jumper wires connect the ESP32 Huzzah v2 board to the breadboard, and the BMP280 sensor to both the breadboard and the ESP32 Huzzah v2 board. The text "fritzing" is at the bottom right of the image.
: circuit diagram::>
fritzing

<a id='515fed8b-52e8-487c-88a1-00b9ee10b97c'></a>

Board 3V to sensor VIN (red wire on
STEMMA QT)
Board GND to sensor GND (black wire on
STEMMA QT)
Board SCL to sensor SCK (yellow wire on
STEMMA QT)
Board SDA to sensor SDI (blue wire on
STEMMA QT)

<a id='7a48a725-1cb9-4bae-af23-f100449bea13'></a>

## Usage

Connect your board to Adafruit IO Wippersnapper and navigate to the [WipperSnapper board list](https://adafru.it/TAu).

<a id='d323e8f9-df5f-4c78-a292-d1ce38880a9e'></a>

On this page, **select the WipperSnapper board you're using** to be brought to the board's interface page.

<a id='b9192a7f-de1b-48b4-a167-0a1c4a05aefd'></a>

©Adafruit Industries

<a id='f4ecb328-9aaf-4583-9071-5d345982e447'></a>

Page 25 of 34