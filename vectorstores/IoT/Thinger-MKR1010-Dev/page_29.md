<a id='35163c68-d6e2-48e6-bb6e-9b76eef5387d'></a>

ArduinoUnoWiFiRev2.ino arduino_secrets.h

<a id='95e70972-9135-49b2-b70e-4308288c7889'></a>

#define THINGER_SERIAL_DEBUG

#include <ThingerWiFiNINA.h>
#include "arduino_secrets.h"

// cannot connect? Update WiFiNiNA and add iot.thinger.io SSL
Certificate
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
  relay, etc)
  thing["led"] << digitalPin(LED_BUILTIN);

  // resource output example (i.e. reading a sensor value, a
  variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}

<a id='0a024af8-06ed-4276-9116-b9ab9831dd16'></a>

For using this board with he default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='1f49e096-af0c-4041-8786-ea5b65038437'></a>

29