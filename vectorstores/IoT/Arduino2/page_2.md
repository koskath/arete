<a id='5d1aa133-8c28-4682-b623-c533d4986676'></a>

12/4/25, 2:51 PM

<a id='15d07dc0-eb1b-4901-8f3d-e72f943fb13e'></a>

ArduinoBLE | Arduino Documentation

<a id='d9d69280-d599-412e-8a96-e9834da28ce4'></a>

ARDUINODOCS

<a id='77ac6573-fff2-4312-95ec-3e9cc1f5eacf'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='e5f82baa-50a0-4772-a2ff-388ce467c5f0'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='43852655-ebd7-4527-a969-9e07475ddd8b'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='39c8f49f-c3bc-41c8-9ec6-d2da7471f69b'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='07f576e2-780a-4882-8af5-ad17246d6883'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='c1e9d5ea-76e4-43b6-b0aa-bdd52dcb81c2'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='10fac00d-0a05-4ce8-87f0-d0aeb85adde4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='cb4e5ba4-a9db-479f-ac2c-1202c1a098f2'></a>

2/24