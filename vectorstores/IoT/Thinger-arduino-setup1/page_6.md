<a id='86dfad77-878e-47ed-aaeb-ebb7cc4a018d'></a>

ESP32.ino arduino_secrets.h

#define THINGER_SERIAL_DEBUG
#include <ThingerESP32.h>
#include "arduino_secrets.h"

ThingerESP32 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
// open serial for debugging
Serial.begin(115200);

pinMode(16, OUTPUT);

thing.add_wifi(SSID, SSID_PASSWORD);

// digital pin control example (i.e. turning on/off a light,
a relay, configuring a parameter, etc)
thing["GPIO_16"] << digitalPin(16);

// resource output example (i.e. reading a sensor value)
thing["millis"] >> outputValue(millis());

// more details at http://docs.thinger.io/arduino/
}

void loop() {
thing.handle();
}

<a id='a83e8c1d-5b6c-418f-9a79-c3bc2d1abc7c'></a>

Previous
SDK SETUP

Next
Visual Studio Code

<a id='19db7669-9015-4a4f-b71d-876d4ea6ad37'></a>

Last updated 5 months ago

Was this helpful?
option :) : [ ]
option :| : [ ]
option :( : [ ]

<a id='03f7c641-24d6-4b6a-be50-e4123a6a1a43'></a>

6