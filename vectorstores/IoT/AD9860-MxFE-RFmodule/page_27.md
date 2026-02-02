<a id='cdf9f290-bd0c-4b9c-a6c5-8c0abcac466d'></a>

--- AD9860/AD9862

<a id='479ff7d7-8e40-44f1-b8ef-ba343c6248a9'></a>

Table IV. Normal Operation Mode Master Timing Guide
<table id="28-1">
<tr><td id="28-2" rowspan="3">ADC2</td><td id="28-3" rowspan="3">DLL Mult</td><td id="28-4" rowspan="3">ADC Clock Rate</td><td id="28-5" colspan="4">ADC Data Rate¹ (MSPS)</td><td id="28-6" rowspan="3">DAC Update Rate</td><td id="28-7" rowspan="2" colspan="3">Dual DAC Data Rate² (MSPS)</td><td id="28-8" rowspan="2" colspan="2">CLKOUT1</td><td id="28-9" rowspan="2" colspan="3">CLKOUT2</td></tr>
<tr><td id="28-a" colspan="2">Non-MUX Mode</td><td id="28-b" colspan="2">MUX Mode</td></tr>
<tr><td id="28-c">No Deci</td><td id="28-d">Deci by 2</td><td id="28-e">No Deci</td><td id="28-f">Deci by 2</td><td id="28-g">1X Interp</td><td id="28-h">2X Interp</td><td id="28-i">4X Interp</td><td id="28-j">CLKSEL = Low</td><td id="28-k">CLKSEL = High</td><td id="28-l">CLKDIV = 1X</td><td id="28-m">CLKDIV = 1/2X</td><td id="28-n">CLKDIV = 1/4X</td></tr>
<tr><td id="28-o">0</td><td id="28-p">1X</td><td id="28-q" rowspan="3">CLKIN</td><td id="28-r" rowspan="3">CLKIN</td><td id="28-s" rowspan="3">CLKIN ÷ 2</td><td id="28-t" rowspan="3">2× CLKIN</td><td id="28-u" rowspan="3">CLKIN</td><td id="28-v">CLKIN</td><td id="28-w">2X CLKIN</td><td id="28-x">CLKIN</td><td id="28-y">CLKIN ÷ 2</td><td id="28-z" rowspan="6">CLKIN</td><td id="28-A" rowspan="6">CLKIN ÷2</td><td id="28-B">CLKIN</td><td id="28-C">CLKIN ÷ 2</td><td id="28-D">CLKIN ÷ 4</td></tr>
<tr><td id="28-E">0</td><td id="28-F">2X</td><td id="28-G">2X CLKIN</td><td id="28-H">4X CLKIN</td><td id="28-I">2X CLKIN</td><td id="28-J">CLKIN</td><td id="28-K">2X CLKIN</td><td id="28-L">CLKIN</td><td id="28-M">CLKIN ÷ 2</td></tr>
<tr><td id="28-N">0</td><td id="28-O">4X</td><td id="28-P">4X CLKIN</td><td id="28-Q">8X CLKIN</td><td id="28-R">4X CLKIN</td><td id="28-S">2× CLKIN</td><td id="28-T">4× CLKIN</td><td id="28-U">2× CLKIN</td><td id="28-V">CLKIN</td></tr>
<tr><td id="28-W">1</td><td id="28-X">1X</td><td id="28-Y" rowspan="3">CLKIN ÷ 2</td><td id="28-Z" rowspan="3">CLKIN ÷ 2</td><td id="28-10" rowspan="3">CLKIN ÷ 4</td><td id="28-11" rowspan="3">CLKIN</td><td id="28-12" rowspan="3">CLKIN ÷ 2</td><td id="28-13">CLKIN ÷2</td><td id="28-14">CLKIN</td><td id="28-15">CLKIN ÷2</td><td id="28-16">CLKIN ÷ 4</td><td id="28-17">CLKIN ÷ 2</td><td id="28-18">CLKIN ÷ 4</td><td id="28-19">CLKIN ÷ 8</td></tr>
<tr><td id="28-1a">1</td><td id="28-1b">2X</td><td id="28-1c">CLKIN</td><td id="28-1d">2X CLKIN</td><td id="28-1e">CLKIN</td><td id="28-1f">CLKIN ÷ 2</td><td id="28-1g">CLKIN</td><td id="28-1h">CLKIN ÷ 2</td><td id="28-1i">CLKIN ÷ 4</td></tr>
<tr><td id="28-1j">1</td><td id="28-1k">4X</td><td id="28-1l">2X CLKIN</td><td id="28-1m">4X CLKIN</td><td id="28-1n">2X CLKIN</td><td id="28-1o">CLKIN</td><td id="28-1p">2× CLKIN</td><td id="28-1q">CLKIN</td><td id="28-1r">CLKIN ÷ 2</td></tr>
</table>
NOTES
1 100 MHz rate max.
2 Single DAC data rate = 1/2 dual DAC data rate.

<a id='c091d8d0-ea98-4215-b71d-9eb03dc40cde'></a>

Table V. Alternative Operation Mode Master Timing Guide
<table id="28-1s">
<tr><td id="28-1t" rowspan="3">ADC2</td><td id="28-1u" rowspan="3">DLL Mult</td><td id="28-1v" rowspan="3">ADC Clock Rate</td><td id="28-1w" colspan="4">ADC Data Rate¹ (MSPS)</td><td id="28-1x" rowspan="3">DAC Update Rate</td><td id="28-1y" rowspan="2" colspan="3">Dual DAC Data Rate2 (MSPS)</td><td id="28-1z" rowspan="2" colspan="2">CLKOUT1</td><td id="28-1A" rowspan="2" colspan="3">CLKOUT2</td></tr>
<tr><td id="28-1B" colspan="2">Non-MUX Mode (two buses)</td><td id="28-1C" colspan="2">MUX Mode (one bus)</td></tr>
<tr><td id="28-1D">No Deci</td><td id="28-1E">Deci by 2</td><td id="28-1F">No Deci</td><td id="28-1G">Deci by 2</td><td id="28-1H">1× Interp</td><td id="28-1I">2× Interp</td><td id="28-1J">4X Interp</td><td id="28-1K">CLKSEL = Low</td><td id="28-1L">CLKSEL = High</td><td id="28-1M">CLKDIV = 1X</td><td id="28-1N">CLKDIV = 1/2X</td><td id="28-1O">CLKDIV = 1/4X</td></tr>
<tr><td id="28-1P">0</td><td id="28-1Q">1X</td><td id="28-1R">CLKIN</td><td id="28-1S">CLKIN</td><td id="28-1T">CLKIN ÷ 2</td><td id="28-1U">2× CLKIN</td><td id="28-1V">CLKIN</td><td id="28-1W">CLKIN</td><td id="28-1X">2× CLKIN</td><td id="28-1Y">CLKIN</td><td id="28-1Z">CLKIN ÷ 2</td><td id="28-20">CLKIN</td><td id="28-21">CLKIN ÷ 2</td><td id="28-22">CLKIN</td><td id="28-23">CLKIN ÷ 2</td><td id="28-24">CLKIN ÷4</td></tr>
<tr><td id="28-25">0</td><td id="28-26">2X</td><td id="28-27">2X CLKIN</td><td id="28-28">2X CLKIN</td><td id="28-29">CLKIN</td><td id="28-2a">4× CLKIN</td><td id="28-2b">2× CLKIN</td><td id="28-2c">2× CLKIN</td><td id="28-2d">4× CLKIN</td><td id="28-2e">2× CLKIN</td><td id="28-2f">2x CLKIN</td><td id="28-2g">CLKIN</td><td id="28-2h">CLKIN</td><td id="28-2i">2X CLKIN</td><td id="28-2j">CLKIN</td><td id="28-2k">CLKIN ÷2</td></tr>
<tr><td id="28-2l">0</td><td id="28-2m">4X</td><td id="28-2n">4X CLKIN</td><td id="28-2o">4X CLKIN</td><td id="28-2p">2X CLKIN</td><td id="28-2q">8X CLKIN</td><td id="28-2r">4X CLKIN</td><td id="28-2s">4X CLKIN</td><td id="28-2t">8X CLKIN</td><td id="28-2u">4X CLKIN</td><td id="28-2v">2X CLKIN</td><td id="28-2w">4X CLKIN</td><td id="28-2x">2X CLKIN</td><td id="28-2y">4X CLKIN</td><td id="28-2z">2X CLKIN</td><td id="28-2A">CLKIN</td></tr>
<tr><td id="28-2B">1</td><td id="28-2C">1X</td><td id="28-2D">CLKIN ÷ 2</td><td id="28-2E">CLKIN ÷ 2</td><td id="28-2F">CLKIN ÷ 4</td><td id="28-2G">CLKIN</td><td id="28-2H">CLKIN ÷ 2</td><td id="28-2I">CLKIN</td><td id="28-2J">2X CLKIN</td><td id="28-2K">CLKIN</td><td id="28-2L">CLKIN ÷ 2</td><td id="28-2M">CLKIN</td><td id="28-2N">CLKIN ÷ 2</td><td id="28-2O">CLKIN</td><td id="28-2P">CLKIN ÷ 2</td><td id="28-2Q">CLKIN ÷ 4</td></tr>
<tr><td id="28-2R">1</td><td id="28-2S">2X</td><td id="28-2T">CLKIN</td><td id="28-2U">CLKIN</td><td id="28-2V">CLKIN ÷ 2</td><td id="28-2W">2X CLKIN</td><td id="28-2X">CLKIN</td><td id="28-2Y">2X CLKIN</td><td id="28-2Z">4X CLKIN</td><td id="28-30">2X CLKIN</td><td id="28-31">CLKIN</td><td id="28-32">2x CLKIN</td><td id="28-33">CLKIN</td><td id="28-34">2X CLKIN</td><td id="28-35">CLKIN</td><td id="28-36">CLKIN ÷ 2</td></tr>
<tr><td id="28-37">1</td><td id="28-38">4X</td><td id="28-39">2X CLKIN</td><td id="28-3a">2X CLKIN</td><td id="28-3b">CLKIN</td><td id="28-3c">4X CLKIN</td><td id="28-3d">2X CLKIN</td><td id="28-3e">4X CLKIN</td><td id="28-3f">8X CLKIN</td><td id="28-3g">4X CLKIN</td><td id="28-3h">2X CLKIN</td><td id="28-3i">4X CLKIN</td><td id="28-3j">2X CLKIN</td><td id="28-3k">4X CLKIN</td><td id="28-3l">2X CLKIN</td><td id="28-3m">CLKIN</td></tr>
</table>

<a id='48b75d24-0d14-462a-a93e-cc3b69bc7ba8'></a>

NOTES
1 100 MHz rate max.
2 Single DAC data rate = 1/2 dual DAC data rate.

<a id='63e0cd6f-04a0-4b50-941c-4729b7c3538c'></a>

REV. 0

<a id='bc7765bc-826f-4e31-a058-eb71f4c4b4a0'></a>

-29-