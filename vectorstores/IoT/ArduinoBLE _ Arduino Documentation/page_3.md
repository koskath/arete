<a id='d640c32f-de61-4eb8-a142-56eee0aaa915'></a>

12/4/25, 2:49 PM

<a id='2fb1b9b3-911e-4134-82d1-5ddb856c6a44'></a>

ArduinoBLE | Arduino Documentation

<a id='ac4f5d41-3c54-441e-b42d-82ed1e8af3e8'></a>

ARDUINODOCS

<a id='7c724c10-00dc-4c54-ba29-159a2484e7b6'></a>

## Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='a87588cd-0eff-4d5a-98bb-3b9e368ad247'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='4a5d6907-be56-46ae-85a8-e682da2be71e'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='2e3a94cb-7b36-4fee-bf84-9eee4cfee2ec'></a>

# Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint in designing services. Given this limit, you should consider how best to store data about your sensors and actuators most effectively for your application. The simplest design pattern is to store one sensor or actuator value per characteristic, in ASCII encoded values.

<a id='3adb809d-169f-4608-8ca1-4b6a82ef3b76'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='4b4b27bd-aa7b-4630-85ec-976239505e26'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='9c01df57-d39c-40eb-89b6-a85f75439534'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='f6e51645-a833-47de-9807-70bb6f994e45'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='47d6d850-893c-4b7a-a39d-b9b7e52a7da3'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='b8b884b2-0c97-4984-b1a9-7bfa163deba0'></a>

Read/write/notify/indicate

<a id='f31a7c8c-449a-433e-9ba1-bfe6e2fb2db8'></a>

There are 4 things a central device can do with a characteristic:

<a id='da51b1bd-352d-47d6-951a-b98f585c8d87'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='0c74cd62-b5f1-4a03-9d8b-a7791e3b07ae'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='9f9e401f-df58-41e0-a5d8-6daa784f4ba9'></a>

3/26

<a id='f09eb424-3b80-460a-97d6-ccc67cb504b1'></a>