<a id='6dc80053-4eb7-4237-87b2-b3fc94c42011'></a>

ARDUINODOCS

<a id='beddd8d6-dce8-4063-9034-8f47576404f5'></a>

## Home Assistant Tips

* Make sure you are using a **64-bit** Home Assistant version (OS or Docker containerized version).
* Use the **Thread®** add-on to verify your available Thread® networks.
* You can just have a Matter device commissioned to one platform at a time.

<a id='560c1c25-a9c4-4d6b-88a6-34dba43347ee'></a>

i
Be aware that the Matter integration for Home Assistant is still in BETA, it can receive major updates and its functionality may vary between different vendors.

<a id='6a39c276-b6b5-446a-9b2c-79bf252396cc'></a>

## Updating the Commissioning QR Code

Each Nano Matter board comes with a default QR code used for commissioning. In this section, you will learn how to **generate a unique QR code** for your device by updating its provisioning ID.

<a id='e9a76183-295e-40de-92c0-fffd656012b7'></a>

<::A figure showing three vertical panels. Each panel contains a QR code at the top and a small electronic development board below it. 

Panel 1:
QR Code #0: A black and white QR code.
Board #1: A small, blue electronic development board with a USB-C port, various components, and pin headers, angled slightly.

Panel 2:
QR Code #1: A black and white QR code.
Board #2: A small, blue electronic development board with a USB-C port, various components, and pin headers, angled slightly, identical to Board #1.

Panel 3:
QR Code #2: A black and white QR code.
Board #3: A small, blue electronic development board with a USB-C port, various components, and pin headers, angled slightly, identical to Board #1 and Board #2.

Unique QR Codes for your Matter devices: figure::>

<a id='caab5d56-e144-4e36-9d64-f475996f1f4a'></a>

By assigning a unique provisioning ID, you can:
* Generate a distinct QR code for each board.
* Commission multiple Nano Matter boards to the same network without conflicts.
* Prepare your devices for real-world field deployment.

<a id='a00020d7-89fd-4d19-8343-ca1ae0c100e7'></a>

## Prerequisites

Before starting, make sure you have the following:

* Make sure the **Arduino IDE** and the **Silicon Labs Arduino Core** are both installed.
* Make sure there is only **one** board connected to your computer at a time.
* Your Matter sketch already flashed to the board.
* Clone the **Arduino Matter Provision Tool** repository on your local machine.

<a id='71c612f9-caa8-4d71-b8e9-234999677845'></a>

### Changing the Provisioning ID

To assign a new provisioning ID and generate a new QR code:

* Open a terminal and navigate to the cloned `/arduino_matter_provision` folder.
* The provisioning command has the following format:

<a id='823af273-2db9-4f31-81d6-6c649d29f794'></a>

```
1 python arduino_matter_provision.py <board_name> <config_numbe
```

<a id='9bae3fa5-a9fc-48d9-a378-18e5f3ab2dab'></a>

* Replace `<board_name>` with `nano_matter` and choose a configuration number (e.g., `1`):