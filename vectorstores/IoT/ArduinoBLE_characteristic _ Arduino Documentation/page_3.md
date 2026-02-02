<a id='661f5b9c-31b8-48b4-90c9-f3f08ed325b2'></a>

12/4/25, 2:50 PM

<a id='d8d5dc2a-931f-4bc3-83c0-9ff22dee4d01'></a>

ArduinoBLE | Arduino Documentation

<a id='da491785-9a5e-4906-9ae8-5a89ebd4ce0e'></a>

ARDUINODOCS

<a id='85550516-d5b2-4e51-aabc-112b0c98a384'></a>

## Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='b4a6473a-bbf5-461f-9c60-657cf9a1e625'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='10ca3b93-a8de-4c10-b907-04dae4ce0ca6'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='55d2c7a2-7b71-4d70-865f-87f4e1512bda'></a>

# Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint in designing services. Given this limit, you should consider how best to store data about your sensors and actuators most effectively for your application. The simplest design pattern is to store one sensor or actuator value per characteristic, in ASCII encoded values.

<a id='28fd47ca-15db-4e80-b364-efea37bf181a'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='c6c0e920-a6e8-4cb2-b24b-5cdf5c0537ae'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='37dc68e8-81f0-418d-af1a-9dee8696cefa'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='4114953c-775d-47ff-a1ad-21ba4e965513'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='6d714b9f-7007-4e31-81aa-0fb379a0ce44'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='d62da9ef-2149-4646-9c05-a8f68f332ab8'></a>

Read/write/notify/indicate

<a id='190cf473-2664-4dd2-aad1-0d767c576dd8'></a>

There are 4 things a central device can do with a characteristic:

<a id='9a806fea-68de-4941-90c9-76b440038d38'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='c328c40e-a673-47fe-86ff-f2e66464dd2a'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='6595c60e-780f-4fde-a85d-beeea28e2614'></a>

3/22

<a id='7dc01968-abd0-4704-a625-479c5c7ed72c'></a>