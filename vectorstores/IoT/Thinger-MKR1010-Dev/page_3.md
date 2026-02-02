<a id='0b4305cd-6cf9-42ac-9830-a7602ff253ab'></a>

ArduinoWiFi.ino arduino_secrets.h

<a id='c0df6105-8caf-4e4d-ae5c-e1f146478971'></a>

```cpp
#define THINGER_SERIAL_DEBUG
#define THINGER_USE_STATIC_MEMORY
#define THINGER_STATIC_MEMORY_SIZE 512

#include <WiFi.h>
#include <ThingerWifi.h>
#include "arduino_secrets.h"

ThingerWifi thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // open serial for debugging
  Serial.begin(115200);

  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);

  pinMode(2, OUTPUT);

  // pin control example (i.e. turning on/off a light, a
  // relay, etc)
  thing["led"] << digitalPin(2);

  // resource output example (i.e. reading a sensor value, a
  // variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}
```

<a id='1fe5ad55-a77a-4f0d-9607-012bbe6c5922'></a>

Arduino with CC3000

<a id='8031627b-78ab-4b6c-878a-4f794f2ed231'></a>

3