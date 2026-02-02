<a id='983590ef-52d5-45d0-97b8-274cebe1a2d3'></a>

ArduinoPortentaH7.ino
arduino_secrets.h

<a id='2bcc025d-c337-4477-8e73-13d15168d3ce'></a>

```cpp
#define THINGER_SERIAL_DEBUG

#include <ThingerMbed.h>
#include "arduino_secrets.h"

ThingerMbed thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // configure LED_BUILTIN for output
  pinMode(LED_BUILTIN, OUTPUT);

  // open serial for debugging
  Serial.begin(115200);

  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);

  // pin control example (i.e. turning on/off a light, a
  // relay, etc)
  thing["led"] << digitalPin(LED_BUILTIN);

  // resource output example (i.e. reading a sensor value, a
  // variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}
```

<a id='99be46d8-a5b4-41f9-93c0-2d0ae069cb1a'></a>

In case of problems when connecting over secure TLS connections, try updating the WiFi firmware by flashing the WiFiFirmwareUpdater example sketch.

<a id='b204aa02-bab0-4a3e-b181-c4d844c67b48'></a>

<::Menu displaying a list of options. The first column shows main categories, and selecting one (indicated by '>') reveals a sub-menu in the second column. The "STM32H747_System" option is highlighted, and its sub-menu is visible.

Left Menu:
- STM32H747_System >
- TFT >
- ThreadDebug >
- USB Mass Storage >
- USBHID >
- USBHOST >

Right Sub-Menu (for STM32H747_System):
- QSPIFormat
- QSPIFReadPartitions
- STM32H747_getBootloaderinfo
- STM32H747_getResetReason
- STM32H747_manageBootloader
- WiFiFirmwareUpdater (highlighted)
: menu::>

<a id='eafddcaa-c9b4-46d5-971c-7cc203a7305e'></a>

21