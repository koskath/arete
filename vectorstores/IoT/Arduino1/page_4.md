<a id='423a8602-37ef-43a8-a3ee-33010d9aa794'></a>

12/4/25, 2:50 PM

<a id='bc449983-7c9a-49d3-83be-0d25497c887a'></a>

ArduinoBLE | Arduino Documentation

<a id='bc10dc56-4ee6-4b32-88c7-76e99447d901'></a>

ARDUINODOCS

<a id='636e23ad-d24f-4103-a344-02de0e95e23b'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='3f5a4088-45c1-4d73-9e98-6ecc1cbc7a3e'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='c55a57b6-90bb-4ff6-9a54-09db79035ecc'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='d341de5c-9f99-4062-9932-3c41f4e49d61'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='4d4f5007-9a4b-4958-853b-e6e376baf6a8'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='25ba315e-f1d7-437f-af56-e7ac4e610c35'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='daa042ec-e32f-46b0-ac2d-4454ccf12fc5'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='05e91d60-f331-47da-b896-5dca1dcfdddf'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='327bd7a2-7864-4075-9a3e-830c689389d8'></a>

BLE class BLEDevice Class BLEService Class

<a id='b4770c03-2e26-4888-8729-f6b658cdc0de'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='22eb070c-0c1f-4b7c-a885-57fd8ecb71d4'></a>

4/10