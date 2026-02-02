<a id='b9fdafeb-1071-47bf-899d-145ef32281c0'></a>

The Arduino Yùn is a microcontroller board based on the ATmega32u4 and the Atheros AR9331. The Atheros processor supports a Linux distribution based on OpenWrt named OpenWrt-Yun. The board has built-in Ethernet and WiFi support, a USB-A port, micro-SD card slot, 20 digital input/output pins (of which 7 can be used as PWM outputs and 12 as analog inputs), a 16 MHz crystal oscillator, a micro USB connection, an ICSP header, and 3 reset buttons. This board lets the programmable ATmega32u4 communicate with the Internet by using the Bridge Library that exposes some functions running in the Linux distribution.

<a id='8fc05de7-e460-4296-9027-53bb8ad44907'></a>

<::image: An overhead view of an Arduino Yun development board. The board is dark grey/brown with various electronic components, connectors, and labels. At the top left, there's an Ethernet port block and a button labeled "RST" next to "3204". Along the top edge, there are pin headers labeled "AREF", "GND", and digital pins from "13" down to "1/TX 0/RX". In the center, there's a prominent white Arduino logo with an infinity symbol and a plus sign, above the text "Arduino™ YUN". To the left, the text "ARDUINO.CC" is visible, along with a USB host port and a button labeled "WAN-RST". On the right side, there's an "ICSP" header (a 2x3 pin array) and a column of LEDs labeled "RX", "TX", "LIN", "WAN", "ON", "WLAN", "USB", and a button labeled "YUN-RST". At the bottom edge, there are more pin headers labeled "IOREF", "RST", "3.3V", "5V", "GND", "GND", "VIN", and analog input pins "A0" through "A5". A large square integrated circuit is visible in the lower-middle section of the board.  
Arduino Yun Board::>

<a id='81baee87-961a-44a0-a64f-5ea520e100a5'></a>

This example will allow connecting an Arduino Yun to the cloud platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just needs to be modified with the relevant information. Notice that it is not required to configure any network parameters in the code, as this is managed by the running Linux distribution. However, it may be necessary to connect with the Arduino Yun via WiFi to connect it to a local network.

<a id='f81080b1-1c8e-4fd6-b50e-3331c4746443'></a>

7