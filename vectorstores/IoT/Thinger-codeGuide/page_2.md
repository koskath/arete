<a id='114b8dde-7bdc-4d8e-8884-b89241b69dac'></a>

// add required headers according to the device
#include <ThingerESP32.h>

// initialize Thinger instance (type can change depending on the
device)
ThingerESP32 thing("username", "deviceId", "deviceCredential");

void setup() {
  // initialize sensors and pins

  // initialize wifi (see examples for the device)

  // add resources here, like sensors, lights, etc.
}

void loop() {
  // call always the thing handled in the loop and avoid any delay
  // here
  thing.handle();
  // here it is possible to call endpoints
  // and also it is possible to stream resources
}

<a id='56359d11-30a4-40e7-bc6f-5b2141c9fee0'></a>

# Setting Credentials

All devices connected to the platform require authentication against the server. When a device is created in the `console`, a new device identifier is generated and device credentials are set. Therefore, these credentials must also be configured in the Arduino code to allow the device to be recognized and associated with the account. This is typically done during the initialization of the Thinger instance in the code, specifically when the `thing` instance is defined. The `username`, `deviceId`, and `deviceCredential` should be replaced with the values registered in the cloud. It is worth noting that credentials used to be defined inside `arduino_secrets.h`.

<a id='151f8a9f-de20-46d9-a4a0-5ac404cbb6fe'></a>

ThingerESP32 thing("username", "deviceId", "deviceCredential");

<a id='e74597dd-ff7a-4755-af10-7a6777c868c0'></a>

Adding Resources

<a id='d28ca4bd-2eb2-4019-bef2-e7b406edc9a1'></a>

2