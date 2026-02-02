<a id='842d66f1-e2ff-475d-a1fb-25b04a7d1ec1'></a>

12/4/25, 2:50 PM

<a id='dd850597-231c-49e5-95d5-43761313b83e'></a>

ArduinoBLE | Arduino Documentation

<a id='ca0ef624-ee91-4629-aaaa-9781a370cabd'></a>

ARDUINODOCS

<a id='332dc4e7-0216-412f-9ab7-c2121626bdb4'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='74cd5f17-d30a-4c17-a8c9-ffccc6dffb09'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='96425fed-1e30-45f3-a3d4-2a7d4ca0cf6a'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='9b7293db-66f3-46a6-9b3f-488231ae07ce'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='0d9eddce-c34e-4924-bef0-4987d614453e'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='27784aa6-00b2-4c92-9826-4a3286a0a18c'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='8cdaad63-de4d-42a5-9dd3-fe6ae67e0766'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='0348b2b6-d180-4463-93b9-95973360a0e2'></a>

2/10