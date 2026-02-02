<a id='4d315896-e5cc-45d7-8786-87452572f086'></a>

<::logo: Arduino
ARDUINO
A gray infinity symbol with a minus sign on the left and a plus sign on the right sits above the company name.::>

<a id='f10543d1-111a-49dc-a68a-1e7e76f3209c'></a>

ARDUINO
MKR FOX 1200
STORE.ARDUINO.CC/MKR-FOX-1200

<a id='98b8db94-b604-4cae-a25b-955f78473240'></a>

<::Arduino Pinout Diagram:figure::>
## Power Input
- Two AA batteries connected to the board.
- Power input labeled 'Power'.

## Power Pins
- +5V
- VIN
- +3V3
- GND
- RESET
- LED_BUILTIN

## Left Side Pins (Digital/Analog)
- INT[3]
- INT[2]
- SC5 P0A: INT[2], TC6/WO[0]
- SC5 P1A: INT[3], TC6/WO[1]
- SC0 P0A: INT[4], TCC0/WO[0]
- SC0 P1A: INT[5], TCC0/WO[1]
- SC0 P2A: INT[6], TCC1/WO[0]
- SC0 P3A: INT[7], TCC1/WO[1], I2S_SD0
- SC3 P0/SC5 P0A: INT[6], TC4/WO[0], TCC0/WO[4]
- SC3 P1/SC5 P1A: INT[7], TC4/WO[1], TCC0/WO[5]
- SC0 P2/SC2 P2A: INT[10], TCC1/WO[0], TCC0/WO[2], I2S_SCK[0]
- SC0 P3/SC2 P3A: INT[11], TCC1/WO[1], TCC0/WO[3], I2S_FS[0]
- SC4 P2A: INT[10], TC5/WO[0], TCC0/WO[4]
- INT[11], TC5/WO[1], TC5/WO[1]

## Middle Left Pins (Analog/Digital)
- AREF/AIN[1]: AREF/AIN[1], PA03, AREF
- DAC0/AIN[0]: DAC0/AIN[0], PA02, A0, D15
- AIN[10]: AIN[10], PB02, A1, D16
- AIN[11]: AIN[11], PB03, A2, D17
- AIN[4]: AIN[4], PA04, A3, D18~
- AIN[5]: AIN[5], PA05, A4, D19~
- AIN[6]: AIN[6], PA06, A5, D20
- AIN[7]: AIN[7], PA07, A6, D21
- PA22: D0~
- PA23: D1~
- AIN[18]: PA10, D2~
- AIN[19]: PA11, D3~
- PB10: D4~
- PB11: D5~

## Right Side Pins (Digital/Communication)
- D14: PB22, TX (SC5) (UART)
  - TC7/WO[0], INT[6], SC5 P2A
- D13: PB23, RX (SC5) (UART)
  - TC7/WO[1], INT[7], SC5 P3A
- ~D12: PA09, SCL (SC2) (I2C), AIN[17], I2S_MCK[0]
  - TCC0/WO[0], TCC1/WO[3], INT[9], SC0 P1/SC2 P1A
- D11: PA08, SDA (SC2) (I2C), AIN[16], I2S_SD1
  - TCC0/WO[0], TCC1/WO[2], NMI, SC0 P0/SC2 P0A
- ~D10: PA19, CIPO (SC1) (SPI)
  - TC3/WO[1], TCC0/WO[3], INT[3], SC1 P3/SC3 P3A
- D9: PA17, SCK (SC1) (SPI)
  - TCC2/WO[1], TCC0/WO[7], INT[1], SC1 P1/SC3 P1A
- ~D8: PA16, COPI (SC1) (SPI)
  - TCC2/WO[0], TCC0/WO[6], INT[0], SC1 P0/SC3 P0A
- ~D7: PA21
  - TC7/WO[1], TCC0/WO[7], INT[5], SC5 P3/SC3 P3A
- ~D6: PA20
  - TC7/WO[0], TCC0/WO[6], INT[4], SC5 P2/SC3 P2A

<a id='a3405939-51d1-45be-bb12-38a51ba96665'></a>

<::Legend:
- Black solid square: Ground
- Red solid square: Power
- Teal solid square: LED
- Grey solid square: Internal Pin
- Brown solid square: SWD Pin
- Orange striped square: Digital Pin
- Orange hollow square: Analog Pin
- White hollow square: Other Pin
- Yellow-orange solid square: Microcontroller's Port
- Yellow solid square: Default
- Dark teal solid square: Analog
- Dark teal striped square: Communication
- Teal solid square: Timer
- Light blue solid square: Interrupt
- White hollow square: Sercom

Warnings:
- Red exclamation mark icon: MAXIMUM current per pin is 7mA
- Red exclamation mark icon: MAXIMUM source current is 46mA
- Red exclamation mark icon: MAXIMUM sink current is 65mA per pin group
: legend::>

<a id='00bf3a01-cbca-4ce1-8236-e1385afe9c00'></a>

VIN Input voltage to the board.

NOTE: CIPO/COPI have previously
been referred to as MISO/MOSI

<a id='12c731f3-6e4d-4953-bfb2-ec17464a486a'></a>

<::logo: Creative Commons
CC BY SA
Three gray circles with white icons, including a double 'c', a person, and a circular arrow, are arranged horizontally above the letters 'BY' and 'SA' in a rounded rectangle.::>