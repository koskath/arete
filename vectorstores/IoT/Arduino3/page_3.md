<a id='df681d2b-3fa7-4b90-aa14-d5f57edb68a2'></a>

12/4/25, 2:51 PM

<a id='1e522255-4b31-4b1e-8d84-c434002660d0'></a>

ArduinoBLE | Arduino Documentation

<a id='8e9ae789-76cb-4ee1-a4c0-764a736fad71'></a>

ARDUINODOCS

<a id='7d879763-bcf7-4793-8042-3bc1c08ad032'></a>

## Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='aae90367-9bb1-496b-b484-686cb60cd94d'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='bdf3abc1-79c8-4896-b363-423d1d47fa72'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='b9012e86-789c-4bf8-a406-c04cd3305013'></a>

Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint
in designing services. Given this limit, you should consider how best to
store data about your sensors and actuators most effectively for your
application. The simplest design pattern is to store one sensor or actuator
value per characteristic, in ASCII encoded values.

<a id='a1ac3e3f-a16d-4bcb-b24f-7d6bfb6f25e7'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='b8c2a5f9-6220-4cb9-80b6-f42c5b86cf93'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='573ea7fd-926e-4120-bba3-95fcfc57855e'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='6895c79b-5b93-484e-83c6-dc3b1929a037'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='ec7cb37b-d57b-4af7-b6bd-afcebce6d2ae'></a>

This is more efficient, but you need to be careful not to exceed the 512-byte limit. The accelerometer characteristic above, for example, takes 11 bytes as an ASCII-encoded string.

<a id='0c4112bb-c9d2-48ef-aaab-7ee075dfadb4'></a>

Read/write/notify/indicate

<a id='ae9bf990-4d21-4da4-9e15-c22b783be853'></a>

There are 4 things a central device can do with a characteristic:

<a id='4c19363c-1c42-4cf8-b267-a6fc610e2c43'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='3e8154ac-2114-404d-a959-090614f16b98'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='9ce1b406-6a93-476d-ba6f-ad67c390717c'></a>

3/9

<a id='85afacbc-3322-4d85-a4de-42ebbf35eb7a'></a>