<a id='c5bf1791-d919-4173-b516-31e974bad5fe'></a>

12/4/25, 2:51 PM

<a id='cd43aad5-4e64-4111-b81d-473e2e9eb80f'></a>

ArduinoBLE | Arduino Documentation

<a id='daa4eea6-f75f-4804-b9be-2ae613aacbda'></a>

ARDUINODOCS

<a id='560fb671-5f6e-49b3-99cc-afdb32cf4316'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='bf33901d-9ad3-4bd4-b415-907691f9ea10'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='de4d6d7e-8293-4471-acc9-72af2649e19a'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='138714c0-273c-4014-8aff-57f87136086d'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='1c256e8f-5087-40b9-abc8-877810e60e00'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='5c968eaa-4a68-43a4-aa76-d6380b352f4c'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='4e62bece-10a4-427d-9a74-927e51f22654'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='25404521-5344-4e51-a727-c2fe3bd06e8e'></a>

2/9