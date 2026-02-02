<a id='251a392d-76cd-465b-af25-36c076be1705'></a>

12/4/25, 2:50 PM

<a id='186ee290-750b-4461-9b8d-d25027c4afe4'></a>

ArduinoBLE | Arduino Documentation

<a id='5cf00db7-7d4c-4d2f-a917-032cd4564227'></a>

ARDUINODOCS

<a id='9c28e01f-4ac8-4596-b922-4722444ee5ed'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='a923d464-5d0f-4018-8916-5bfd2ea12f2c'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='04a006a0-7357-48a7-8cf8-65932d35f07f'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='c35e4e66-ef35-4b6c-bcac-364e82bcc554'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='365c1188-60d8-4073-8f0f-2da8503bd0d2'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='ca4f8806-83fc-4cdc-a131-131528dc85ce'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='b23af4b0-7719-4088-a4de-1ad7c0e665af'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='ad843ef3-61b4-456b-9c0a-c51d0e3958c0'></a>

2/22