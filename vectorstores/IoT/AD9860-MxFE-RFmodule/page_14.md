<a id='f3ed6536-ce46-410c-b01c-0f62e3b0afe5'></a>

AD9860/AD9862

<a id='71746118-aa62-480b-bf1b-a6111a32e450'></a>

**BIT 5: Q/I Order**
This register indicates the order of received complex transmit
data. By default this bit is low, representing I data preceding
Q data. Alternatively, if this bit is set high, the data format is
defined as Q data preceding I data.

<a id='56c164ea-f8c8-4f9e-becb-ee945c26ab68'></a>

BIT 4: Inv TxSync
This register identifies how the first and second data sets are identified in a complex data set using the TxSYNC bit. By default this bit is low, and TxSYNC low indicates the first data set is at the Tx port; TxSYNC high indicates the second data set is at the Tx port. Setting this bit high inverts the TxSYNC bit. TxSYNC high indicates the first of the data set, and TxSYNC low indicates the second of the data set.

<a id='c41bb38b-f9f4-4fe3-8da4-d73494e2d155'></a>

BIT 3: Twos Complement
The default data format for Tx data is straight binary. Set this bit high when providing twos complement Tx data.

<a id='1aa08c49-30da-4f23-a8d4-8d00f4d14d4b'></a>

**BIT 2: Inverse Sample**
By default, the transmit data is sampled on the rising edge of the
CLKOUT. Setting this bit high will change this, and the transmit
data will be sampled on the falling edge.

<a id='15e590f3-86e0-4d78-88ac-cb3c65400723'></a>

**BIT 1: 2 Edges**
If the CLKOUT rate is running at half the interleaved data rate, both edges of the CLKOUT must latch transmit data. Setting this bit high allows this clocking configuration.

<a id='d40d3a05-945d-483c-b614-c5e600f78967'></a>

**BIT 0: Interleaved**
By default, the AD9860/AD9862 powers up in single DAC
operation. If dual transmit data is to be used, the interleaved data
option needs to be enabled by setting this bit high.

<a id='920af05c-4b62-4cab-9c37-d18b74c73732'></a>

**REGISTER 19: Tx DIGITAL**
**BIT 4: 2 Data Paths**
Setting this bit high enables both transmit digital paths. By default, this bit is low and the transmit path utilizes only a single channel.

<a id='520ab467-8b7f-453a-bb39-e92b0abbdffd'></a>

**BIT 3: Keep -ve**
This bit configures the Tx Hilbert filter for either positive or negative frequencies pass band, assuming it is enabled. By default this bit is low, which selects the positive frequencies. Setting this bit high will setup the Hilbert filter to pass negative frequencies.

<a id='ae7b57ce-2625-4db3-8001-1b1b45f98205'></a>

**BIT 2: Hilbert**
This bit enables or disables the Hilbert filter in the transmit path.
By default, this bit is low, which disables the transmit Hilbert
filter. Setting this bit high enables the transmit Hilbert filter.

<a id='c5b37df1-ee0a-40c6-a1c1-8b0b9d794a63'></a>

**BIT 1,0: Interpolation Control**
These register bits control the interpolation rate of the transmit path. Default settings are both bits low, indicating that both interpolation filters are bypassed. The MSB and LSB are address D19, Bits 1 and 0, respectively. Setting binary 01 provides an interpolation rate of 2×; binary 10 provides an interpolation rate of 4×.

<a id='87a1452d-b674-4213-a27e-fcb5a757370f'></a>

**REGISTER 20: Tx MODULATOR**

**BIT 5: Negative Fine Tune**
When this bit is low (default), the Numerically Controlled Oscillator (NCO) provides positive shifts in frequency, assuming fine modulation is enabled. Setting this bit high will use a negative frequency shift in the Fine Complex Modulator.

<a id='516ae8e6-6b6f-43b5-af4b-3138fb01e40f'></a>

**BIT 4: Fine Mode**
By default, the NCO and fine modulation stage are bypassed. Setting this bit high will enable the use of the digital complex modulator, enabling tuning with the NCO.

<a id='144dc309-f7de-4325-bb6e-015a0fc8b9f1'></a>

**BIT 3: Real Mix Mode**
This bit determines if the coarse modulation (controlled by register Coarse Modulation, will perform a separate real mix on each channel or a complex mix using the dual channel data. By default, this bit is set low and a complex mix will be performed. Setting this bit high will enable the Real Mix mode. Note, the Fine Modulator Block only performs complex mixing.

<a id='daa7b36e-5979-4f74-9d62-7ae856a7b101'></a>

**BIT 2: Negative Coarse Tune**
When this bit is low (default), the coarse modulator provides positive shifts in frequency. Setting this bit high will shift the coarse modulator processed data negative in frequency.

<a id='21c96319-72ba-4e50-9826-4d7f34e83059'></a>

**BIT 1,0: Coarse Modulation**
These bits control what coarse modulation processing will be performed on the transmit data. A setting of binary 00 (default) will bypass the modulation block, a setting of binary 01 will shift the transmit data by f_DAC/4, and a setting of binary 10 will shift the transmit data by f_DAC/8.

<a id='15a74aae-e8ce-4c48-b59a-98c60bb2d427'></a>

REGISTER 21/22/23: NCO TUNING WORD
FTW [23:0]
These three registers set the 24-bit frequency tuning word (FTW) for the NCO in the fine modulator stage of the Tx path. The NCO full-scale tuning word is straight binary and produces a frequency equivalent to fDAC/4 with a resolution of fDAC/2^26.

<a id='af316e7a-1a7b-4d14-93c1-983fee347e47'></a>

REGISTER 24: DLL
BIT 6: Input Clock Control
This bit defines what type of clock will be driving the AD9860/
AD9862. The default state is low, which allows either crystal con-
nected to OSC1 and OSC2 or single-ended reference clock driving
OSC1 to drive the internal timing circuits. If a crystal will not be
used, the internal oscillator should be disabled after power-up
by setting this bit high.

<a id='7208e965-53e0-41d6-a68c-8e727c2b7212'></a>

**BIT 5: ADC Div2**
By default, the ADC is driven directly by the input clock in Normal Timing Operation mode or the DLL output in the Alternative Timing Operation mode. Setting this bit high will clock the ADC at one half the previous clock rate. This is described further in the timing section.

<a id='0d2a0b4b-cd62-47a8-924c-706a367c76be'></a>

BIT 4,3: DLL Multiplier
These bits control the DLL multiplication factor. A setting of binary 00 will bypass the DLL, a setting of binary 01 will multiply the input clock by 2, and a setting of binary 10 will multiply the input clock by 4. Default mode is defined by Mode/TxBlank logic level at power-up or RESET, which configures either Normal Operation Timing mode or Alternative Timing mode. In Alternative Timing mode, the DLL will lock to 4× multiplication factor (the DLL FAST register remains low by default). If the Mode/TxBlank pin is low, by default the DLL will be bypassed and a 1× clock is used internally.

<a id='e75cbcfb-f505-4f28-be07-6aca6af0e5d8'></a>

**BIT 2: DLL Power-Down**
Setting this register bit high forces the CLK IN multiplier to a power-down state. This mode can be used to conserve power or to bypass the internal DLL. To operate the AD9860/AD9862 when the DLL is bypassed, an external clock equal to the fastest on-chip clock is supplied to the OSC pin(s).

<a id='f48e9bbf-65bd-4d42-a03f-93aabac8f769'></a>

**BIT 0: DLL FAST**
The DLL can be used to generate output frequencies between 32 MHz to 128 MHz. Because of the large range of locking fre-quencies allowed, the DLL is separated into two output frequency ranges, a "slow" range between 32 MHz to 64 MHz and a "fast" range starting at frequencies above 64 MHz to 128 MHz. By

<a id='fcce0517-32ab-4681-84fb-74149f102b6d'></a>

REV. 0

<a id='dfe3f871-5f79-40a1-a489-bd1043a861ef'></a>

-15-