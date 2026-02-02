<a id='098c3b09-f02f-482c-bfbb-1a36f4a38b7c'></a>

AD9860/AD9862
The output will be latched using some configuration of CLKOUT1 or CLKOUT2 edges as defined in the Clock Overview section of the data sheet. The Rx path available options include bypassing the input buffer, RxPGA control and using the decimation filter.

<a id='03caf980-4fd6-4a9c-8651-780202840b77'></a>

The input buffer description above explains the conditions under which the buffer should be bypassed.

<a id='bd2a5374-d6bd-4bed-ada8-6bd355bac85b'></a>

If the input signal, or the undersampled alias signal for the IF sampling case, falls below 40% of the ADC Nyquist rate, the decimation filter can be enabled to suppress out-of-band noise and spurious signals by 40 dB or more. With the decimation filter enabled the SNR of the Rx path improves by about 2.3 dB.

<a id='a42d5229-d5b0-4037-86c2-9e831152075f'></a>

**Dual Channel Complex ADC Signal**
The Dual Channel Complex ADC Signal mode is used to receive
baseband I and Q signals or a single sideband signal at some IF.
In this mode, a complex input signal is generated from an external
quadrature demodulator. The in-phase channel (I channel) is
connected to VIN+A and VIN-A, and the Quadrature Data
(Q channel) is connected to the VIN+B and VIN-B differential
pins. The Rx path available options include bypassing the input
buffer, RxPGA control, the decimation filter, and using the digital
Hilbert filter. Shared Reference mode is also discussed below.

<a id='a94aab3b-c15c-4adb-a336-eadddd74d178'></a>

The RxPGA provides 0 dB to 20 dB gain control for both chan-
nels. The input buffer description above explains the conditions
under which the buffer should be bypassed.

<a id='355e543b-86bd-4e9b-8f46-7e08e54f24ea'></a>

If the input signal, or the undersampled alias signal for the IF sam-
pling case, falls below 40% of the ADC Nyquist rate, the decimation
filter can be enabled to suppress out-of-band noise and spurious
signals by 40 dB or more. With the decimation filter enabled,
the SNR of the Rx path improves by about 2.3 dB.

<a id='5a1360e0-29ae-4f14-91c0-d0635e42f0b5'></a>

A digital Hilbert filter can be enabled to provide a receive image rejection architecture on-chip. The digital Hilbert filter combines the I data and a phase shifted version of the Q data to produce a single combined Rx signal. The filter can provide 50 dB image suppression in the pass band (less than 0.1 dB ripple). The pass band of the filter is from 25% to 75% of Nyquist rate of the data entering the Hilbert filter. Note, the Hilbert filter's maximum input data rate is 32 MSPS, at ADC rates above 32 MSPS. The decimation filter is required to reduce the data rate. With the decimation filter also enabled, the pass band of the Hilbert filter will be 12.5% to 37.5% of the ADC Nyquist rate (still 25% to 75% of the Nyquist rate of the data entering the Hilbert filter).

<a id='b6c6ae5a-68a5-4970-98a3-bae2f8248a67'></a>

An optional Shared Reference mode allows the user to connect the
differential references from the dual ADC together externally for
superior gain matching performance. To enable the Shared Ref-
erence mode, the Shared Ref register (d4, b1) should be set high.

<a id='c6c1e580-3ca1-4732-b8e2-bc4fb54ebc99'></a>

TIMING GENERATION BLOCK
The AD9860/AD9862 Timing Generation block uses a single external clock reference to derive all internal clocks to operate the transmit and receive channels. The input clock reference can consist of either an external single ended clock applied to the OSC1 pin, with the OSC2 pin left floating or an external crystal connected between the clock input pins (OSC1 and OSC2).

<a id='c50b8a15-e1c2-4e34-8147-7ffa8aba03cd'></a>

By default, the AD9860/AD9862 can accept either an external reference clock or a crystal to generate the input clock. The internal oscillator, if not used, should be disabled by setting the Input Control Clock register. The OSC1 input impedance is a relatively high resistive impedance (typically, about 500 KΩ).

<a id='489d7864-eca1-4802-ac6b-b2e076f82a8b'></a>

An internal Delay Lock Loop (DLL) based clock multiplier pro-
vides a low noise, 2× or 4× multiplication of the input clock over
an output frequency range of 32 MHz to 128 MHz. The DLL
Fast register should be used to optimize the DLL performance.
For DLL output frequencies between 32 MHz and 64 MHz, this
bit should be set low. For output frequencies between 64 MHz
to 128 MHz, the Fast bit should be set high (for a 64 MHz out-
put frequency, the register can be set either high or low). The DLL
can be bypassed by setting a 1× multiplication factor in the DLL
Multiplier register. The DLL can be powered down when it is
bypassed for power savings by setting the DLL PwrDwn register.

<a id='327cb9ec-66ff-40b6-87ab-9e5a6133c743'></a>

For applications where an external crystal is desired, the AD9860/
AD9862 internal oscillator circuit and the DLL clock multiplier
enable a low frequency, lower cost quartz crystal to be used to
generate the input reference clock. The quartz crystal would be
connected between the OSC1 and OSC2 pins with parallel
resonant load capacitors as specified by the crystal manufacturer.

<a id='192cd3a2-6f75-41d9-80a9-a62f36af122f'></a>

An internal Duty Cycle Stabilizer (DCS) can be enabled on the
AD9860 by setting the Clk Duty register. This provides a stable
50% duty cycle to the ADC for high speed clock rates between
40 MSPS to 64 MSPS when proper duty cycle is more critical.

<a id='e0bd9614-d155-418c-9592-acba9c3c509a'></a>

**System Clock Distribution Circuitry** There are many variables involved in the timing distribution. External variables include CLKIN, CLKOUT1, CLKOUT2, Rx Data Rate, Tx Data Rate. Internal variables include ADC conversion rate, DAC update rate, interpolation rate, decimation rate, Rx data multiplexing and Tx data demultiplexing. Many of these parameters are interrelated and based on CLKIN. Optimal power versus performance and ease of integration options can be chosen to suit a particular application.

<a id='07af821b-1be2-49da-9aa5-dfd5441968ce'></a>

<::block diagram: Normal Operation Timing Block Diagram. The diagram shows two main data paths (Rx and Tx) and a clock path, with a legend indicating solid lines for CLOCK PATH and dashed lines for DATA PATH. The diagram's components are as follows:1. Rx Data Path (Top):  - An ADC (Analog-to-Digital Converter) feeds into a block labeled "NO DECIMATION, ↓2" which represents a filter. This filter is controlled by "DECIMATE: REG D6 B0".  - The output of the filter goes to a "DATA MUX AND LATCH" block.  - The output of the "DATA MUX AND LATCH" is "Rx DATA [0:23]". Associated controls are "MUX OUT: REG D5 B0" and "Rx RETIME: REG D5 B3".2. Tx Data Path (Bottom):  - A DAC (Digital-to-Analog Converter) feeds into a block labeled "NO INTERP ↑2, ↑4" which represents a filter. This filter is controlled by "INTERPOLATION: REG D19 B0, 1".  - The output of the filter goes to a "DATA LATCH AND DEMUX" block.  - The output of the "DATA LATCH AND DEMUX" is "Tx DATA [0:13]". Associated controls are "2 DATA PATHS: REG D19 B4", "Q/I ORDER: REG D18 B5", and "Tx RETIME: REG D18 B6".3. Clock Path (Horizontal and branching):  - An input labeled "CLKIN" splits into two paths:    - Upper path: A "DIV" block with input options "1x, 1/2x". Its output is "CLKSEL".      - "CLKSEL" connects to the ADC.      - "CLKSEL" also connects to an "INV" (Inverter) block, labeled "NO INVERSION, INVERT", which is controlled by "INV1: REG D25 B1". The output of this inverter is "CLKOUT1".    - Lower path: A "DIV" block with input options "1x, 1/2x". It is controlled by "ADC DIV2: REG D24 B5".      - The output of this DIV block feeds into a "DLL" (Delay-Locked Loop) block with input options "1x, 2x, 4x". It is controlled by "DLL MULTIPLIER: REG D24 B3, 4".      - The output of the DLL splits into two paths:        - One path goes to another "DIV" block with input options "1x, 1/2x, 1/4x". It is controlled by "CLKOUT2 DIV FACTOR: REG 25 B6, 7".        - The other path goes to an "INV" (Inverter) block, labeled "NO INVERSION, INVERT", which is controlled by "INV2: REG D25 B5". The output of this inverter is "CLKOUT2".::>Figure 8. Normal Operation Timing Block Diagram

<a id='f1103d68-c9f6-4b85-bd58-c7d8fcb51ea6'></a>

One of two possible timing operation modes can be selected. The typical timing mode is called Normal Operation mode; a block diagram is shown in Figure 8. The other mode is called Alternative Operation mode, and a block diagram is shown in Figure 12.

<a id='36004a1d-a83f-4bcf-b343-17b696a88032'></a>

-24-

<a id='a8bdb07f-efdc-4bfd-991b-f614b9904693'></a>

REV. 0