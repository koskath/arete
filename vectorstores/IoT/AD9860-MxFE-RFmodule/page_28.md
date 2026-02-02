<a id='e6792c3f-d1ce-40c5-a7e7-3a7ed7ea71b3'></a>

## AD9860/AD9862

The timing block diagrams in Figures 14 and 15 show how the various clocks of the single and dual Tx path are affected by the various register settings.

<a id='deca2e16-8177-421c-a9c7-e0e12bb9ca49'></a>

For dual Tx data, an option to redirect demultiplexed data to either path is available. For example, the AD9860/AD9862 can accept complex data in the form of I then Q data or Q then I data, controlled through QI Order register.

<a id='7e319c02-6c3a-4c2e-a748-6d582f2dac1b'></a>

For the dual Tx data cases, the Tx_SYNC pin input logic level defines what data is currently on the Tx data bus. By default, when Tx_SYNC is low, Channel A data (first of the set) should be on the data bus. If TxSYNC is high, Channel B data (or the second of the set) should be on the Tx bus. This can be reversed by setting the Inv TxSYNC register.

<a id='fd902323-45a0-4e4c-990b-5d453a912866'></a>

## ADDITIONAL FEATURES
In addition to the features mentioned above in the transmit, receive and clock paths, the AD9860/AD9862 also integrates components typically required in communication systems. These components include auxiliary analog-to-digital converters (AUX ADC), auxiliary digital-to-analog converters (AUX DAC), and a sigma-delta output.

<a id='4fd0598f-f487-45d9-a139-e363ade0c038'></a>

**Auxiliary ADC**
Two auxiliary 10-bit SAR ADCs are available for various external signals throughout the system, such as a Receive Signal Strength Indicator (RSSI) function or Temperature Indicator. The auxiliary ADCs can convert at rates up to 1.25 MSPS and have a bandwidth of around 200 kHz. The two auxiliary ADCs (AUX ADC A and AUX ADC B) have multiplexed inputs, so that up to four system signals can be monitored.

<a id='864736c9-f351-443a-985e-48f0bd588204'></a>

The AUX ADC A multiplexer controls whether pin AUX_ADC_A1 or pin AUX_ADC_A2 is connected to the input of Auxiliary ADC A. The multiplexer is programmed through Register D34 B1, SelectA. By default, the register is low, which connects the AUX_ADC_A2 Pin to the input. Similarly, AUX ADC B has a multiplexed input controlled by Register D34 B4, SelectB. The default setting for SelectB is low, which connects the AUX_ADC_B2 input pin to AUX ADC B. If the SelectA or SelectB register bit is set high, then the AUX_ADC_A1 Pin or the AUX_ADC_B1 pin is connected to the respective AUX ADC input.

<a id='a03ba7cb-7ade-4bcc-8ded-a43d468d8e3f'></a>

An internal reference buffer provides a full-scale reference for both of the auxiliary ADCs that is equal to the supply voltage for the auxiliary ADCs. An external full-scale reference can be applied to either or both of the AUX ADCs by setting the appropriate bit(s), RefselB for the AUX ADC B and Refsel A for the AUX ADC B in the Register Map. Setting either or both of these bits high will disconnect the internal reference buffer and enable the externally applied reference from the AUX_REF Pin to the respective channel(s).

<a id='e1f105dd-b3a0-4ece-aed6-7f63dc3e1f6a'></a>

Timing for the auxiliary ADCs is generated from a divided down
Rx ADC clock. The divide down ratio is controlled by register
D35 B0, CLK/4 and is used to maintain a maximum clock rate of
20 MHz. By default, CLK/4 is set low dividing the Rx ADC clock
by 2; this is acceptable when running the Rx ADC at rate of
40 MHz or less. At Rx ADC rate greater than 40 MHz, the CLK/4
register bit should be set high and will divide the Rx ADC clock
by 4 to derive the auxiliary ADC Clock. The conversion time,
including setup, takes 16 clock cycles (16 Rx ADC clock cycles);
when CLK/4 is set low, divide by 2 mode, or 32 clock cycles
when CLK/4 is set high.

<a id='52ed9a50-2aee-4026-a99e-ebb69a1e9142'></a>

<::block diagram: Figure 14. Single Tx Timing Block Diagram, Alternative Operation::>
CLKIN input signal branches into two paths:
1. An output labeled "ADC SAMPLE RATE (NOT TO EXCEED 64MHz)"
2. An input to a block labeled "DLL MULT". The DLL MULT block has an input labeled A and an output labeled B. Its internal logic is defined as:
   - 00: B = A
   - 01: B = 2 × A
   - 10: B = 4 × A
The output B from the "DLL MULT" block branches into two paths:
1. An output labeled "DLL OUTPUT RATE (NOT TO EXCEED 128MHz)"
2. An input to a block labeled "CLKOUT2 DIV". The CLKOUT2 DIV block has an input labeled B and an output labeled C. Its internal logic is defined as:
   - 00: C = B
   - 01: C = B/2
   - 10: C = B/4
The output C from the "CLKOUT2 DIV" block branches into two paths:
1. An output labeled "CLKOUT2"
2. An input to a block labeled "INTERP". The INTERP block has an input labeled C and an output labeled D. Its internal logic is defined as:
   - 00: D = C
   - 01: D = 2 × C
   - 10: D = 4 × C
The output D from the "INTERP" block branches into two paths:
1. An output labeled "INPUT Tx DATA RATE (SINGLE CHANNEL)"
2. An output labeled "TxDAC UPDATE RATE SINGLE CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)"

<a id='692f08c5-f9fa-49ef-b49c-3fb753e24d64'></a>

<::block_diagram
CLKIN
|
v
[DLL MULT]
Input: A (from CLKIN)
00: B = A
01: B = 2 × A
10: B = 4 × A
Output: B
|
v
ADC SAMPLE RATE (NOT TO EXCEED 64MHz)
|
v
[CLKOUT2 DIV]
Input: B (from DLL MULT)
00: C = B
01: C = B/2
10: C = B/4
Output: C
|
v
DLL OUTPUT RATE (NOT TO EXCEED 128MHz)
|
v
[2 EDGES]
Input: C (from CLKOUT2 DIV)
0: D = C
1: D = 2 × C
Output: D
|
v
CLKOUT2
|
v
[DUAL CHANNEL FACTOR]
Input: D (from 2 EDGES)
E = D/2
Output: E
|
v
INPUT Tx DATA RATE
|
v
[INTERP]
Input: E (from DUAL CHANNEL FACTOR)
00: F = G
01: F = 2 × G
10: F = 4 × G
Output: F
|
v
INPUT TX DATA RATE EACH CHANNEL
|
v
TxDAC UPDATE RATE EACH CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)
::>
Figure 15. Dual Tx Timing Block Diagram, Alternative Operation

<a id='6da0e656-c045-4686-959d-ed911d793461'></a>

-30-

<a id='b3b698df-8522-4f60-aca4-969ac2161baa'></a>

REV. 0