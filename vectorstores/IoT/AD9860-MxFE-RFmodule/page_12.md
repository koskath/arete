<a id='e54a49c8-4ecc-4b89-88fa-1f2cad022b5b'></a>

AD9860/AD9862

<a id='8a281645-37c7-4b9d-93ba-b4b3d2784585'></a>

REGISTER BIT DEFINITIONS
REGISTER 0: GENERAL

<a id='301e7be7-64cb-471f-8128-a41ee39e93ea'></a>

**BIT 7: SDIO BiDir (Bidirectional)**
Default setting is low, which indicates SPI serial port uses dedicated input and output lines (i.e., 4-wire interface), SDIO and SDO Pins, respectively. Setting this bit high configures the serial port to use the SDIO Pin as a bidirectional data pin.

<a id='9e679741-72c6-4baa-9132-cc027f7b8dd4'></a>

**BIT 6: LSB First**
Default setting is low, which indicates MSB first SPI Port Access
Mode. Setting this bit high configures the SPI port access to
LSB first mode.

<a id='b90105a3-1449-4133-8d4a-c7bfe9b16a1d'></a>

**BIT 5: Soft Reset**
Writing a high to this register resets all the registers to their default values and forces the DLL to relock to the input clock. The Soft Reset Bit is a one shot register and is cleared immediately after the register write is completed.

<a id='406abcda-d272-406e-a542-a3f59ccfc9c4'></a>

**REGISTER 1: Rx PWRDWN**
**BIT 7: VREF, diff (Power-Down)**
Setting this bit high will power down the ADC's differential
references (i.e., REFT and REFB).

<a id='f197e1f8-fcbb-47fb-8067-d2142700e196'></a>

**BIT 6: VREF (Power-Down)**
Setting this register bit high will power down the ADC reference circuit (i.e., VREF).

<a id='8d5a3dd2-047b-4343-b87f-d550b3d425e0'></a>

**BIT 5: Rx Digital (Power-Down)**
Setting this bit high will power down the digital section of the
receive path of the chip. Typically, any unused digital blocks are
automatically powered down.

<a id='bb7dc2a3-eb49-42b9-94cc-2470933ab11d'></a>

BIT 4/3: Rx Channel B/Rx Channel A (Power-Down)
Either ADC or both ADCs can be powered down by setting the appropriate register bit high. The entire Rx channel is powered down, including the differential references, input buffer, and the internal digital block. The bandgap reference remains active for quick recovery.

<a id='c4e2b612-97d1-43dd-ae88-6d10416f8a80'></a>

**BIT 2/1: Buffer B/Buffer A (Power-Down)**
Setting either of these bits high will power down the input buffer
circuits for the respective channel. The input buffer should be
powered down when bypassed. By default, these bits are low and
the input buffers are enabled.

<a id='b33a7bed-a93a-4719-92f3-ffb9162dbe3c'></a>

BIT 0: All Rx (Power-Down)
Setting this bit high powers down all circuits related to the receive path.

<a id='8a976f26-049b-4bdc-87bd-fba305aeb362'></a>

**REGISTER 2/3: Rx A/Rx B**
**BIT 7: Bypass Buffer A/Bypass Buffer B**
Setting either of these bits high will bypass the respective input buffer circuit. When the buffer is bypassed, the input signal is routed directly to the switched capacitor SHA input of the RxPGA. When operating with buffer bypassed, it should be powered down.

<a id='46c2e5ec-1b6a-4554-baff-da9def4648c1'></a>

BIT 0–4: RxPGA A/RxPGA B
These 5-bit straight binary registers (Bit 0 is the LSB, Bit 4 is the MSB) provide control for the programmable gain amplifiers in the dual receive paths. A 0 dB to 20 dB gain range is accomplished through a switched capacitor network with fast settling of a few clock cycles. The step size is approximately 1 dB. The register default setting is minimum gain or hex00. The maximum setting for these registers is hex14.

<a id='24455a63-f960-4c1e-b792-eed659e8a981'></a>

REGISTER 4: Rx MISC
BIT 2: HS (High Speed) Duty Cycle
Setting this bit high optimizes duty cycle of the internal ADC
sampling clock. It is recommended that this bit be set high in

<a id='ee23547d-205b-4e96-99ea-c7233adaad72'></a>

high speed applications when clock duty cycle affects noise and distortion performance the most. This bit should be set high in conjunction with Clk Dut Enable register bit.

<a id='a5fe14d5-e25c-478c-8b5c-60b47d12c170'></a>

**BIT 1: Shared Ref**
Setting this bit high forces the dual receive ADCs into a mode
to share their differential references to provide superior gain
matching. When this option is enabled, the REFT of Channel A
and Channel B should be connected together off-chip and the
REFB of both channels should be connected.

<a id='c300f610-5f73-419d-93cb-484329b1a97c'></a>

**BIT 0: Clk Duty**
Setting this bit high enables an on-chip duty cycle stabilizer (DCS) circuit to generate the internal clock for the Rx block. This option is useful for adjusting for high speed input clocks with skewed duty cycle. The DCS Mode can be used with ADC sampling frequencies over 40 MHz.

<a id='f491772d-79fa-4f79-bc8e-8c747c941c92'></a>

REGISTER 5: Rx I/F (INTERFACE)
BIT 4: Three-state
Setting this bit high will force both Rx data output buses, including
the RxSYNC Pin, into a three-state mode.

<a id='9f8347e2-768c-4d74-bdd5-1e3acf653633'></a>

**BIT 3: Rx Retime**
The Rx path can use either of the clock outputs, CLKOUT1 or CLKOUT2, to latch the Rx output data. Since CLKOUT1 and CLKOUT2 have slight phase offsets, this provides some timing flexibility with the interface. By default, this bit is low and the Rx output latches use CLKOUT1. Setting this bit will force the Rx output latches to use CLKOUT2.

<a id='1d20b108-9243-4d60-a3d5-693a61e95715'></a>

BIT 2: Twos Complement
Default data format for the Rx data is straight binary. Setting this
bit high will generate two's complement data.

<a id='8b6df124-01d4-42b8-a60b-ed9cd1f0c125'></a>

**BIT 1: Inv RxSync**
When the receive data is multiplexed onto one data port (i.e., Mux Mode Enabled), the RxSYNC Pin can be used to decode which channel generated the current output data at the active port. Default condition is that RxSYNC is high when Channel A is at the output and is low when Channel B is at the output. Setting this bit high reverses this synchronization.

<a id='343e0df9-85c0-4198-b9b0-6244fd31728a'></a>

**BIT 0: Mux Out**
Setting this bit high enables the Rx Mux Mode. Default setting is low, which is Dual Port Mode, (i.e., non Rx Mux Mode). When in Rx Mux Mode, both Rx channels share the same output data bus, pins D0A to D9A (for AD9860) or D0A to D11A (for AD9862). The other Rx output bus (pins D0B to D9B or D0B to D11B) outputs a low logic.

<a id='c2a58723-de43-4e5a-aed8-ecd18445c340'></a>

**REGISTER 6: Rx Digital**
**BIT 3: 2 Channel**
Setting this bit low disables the Rx B output data port (pins D0B to D9B or D11B), forcing the output pins to zero. By default, the bit is high and both data paths are active.

<a id='289775c7-e21f-4218-abc0-f58055b8ca75'></a>

**BIT 2: Keep –ve**
This bit selects whether the receive Hilbert filter will filter positive or negative frequencies, assuming the filter is enabled. By default this bit is low, which passes positive frequencies. Setting this bit high will configure the filter to pass negative frequencies.

<a id='c1d38e18-a1ca-4e04-879f-455d62e2d96c'></a>

**BIT 1: Hilbert**
This bit enables or disables the Hilbert filter in the receive path.
By default, this bit is low, which disables the receive Hilbert filter.
Setting this bit high enables the receive Hilbert filter.

<a id='e966a5d5-88f6-4417-b82b-8420b0d91158'></a>

**BIT 0: Decimate**
This register enables or disables the decimation filters. By default,
the register setting is low and the decimation filter is disabled.

<a id='b5cb3c27-0646-43f2-9772-54923d2637b3'></a>

REV. 0

<a id='4516fc44-fc76-4ecb-a4e6-96632e183101'></a>

-13-