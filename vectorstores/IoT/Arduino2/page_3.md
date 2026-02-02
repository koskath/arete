<a id='11df5073-c015-40b9-9955-8c005280b7a9'></a>

12/4/25, 2:51 PM

<a id='744a5ec0-d235-4600-ae25-0d7177fa93d7'></a>

ArduinoBLE | Arduino Documentation

<a id='aa513f75-acf7-4f1a-8aad-3fb302482048'></a>

ARDUINODOCS

<a id='0e1e7514-932e-4cef-860d-b498e66ba01b'></a>

# Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='1f0d3b02-d064-43b8-ad9a-c59cdf01814f'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='0c440740-84c5-4b5e-b0de-87166106efb3'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='75234a61-419b-4672-a40a-acb08153c0d7'></a>

Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint
in designing services. Given this limit, you should consider how best to
store data about your sensors and actuators most effectively for your
application. The simplest design pattern is to store one sensor or actuator
value per characteristic, in ASCII encoded values.

<a id='1e18f61c-55b3-425f-8aac-f0b3718d4f18'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='1b9f389d-8d1b-46ec-a105-17ca30396b3f'></a>

This is also the most expensive in memory terms, and would take the longest to read. But it's the simplest for development and debugging.

<a id='e06be320-f1a9-457d-ae05-60689cb2f109'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='edcd5b9e-3562-405f-8f14-189afaf0f25d'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='4ac1845d-3c50-44c1-9ced-6dda1aa951cb'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='b4f8640f-3ddb-4b14-a50a-e9ef678eec93'></a>

Read/write/notify/indicate

<a id='443c52ac-0ec0-4c58-adb0-47b8cc81fa15'></a>

There are 4 things a central device can do with a characteristic:

<a id='4003e3be-f46f-4dc4-98a5-513d2b8468d0'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='aa1e0b7a-9ea8-4cdb-9332-afd42fe3dc05'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='1ba53e8b-287e-4c33-bcb0-7fc35712a3c2'></a>

3/24

<a id='47cde113-fdc4-43b1-bfbc-53cb7ad0f4be'></a>