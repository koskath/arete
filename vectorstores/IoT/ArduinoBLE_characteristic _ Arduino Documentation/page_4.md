<a id='8a071277-ac60-4971-bde1-8f88744c68d1'></a>

12/4/25, 2:50 PM

<a id='ced33241-7deb-4bd2-9663-8a17aaf0e692'></a>

ArduinoBLE | Arduino Documentation

<a id='3b716c8f-7989-46f2-8568-efc88e969bdf'></a>

ARDUINODOCS

<a id='13984431-77ab-4655-85fe-87d6f632f921'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='23302c5c-d250-467d-87a2-c6ed975d21dc'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='b59680aa-7011-43eb-b835-007819742a91'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='15ea87f3-5455-470f-b301-281ad3c9c770'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='bb979a10-3fe6-4171-a023-0f874b7ffd06'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='4807a0ba-ff58-4fee-bcf4-7202306bf5e2'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='eb4c6a49-f33a-47d9-b26c-ad0885a70a0c'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='0404b35b-153b-4b43-ad47-eb7a539a2879'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='0be6187f-e924-497a-914c-de8183d638f5'></a>

BLE class BLEDevice Class BLEService Class

<a id='905d083f-e554-44eb-b8d8-8180dca5b4a7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='703a63af-19b9-4fe7-9ae2-48bf69028088'></a>

4/22