<a id='9c5cdcc0-2de2-4357-8b44-55e3f88e6856'></a>

12/4/25, 2:50 PM

<a id='fae54cd6-5e0a-4293-a929-a7050a892b7c'></a>

ArduinoBLE | Arduino Documentation

<a id='16e8e289-57b5-47a8-b590-18217f3aa9ec'></a>

ARDUINODOCS

<a id='89d23e78-3700-4255-96f3-89e8c77bbaff'></a>



<a id='6cecd41d-b740-40de-aa7a-af15ceb1a9f8'></a>

bleCharacteristic.writeValue()

Write the value of the characteristic. If the characteristic is on a remote device, a write request or command will be sent.

## Syntax
```
bleCharacteristic.writeValue(buffer, length)
bleCharacteristic.writeValue(value)
```

## Parameters

buffer: byte array to write value with
length: number of bytes of the buffer argument to write
value: value to write

## Returns

1 on success,
0 on failure

## Example
```c
// read the button pin
int buttonState = digitalRead(buttonPin);

if (oldButtonState != buttonState) {
  // button changed
  oldButtonState = buttonState;

  if (buttonState) {
    Serial.println("button pressed");

    // button is pressed, write 0x01 to turn
    ledCharacteristic.writeValue((byte)0x01);
  } else {
    Serial.println("button released");

    // button is released, write 0x00 to turn
    ledCharacteristic.writeValue((byte)0x00);
  }
}
```

<a id='6d38fc2c-6059-45dd-a775-ac2fe31bbc51'></a>

bleCharacteristic.setEventHandler()
Set the event handler (callback) function that will be called when the specified event occurs.

<a id='c2de5d1b-8f52-4c58-91be-73de8f71cba6'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='5191d198-0300-419f-84d5-1a6896375c76'></a>

10/22