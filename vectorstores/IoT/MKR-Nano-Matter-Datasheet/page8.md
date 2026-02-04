<a id='73278f9b-f2e1-44be-a4d3-ba667f041084'></a>

<::logo: Arduino
A teal-colored infinity symbol with a plus sign on the right side and a small circle on the left::>

<a id='656896b9-8e3e-4ca7-9879-53b2485e8f93'></a>

Arduino® Nano Matter

<a id='a513a670-a9be-40fc-9c8e-5a681508bde2'></a>

4.2 Block Diagram

<a id='992d6b55-41f8-466e-a391-0a6281c5dab5'></a>

An overview of the high-level architecture of the Nano Matter is illustrated in the figure below.
<::The image displays a block diagram titled "An overview of the high-level architecture of the Nano Matter".

The diagram shows the following components and their connections:

**Left Side:**
*   **Nano Headers (JP1) (JP2) 2.54 mm** (orange block)
    *   Connected to **Microcontroller MGM240SD22VNA2R (U5)** via:
        *   UART0 (bidirectional arrow)
        *   I2C (bidirectional arrow)
        *   GPIO (bidirectional arrow)
        *   SPI (bidirectional arrow)
        *   PWM (bidirectional arrow)
        *   ANALOG (bidirectional arrow)

**Center:**
*   **Microcontroller MGM240SD22VNA2R (U5)** (yellow block)
    *   Connected to an antenna symbol at the top.
    *   Connected to **Clock Signal 32.768kHz CM315D32768DZFT (Y1)** (gray block, bottom left) with a unidirectional arrow pointing to the microcontroller.
    *   Connected to **USB Bridge ATSAM-D11-D14A-MUT (U1)** via:
        *   UART (bidirectional arrow)
        *   SWD (bidirectional arrow)
    *   Connected to **LED RGB UHD1110-FKA-CL1A13R3Q1BBQFMF3 (DL1)** via a line labeled "LED RGB" with a unidirectional arrow pointing to the LED RGB component.

**Right Side:**
*   **USB-C Connector CX90B-16P (J1)** (orange block, top right)
    *   Connected to **USB Bridge ATSAM-D11-D14A-MUT (U1)** with a unidirectional arrow pointing to the USB Bridge.
*   **TVS Array PRTR5V0U2X, 215 (D1)** (gray block, top right)
    *   Connected to **USB Bridge ATSAM-D11-D14A-MUT (U1)** with a unidirectional arrow pointing to the USB Bridge.
*   **USB Bridge ATSAM-D11-D14A-MUT (U1)** (gray block, middle right)
*   **LED RGB UHD1110-FKA-CL1A13R3Q1BBQFMF3 (DL1)** (gray block, bottom right)

**Legend (bottom left):**
*   Connector (orange square)
*   Main Part (yellow square)
*   Internal Part (gray square)
*   I2C (dark blue square)
*   SPI (light blue square)
*   UART (pink square)
*   ADC (dark green square)
*   PWM (light green square with outline)
*   Other (white square with outline)

**Footer (bottom right):**
*   ARDUINO logo
*   Nano Matter
*   SKU code: ABX00112
*   Block Diagram
*   Last update: 19 Mar, 2024
: flowchart::>

<a id='8832ce1d-33e1-4782-a4f9-372c545b6fbc'></a>

8 / 18

<a id='af64a29e-8d2b-4f51-9f97-df799f1ab183'></a>

Arduino® Nano Matter

<a id='00faf8c6-7a90-4444-b1ab-1caad0326836'></a>

Modified: 29/01/2026