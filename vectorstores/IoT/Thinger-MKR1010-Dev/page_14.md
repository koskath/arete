<a id='44849048-87db-4999-9c7a-55688a6cb075'></a>

ArduinoMKR1010.ino arduino_secrets.h

<a id='9af2c55c-1453-4896-81a6-ea333163bae6'></a>

#define THINGER_SERIAL_DEBUG
#include <ThingerWiFiNINA.h>
#include "arduino_secrets.h"

// cannot connect? Update WiFiNINA and add iot.thinger.io SSL
// Certificate
// https://support.arduino.cc/hc/en-us/articles/360016119219

ThingerWiFiNINA thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

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

<a id='f2f74bc2-8f9c-44d8-98cd-6c27df2d512b'></a>

For using MKR1010 over the default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='b86f6f47-e966-4d92-bba3-f756d00f2fd4'></a>

14