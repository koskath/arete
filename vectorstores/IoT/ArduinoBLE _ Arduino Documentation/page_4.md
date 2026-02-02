<a id='4ed0ce9f-3185-4cb0-8ae4-1a4993bc7ca8'></a>

12/4/25, 2:49 PM

<a id='7fba2ad5-bd69-40da-817c-24e4a3bbb818'></a>

ArduinoBLE | Arduino Documentation

<a id='72d27ed7-6da5-479c-8fda-63ad50f351fe'></a>

ARDUINODOCS

<a id='97609240-dc6a-4886-8a33-9415c7c60603'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='01883dbe-bf72-45ae-86cf-ca33c5617548'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='0391cbd4-462e-49b3-a7d2-d041d0123d06'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='4e55fa3b-d965-4c2f-af0f-9de899a74fe1'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='5f395aa2-53fd-4301-906f-a88ba434b853'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='39e6f555-d0fd-4815-a9ed-5a5a3a20d7c4'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='776031e9-066c-4cfd-a74a-407d45ba657f'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='9a258263-2eab-4441-9f11-70fbc7956721'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='ed68171c-5fb5-4e30-afe5-2f5b437afa99'></a>

BLE class BLEDevice Class BLEService Class

<a id='f3fea811-6b3c-4acc-a3bd-e65c62282ec8'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='3f0d6241-b169-417b-a00b-28fb54f91ffb'></a>

4/26