<a id='5f6947b5-ed24-47e1-9ee2-72cbc0c06272'></a>

AD9860/AD9862

Setting this bit high enables the decimation filters and decimates the receive data by two.

<a id='f02fd079-5f9e-4990-8a62-617ec19c7130'></a>

## REGISTER 8: Tx PWRDWN
### BIT 5: Alt Timing Mode
The timing section in the data sheet describes two timing modes, the "Normal Operation" and the "Alternate Operation" modes. At power up, the default configuration is established from the logic level of the Mode/TxBlank pin. If Mode/TxBlank is logic low, the Normal Operation mode is the default; if the Mode/ TxBlank pin is held at a logic high, the Alternative Operation mode is configured at power-up (the DLL is forced to multiply by 4 at power-up by default in this mode). After power up, the operation mode can be configured so that the Mode/TxBlank pin can be used for other functions. To allow this, set this bit high.

<a id='bdf95058-8438-43f3-ad9c-3f658465ac0e'></a>

**BIT 4: TxOff Enable**
By default, the Mode/TxBlank pin is not used for any transmit synchronization. The Mode/TxBlank pin input can be used to serve two functions, blanking the DAC outputs and slaving the TxPGA gain control. When this bit is set high, a logic high on the Mode/TxBlank pin forces the Tx digital block to stop clocking. In this mode, the Tx outputs will be static, holding their last update values. To slave the TxPGA gain control to the Mode/TxBlank pin input, register Slave Enable (Register 17, Bit 1) needs to also be programmed. See that register for more information.

<a id='43fd0aaf-2531-4cf6-98e9-0eb9f4fa2a43'></a>

**BIT 3: Tx Digital (Power-Down)**
By default this bit is low, enabling the transmit path digital to operate as programmed through other registers. By setting this bit high, the digital blocks are not clocked to reduce power consumption. When enabled, the Tx outputs will be static, holding their last update values.

<a id='bb625de3-5ce6-4bc3-8b5e-6451486324b3'></a>

BIT 0-2: Tx Analog (Power-Down)
Three options are available to reduce analog power consumption for the Tx channels. The first two options disable the analog output from Tx channel A or B independently, and the third option disables the output of both channels and reduces the power consumption of some of the additional analog support circuitry for maximum power savings. With all three options, the DAC bias current is not powered down so recovery times are fast (typically a few clock cycles). The list below explains the different modes and settings used to configure them.

<a id='6dfa8035-db81-4890-bb53-eaf6ed99fead'></a>

**Power-Down Option**

Tx Analog Power-Down Bits Setting [2:0]

Power-Down Tx B Channel Analog Output [1 0 0]
Power-Down Tx A Channel Analog Output [0 1 0]
Power-Down Tx A and Tx B Analog Outputs [1 1 1]

<a id='3bd048ed-620e-4241-8b4d-2153376550b2'></a>

REGISTER 10/11/12/13: DAC OFFSET A/B
DAC A/DAC B Offset
These 10-bit, twos complement registers control a dc current
offset that is combined with the Tx A or Tx B output signal. An
offset current of up to 12% I₀₅₄₃ (2.4 mA for a 20 mA full-
scale output) can be applied to either differential pin on each
channel. The offset current can be used to compensate for offsets
that are present in an external mixer stage, reducing LO leakage
at its output. Default setting is hex00, no offset current. The
offset current magnitude is set using the lower nine bits. Setting
the MSB high will add the offset current to the selected differen-
tial pin, while an MSB low setting will subtract the offset value.

<a id='533b517a-dfe1-477e-9d37-41de5381a1a9'></a>

**DAC A/DAC B Offset Direction**
This bit determines to which of the differential output pins for the selected channel the offset current will be applied. Setting this bit low will apply the offset to the negative differential pin. Setting this bit high will apply the offset to the positive differential pin.

<a id='89b10c57-b298-4a9c-917e-3f61d327bb0e'></a>

REGISTER 14/15: DAC GAIN A/B
BIT 6, 7: DAC A/DAC B Coarse Gain Control
These register bits will scale the full-scale output current (IOUTFS)
of either Tx channel independently. IOUT of the Tx channels is a
function of the RSET resistor, the TxPGA setting, and the Coarse
Gain Control setting.

<a id='e9716d2c-f40f-4afd-8445-0ea87ff2a287'></a>

<table><thead><tr><th>MSB, LSB</th><th>Tx Channel Current Scaling</th></tr></thead><tbody><tr><td>10 or 11</td><td>Does not scale output current</td></tr><tr><td>01</td><td>Scales output current by 1/2</td></tr><tr><td>00</td><td>Scales output current by 1/11</td></tr></tbody></table>

<a id='48a44ba5-9130-4733-b23b-23d9af1bf09c'></a>

**BIT 5–0: DAC A/DAC B Fine Gain**
The DAC output curve can be adjusted fractionally through the Gain Trim Control. Gain trim of up to \u00b14% can be achieved on each channel individually. The Gain Trim register bits are a twos complement attention control word.

<a id='d439b31d-ad7e-471b-8c53-b24574514b9f'></a>

<table><thead><tr><th>MSB, LSB</th><th>Description</th></tr></thead><tbody><tr><td>100000</td><td>Maximum positive gain adjustment</td></tr><tr><td>111111</td><td>Minimum positive gain adjustment</td></tr><tr><td>000000</td><td>No adjustment (default)</td></tr><tr><td>000001</td><td>Minimum negative gain adjustment</td></tr><tr><td>011111</td><td>Maximum negative gain adjustment</td></tr></tbody></table>

<a id='bb77b4df-99ee-41c5-9679-48836246f96c'></a>

**REGISTER 16: TxPGA GAIN**
**BIT 0–7: TxPGA Gain**
This 8 bit, straight binary (Bit 0 is the LSB, Bit 7 is the MSB) register controls for the Tx programmable gain amplifier (TxPGA). The TxPGA provides a 20 dB continuous gain range with 0.1 dB steps (linear in dB) simultaneously to both Tx channels. By default, this register setting is hex00.

<a id='5093460d-2e6f-4e44-bce7-7132f1e88f68'></a>

MSB, LSB

000000 Minimum gain scaling -20 dB
111111 Maximum gain scaling 0 dB

<a id='2fe4ba36-7eea-490f-8e15-e6c32f284ee5'></a>

REGISTER 17: Tx MISC
BIT 1: Slave Enable
The TxPGA Gain is controlled through register TxPGA Gain
setting and by default is updated immediately after the register
write. If this bit is set, the TxPGA Gain update is synchronized
with the rising edge of a signal applied to the Mode/TxBlank
pin. Setting TxOff enable in Register 8 is also required.

<a id='c457cb18-38a3-4b36-8b17-1f064dc78559'></a>

**BIT 0: TxPGA Fast (Update Mode)**
The TxPGA Fast bit controls the update speed of the TxPGA.
When Fast Update mode is enabled, the TxPGA provides fast gain
settling within a few clock cycles. Default setting for this bit
is low, which indicates Normal Update mode. Fast mode is
enabled when this bit is set high.

<a id='658753cd-c305-4627-9600-4edf8dd5aa8d'></a>

**REGISTER 18: Tx IF (INTERFACE)**
**BIT 6: Tx Retime**
The Tx path can use either of the clock outputs, CLKOUT1 or CLKOUT2, to latch the Tx input data. Since CLKOUT1 and CLKOUT2 have slight phase offsets, this provides some timing flexibility with the interface. By default, this bit is high and the Tx input latches use CLKOUT1. Setting this bit low will force the Tx latches to use CLKOUT2.

<a id='56a27634-044a-4383-b62c-b2f34375da20'></a>

-14-

<a id='8e5f7296-49cd-451e-acd2-033d07edf486'></a>

REV. 0