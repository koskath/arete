<a id='1e6e4df7-611c-4eb8-884b-bcb8185f7769'></a>

AD9860/AD9862

<a id='1fb4a181-b5fe-448f-886e-32a3e80e7d3b'></a>

**DEFINITIONS OF SPECIFICATIONS**

**Differential Nonlinearity Error (DNL, No Missing Codes)**
An ideal converter exhibits code transitions that are exactly 1 LSB apart. DNL is the deviation from this ideal value. Guaranteed no missing codes to 10-bit resolution indicate that all 1024 codes respectively, must be present over all operating ranges.

<a id='48398a84-31a6-4163-a5ca-5f084006e8c1'></a>

**Integral Nonlinearity Error (INL)**
Linearity error refers to the deviation of each individual code from
a line drawn from "negative full scale" through "positive full
scale." The point used as "negative full scale" occurs 1/2 LSB
before the first code transition. "Positive full scale" is defined as
a level 1 1/2 LSB beyond the last code transition. The deviation
is measured from the middle of each particular code to the true
straight line.

<a id='a018aa00-9cbf-4d0f-ba7b-209010ee9720'></a>

## Phase Noise
Single-sideband phase noise power is specified relative to the carrier (dBc/Hz) at a given frequency offset (1 kHz) from the carrier. Phase noise can be measured directly in Single Tone Trans- mit Mode with a spectrum analyzer that supports noise marker measurements. It detects the relative power between the carrier and the offset (1 kHz) sideband noise and takes the resolution bandwidth (rbw) into account by subtracting 10 log(rbw). It also adds a correction factor that compensates for the implementation of the resolution bandwidth, log display, and detector characteristic.

<a id='a73117fe-e829-4c52-9540-5f5c725dc782'></a>

**Output Compliance Range**
The range of allowable voltage at the output of a current-output DAC. Operation beyond the maximum compliance limits may cause either output stage saturation or breakdown, resulting in nonlinear performance.

<a id='98df7001-6228-4b30-a9e0-db33e0846278'></a>

**Spurious-Free Dynamic Range (SFDR)**
The difference, in dB, between the rms amplitude of the DAC's output signal (or ADC's input signal) and the peak spurious signal over the specified bandwidth (Nyquist bandwidth unless otherwise noted).

<a id='07fc98d1-c7d4-4bf0-b954-98bc618dd288'></a>

**Pipeline Delay (Latency)**
The number of clock cycles between conversion initiation and
the associated output data being made available.

<a id='3a6cb6a3-96e8-42e4-aa52-635e6a1bae1c'></a>

### Offset Error
First transition should occur for an analog value 1/2 LSB above
-full scale. Offset error is defined as the deviation of the actual
transition from that point.

<a id='a3bbf2e1-a204-4615-92a4-a80ba429582c'></a>

**Gain Error**
The first code transition should occur at an analog value 1/2 LSB
above -full scale. The last transition should occur for an analog
value 1 1/2 LSB below the nominal full scale. Gain error is the
deviation of the actual difference between first and last code
transitions and the ideal difference between first and last code
transitions.

<a id='00362d20-e740-4748-ac84-315d2766eb8e'></a>

**Aperture Delay**
The aperture delay is a measure of the Sample-and-Hold Ampli-
fier (SHA) performance and specifies the time delay between the
rising edge of the sampling clock input to when the input signal
is held for conversion.

<a id='01e68186-9f0f-4ad6-bfb7-fc6a1554e759'></a>

**Aperture Uncertainty (Jitter)**
Aperture jitter is the variation in aperture delay for successive samples and is manifested as noise on the input to the ADC.

<a id='2d1bf1bf-d62e-411d-a3dd-22b606a70cd6'></a>

**Input Referred Noise**
The rms output noise is measured using histogram techniques.
The ADC output code's standard deviation is calculated in LSB
and converted to an equivalent voltage. This results in a noise
figure that can be referred directly to the input of the AD9860/
AD9862.

<a id='fd46b555-4ffc-4045-bd42-70ee56fe44f8'></a>

**Signal-to-Noise and Distortion (S/N+D, SINAD) Ratio**
S/N+D is the ratio of the rms value of the measured input signal
to the rms sum of all other spectral components below the Nyquist
frequency, including harmonics but excluding dc. The value for
S/N+D is expressed in decibels.

<a id='887f901b-f5cb-4c36-8fc1-40450de99c8d'></a>

**Effective Number of Bits (ENOB)**
For a sine wave, *SINAD* can be expressed in terms of the number
of bits. Using the following formula:

<a id='f8b97a9b-2fc5-4e61-9f61-94ef90a9e88f'></a>

N = (SINAD - 1.76 dB) / 6.02

<a id='2bb5a226-1ebd-48e3-99f9-1601e46c661f'></a>

it is possible to get a measure of performance expressed as N,
the effective number of bits. Thus, effective number of bits for
a device for sine wave inputs at a given input frequency can be
calculated directly from its measured SINAD.

<a id='8826acad-2ec4-4a08-8aae-57da9ea8cea6'></a>

**Signal-to-Noise Ratio (SNR)**
SNR is the ratio of the rms value of the measured input signal to the rms sum of all other spectral components below the Nyquist frequency, excluding harmonics and dc. The value for SNR is expressed in decibels.

<a id='d3cd6387-f972-4098-a1b7-8d8b2e2740cc'></a>

**Total Harmonic Distortion (THD)**
THD is the ratio of the rms sum of the first six harmonic
components to the rms value of the measured input signal and
is expressed as a percentage or in decibels.

<a id='14db4ec9-9914-48a4-b9a7-074a86736a06'></a>

**Power Supply Rejection**
Power supply rejection specifies the converter's maximum full-scale change when the supplies are varied from nominal to minimum and maximum specified voltages.

<a id='ea893c6e-3d10-42f1-a472-2d99e8554353'></a>

**Channel-to-Channel Isolation (Crosstalk)**
In an ideal multichannel system, the signal in one channel will not influence the signal level of another channel. The channel- to-channel isolation specification is a measure of the change that occurs to a grounded channel as a full-scale signal is applied to another channel.

<a id='f02a5411-e193-4991-871a-3275a9e67050'></a>

-8-

<a id='89e8abf6-d607-4eac-8f14-9cae9cef711e'></a>

REV. 0