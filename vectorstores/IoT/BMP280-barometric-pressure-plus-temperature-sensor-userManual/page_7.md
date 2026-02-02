<a id='69a1e2ed-e376-47ec-9a06-10e7cfe01a06'></a>

GND - common ground for power and logic

<a id='04634302-f960-4f10-860d-93ab047950df'></a>

# SPI Logic pins:

All pins going into the breakout have level shifting circuitry to make them 3-5V logic level safe. Use whatever logic level is on **Vin**!

* **SCK** - This is the **SPI Clock** pin, its an input to the chip
* **SDO** - this is the **Serial Data Out** / **Microcontroller In Sensor Out** pin, for data sent from the BMP280 to your processor
* **SDI** - this is the **Serial Data In** / **Microcontroller Out Sensor In** pin, for data sent from your processor to the BMP280
* **CS** - this is the **Chip Select** pin, drop it low to start an SPI transaction. Its an input to the chip

<a id='2cb36188-7dc1-428b-b7b5-11d275463f6a'></a>

If you want to connect multiple BMP280's to one microcontroller, have them share the SDI, SDO and SCK pins. Then assign each one a unique CS pin.

<a id='895cc4b5-4093-4378-a438-abcc7cd2a530'></a>

I2C Logic pins:

*   **SCK** - this is also the I2C clock pin (**SCL**), connect to your microcontroller's I2C clock line.
*   **SDI** - this is also the I2C data pin (**SDA**), connect to your microcontroller's I2C data line.

<a id='2990b196-84b2-40c2-bb23-6a983929d281'></a>

Leave the other pins disconnected

<a id='7045534b-0c88-4ac9-af82-c001fb1b796f'></a>

©Adafruit Industries

<a id='b208eb36-3183-4ce8-8aa8-831633a94d72'></a>

Page 7 of 34