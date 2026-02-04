<a id='c5b0fc12-b89b-4733-8649-e1d7458f77cb'></a>

ARDUINODOCS

<a id='bd997365-8c16-41ff-908b-27797abfb58b'></a>



<a id='9267492c-7003-4ad5-bfaa-c1847a5a49c3'></a>

Installing the Silicon Labs core in the Arduino IDE

<a id='89d40090-b610-43f9-96c0-38d468007274'></a>

# Product Overview
The Nano Matter merges the well-known Arduino way of making complex technology more accessible with the powerful MGM240S from Silicon Labs, to bring Matter closer to the maker world, in one of the smallest form factors in the market.

<a id='524945d8-8e52-44ee-9a2a-568786b54dcb'></a>

It enables 802.15.4 (Thread®) and Bluetooth® Low Energy connectivity, to interact with
Matter-compatible devices with a user-friendly software layer ready for quick
prototyping.

<a id='939e7dc5-15c8-48de-b76c-1812e6415648'></a>

### Board Architecture Overview

The Nano Matter features a compact and efficient architecture powered by the MGM240S (32-bit Arm® Cortex®-M33) from Silicon Labs, a high-performance wireless module optimized for the needs of battery and line-powered IoT devices for 2.4 GHz mesh networks.

<a id='01b1a94a-38e8-475c-a4b9-c89acd2c4a78'></a>

<::A diagram of the Arduino Nano Matter circuit board, highlighting its main components:
- **USB-C connector**: Located on the left side of the board.
- **ATSAM-D11-D14A USB bridge**: Located near the USB-C connector.
- **MGM240S ARM Cortex-M33 Matter and BLE**: A large chip located on the right side of the board.
- **RGB LED**: Located near the center of the board.
- **2.4GHz antenna Matter and BLE**: Located on the far right edge of the board.
The board also shows various pins labeled D12 to D0, RST, RX0, TX1, D13, 3.3V AREF, A0 to A7, 5V, NC, and VIN.
: diagram::>

Nano Matter's main components

<a id='c528db05-f8eb-421a-89c1-53d97fda2042'></a>

<::logo: Arduino
ARDUINO
A stylized infinity symbol forms the main part of the logo, with the company name 'ARDUINO' beneath it.::>

<a id='553a5bea-5688-4dbd-b90e-5834d4600bdd'></a>

Here is an overview of the board's main components, as shown in the image above:

*   **Microcontroller:** at the heart of the Nano Matter is the MGM240S, a high-performance wireless module from Silicon Labs. The MGM240S is built around a 32-bit Arm® Cortex®-M33 processor running at 78 MHz.
*   **Wireless connectivity:** the Nano Matter microcontroller also features multiprotocol connectivity to enable Matter IoT protocol and Bluetooth® Low Energy. This allows the Nano Matter to be integrated with smart home systems and communicate wirelessly with other devices.

<a id='b93bd322-c223-4fcc-9e09-f1b7e4d6a86a'></a>

Pinout

<a id='d82be4d7-57a4-49b4-8b79-f4180a376a5c'></a>

<::Arduino Pinout Diagram

**Left Side Pins (Top to Bottom):**
- **Reset Button**: RESET
- **RGB LED**: LEDR, LEDG, LEDB
- **DAC**: SCK (orange, Digital), D-13 (orange, Digital), +3V3 OUT (red, Power), AREF (light orange, Analog)
- DAC0 (light orange, Analog) connected to A0 ~14 (light orange, Analog)
- DAC2 (light orange, Analog) connected to A1 ~15 (light orange, Analog)
- I2C0: SDA (dark blue D, Default) connected to A4 ~18 (light orange, Analog)
- SCL (dark blue D, Default) connected to A5 ~19 (light orange, Analog)
- DAC1 (light orange, Analog) connected to A6 ~20 (light orange, Analog)
- DAC3 (light orange, Analog) connected to A7 ~21 (light orange, Analog)
- +5V (red, Power)
- NC (no connection)
- GND (black, Power)
- +21V max: VIN (red, Power), EN (red, Power)

**Right Side Pins (Top to Bottom):**
- USB-C
- POWER LED
- SPI0: D-12 (orange, Digital), MISO (light blue, SPI), D-11 (orange, Digital), MOSI (light blue, SPI), D-10 (orange, Digital), SS (light blue, SPI)
- D-09 (orange, Digital)
- D-08 (orange, Digital)
- D-07 (orange, Digital)
- D-06 (orange, Digital)
- D-05 (orange, Digital)
- D-04 (orange, Digital)
- SPI1: D-03 (orange, Digital), SS1 (light blue, SPI), D-02 (orange, Digital), SCK1 (light blue, SPI)
- I2C1: SCL1 (dark blue D, Default), SDA1 (dark blue D, Default)
- GND (black, Power)
- RST (reset)
- UART/USART: D-01 (orange, Digital), MISO1 (light blue, SPI), PIN_SERIAL_RX1 (purple, UART/USART), D-00 (orange, Digital), MOSI1 (light blue, SPI), PIN_SERIAL_TX1 (purple, UART/USART)
- User Button: BTN_BUILTIN

**Notes:**
1. Outputs +5V when the board is USB powered.
2. The board has some solder jumpers at the bottom side to manage the board's power rails and ADC reference. Refer to full pinout for more details.

**Legend:**
- Power: Red
- Digital: Orange
- Analog: Light Orange
- SPI: Light Blue
- UART/USART: Purple
- Default: Dark Blue D symbol
: figure::>

Outputs +5V when the board is
USB powered.
The board has some solder jumpers at the bottom side
to manage the board's power rails and ADC reference.
Refer to full pinout for more details.

Legend:

Power          Digital        SPI
Analog         UART/USART     Default

                                                                 ARDUINO
<::Arduino logo: A stylized infinity symbol with the word "ARDUINO" underneath. : logo::>