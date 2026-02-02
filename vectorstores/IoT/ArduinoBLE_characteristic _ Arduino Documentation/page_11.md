<a id='5cf9b423-f9d6-4b48-a259-ad88c19b2f56'></a>

12/4/25, 2:50 PM

<a id='2e83c46b-f8cf-4694-809e-986d6244a4e1'></a>

ArduinoBLE | Arduino Documentation

<a id='b9542587-9903-47c4-a24d-e08dac61374d'></a>

ARDUINODOCS

<a id='4cb9f7ce-c5c8-4332-8b5d-cfa134504fa7'></a>

## Syntax

```
1 bleCharacteristic.setEventHandler(eventType, call
```

<a id='4f515a37-acc3-4b3d-a3f2-8eadd30e48ac'></a>

# Parameters

**eventType**: event type (BLESubscribed, BLEUnsubscribed,
BLERead, BLEWritten)
**callback**: function to call when the event occurs

<a id='19372c32-c3d8-4b4f-a126-1eebb3d90c4f'></a>

Returns

Nothing

<a id='15b9c77c-48d2-46cc-b32c-54ff6b643266'></a>

Example

```c
// create switch characteristic and allow remote
BLEByteCharacteristic switchCharacteristic("19B16");



// assign event handlers for characteristic
switchCharacteristic.setEventHandler(BLEWritter);



void switchCharacteristicWritten(BLEDevice central) {
  // central wrote new value to characteristic, it
  Serial.print("Characteristic event, written: ");

  if (switchCharacteristic.value()) {
    Serial.println("LED on");
    digitalWrite(ledPin, HIGH);
  } else {
    Serial.println("LED off");
    digitalWrite(ledPin, LOW);
  }
}
```

<a id='a146d44e-7f12-4d83-aead-39d51c331919'></a>

- bleCharacteristic.broadcast()
  > Broadcast the characteristics value as service data when advertising.

<a id='a870b002-3a93-48fb-b2b4-5eedd0108464'></a>

# Syntax
---
1. h1>Characteristic broadcast()

<a id='b134fd17-ccb0-4962-a4b0-5945b94a759b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='45fc5ba8-bb34-4ddc-adcd-6cd6e73d99de'></a>

11/22