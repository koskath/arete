<a id='25e2e2ce-1b2b-4424-a6bc-fe3453444e38'></a>

AD9860/AD9862

<a id='5f3d30d3-56af-41a2-909c-b66a7d53ed64'></a>

from each to ground. The internal references can also be disabled (powered down) and driven externally to provide a different input voltage range or low drift reference. If an external VREF reference is used, it should not exceed 1.0 V.

<a id='fb1167d0-6066-479b-80d5-9bf12466cc09'></a>

A Shared Reference mode allows the user to connect the differen-tial references from both ADCs together externally for superior gain matching performance. If the ADCs are to function inde-pendently, then the reference can be left separate and will provide superior isolation between the dual channels. Shared Reference mode can be enabled through the Shared Ref register.

<a id='3841db3c-f072-4efe-83cd-02fb09be1ca5'></a>

A power-down option allows the user to power down both ADCs (sleep mode) or either ADC individually to reduce power consumption.

<a id='2e36558f-fd36-482f-a85e-c31664c50994'></a>

## Decimation Stage
For signals with maximum frequencies less than or equal to 3/16 the ADC sampling rate, fADC, the decimate by 2 filter (or half-band filter) can be used to provide on-chip suppression of out-of- band images and noise. When data is present in frequencies greater than 1/4 fADC, the decimate by 2 filter can be disabled by switching the filter out of the circuit. The decimation filter allows the ADC to oversample the input while decreasing the output data rate by half. The two main benefits are a simplification of the input anti-aliasing filter and a slower data interface rate with the external digital ASIC. The decimation filter is an 11 tap filter and suppresses out of band noise by 38 dB.

<a id='9d0415d4-7fcd-4e50-b498-f7a52887c601'></a>

## Hilbert Block
The Hilbert filter is available to provide a Hilbert Transform of the data from the ADC in Channel B. The Digital Hilbert Transform, in combination with an external complex downconverter, enables a receive image rejection architecture (similar to Hartley image rejection architecture). The Hilbert filter pass-band (< 0.1 dB ripple) is between 25% to 75% of the Nyquist rate of its input data rate. The maximum data rate of the Rx Hilbert filter is 32 MSPS. At ADC rates higher than this, the decimation filters should be enabled. The Hilbert filter transfer function plots are shown in Figure 7.

<a id='9987d598-6108-46b2-a897-327045a0749d'></a>

<::chart: A line graph titled "Figure 7. Rx Hilbert Filter, Keeping Positive Frequencies Response". The y-axis is labeled "MAGNITUDE - dB" and ranges from -120 to 0. The x-axis is labeled "NORMALIZED - f_s" and ranges from -0.5 to 0.5. The graph shows the frequency response of a filter. There is a passband from approximately 0.1 to 0.5 on the positive frequency side and from approximately -0.1 to -0.5 on the negative frequency side, with a stopband centered around 0. The stopband exhibits multiple ripples, reaching magnitudes below -100 dB.::>

<a id='0efd4548-6de0-4b7b-881b-abdfb8ce1644'></a>

**Data Output Multiplexer Stage**
The Rx data output format can be configured for either twos
complement or offset binary. This is controlled by the Rx Twos
Complement register.

<a id='cf3d7ac8-3fee-4aa6-aee5-e76b0bf0dfae'></a>

The output data from the dual ADCs can be multiplexed onto a single 10-/12-bit output bus. The multiplexing is synchronized using the RxSYNC output pin that indicates which channel data is on the output bus.

<a id='0c0546ca-5935-4514-ba91-838c48b167e4'></a>

**RECEIVE APPLICATIONS SECTION**
The AD9860/AD9862 receive path (Rx) includes two high speed,
high performance, 10-/12-bit ADCs. Figure 6 shows a detailed
block diagram of the Rx data path and can be referred to through-
out the explanation of the various modes of operation. The various
Rx modes of operation are broken into three parts determined by
the type of input signal:
1. Single Channel ADC Signal
2. Dual Channel Real ADC Signal (diversity or dual channel)
3. Dual Channel Complex ADC Signal (I and Q or Single
Sideband).

<a id='8b9a463d-fd13-4d97-8022-e62c45b7b4f1'></a>

Each one of these parts is further divided into two cases, sampling
input signals up to Nyquist of the ADC (Nyquist sampling) and
sampling at rates above ADC Nyquist rate (IF sampling or
undersampling).

<a id='8498f8c0-5719-4d1b-a592-6ed6c648e210'></a>

The AD9860/AD9862 uses oversampling and decimation filters to ease requirements on external filtering components. The decimation filters (for both receive paths) can be used or bypassed so as to accommodate different signal bandwidths and provide different output data rates to allow easy integration with several different data processing schemes.

<a id='92a332e7-6fde-4916-ae0a-1cbd0fdeceab'></a>

Nonbaseband data can be used in an effort to avoid the dc offsets in the receive signal path that can cause errors. By receiving nonbaseband data, the requirements of external filtering may be greatly reduced.

<a id='ed4e37c5-915c-435d-8c75-252b32c047d2'></a>

In each of the different receive modes, the input buffer, Program- mable Gain Amplifier (RxPGA), and output multiplexer remain within the receive path.

<a id='0a703740-afd2-431e-abb2-8c994a770189'></a>

**Single Channel ADC Signal**
In this mode, a single input signal to be digitized is connected to the differential input pins, VIN+A and VIN-A. The 10-/12-bit output Rx data is latched using either CLKOUT1 or CLKOUT2 edges as defined in the Clock Overview section. The Rx path available options include bypassing the input buffer, Rx PGA control and using the Decimation Filter. By default, both Rx paths are enabled and the unused one should be powered down using the appropriate bit in the Rx Power-Down register, d1.

<a id='db5bfb11-8dc7-4615-acb7-58594dd38306'></a>

The input buffer description above explains the conditions under which the buffer should be bypassed.

<a id='3c893bdb-e6bc-4c4f-9968-7c6c51146498'></a>

If the input signal, or the undersampled alias signal for the
IF sampling case, falls below 40% of the ADC Nyquist rate, the
decimation filter can be enabled to suppress out-of-band noise and
spurious signals by 40 dB or more. With the decimation filter
enabled, the SNR of the Rx path improves by about 2.3 dB.

<a id='e1941c05-6a14-4f88-a172-38b54b7f45fc'></a>

**Dual Channel Real ADC Signal**
The Dual Channel Real ADC Signal mode is used to receive diversity signals or dual independent channel signals that will be processed independent of each other. In this mode, the two input signals to be digitized are connected to the differential input pins of the AD9860/AD9862, VIN+A, VIN-A, VIN+B, and VIN-B. The two 10-/12-bit Rx outputs can be either interleaved onto a single 10-/12-bit bus or output in parallel on two 10-/12-bit buses.

<a id='317b0a75-8961-406e-96a2-57d80f433a94'></a>

REV. 0

<a id='19ed2c1f-5e36-44c1-b592-ea9a2e568446'></a>

-23-