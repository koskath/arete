<a id='ea7d85a3-712c-4068-957f-df6a54e70397'></a>



<a id='384f80e3-e55e-4859-8ff3-672adf1460ca'></a>

Arduino® Nano Matter

<a id='e27a4b2e-136f-4c49-b25e-a2dca2f366f9'></a>

# 4 Functional Overview
The core of the Nano Matter is the MGM240SD22VNA microcontroller from Silicon Labs. The board also contains several peripherals and actuators connected to its microcontroller, such as a push button and an RGB LED available for the user.

<a id='571162e7-3879-42ee-a054-c0733df511ad'></a>

4.1 Pinout
The Nano-styled header connectors pinout is shown in the figure below.
<::Pinout diagram of a Nano-styled board.

**Left Header (from top to bottom):**
*   **Reset Button:** RESET
*   **RGB LED:** LEDR, LEDG, LEDB
*   **Digital Pins / Analog Inputs:**
    *   DAC
    *   SPI0: SCK (D)
    *   ~D13 (OUT)
    *   +3V3 (OUT)
    *   AREF
    *   A0 (~14)
    *   A1 (~15)
    *   A2 (~16)
    *   A3 (~17)
    *   I2C0: SDA (D) A4 (~18)
    *   I2C0: SCL (D) A5 (~19)
    *   DAC1: A6 (~20)
    *   DAC3: A7 (~21)
    *   +5V
    *   NC
    *   GND
    *   +21V max: VIN (IN)

**Right Header (from top to bottom):**
*   **USB-C**
*   **POWER LED**
*   **Digital Pins / Analog Inputs:**
    *   SPI0: ~D12 (D MISO)
    *   SPI0: ~D11 (D MOSI)
    *   SPI0: ~D10 (D SS)
    *   ~D9
    *   ~D8
    *   ~D7
    *   ~D6
    *   ~D5
    *   ~D4
    *   SPI1: ~D3 (SS1)
    *   SPI1: ~D2 (SCK1)
    *   GND
    *   RST
    *   UART / USART: ~D1 (MISO1, PIN_SERIAL_RX1)
    *   UART / USART: ~D0 (MOSI1, PIN_SERIAL_TX1)
*   **User Button:** BTN_BUILTIN

**Notes:**
1.  Outputs +5V when the board is USB powered.
2.  The board has some solder jumpers at the bottom side to manage the board's power rails and ADC reference. Refer to full pinout for more details.

**Legend:**
*   Digital (orange)
*   Power (red)
*   Ground (black)
*   SPI (light blue)
*   Analog (white)
*   I2C (dark blue)
*   UART/USART (purple)
*   Not Connected (light grey)
*   D Default (light blue with 'D')

**Board Information:**
ARDU
Nano M
SKU code: ABX P
Last update: 02 Dec, 
: figure::>

<a id='416bec40-b018-404a-91dd-c45b799fcac9'></a>

The **Nano Matter with headers (ABX00137)** shares the same architecture as the **Nano Matter (ABX00112)** but comes with headers pre-installed.

<a id='52bfa283-3840-4dc2-b52c-95d498c980fb'></a>

7 / 18

<a id='750b1340-cf40-4127-a15a-264006ed0992'></a>

Arduino® Nano Matter

<a id='c5437b88-3e71-4cd0-a664-9bb661c6e5c2'></a>

Modified: 29/01/2026

<a id='14d5751e-9acd-4965-838d-f07560bf28fb'></a>

<::logo: JINO
JINO
A black and white logo with a circular shape containing a plus sign and an arrow pointing to the right, resembling a Creative Commons share-alike symbol, above the text "JINO".::>