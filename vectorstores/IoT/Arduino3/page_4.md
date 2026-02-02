<a id='fd4813ef-4ff9-4a53-9d09-7871cfd2c3fb'></a>

12/4/25, 2:51 PM

<a id='daec8e2b-618a-4be3-98a9-722047a9faa3'></a>

ArduinoBLE | Arduino Documentation

<a id='8d214c3d-7fd4-45a5-a1cb-3f7b2b23ce20'></a>

ARDUINODOCS

<a id='a4edf696-c0b6-4bb5-afba-449a87b2a757'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='dab266cd-0b94-40f2-865d-eaaf93785a74'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='f04c00bb-2a11-4dcb-b3d2-97055efcbde6'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='329fab6a-2d54-48c2-ab6e-630fe6a377b8'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='2538ac1a-4127-4fc9-9961-096ece98ad72'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='1b94ae7b-6e60-4160-a216-84cb1e552f24'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='a73c68fa-de22-43da-ba15-75768fa55b3b'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='77e54ff2-8241-4d18-ba9a-b3d73b14c8dc'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='3e592232-e569-465e-be77-b8912593d739'></a>

BLE class BLEDevice Class BLEService Class

<a id='e30b203c-d266-46c3-98c7-008c9820b127'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='2a22c9d3-7328-47e1-abf9-cc9076084943'></a>

4/9