<a id='2c3e0620-176d-4d8b-8a96-696fc18376d5'></a>

#define THINGER_SERIAL_DEBUG

<a id='4c7e4eb2-21a2-4bd1-9707-33e36c6d7228'></a>

#include <ThingerMbed.h>
#include <ThingerPortentaOTA.h>
#include "arduino_secrets.h"

<a id='87748d35-1871-4bc4-a40b-3260cbd01378'></a>

ThingerMbed thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);
ThingerPortentaOTA ota(thing);

<a id='c49ecdfa-52ef-4a37-9f26-c9899d38de24'></a>

void setup() {
// open serial for debugging
Serial.begin(115200);
}

<a id='be852785-9411-462b-a854-1561abd3c25f'></a>

```
// configure leds for output
pinMode(LED_D0, OUTPUT);
pinMode(LED_D1, OUTPUT);
pinMode(LED_D2, OUTPUT);
pinMode(LED_D3, OUTPUT);
pinMode(LEDR, OUTPUT);
pinMode(LED_BUILTIN, OUTPUT);
```

<a id='3b5e6d49-ba36-47b6-b6f6-7fae4348581a'></a>

```
// configure relays for output
pinMode (D0, OUTPUT);
pinMode (D1, OUTPUT);
pinMode (D2, OUTPUT);
pinMode (D3, OUTPUT);
```

<a id='e8aa347a-2460-4796-bf03-c5aabdec8e17'></a>

// example for controlling relays and status LED
thing["relay_d0"] << [](pson& in) {
    if(in.is_empty()) {
        in = (bool) digitalRead(D0);
    }else{
        digitalWrite(D0, in? HIGH : LOW);
        digitalWrite(LED_D0, in? HIGH : LOW);
    }
};

<a id='6490ff27-af1f-4bd2-bf57-322f560b0136'></a>

```
thing["relay_d1"] << [] (pson& in){
  if(in.is_empty()){
    in = (bool) digitalRead(D1);
  }else{
    digitalWrite(D1, in ? HIGH : LOW);
    digitalWrite(LED_D1, in ? HIGH : LOW);
  }
};
```

<a id='bfe32285-01f5-4438-b0f2-236954401cd1'></a>

thing["relay_d2"] << [] (pson& in){
if(in.is_empty()){


<a id='2e522097-ae45-4479-8bda-c3fd10b9a2f2'></a>

26