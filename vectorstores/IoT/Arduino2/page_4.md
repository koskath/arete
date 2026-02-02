<a id='282bfb95-cefe-463e-b014-9117d53d050e'></a>

12/4/25, 2:51 PM

<a id='e858013d-31b7-44d3-a147-0ea384bf6075'></a>

ArduinoBLE | Arduino Documentation

<a id='4accd674-b650-43bd-b434-16f1b5b011e6'></a>

ARDUINODOCS

<a id='98f91b39-0b23-4ac3-a67c-ea228c69d103'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='d05f0068-1b43-4f34-89eb-e1eb364e5fee'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='3e74d089-570f-4c84-9b01-204133a0fba7'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='86ac59a4-48fe-427b-9243-4b86c77bc23b'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='30390742-aeb7-48b9-b47c-795bcdaf98a8'></a>

You can provide additional services that are not advertised. Central devices will learn about these through the connection/bonding process. Non-advertised services cannot be used to discover devices, though. Sometimes this is not an issue. For example, you may have a custom peripheral device with a custom service, but in your central device app you may know that it also provides the Battery Service and other services.

<a id='d9d02e99-b0cc-4658-82e7-f7472eccc569'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='3c12a3c7-0cb8-4e48-af14-1a9bdd0dc6a0'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='32996292-5b03-4c65-b15d-76bbdc728da5'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='56e52f78-3d8b-443e-9d72-262d05002d11'></a>

BLE class BLEDevice Class BLEService Class

<a id='423fba50-4c61-4d58-a114-dda01c349487'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='465a30fd-5092-4f12-b365-ab2dc507f434'></a>

4/24