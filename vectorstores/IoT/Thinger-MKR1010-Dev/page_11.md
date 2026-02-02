<a id='2cd07a6f-e79e-452f-978f-50d3c5b18ce8'></a>

C++ arduino_secrets.h

<a id='4b704de2-444c-4aac-a30f-24ba9f26f701'></a>

#define THINGER_SERIAL_DEBUG
#include <ThingerWifi101.h>
#include "arduino_secrets.h"

// cannot connect? Update WiFi101 firmware and add
iot.thinger.io SSL Certificate
// https://support.arduino.cc/hc/en-us/articles/360016119219

ThingerWifi101 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
// open serial for debugging
Serial.begin(115200);

// configure wifi network
thing.add_wifi(SSID, SSID_PASSWORD);

pinMode(LED_BUILTIN, OUTPUT);

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

<a id='556d6d93-7b3a-46f2-a7db-0d944da1546f'></a>

ⅰ For using MKR1000 over the default TLS/SSL connection, it is required to install the Thinger.io server certificate on the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='d9387c9a-dc6a-4bb9-9c3b-1f3fee248d18'></a>

11