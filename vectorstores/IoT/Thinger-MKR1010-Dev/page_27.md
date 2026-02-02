<a id='c2844b47-4b61-4267-bb13-913915be508d'></a>

```
in = (bool) digitalRead (D2);
}else{
    digitalWrite(D2, in? HIGH: LOW);
    digitalWrite(LED_D2, in ? HIGH : LOW);
}
```

<a id='51540ba3-60a9-4833-99fb-09b18c2679d5'></a>

```
};
thing["relay_d3"] << [](pson& in){
  if(in.is_empty()){
    in = (bool) digitalRead(D3);
  }else{
    digitalWrite(D3, in ? HIGH : LOW);
    digitalWrite(LED_D3, in ? HIGH : LOW);
  }
};
```

<a id='1515a5a9-214b-41f3-b79c-8227f177dee6'></a>

// example for controlling the LED
thing["led"] << digitalPin(LED_BUILTIN);
thing["led_r"] << digitalPin(LEDR);

<a id='c8739503-ee81-46ac-bb3e-e73579e0175f'></a>

// resource output example (i.e. reading a sensor value, a
variable, etc)
thing["millis"] >> outputValue(millis());

<a id='bcde49ab-2b09-4097-8e0f-b4f9f7b41a95'></a>

// start thinger on its own task
thing.start();

// more details at http://docs.thinger.io/arduino/

<a id='dce055df-9fd0-48a3-a2e8-1c0c2c6ea27c'></a>

}
void loop() {
// use loop as in normal Arduino Sketch
// use thing.lock() thing.unlock() when using/modifying
variables exposed on thinger resources
delay(1000);


<a id='ae1f365f-1754-4f0c-9ac2-b787d5161110'></a>

option : [x] In case of problems when connecting over secure TLS connections, try updating the WiFi firmware by flashing the WiFiFirmwareUpdater example sketch.

<a id='109aaced-6641-40f2-8134-79017aa0aa46'></a>

<::A menu interface is displayed. The menu has two columns. The left column lists main options, and the right column shows sub-options or actions associated with the selected main option. The 'USBHOST' option in the left column is selected, and its corresponding action 'WiFiFirmwareUpdater' in the right column is highlighted, indicating it is the active selection. The full list of options and their associated actions are:
- STM32H747_System > QSPIFormat
- TFT > QSPIFReadPartitions
- ThreadDebug > STM32H747_getBootloaderinfo
- USB Mass Storage > STM32H747_getResetReason
- USBHID > STM32H747_manageBootloader
- USBHOST > WiFiFirmwareUpdater
- USBLIB
: menu::>

<a id='a55af4f0-264f-46bd-856f-87d3ce129bf5'></a>

27