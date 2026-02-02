<a id='d12311f4-fcf7-464a-8854-5cff88bc711d'></a>

12/4/25, 2:49 PM

<a id='a8fae72f-1e1a-469b-9ec1-cc64752a02ac'></a>

ArduinoBLE | Arduino Documentation

<a id='0e45a1bb-ab89-4617-a33d-1a64eab7ef34'></a>

ARDUINODOCS

<a id='3ddaf491-e15f-4f13-aa8c-b5af53aac0f7'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='d22d5cb8-2d1f-4a86-8d23-5a17c7c543ef'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='ff34c634-d8c4-410c-a94f-e911329d7ecb'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='0915fdf2-6934-4dbb-a5c4-eb8f95764ca2'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='b8b8fbfa-f5c9-41bb-ac42-bc735405ecb5'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='69de824d-2c17-4cc0-938d-18ffd6783ed4'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='d5a6457d-4fd1-41b4-a7ea-bfbead67505c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='86c3df77-56e1-4e93-beba-2f68cae05e81'></a>

2/26