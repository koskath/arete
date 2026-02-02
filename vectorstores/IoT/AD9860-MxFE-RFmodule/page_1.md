<a id='35ae14e4-b1e9-4819-8328-576ffede1d65'></a>

<::logo: Analog Devices
ANALOG DEVICES
A black square with a white play symbol to the left of the company name.::>

<a id='5593fc71-db36-4a04-bd21-744d7cbcfade'></a>

Mixed-Signal Front-End (MxFE™) Processor
for Broadband Communications

<a id='c75f2f96-1355-43a7-998c-683b62c1c83d'></a>

AD9860/AD9862*

<a id='e27324dd-7066-4663-a3e4-8e0671f08a9f'></a>

## FEATURES

Mixed-Signal Front-End Processor with Dual Converter Receive and Dual Converter Transmit Signal Paths

**Receive Signal Path Includes:**
*   Two 10-/12-Bit, 64 MSPS Sampling A/D Converters with Internal or External Independent References,
*   Input Buffers, Programmable Gain Amplifiers,
*   Low-Pass Decimation Filters, and a Digital Hilbert Filter

**Transmit Signal Path Includes:**
*   Two 12-/14-Bit, 128 MSPS D/A Converters with
*   Programmable Full-Scale Output Current, Channel
*   Independent Fine Gain and Offset Control, Digital
*   Hilbert and Interpolation Filters, and Digitally Tunable
*   Real or Complex Up-Converters

Delay-Locked Loop Clock Multiplier and Integrated Timing Generation Circuitry Allow for Single Crystal or Clock Operation

Programmable Output Clocks, Serial Programmable Interface, Programmable Sigma-Delta, Three Auxiliary DAC Outputs and Two Auxiliary ADCs with Dual Multiplexed Inputs

<a id='8451eb28-d64d-49ec-8798-c283c8e0b739'></a>

## **APPLICATIONS**

**Broadband Wireless Systems**
*   Fixed Wireless, WLAN, MMDS, LMDS

**Broadband Wireline Systems**
*   Cable Modems, VDSL, PowerPlug

**Digital Communications**
*   Set-Top Boxes, Data Modems

<a id='1325ccd9-dc53-41fe-94c0-983e7fd17312'></a>

**GENERAL DESCRIPTION**
The AD9860 and AD9862 (AD9860/AD9862) are versatile
integrated mixed-signal front-ends (MxFE) that are optimized
for broadband communication markets. The AD9860/AD9862
are cost effective, mixed signal solutions for wireless or wireline
standards based or proprietary broadband modem systems where
dynamic performance, power dissipation, cost, and size are all
critical attributes. The AD9860 has 10-bit ADCs and 12-bit DACs;
the AD9862 has 12-bit ADCs and 14-bit DACs.

<a id='19a92872-9ad3-49ea-9087-6ee3f072367f'></a>

The AD9860/AD9862 receive path (Rx) consists of two channels
that each include a high performance, 10-/12-bit, 64 MSPS analog-
to-digital converter (ADC), input buffer, Programmable Gain
Amplifier (RxPGA), digital Hilbert filter, and decimation filter. The
Rx can be used to receive real, diversity, or I/Q data at baseband or
low IF. The input buffers provide a constant input impedance for
both channels to ease impedance matching with external com-
ponents (e.g., SAW filter). The RxPGA provides a 20 dB gain

<a id='5edc5d1c-8c08-4bfb-b594-77fc638d8a49'></a>

*Protected by U.S.Patent No. 5,969,657.MxFE is a trademark of Analog Devices, Inc.

<a id='e64f8368-4a3b-4194-b168-700eb082b43f'></a>

REV. 0

<a id='8aa11499-7696-4398-bd04-4ba4efcfa46e'></a>

Information furnished by Analog Devices is believed to be accurate and reliable. However, no responsibility is assumed by Analog Devices for its use, nor for any infringements of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of Analog Devices.

<a id='0d23c9ca-8fd4-4b73-b37d-874c025d3026'></a>

FUNCTIONAL BLOCK DIAGRAM

<::Functional Block Diagram: AD9860/AD9862

Inputs (Left Side):
VIN+A, VIN-A connect to a 1x gain block, then PGA, then ADC, which feeds into a BYPASSABLE LOW-PASS DECIMATION FILTER. This filter connects to a HILBERT FILTER, which then feeds a multiplexer for RxA DATA [0:11].
VIN+B, VIN-B connect to a 1x gain block, then PGA, then ADC, which feeds into a multiplexer for RxB DATA [0:11]. This multiplexer also receives a LOGIC LOW input.
SIGDELT connects to a Σ-Δ block.
AUX_DAC_A, AUX_DAC_B, AUX_DAC_C each connect to an AUX DAC block.
AUX_ADC_A1, AUX_ADC_A2 connect to an AUX ADC block.
AUX_ADC_B1, AUX_ADC_B2 connect to another AUX ADC block.
IOUT+A, IOUT-A connect to a PGA, then a DAC, which feeds into a BYPASSABLE DIGITAL QUADRATURE MIXER. This mixer also receives input from a BYPASSABLE LOW-PASS INTERPOLATION FILTER (with FS/4, FS/8 options).
IOUT+B, IOUT-B connect to a PGA, then a DAC, which feeds into another BYPASSABLE DIGITAL QUADRATURE MIXER. This mixer also receives input from the BYPASSABLE LOW-PASS INTERPOLATION FILTER and an NCO.

Central Blocks:
SPI REGISTERS connect to an SPI INTERFACE.
Rx PATH TIMING and Tx PATH TIMING feed into a CLOCK DISTRIBUTION BLOCK. This block connects to a DLL (1x, 2x, 4x), which outputs to OSC1 and OSC2. The CLOCK DISTRIBUTION BLOCK also outputs CLKOUT1 and CLKOUT2.

Outputs (Right Side):
RxA DATA [0:11] is output from a multiplexer fed by the HILBERT FILTER.
RxB DATA [0:11] is output from a multiplexer fed by the ADC path and LOGIC LOW.
SPI INTERFACE is connected to SPI REGISTERS.
OSC1, OSC2 are outputs from the DLL.
CLKOUT1, CLKOUT2 are outputs from the CLOCK DISTRIBUTION BLOCK.
Tx DATA [0:13] is output from a multiplexer, which is fed by a HILBERT FILTER. This HILBERT FILTER is fed by the two BYPASSABLE DIGITAL QUADRATURE MIXERS.::>

<a id='0cbffbc4-ceae-43a4-ad00-62990c9df5aa'></a>

range for both channels. The output data bus can be multi-
plexed to accommodate a variety of interface types.

<a id='1bace24c-885f-4263-8bca-89c1c73ed8dc'></a>

The AD9860/AD9862 transmit path (Tx) consists of two chan-
nels that contain high performance, 12-/14-bit, 128 MSPS
digital-to-analog converters (DAC), programmable gain amplifiers
(TxPGA), interpolation filters, a Hilbert filter, and digital mixers
for complex or real signal frequency modulation. The Tx latch
and demultiplexer circuitry can process real or I/Q data. Interpo-
lation rates of 2× and 4× are available to ease requirements on
an external reconstruction filter. For single channel systems, the
digital Hilbert filter can be used with an external quadrature
modulator to create an image rejection architecture. The two
12-/14-bit, high performance DACs produce an output signal
that can be scaled over a 20 dB range by the TxPGA.

<a id='f9a6b0cd-ae5a-4f16-88d0-ab452fef940d'></a>

A programmable delay-locked loop (DLL) clock multiplier and integrated timing circuits enable the use of a single external reference clock or an external crystal to generate clocking for all internal blocks and also provides two external clock outputs. Additional features include a programmable sigma-delta output, four auxiliary ADC inputs and three auxiliary DAC outputs. Device programmability is facilitated by a serial port interface (SPI) combined with a register bank. The AD9860/AD9862 is available in a space saving 128-lead LQFP.

<a id='48444cae-9227-4565-93d9-aa11783d4b70'></a>

One Technology Way, P.O. Box 9106, Norwood, MA 02062-9106, U.S.A.
Tel: 781/329-4700
Fax: 781/326-8703
www.analog.com
© Analog Devices, Inc., 2002