<a id='50a519c7-6b66-4015-95db-9adac27b4e51'></a>

AD9860/AD9862

<a id='a0b584ec-71ed-4598-9bfb-3db21972253a'></a>

## Blank Registers
Blank registers, i.e., the registers with 0 settings and no indicated function, are placeholders used throughout the register map for spacing the AD9860/AD9862 control bits in a logic fashion and, potentially can be used for future development. A low should always be written to these registers if a write needs to take place.

<a id='d4feb441-77b9-4067-a901-ddb6c5ca3911'></a>

## SERIAL PORT INTERFACE
The Serial Port Interface (SPI) is used to write to and read from the AD9860/AD9862 internal programmable registers. The serial interface uses four pins: SEN, SCLK, SDIO, and SDO by default. SEN is a serial port enable pin, SCLK is the serial clock pin, SDIO is a bidirectional data line and SDO is a serial output pin.

<a id='34592307-0233-4ef9-ac09-dbdf307e8776'></a>

SEN is an active low control gating read and write cycles. When
SEN is high, SDO and SDIO are three-stated.

<a id='59b5d41b-bfba-4e1b-9ce2-4dc58a383218'></a>

SCLK is used to synchronize SPI read and writes at a maximum
bit rate of 16 MHz. Input data is registered on the rising edge and
output data transitions on the falling edge. During write opera-
tions, the registers are updated after the 16th rising clock edge
(and 24th rising clock edge for the dual byte case). Incomplete
write operations are ignored.

<a id='d8722369-8181-4de5-b453-ce213e9f2332'></a>

SDIO is an input only by default. Optionally, a 3-pin interface may be configured using the SDIO for both input and output operations and three-stating the SDO pin (see SDIO BiDir register).

<a id='d4fcc488-7a2c-4459-9da1-deb60018ebfe'></a>

SDO is a serial output pin used for read back operations in 4-wire mode and is three-stated when SDIO is configured for bidirectional operation.

<a id='d0de0cea-7a64-4386-b481-7da96b9d4516'></a>

## Instruction Header
Each SPI read or write consists of an instruction header and data. The instruction header is made up of an 8-bit word and is used to set up the register data transfer. The 8-bit word consists of a read/not write bit, R/nW (the MSB), followed by a double/not single bit (2/n1) and the 6-bit register address.

<a id='6a1b0b54-c756-4604-9e65-8723a78a49e9'></a>

### Write Operations
The SPI write operation uses the instruction header to configure a one or two register write using the 2/n1 bit. The instruction byte followed by the register data, is written serially into the device through the SDIO pin on rising edges of the interface clock at SCLK. The data can be transferred MSB first or LSB first depending on the setting of the LSB First register.

<a id='496b94a7-b0cc-4b23-9ea2-5c7463f6645a'></a>

Figure 1 includes a few examples of writing data into the device.
Figure 1a shows a write using 1 Byte and MSB First mode set;
Figure 1b shows an MSB first, 2 Byte write; and Figure 1c
shows an LSB first, 2 Byte write. Note the differences between
LSB and MSB First modes: instruction header and data are
reversed, and in 2 Byte writes, the first data byte is written to
the address in the header, N and the second data byte is written
to the n-1 address. In LSB First mode, the first data byte is still
written to the address in the instruction header, but the second
data byte is written to the N+1 address.

<a id='9fe989bd-89da-4083-b481-b567f2a1b1ab'></a>

<::Timing diagram showing three signals: SEN, SCLK, and SDIO. From left to right:  SEN is initially high, then goes low, and stays low for a period, then goes high again.  SCLK is initially labeled "DON'T CARE", then shows a series of clock pulses (low-high-low transitions), and finally is labeled "DON'T CARE" again.  SDIO is initially labeled "DON'T CARE". After a period, it shows "R/nW", followed by "2/n1". Then, it shows a sequence of address bits "A5", "A4", "A3", "A2", "A1", "A0", which are grouped under the label "INSTRUCTION HEADER". This is followed by data bits "D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0", which are grouped under the label "REGISTER DATA". Finally, SDIO is labeled "DON'T CARE" again.  Various timing parameters are indicated with arrows: tS (setup time for SEN), tDH (data hold time), tDS (data setup time), tLO (SCLK low time), tHI (SCLK high time), tCLK (SCLK period), and tH (hold time for SEN).: timing diagram::>

<a id='a6877631-a1ba-4fb9-82cf-8ddcaabf724f'></a>

<::Timing Diagram: This diagram illustrates the timing sequence for SEN, SCLK, and SDIO signals.  

**Signals:**  
*   **SEN:** An active-low signal, initially high, goes low, then high again after a duration tH.  
*   **SCLK:** A clock signal, initially in a "DON'T CARE" state, then shows a series of square waves (clock pulses), and finally returns to a "DON'T CARE" state.  
*   **SDIO:** A data input/output signal, initially in a "DON'T CARE" state, then shows various data bits, and finally returns to a "DON'T CARE" state.  

**Timing Parameters:**  
*   **tS:** Setup time, from the falling edge of SEN to the rising edge of the first SCLK pulse.  
*   **tDS:** Data setup time.  
*   **tDH:** Data hold time.  
*   **tLO:** Low pulse width of SCLK.  
*   **tHI:** High pulse width of SCLK.  
*   **tCLK:** SCLK period.  
*   **tH:** Hold time, from the rising edge of the last SCLK pulse to the rising edge of SEN.  

**SDIO Data Content:**  
*   The first active segment of SDIO contains "R/nW" followed by "2/n1", then address bits "A5", "A4", "A3", "A2", "A1", and "A0". This entire section is labeled as "INSTRUCTION HEADER (REGISTER N)".  
*   The next segment contains data bits "D7", "D6", "D5", "D4", "D3", "D2", "D1", and "D0". This section is labeled as "REGISTER (N) DATA".  
*   The final active segment contains data bits "D7", "D6", "D5", "D4", "D3", "D2", "D1", and "D0". This section is labeled as "REGISTER (N-1) DATA".  

**Overall Flow:**  
The SEN signal initiates the communication. SCLK provides the clock for data transfer. SDIO carries the instruction header, followed by data for Register N, and then data for Register N-1.  
::>

<a id='9dba47a2-b559-4995-a391-745017ac8d87'></a>

<::timing diagram: The diagram shows three waveforms over time for an SPI write operation. The y-axis labels are SEN, SCLK, and SDIO from top to bottom. The x-axis represents time.

**SEN (Slave Enable):** Starts high, goes low for the duration of the data transfer, and then returns high. Timing parameters t_S (setup time) and t_H (hold time) are indicated relative to SEN's falling and rising edges, respectively.

**SCLK (Serial Clock):** Is initially low, then shows a series of clock pulses (square waves) during the active low period of SEN. Timing parameters t_LO (clock low time), t_HI (clock high time), and t_CLK (clock period) are indicated.

**SDIO (Serial Data Input/Output):** Shows data bits being transmitted synchronously with the SCLK pulses. The data bits are labeled sequentially:
- A0, A1, A2, A3, A4, A5 (part of the "INSTRUCTION HEADER (REGISTER N)")
- 2/n1
- R/nW (Read/Not Write)
- D0, D1, D2, D3, D4, D5, D6, D7 (part of "REGISTER (N) DATA")
- D0, D1, D2, D3, D4, D5, D6, D7 (part of "REGISTER (N+1) DATA")
- "DON'T CARE" at the end.

Timing parameters t_DS (data setup time) and t_DH (data hold time) are indicated relative to the SCLK edges and SDIO data transitions.

Below the SDIO line, three sections are labeled:
1. "INSTRUCTION HEADER (REGISTER N)" encompassing A0 through R/nW.
2. "REGISTER (N) DATA" encompassing the first set of D0-D7.
3. "REGISTER (N+1) DATA" encompassing the second set of D0-D7.

Figure 1. SPI Write Examples a. (top) 1 Byte, MSB First Mode; b. (middle) 2 Byte, MSB First Mode; c. (bottom) 2 Byte, LSB First Mode::>

<a id='97173e5d-f814-46a7-84b6-675e39a60482'></a>

REV. 0

<a id='64c48b21-bc3e-47f2-93c8-cc9409317372'></a>

-17-