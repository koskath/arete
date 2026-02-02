<a id='e8ea5755-bd6b-441c-8e44-358091ebc84c'></a>

12/4/25, 2:50 PM

<a id='d1575c57-8c99-4c71-9d06-1667e92267a7'></a>

ArduinoBLE | Arduino Documentation

<a id='d253b197-2b57-49d5-80b8-13dc495e6b6e'></a>

ARDUINODOCS

<a id='3c96cf49-861c-46a6-91dd-384ef151392c'></a>

# Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='36017858-2115-45fc-991a-636174f8bb5f'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='f76086cc-fef9-4a19-91dc-a3ffe14a4794'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='035f55ab-0769-4f88-af52-f466ee6ca2c0'></a>

# Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint in designing services. Given this limit, you should consider how best to store data about your sensors and actuators most effectively for your application. The simplest design pattern is to store one sensor or actuator value per characteristic, in ASCII encoded values.

<a id='5101fdd9-259e-4394-b0a4-085492713595'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='13033691-549a-4395-8dae-aec0f33c6fb6'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='452a3d02-079c-438a-a985-23cd3e4b3a82'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='3d40da86-a611-421f-9a1d-a7ecf55e4993'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='c48b963d-ec17-407f-bf0a-d6f7e051f41f'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='a7032c21-aeef-4924-9072-bac5f46e67af'></a>

Read/write/notify/indicate

<a id='04385798-713e-4658-8561-8311dcb539f6'></a>

There are 4 things a central device can do with a characteristic:

<a id='86d6fc23-317b-4be3-be60-9c2688641f63'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='236ae1f2-3560-48d3-a061-387a5a40c033'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='904b5ef9-ab26-4f61-a0d9-6c3ee730f2c4'></a>

3/10

<a id='4b8da8e2-df9e-4b55-b0a8-c50b7bb1abbc'></a>