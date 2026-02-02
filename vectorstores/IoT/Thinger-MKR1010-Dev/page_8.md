<a id='89e241d5-6394-4f03-bd27-9e366999c902'></a>

ArduinoYun.ino arduino_secrets.h

<a id='4ba2ff29-2b2e-40a3-b905-0c2e46f52f0f'></a>

#include <ThingerYun.h>
#include "arduino_secrets.h"

<a id='21245a51-0d3a-4c08-b3c5-e83819977da8'></a>

thinger.io

<a id='b7ddb650-4ca7-49b5-9a33-b042cb6fcc4b'></a>

<::A magnifying glass icon is centered within a rounded square with a subtle shadow.: icon::>

<a id='3ba1782c-b67f-4c21-bbc8-9946de9cce75'></a>

pinMode(LED_BUILTIN, OUTPUT);

// initialize bridge
Bridge.begin();

// pin control example (i.e. turning on/off a light, a
relay, etc)
thing["led"] << digitalPin(LED_BUILTIN);

// resource output example (i.e. reading a sensor value, a
variable, etc)

// more details at http://docs.thinger.io/arduino/
}

void loop() {
thing.handle();
}

<a id='3e736aa2-5e91-4926-8733-cde356d93dd0'></a>

i For using Arduino Yun, the device must be connected to a network with Internet, just via Ethernet or a Wifi connection. It can be configured in the Arduino Yun web configuration.

<a id='73a40e04-3f30-4f51-a611-6790145e4ac9'></a>

8