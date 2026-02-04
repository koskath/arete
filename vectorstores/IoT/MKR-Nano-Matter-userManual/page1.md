<a id='22b77537-79f6-4de5-a3d2-268a6f8105f7'></a>

ARDUINODOCS

<a id='a9e40793-9419-4d9a-ab41-7a6ce74cba21'></a>

Search on Docs /

<a id='50ca7243-cc23-4482-b147-77d265bed7d5'></a>

← Go Back

# Hardware

<

<a id='2356391c-b772-456a-b11c-b3ae628a70ef'></a>

Nano Matter v

Tutorials
- Nano Matter User Manual (selected)
- Getting Started with Nano Matter Display
- Matter Smart Fan with the Arduino Nano Matter
- Matter Smart Relay with the Arduino Nano Matter
- Matter RGB Light with the Arduino Nano Matter
- Matter Temperature Sensor with the Arduino Nano Matter
- Open Thread Border Router with Nano Matter & ESP32
- ML Magic Wand with the Arduino Nano Matter

<a id='b3b3b83f-cc9b-467a-b792-61ec9b3a6f2a'></a>

Home / Hardware / Nano Matter / Nano Matter User Manual

<a id='4891da6e-144f-4183-8eb3-162b8e632c99'></a>

# Nano Matter User Manual
Learn about the hardware and software features of the Arduino® Nano Matter.

<a id='013136b9-de33-4db1-858e-38cbc81d81b8'></a>

Author • Christopher Mendez

Last revision • 10/15/2025

<a id='e64f064b-d7ed-425e-aaef-22c85bfa0925'></a>

# Overview

This user manual will guide you through a practical journey covering the most interesting features of the Arduino Nano Matter. With this user manual, you will learn how to set up, configure and use this Arduino board.

<a id='6679939b-e051-48d6-b1c7-6dd4cd79b22e'></a>

<::Arduino IDE displaying C++ code for a Matter-enabled lightbulb, a smartphone app for controlling the lightbulb's color, and an Arduino Nano Matter board:

**1. Arduino IDE Window**
- **Title:** nano_matter_lightbulb_color (Arduino IDE 1.8.19)
- **Menu:** File Edit Sketch Tools Help
- **Toolbar:** Icons for Verify, Upload, New, Open, Save, Serial Monitor
- **Tab:** nano_matter_lightbulb_color
- **Code Snippet:**
  ```cpp
  15 #include <matter.h>
  16 #include <matterlightbulb.h>
  17
  18 #define LED_R LED_BUILTIN
  19 #define LED_G LED_BUILTIN_1
  20 #define LED_B LED_BUILTIN_2
  21
  22 MatterColorLightBulb matter_color_bulb;
  23
  24 void update_led_color();
  25 void led_off();
  26 void handle_button_press();
  27 volatile bool button_pressed = false;
  28
  29 void setup() {
  30   //
  31   Serial.begin(115200);
  32   Matter.begin();
  33   matter_color_bulb.begin();
  34   matter_color_bulb.boost_saturation(5); // Boost saturation by 5 percent
  35 }
  ```
- **Output Serial Monitor:**
  - Message (Enter to send message to 'Arduino Nano Matter' on COM9)
  - Log entries:
    - 11:23:29.532 -> Bole OK
    - 11:23:30.532 -> Setting bulb color to r = 254 g = 254 b = 254
    - 11:23:30.554 -> Setting bulb color to r = 254 g = 140 b = 253
    - 11:23:30.595 -> Setting bulb color to r = 254 g = 0 b = 25
    - 11:23:30.606 -> Setting bulb color to r = 247 g = 149 b = 254
    - 11:23:30.678 -> Setting bulb color to r = 233 g = 202 b = 254
- **Status Bar:** Lin 180 Col 7 Arduino Nano Matter on COM9

**2. Smartphone Screen**
- **Status Bar:** 16:23, Wi-Fi, battery icon
- **App Header:** X Matter bulb (with close icon and three-dot menu icon)
- **Content:**
  - Light color dropdown header
  - Color label
  - Circular color picker wheel with a white center, showing a full spectrum of colors.
  - Buttons: Cancel, Done

**3. Arduino Nano Matter Board**
- A compact circuit board with a USB-C port, various pins labeled D13, 3.3V, AREF, D0-D12, RST, 5V, GND, VIN, etc.
- Features a central chip with 'SILICON LABS' logo and 'ARDUINO NANO MATTER' branding with the Matter logo (three arrows forming a triangle).
- Includes several smaller components, resistors, capacitors, and indicator LEDs.
: three-part visual::>

<a id='98b74785-ed7e-487d-8ae3-4b6118f2cbd2'></a>

Hardware and Software Requirements

<a id='373b118c-179b-4fac-a5fc-a900802fcdaa'></a>

# Hardware Requirements

*   Nano Matter (x1)
*   USB-C® cable (x1)

<a id='bb4ed7a2-0b71-4a78-9c19-85948f2c1583'></a>

## Software Requirements

* Arduino IDE 2.0+ or Arduino Cloud Editor

<a id='8d44d35f-78d2-469e-a9bc-9ee33038d324'></a>

# Board Core and Libraries

The **Silicon Labs** core contains the libraries and examples you need to work with the board's components, such as its Matter, Bluetooth® Low Energy, and I/Os. To install the Nano Matter core, navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `Nano Matter` and install the latest `Silicon Labs` core version.

<a id='6aba622c-fac2-4c6c-b173-a1b44d67091f'></a>

sketch_nov22a | Arduino IDE 2.3.3

File Edit Sketch Tools Help

Arduino Nano Matter

BOARDS MANAGER

sketch_nov22a.ino

Nano Matter

Type: All

Silicon Labs by Silicon
Labs
2.1.0 installed

Boards included in this package:
Ezurio Lyra 24P 20dBm Dev Kit,
Arduino Nano Matter, SparkFun...
More info

2.1.0 REMOVE

1 void setup() {
2 // put your setup code here, to run once:
3
4 }
5
6 void loop() {
7 // put your main code here, to run repeatedly:
8
9
10

<a id='c573b1bf-1e58-4c5c-86e6-a6f7baf4defc'></a>

ON THIS PAGE

<a id='500385a6-54a3-4695-b276-1f9321e3d14f'></a>

Overview
Hardware and Software
Requirements +
Product Overview +
First Use +
Matter +
Arduino Cloud +
Bluetooth® Low Energy +
Onboard User Interface +
Pins +
Communication +
Support +

<a id='52242fbc-540a-47a5-82e8-e80951f09805'></a>

<::logo: 
Help
A dark gray, rounded rectangular button with a question mark icon and the word "Help" in white.::>