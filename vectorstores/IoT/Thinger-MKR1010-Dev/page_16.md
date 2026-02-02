<a id='a1972462-c177-4f23-87d5-631203c569be'></a>

<::A close-up photograph of a small, black circuit board, likely a microcontroller board, with various electronic components. The board features a row of through-hole pins along its top and bottom edges. On the left side, there is a silver micro-USB connector. Above the USB connector, the word "ON" is visible. Towards the center-left, there is a small, round reset button labeled "RST". Along the top edge, the text "ARDUINO.CC" is printed. The central component is a large, square integrated circuit chip labeled "Atmel ATSAMD21 G18A-U 1838". To the right of the Atmel chip, there is a rectangular module with a white label. This module has a QR code and text that reads "ublox" at the bottom, and vertically oriented text "008-0019/10 MODEL:NINA-W102" along its right side. Other smaller surface-mount components, such as resistors, capacitors, and smaller integrated circuits, are scattered across the board.: figure::>

<a id='dea14bc0-b2e1-4f7c-bdfe-e8d8f8f0d6b7'></a>

! The integration with Thinger.io requires downloading an additional library called "Arduino WIFININA" that allows communicating with the U-BLOX WiFi module.

<a id='2d028935-e5aa-4f3a-af8d-9627bcfde256'></a>

This example will allow connecting the Arduino Nano 33 IoT device to the cloud
platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just
needs to be modified with the relevant information.

<a id='fa6a669b-2d8c-484d-8201-19fc8731db06'></a>

ArduinoNano33IoT.ino arduino_secrets.h
#define USERNAME "your_user_name"
#define DEVICE_ID "your_device_id"
#define DEVICE_CREDENTIAL "your_device_credential"

#define SSID "your_wifi_ssid"
#define SSID_PASSWORD "your_wifi_ssid_password"

<a id='ed7f9310-679e-4957-b998-9a26427fbf5a'></a>

i For using Arduino 33 IoT over the default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='6cc6eb71-ba32-452b-9afb-57869232c55f'></a>

16