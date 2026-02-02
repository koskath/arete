<a id='40eee5c1-972b-4780-b0c8-950fda618850'></a>

**AD9860/AD9862**

The second interpolation filter will provide an additional 2× interpolation for an overall 4× interpolation. The second filter is a 15 tap filter. It suppresses out-of-band signals by 60 dB or more. The flat passband response (less than 0.1 dB attenuation) is 38% of the Tx input data rate (9.5% of fDAC). The maximum input data rate per channel is 32 MSPS per channel when using 4× interpolation.

<a id='2c21da68-eb33-4220-90ca-004a90a5502d'></a>

The 2× and 4× Interpolation Filter Transfer function plots are shown in Figure 4a and 4b, respectively.

<a id='89e02f6a-0e3b-488e-aab4-39f02503f84d'></a>

<::Graph showing the frequency response of two filters. The x-axis is labeled "NORMALIZED - fS" and ranges from 0 to 1.0. The y-axis is labeled "MAGNITUDE - dB" and ranges from -100 to 10. Two curves are plotted: one labeled "INTERPOLATION FILTER" and another labeled "INCLUDUNG SIN (X)/X". Both curves show a low-pass filter characteristic, with the interpolation filter having a sharper cutoff and more ripple in the stopband compared to the other curve.::>

<a id='ff10e88c-ba29-41e6-bed6-e3e0be20dc34'></a>

<::A line graph titled "Spectral Response" with two curves. The Y-axis is labeled "MAGNITUDE - dB", ranging from 10 dB at the top to -100 dB at the bottom. The X-axis is labeled "NORMALIZED - fs", ranging from 0 to 1.0. Two curves are plotted: one labeled "INTERPOLATION FILTER" and another labeled "INCLUDING SIN (X)/X". Both curves start at 0 dB at X=0. The "INTERPOLATION FILTER" curve drops sharply to below -60 dB around X=0.15 and then shows a stopband with ripples, rising towards 0 dB again as X approaches 1.0. The "INCLUDING SIN (X)/X" curve also drops sharply, slightly earlier than the first, and exhibits a stopband with more pronounced and higher-frequency ripples, also rising towards 0 dB near X=0.9. This graph illustrates the spectral response for 2x and 4x interpolation filters.::>Figure 4. Spectral Response of 2× Interpolation Filter (top) and 4× Interpolation Filter (bottom)

<a id='c8b0f65f-bb80-4aef-ae94-46ef282c5809'></a>

## Fine Modulation Stage
A digital fine modulation stage is available in the transmit path to shift the complex Tx output spectrum using a 24-bit numerically controlled oscillator (NCO). To utilize the Fine Modulation Block, 4× interpolation is required. Therefore, the maximum input data rate is 32 MSPS per channel, which generates a DAC update rate, f_DAC, of 128 MSPS. The NCO can tune up to 1/4 of f_DAC, providing a step resolution of f_DAC/2^26. Since the Fine Modulation Stage precedes the Interpolation Filters, care must be taken to ensure the entire desired signal is placed within the pass band of the Interpolation Filter.

<a id='2658d8ee-04eb-4bd3-9ff2-53482a408bd9'></a>

By default, the Fine Modulation Block is bypassed. To enable it to perform a complex mix of the Tx I and Q data, Register 2's data paths, Fine Mod and Fine, should be configured. The NCO frequency tuning word is set in the three FTW registers.

<a id='af02f61c-85f7-4f71-9405-02d60325b089'></a>

## Hilbert Filter
The Hilbert filter is available to provide a Hilbert transform of "real" input data at a low intermediate frequency (IF) between 12.5% to 38% of the input data rate. The Hilbert filter essentially transforms this "real," single channel input data into a complex representation (i.e., I and Q components) that can be used as part of an image rejection architecture. The complex data can then be processed further using the on-chip digital complex modulators. The Hilbert filter requires 4× interpolation to be enabled and accepts data at a maximum 32 MSPS. Figure 5 shows a spectral plot of the Hilbert filter impulse response.

<a id='87306936-771b-49c3-9eb5-a29e6d679223'></a>

<::chart: spectral plot::>
## Figure 5. Tx Hilbert Filter, Keeping Positive Frequencies Spectral Plot
This spectral plot displays dB (decibels) on the y-axis, ranging from -100 to 100, against FREQUENCY - MHz on the x-axis, ranging from -20 to 20. The plot shows a frequency response with significant attenuation (low dB values) for negative frequencies and frequencies below approximately 3 MHz. There is a prominent bandpass region for positive frequencies, roughly between 4 MHz and 11 MHz, where the response is high, peaking around 80 dB. Beyond this band, the response drops again, showing ripples and lower dB values for frequencies above 11 MHz.
<::>

<a id='3541ff9d-3c1d-49eb-9d7f-f200d1434975'></a>

## Latch/Demultiplexer
The AD9860/AD9862 Tx path accepts dual or single channel data. The dual channel data can represent two independent real signals or a complex signal. Various input data latching schemes relative to one of the output clocks, CLKOUT1 or CLKOUT2, are allowed, including using any combination of rising and falling clock edges.

<a id='1d4a4854-fe15-4300-b56d-b539b0e0cf3a'></a>

Associated Tx timing is discussed in detail in the Clock Overview section of the data sheet.

<a id='676afb7f-467e-4732-86b0-1a139c278276'></a>

**TRANSMIT APPLICATIONS SECTION**
The AD9860/AD9862 transmit path (Tx) includes two, high speed,
high performance, 12-/14-bit TxDACs. Figure 3 shows a detailed
block diagram of the transmit data path and can be referred to
throughout the explanation of the various modes of operation.
The various Tx modes of operation are broken into three parts,
determined by the format of the input data. They are:
1. Single Channel DAC Data
2. Two Independent Real Signal DAC Data (diversity or dual
channel
3. Dual Channel Complex DAC Data (I and Q or Single Sideband)

<a id='27368c94-f2fa-45cf-97d3-0f4d11f4dd9a'></a>

**Single Channel DAC Data**
In this mode, 12-/14-bit single channel Tx data is provided to the AD9860/AD9862 and latched using either CLKOUT1 or CLKOUT2 edges as defined in the Clock Overview section of the data sheet. All Tx digital signal processing blocks can be utilized to address reconstruction filtering at the DAC output and aid in frequency tuning.

<a id='b6c4cd04-459f-4778-b70b-2134a3cc390f'></a>

-20-

<a id='97ecadbc-83bf-4a7c-8b05-ab8496ad70df'></a>

REV. 0