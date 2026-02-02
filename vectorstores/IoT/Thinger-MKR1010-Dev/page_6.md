<a id='f11e690e-c39a-448c-9ffd-90df572a155f'></a>

ArduinoCC3000.ino arduino_secrets.h

<a id='dfd80ba6-731d-404a-bcb2-9ed20a6f4425'></a>

```c
#define THINGER_SERIAL_DEBUG

#include <ThingerCC3000.h>
#include "arduino_secrets.h"

ThingerCC3000 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

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

<a id='63537f1b-2e3b-4139-91f0-cad98b8dc8a5'></a>

Arduino Yun

<a id='42a79acf-9cee-412e-a133-0e59f755f881'></a>

6