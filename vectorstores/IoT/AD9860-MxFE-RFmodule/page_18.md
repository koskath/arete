<a id='3264681b-e45d-40a2-96a1-b42b0e7b3e71'></a>

---
AD9860/AD9862

<a id='c437f2fa-153d-489b-b6ea-b081605370b0'></a>

<::block diagram: flowchart::>BLOCK A: DAC
- Inputs: IOUT+A and IOUT-A, which feed into a PGA (Programmable Gain Amplifier), then to a TxDAC (Transmit Digital-to-Analog Converter).
- Inputs: IOUT+B and IOUT-B, which feed into a PGA, then to a TxDAC.
- Outputs of both TxDACs connect to BLOCK B.

BLOCK B: Bypassable Digital Quadrature Mixer
- Inputs from BLOCK A connect to two multiplexers.
- The outputs of the multiplexers are fed into a mixer (labeled X) and also have connections for I and Q signals.
- Control signals for this block are fs/4 and fs/8.
- Outputs connect to BLOCK C.

BLOCK C: Bypassable Low-Pass Interpolation Filter
- Inputs from BLOCK B.
- Contains two parallel low-pass filter components.
- Outputs connect to BLOCK D.

BLOCK D: Bypassable Digital Quadrature Mixer
- Inputs from BLOCK C connect to two multiplexers.
- The outputs of the multiplexers are fed into a mixer (labeled X) and also have connections for I and Q signals (Q is explicitly labeled).
- Control signal for this block is DDS (Direct Digital Synthesizer).
- Outputs connect to BLOCK E.

BLOCK E: Hilbert Filter
- Inputs from BLOCK D.
- Contains two parallel Hilbert Filter components.
- The outputs of the Hilbert Filters connect to a final output multiplexer.

Output:
- The final multiplexer outputs TxDATA [0:13].

Figure 3. Transmit Section Block Diagram<::>

<a id='937938aa-ce51-420e-87d8-f67e47be8957'></a>

Interpolation Stage (Block C), Fine Modulation Stage (Block D),
Hilbert filter (Block E), and the Latch/Demultiplexing circuitry.

<a id='7c954505-57d7-482e-8117-0f67646158d0'></a>

DAC
The DAC stage of the AD9860/AD9862 integrates a high performance TxDAC core, a programmable gain control through a Programmable Gain Amplifier (TxPGA), coarse gain control, and offset adjustment and fine gain control to compensate for system mismatches.

<a id='7bc0b010-cb9b-4414-94e0-9266e5600dac'></a>

The TxDAC core of the AD9860/AD9862 provides dual, differen-
tial, complementary current outputs generated from the 12-/14-bit
data. The 12-/14-bit Dual DACs support update rates up to
128 MSPS. The differential outputs (i.e., IOUT+ and IOUT-)
of each dual DAC are complementary, meaning they always sum
to the full-scale current output of the DAC, I_{OUTFS}. Optimum
ac performance is achieved with the differential current interface
drives balanced loads or a transformer.

<a id='60c2c279-8e9d-4b70-8b5c-a3aa6b098cca'></a>

The maximum full-scale output current, IOUTF SMAX, is set by the external resistor (RSET), which sets the DAC reference current.
The RSET resistor is connected between the FSADJ Pin to ground.
The relationship between IOUTF SMAX and RSET is:

<a id='44853328-dd4a-4d7f-b98a-86ff2dd05b77'></a>

$$I_{OUTFSMAX} \sim 67 \times \left(\frac{1.23\ V}{R_{SET}}\right)$$

<a id='3829d6c5-0d17-4a84-b3cf-4020c75da296'></a>

Typically, RSET is 4 kΩ, which sets IOUTFSMAX to 20 mA, the optimal dynamic setting for the TxDACs. Increasing RSET by a factor of 2 will proportionally decrease IOUTFSMAX by a factor of 2. IOUTFSMAX of each DAC can be re-scaled either simultaneously with the TxPGA Gain register or independently with DAC A/B Coarse Gain registers.

<a id='e1db17b6-d577-4c00-8191-fd9c9f6d006d'></a>

The TxPGA function provides 20 dB of simultaneous gain
range for both DACs and is controlled by writing to SPI register
TxPGA Gain for a programmable full-scale output of 10% to
100% IOUTFSMAX. The gain curve is linear in dB, with steps of
about 0.1 dB. Internally, the gain is controlled by changing the
main DAC bias currents with an internal TxPGA DAC whose
output is heavily filtered via an on-chip R-C filter to provide
continuous gain transitions. Note, the settling time and band-
width of the TxPGA DAC can be improved by a factor of 2 by
writing to the TxPGA Fast register.

<a id='9bdd2918-32fa-4ac5-84db-5c5ba54c470f'></a>

Each DAC has independent coarse gain control. Coarse gain control can be used to accommodate different IOUTFS from the dual DACs. The coarse full-scale output control can be adjusted using the DAC A/B Coarse Gain registers to 1/2 or 1/11th of the nominal full scale current.

<a id='166fd279-2e0f-4ad9-9c2d-5e4cfdbd23c8'></a>

Fine Gain controls and dc offset controls can be used to compen-sate for mismatches (for system level calibration), allowing improved matching characteristics of the two Tx channels and aiding in suppres-sing LO feedthrough. This is especially useful in image rejection architectures. The 10-bit dc offset control of each DAC can be used independently to provide a 12% IOUTFSMAX of offset to either differential pin, thus allowing calibration of any system offsets. The fine gain control with 5-bit resolution allows the IOUTFSMAX of each DAC to be varied over a 4% range, thus allowing compensation of any DAC or system gain mismatches. Fine gain control is set through the DAC A/B Fine Gain registers and the offset control of each DAC is accomplished using DAC A/B Offset registers.

<a id='68a59e77-14d9-4b85-b5f7-2c2b9acfe63f'></a>

A power-down option allows the user to power down the analog supply current to both DACs or either DAC, individually. A digital power-down is also possible through either the Tx PwrDwn register or the Mode/TxBlank pin.

<a id='6cb81fb5-95e2-4b27-bce5-0acbc03f3cd3'></a>

Coarse Modulator
A digital coarse modulator is available in the transmit path to
shift the spectrum of the input data by fDAC/4 or fDAC/8. If the
input data consists of complex data, the modulator can be con-
figured to perform a complex modulation of the input spectrum.
If the data in the transmit path is not complex, a real mix can be
performed separately on each channel thereby frequency shifting
the real data and images by fDAC/4 or fDAC/8. Real or complex
mixing is configured by setting the Real Mix register.

<a id='ca099544-b647-4015-8d02-e7211357fe8f'></a>

By default, the coarse modulator is bypassed. It can be configured using Coarse Modulation and Neg Coarse Tune registers.

<a id='dd6dde26-3daf-4804-a237-4ee5a84c35d8'></a>

**Interpolation Stage**
Interpolation filters are available for use in the AD9860/AD9862 transmit path, providing 1× (bypassed), 2×, or 4× interpolation.
The interpolation filters effectively increase the Tx data rate while suppressing the original images. The interpolation filters digitally shift the worst case image further away from the desired signal, thus reducing the requirements on the analog output reconstruction filter.

<a id='5144e212-9f3d-4627-83d8-f1fe00557848'></a>

There are two 2x interpolation filters available in the Tx path.
An interpolation rate of 4x is achieved using both interpolation
filters; an interpolation rate of 2x is achieved by enabling only
the first 2x interpolation filter.

<a id='d57eaa80-c31c-41aa-97d3-1a9a42828324'></a>

The first interpolation filter provides 2× interpolation using a 39 tap filter. It suppresses out-of-band signals by 60 dB or more and has a flat passband response (less than 0.1 dB ripple) extending to 38% of the AD9860/AD9862 input Tx data rate (19% of the DAC update rate, f₁₂₃₄). The maximum input data rate is 64 MSPS per channel when using 2× interpolation.

<a id='7ffac80f-eab3-4a1c-8b4a-24e6e98ec9ff'></a>

REV. 0

<a id='78fa9555-5077-411b-83d0-1cfbc541c6fa'></a>

-19-