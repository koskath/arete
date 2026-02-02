<a id='70c0606f-5c70-4376-ae38-2c6b285b0b4f'></a>

AD9860/AD9862
<::timing diagram: The diagram shows a timing waveform for the AD9860/AD9862 device with four signal lines: SEN, SCLK, SDIO, and SDO. Various timing parameters are indicated.

**SEN signal**: Starts high, goes low for a duration, then returns high.
  - Timing parameters associated with SEN: t_S (setup time before falling edge), t_H (hold time after rising edge).

**SCLK signal**: Starts with "DON'T CARE", then shows a series of clock pulses (square wave), and ends with "DON'T CARE".
  - Timing parameters associated with SCLK: t_LO (low pulse width), t_HI (high pulse width), t_CLK (clock period).

**SDIO signal**: Starts with "DON'T CARE". During the active clock period, it shows the following data bits: R/nW, 2/n1, A5, A4, A3, A2, A1, A0. This entire segment is labeled "INSTRUCTION HEADER (REGISTER N)". It ends with "DON'T CARE".
  - Timing parameters associated with SDIO: t_DS (data setup time to clock edge), t_DH (data hold time from clock edge).

**SDO signal**: Starts with "DON'T CARE". During a later active clock period, it shows the following data bits: D7, D6, D5, D4, D3, D2, D1, D0. This entire segment is labeled "OUTPUT REGISTER DATA". It ends with "DON'T CARE".
  - Timing parameters associated with SDO: t_DV (data valid delay from clock edge).

The timing parameters t_S, t_DS, t_DH, t_LO, t_HI, t_CLK, t_DV, and t_H are shown with arrows indicating their respective durations relative to the signal transitions.::>


<a id='7c6fcac8-0011-4fd5-8a7e-9fdf5c6d1b67'></a>

<::Timing Diagram: This diagram illustrates the timing relationships between three signals: SEN, SCLK, and SDIO.

**Signals and their waveforms:**
- **SEN**: Starts high, transitions low, remains low for a period, then transitions high again.
- **SCLK**: Starts with "DON'T CARE", followed by a series of clock pulses (square wave), and ends with "DON'T CARE".
- **SDIO**: Starts with "DON'T CARE", then presents data in segments: "R/nW", "2/n1", "A5", "A4", "A3", "A2", "A1", "A0", followed by "D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0", and finally "DON'T CARE".

**Timing Parameters:**
- **t_s**: Setup time for SEN (before falling edge).
- **t_DS**: Data setup time for SDIO (before SCLK rising edge).
- **t_DH**: Data hold time for SDIO (after SCLK falling edge).
- **t_LO**: SCLK low pulse width.
- **t_HI**: SCLK high pulse width.
- **t_CLK**: SCLK clock period.
- **t_DV**: Data valid time for SDIO (after SCLK falling edge).
- **t_H**: Hold time for SEN (after rising edge).

**Data Sections on SDIO:**
- The segment from "R/nW" to "A0" is labeled as **INSTRUCTION HEADER**.
- The segment from "D7" to "D0" is labeled as **OUTPUT REGISTER DATA**.
: timing diagram::>

<a id='8ddd37b7-3e8a-493e-95c1-60857323c8c4'></a>

<::Timing Diagram:SEN: Starts high, goes low, then stays low for a period, and finally goes high. t_S indicates the setup time from the falling edge of SEN to the first rising edge of SCLK. t_H indicates the hold time from the last falling edge of SCLK to the rising edge of SEN.SCLK: Initially "DON'T CARE". After SEN goes low, SCLK starts clocking with alternating high and low pulses. t_HI is the high pulse width, t_LO is the low pulse width, and t_CLK is the clock period. Ends with "DON'T CARE".SDIO: Initially "DON'T CARE". Transmits data bits: A0, A1, A2, A3, A4, A5, 2/n1, R/nW. This entire segment is labeled "INSTRUCTION HEADER". t_DS is the data setup time, and t_DH is the data hold time relative to SCLK edges. Ends with "DON'T CARE".SDO: Initially "DON'T CARE". Transmits data bits: D0, D1, D2, D3, D4, D5, D6, D7. This entire segment is labeled "OUTPUT REGISTER DATA". t_DV is the data valid time after the rising edge of SCLK. Ends with "DON'T CARE".::>

<a id='d3ae234e-ae3d-49cf-bdd8-b8f7db987e79'></a>

Figure 2. SPI Read Examples a. (top) 4-Wire Interface, MSB first; b. (middle) 3-Wire Interface, MSB first;
c. (bottom) 4-Wire Interface, LSB first

<a id='801891ae-03e9-462e-83a7-3effa2b04f59'></a>

## Read Operation
The read back of registers is a single data byte operation. The readback can be configured to use three pins or four pins and can be formatted as MSB first or LSB first. The instruction header is written to the device either MSB or LSB first (depending on the mode) followed by the 8-bit output data (appropriately MSB or LSB justified). By default, the output data is sent to the dedicated output pin (SDO). 3-wire operation can be configured by setting the SDIO BiDir register. In 3-wire mode, the SDIO pin will become an output pin after receiving the 8-bit instruction header with a read back request.

<a id='b38d84c0-e9b8-4244-87aa-cbf23b3f12b2'></a>

Figure 2a shows an MSB first, 4-pin SPI read; Figure 2b shows an MSB first, 3-pin read; and Figure 2c shows an LSB first, 4-pin read.

<a id='0df181b8-8779-4908-8b77-a5c0e152d184'></a>

SYSTEM BLOCK DESCRIPTION
The AD9860/AD9862 integrates transmit and receive paths with
digital signal processing blocks and auxiliary features. The auxiliary

<a id='95a873e6-3013-4f86-bb6a-8b7233c5693d'></a>

features include two auxiliary ADCs, a programmable sigma-delta output, three auxiliary DACs, integrated clock circuitry to generate all internal clocks, and buffered output clocks from a single input reference.

<a id='18f73951-862c-4873-b1e6-784b2f9e87bb'></a>

The AD9860/AD9862 system functionality is described in the following four sections: the Transmit Block, Receive Block, Timing Generation Block, and the Auxiliary Function Block. The following sections provide a brief description of the blocks and applications for the four sections.

<a id='f6ba47fa-cfd1-4300-afa5-6c955886a6e9'></a>

## TRANSMIT SECTION COMPONENTS
The transmit block (Tx) accepts and can process real or complex data. The Tx interface is configurable for a variety of data formats and has special processing options such as interpolation and Hilbert filters. A detailed block diagram of the AD9860/AD9862 transmit path is shown in Figure 3. The transmit block diagram is broken into these stages: DAC (Block A), Coarse Modulation (Block B),

<a id='3dedd375-33f7-44dc-81dc-0263c4f998ac'></a>

-18-

<a id='a0767d02-f972-4ccc-97bd-d4e741cd6ba1'></a>

REV. 0