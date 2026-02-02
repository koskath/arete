<a id='1abe3ce2-df9a-487d-b5da-1df9aa447ef3'></a>

AD9860/AD9862<::block diagram: The diagram, titled "Receive Section Block Diagram", illustrates the signal processing chain. It is divided into five main conceptual blocks, A through E, outlined by dashed lines.Two parallel input paths, one for A and one for B, are shown.Top Path (A):VIN+A and VIN-A inputs feed into a differential amplifier labeled "1x" (Block A). The output of this amplifier goes into a PGA (Programmable Gain Amplifier) (Block B). The PGA's output then feeds into an ADC (Analog-to-Digital Converter) (Block C). The ADC's output goes into a LOW-PASS DECIMATION FILTER (Block D).Bottom Path (B):VIN+B and VIN-B inputs feed into a differential amplifier labeled "1x" (Block A). The output of this amplifier goes into a PGA (Block B). The PGA's output then feeds into an ADC (Block C). The ADC's output goes into a LOW-PASS DECIMATION FILTER (Block D).After Block D, the outputs from both the top and bottom LOW-PASS DECIMATION FILTERS converge and feed into a single HILBERT FILTER (Block E).The output of the HILBERT FILTER then splits into two paths:One path goes through a series of two multiplexers/selectors to produce "RxA DATA [0:11]".The other path goes through a single multiplexer/selector to produce "RxB DATA [0:11]".Figure 6. Receive Section Block Diagram::>

<a id='7291f2c7-f5fb-4de8-97c3-6568da8526ff'></a>

**RECEIVE SECTION COMPONENTS**
The receive block is configurable to process input signals of different formats and has special features such as an input buffer, gain stage, and decimation filters. The AD9860/AD9862 receive path block diagram is shown in Figure 6. The block diagram can be broken into the following stages: Input Buffer (Block A), RxPGA (Block B), dual, 10-/12-bit, 64 MSPS ADC (Block C), Decimation filter (Block D), Digital Hilbert Block (Block E), and a Data Output Multiplexer. The function of each stage is explained in the following paragraphs.

<a id='7d3c4aed-5c90-438b-a5b3-d7632dc11a1f'></a>

**Input Buffer Stage**
The input buffer stage buffers the input signal on-chip for both receive paths. The buffer stage has two main benefits, providing a constant input impedance and reducing any "kick-back" noise that might be generated on-chip, affecting the analog input signal.

<a id='2f34045e-78ac-4c79-b092-9f4ef0241ef3'></a>

The Rx path sampling mode can be split into two categories,
depending on the frequency of the input signal. When sampling
input signals up to Nyquist of the ADC, the sampling is referred to
as Nyquist sampling. When sampling at rates above ADC Nyquist
rate, the sampling is referred to as IF sampling or undersampling.

<a id='10238e96-9ef5-416f-916b-83674f1c06ab'></a>

For Nyquist sampling, the input buffer provides a constant 200 Ω impedance over the entire input signal range. The constant input impedance accommodates matching networks to ensure proper transfer of signal to the input of the device. The input buffer is self-biased to ~ 2 V, and therefore the input signal should be ac-coupled to the Rx differential input or have a common-mode voltage of about 2 V. If an external buffer is present, the internal input buffer can be bypassed and powered down to reduce power consumption. The input buffer accepts up to a 2 V p-p input signal for maximum SNR performance. Optimal THD performance occurs with 1 V p-p input signal.

<a id='12871680-ae74-4421-9bcc-1e2f75e3505b'></a>

For IF sampling, the input buffer can be used with input signals
up to about 100 MHz, the 3 dB bandwidth of the buffer. When
undersampling the input signal, the output spectrum will contain
an aliased version of the original, higher frequency signal. As was
the case with Nyquist sampling, the input signal should be
ac-coupled to the Rx differential input or have a common-mode
voltage of~2 V. For input signals over 100 MHz to about 250 MHz,
the input buffer needs to be bypassed and an external input
buffer is required. In the case that the input buffer is bypassed,
the input circuit is a switched capacitor network. The switching
input impedance during the sample phase is about 1/(2(π)FC),
where F is the input frequency and C is the input capacitance
(about 4 pF). During hold mode, the input impedance is > 1 MΩ.

<a id='4bb65bf5-58ae-48fc-abae-4bfef5de46d4'></a>

RxPGA
The RxPGA stage has a Programmable Gain Amplifier that can be used to amplify the input signal to utilize the entire input range of the ADC. The RxPGA stage provides a 0 dB to 20 dB gain range in steps of about 1 dB. The Rx channel independent gain control is accomplished through two 5-bit SPI programmable RxPGA A/B registers. The gain curve is linear in dB with a minimum gain setting (0 dB, nominally) of hex00 and a maximum gain setting (20 dB, nominally) of hex14.

<a id='cecb7c5e-130a-49c7-ab93-6243a4054641'></a>

The RxPGA stage can provide up to a 2 V p-p signal to the ADC input.

<a id='3afe1fd6-1b5c-40b1-accd-bf7bad0b5654'></a>

## Analog-to-Digital (A/D) Converter
The analog-to-digital converter (ADC) stage consists of two high performance 10-/12-bit, 64 MSPS analog-to-digital (A/D) converters. The dual A/D converter paths are fully independent, except for a shared internal bandgap reference source, VREF. Each of the A/D converter's paths consists of a front-end sample and hold amplifier followed by a pipelined, switched capacitor, A/D converter. The pipelined A/D converter is divided into three sections, consisting of a 4-bit first stage followed by eight 1.5-bit stages and a final 3-bit flash. Each stage provides sufficient overlap to correct for flash errors in the preceding stages. The quantized outputs from each stage are combined into a final 12-bit result through a digital correction logic block. The pipelined architecture permits the first stage to operate on a new input sample while the remaining stages operate on preceding samples. Sampling occurs on the rising clock edge.

<a id='1d6601c8-c0ca-4b77-a5dc-49110ae3ed2c'></a>

Each stage of the pipeline, excluding the last, consists of a low resolution flash A/D connected to a switched capacitor DAC and interstage residue amplifier (MDAC). The residue amplifier magnifies the difference between the reconstructed DAC output and the flash input for the next stage in the pipeline. One bit of redundancy is used in each one of the stages to facilitate digital correction of flash errors. The last stage simply consists of a flash A/D.

<a id='a0ebfe8f-d725-4a70-b15f-76aae93decf5'></a>

A stable and accurate 1.0 V bandgap voltage reference is built into the AD9860/AD9862 and is used to set a 2 V p-p differential input range. The internally generated reference should be decoupled at the VREF pin using a 10 µF and a 0.1 µF capacitor in parallel to ground. Separate top and bottom references, VRT and VRB, for each converter are generated from VREF and should also be decoupled. Recommended decoupling for the top and bottom references consists of using 10 µF and 0.1 µF capacitors in parallel between the differential reference pins, and a 0.1 µF capacitor

<a id='d6fbfeae-b816-4df7-be04-37febcc6ae06'></a>

-22-

<a id='3a3512d4-ee9d-4304-89c8-05cb98020d04'></a>

REV. 0