<a id='fcc7f589-1437-4eca-b5ed-ee30cc672379'></a>

AD9860/AD9862

<a id='81ebee92-3dbd-4048-ab3d-8d5fcf53d25f'></a>

Tx Path (Normal Operation)
The DAC update rate, the Tx input data rate, and the rate of
CLKOUT2 (clock used to latch Tx input data) are the parameters
of interest for the transmit path data. These parameters, in addition
to the output signal bandwidth, are related to CLKIN by the settings
of the ADC Div2, the DLL multiplier, the CLKOUT2 Div, the
two edges, and the interpolation registers.

<a id='93093ace-b283-47ac-8905-13e2233c6742'></a>

The Tx data is timed relative to the CLKOUT2 pin (unless it is retimed relative to CLKOUT1 by setting Tx Retime register) and the input Tx data is latched on either each rising edge, each falling edge or both edges (controlled through the Inverse Sample and two edges registers). The timing diagrams for these cases are shown in Figure 12.

<a id='d6e82f48-33e7-4c84-bac7-f3092d9a326a'></a>

The Dual Tx data is multiplexed onto a single bus so that fewer digital bits are necessary to transfer data. Throughout this discus-sion of Tx path timing, Tx digital processing options other than interpolation are ignored because they do not change data timing; Tx data timing reflects whether single or dual channel data is latched into the AD9860/AD9862.

<a id='5cafaf4a-e731-493e-b008-ecf60c15a0a7'></a>

The rates of CLKOUT2 (and the input data rate) are related
to CLKIN by the DLL Multiplier Register, the setting of the
CLKOUT2 Divide Factor Register and the register ADC Div2.
These relationships are shown in Table II.

<a id='cda7a8c1-eaef-436a-aba3-d3f8773c0c26'></a>

Table II. CLKOUT2 Timing Relative to CLKIN
for Normal Operation Mode
<table id="26-1">
<tr><td id="26-2">CLK DIV2</td><td id="26-3">DLL Mult</td><td id="26-4">CLKOUT2 Div Factor</td><td id="26-5">CLKOUT2</td></tr>
<tr><td id="26-6" rowspan="9">No Div</td><td id="26-7" rowspan="3">1×</td><td id="26-8">/1</td><td id="26-9">CLKIN</td></tr>
<tr><td id="26-a">/2</td><td id="26-b">CLKIN/2</td></tr>
<tr><td id="26-c">/4</td><td id="26-d">CLKIN/4</td></tr>
<tr><td id="26-e" rowspan="3">2×</td><td id="26-f">/1</td><td id="26-g">2×CLKIN</td></tr>
<tr><td id="26-h">/2</td><td id="26-i">CLKIN</td></tr>
<tr><td id="26-j">/4</td><td id="26-k">CLKIN/2</td></tr>
<tr><td id="26-l" rowspan="3">4×</td><td id="26-m">/1</td><td id="26-n">4XCLKIN</td></tr>
<tr><td id="26-o">/2</td><td id="26-p">2XCLKIN</td></tr>
<tr><td id="26-q">/4</td><td id="26-r">CLKIN</td></tr>
<tr><td id="26-s" rowspan="9">Div by 2</td><td id="26-t" rowspan="3">1×</td><td id="26-u">/1</td><td id="26-v">CLKIN/2</td></tr>
<tr><td id="26-w">/2</td><td id="26-x">CLKIN/4</td></tr>
<tr><td id="26-y">/4</td><td id="26-z">CLKIN/8</td></tr>
<tr><td id="26-A" rowspan="3">2×</td><td id="26-B">/1</td><td id="26-C">CLKIN</td></tr>
<tr><td id="26-D">/2</td><td id="26-E">CLKIN/2</td></tr>
<tr><td id="26-F">/4</td><td id="26-G">CLKIN/4</td></tr>
<tr><td id="26-H" rowspan="3">4×</td><td id="26-I">/1</td><td id="26-J">2xCLKIN</td></tr>
<tr><td id="26-K">/2</td><td id="26-L">CLKIN</td></tr>
<tr><td id="26-M">/4</td><td id="26-N">CLKIN/2</td></tr>
</table>

<a id='1102a264-bb86-485f-b7e3-59a070a3b9d5'></a>

<::block diagram: Alternative Operation Timing Block Diagram::>CLKIN input feeds into a DLL block labeled "DLL MULTIPLIER: REG D24 B3, 4".The output of the DLL splits into multiple paths.One path goes to a "DIV" block labeled "1x, 2x, 4x" which is connected to CLKSEL.The CLKSEL output connects to another "DIV" block labeled "1x, 1/2x" for ADC. This "DIV" block is further labeled "ADC DIV2: REG D24 B5".The output of this "DIV" block goes to an "ADC" block.The output of the "ADC" block (dashed line, DATA PATH) goes to a filter symbol labeled "NO DECIMATION, ↓2" with "DECIMATE: REG D6 B0".This filter output then goes to a "DATA MUX AND LATCH" block labeled "MUX OUT: REG D5 B0" and "Rx RETIME: REG D5 B3".The output of the "DATA MUX AND LATCH" block is "Rx DATA [0:23]".Another path from the DLL output goes to a "DIV" block labeled "1x, 1/2x".The output of this "DIV" block goes to an "INV" block labeled "NO INVERSION, INVERT" and "INV1: REG D25 B1".The output of this "INV" block is "CLKOUT1".A third path from the DLL output goes to a "DIV" block labeled "1x, 1/2x, 1/4x" and "CLKOUT2 DIV FACTOR: REG 25 B6, 7".The output of this "DIV" block goes to an "INV" block labeled "NO INVERSION, INVERT" and "INV2: REG D25 B5".The output of this "INV" block is "CLKOUT2".Additionally, the CLKIN input feeds into a "DAC" block.The output of the "DAC" block (dashed line, DATA PATH) goes to a filter symbol labeled "NO INTERP, ↑2, ↑4" with "INTERPOLATION: REG D19 B0, 1".This filter output then goes to a "DATA LATCH AND DEMUX" block labeled "2 DATA PATHS: REG D19 B4", "Q/I ORDER: REG D18 B5", and "Tx RETIME: REG D18 B6".The output of the "DATA LATCH AND DEMUX" block is "Tx DATA [0:13]".A legend at the bottom left indicates:"--- CLOCK PATH" (solid line)"--- DATA PATH" (dashed line)Figure 13. Alternative Operation Timing Block Diagram

<a id='ac930a71-66f7-4a55-b875-dcc2ac908e04'></a>

REV. 0

<a id='987e608a-6ef5-4126-b727-736e55c76d37'></a>

-27-