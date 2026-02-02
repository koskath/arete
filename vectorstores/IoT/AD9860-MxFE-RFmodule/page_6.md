<a id='0fdba30c-b317-4aa0-97f3-9c0fb4994412'></a>

AD9860/AD9862

<a id='be6e9a55-fb70-4fbf-a981-44a920f6dae5'></a>

PIN FUNCTION DESCRIPTIONS

<a id='c4c1b166-213e-47e2-a7b4-1728378f8f17'></a>

<table id="6-1">
<tr><td id="6-2">Pin No.</td><td id="6-3">Mnemonic</td><td id="6-4">Function</td></tr>
<tr><td id="6-5" colspan="3">Receive Pins</td></tr>
<tr><td id="6-6">68/70–79</td><td id="6-7">D0A to D9A/D11A</td><td id="6-8">10-/12-Bit ADC Output of Receive Channel A</td></tr>
<tr><td id="6-9">80/82–91</td><td id="6-a">D0B to D9B/D11B</td><td id="6-b">10-/12-Bit ADC Output of Receive Channel B</td></tr>
<tr><td id="6-c">92</td><td id="6-d">RxSYNC</td><td id="6-e">Synchronization Clock for Channel A and Channel B Rx Paths</td></tr>
<tr><td id="6-f">98, 99,</td><td id="6-g">AVDD</td><td id="6-h">Analog Supply Pins</td></tr>
<tr><td id="6-i">104, 105,</td><td id="6-j"></td><td id="6-k"></td></tr>
<tr><td id="6-l">117, 118,</td><td id="6-m"></td><td id="6-n"></td></tr>
<tr><td id="6-o">123, 124,</td><td id="6-p"></td><td id="6-q"></td></tr>
<tr><td id="6-r">100, 103,</td><td id="6-s">AGND</td><td id="6-t">Analog Ground Pins</td></tr>
<tr><td id="6-u">106, 109,</td><td id="6-v"></td><td id="6-w"></td></tr>
<tr><td id="6-x">110, 112,</td><td id="6-y"></td><td id="6-z"></td></tr>
<tr><td id="6-A">113, 116,</td><td id="6-B"></td><td id="6-C"></td></tr>
<tr><td id="6-D">119, 122,</td><td id="6-E"></td><td id="6-F"></td></tr>
<tr><td id="6-G">101</td><td id="6-H">REFT_B</td><td id="6-I">Top Reference Decoupling for Channel B ADC</td></tr>
<tr><td id="6-J">102</td><td id="6-K">REFB_B</td><td id="6-L">Bottom Reference Decoupling for Channel B ADC</td></tr>
<tr><td id="6-M">107</td><td id="6-N">VIN+B</td><td id="6-O">Receive Channel B Differential (+) Input</td></tr>
<tr><td id="6-P">108</td><td id="6-Q">VIN-B</td><td id="6-R">Receive Channel B Differential (-) Input</td></tr>
<tr><td id="6-S">111</td><td id="6-T">VREF</td><td id="6-U">Internal ADC Voltage Reference</td></tr>
<tr><td id="6-V">114</td><td id="6-W">VIN-A</td><td id="6-X">Receive Channel A Differential (-) Input</td></tr>
<tr><td id="6-Y">115</td><td id="6-Z">VIN+A</td><td id="6-10">Receive Channel A Differential (+) Input</td></tr>
<tr><td id="6-11">120</td><td id="6-12">REFB_A</td><td id="6-13">Bottom Reference Decoupling for Channel A ADC</td></tr>
<tr><td id="6-14">121</td><td id="6-15">REFT_A</td><td id="6-16">Top Reference Decoupling for Channel A ADC</td></tr>
</table>

<a id='413bf942-98b0-4deb-a4a6-201d15b0ea5b'></a>

Transmit Pins
<table id="6-17">
<tr><td id="6-18">18, 20</td><td id="6-19">AVDD</td><td id="6-1a">Analog Supply Pins</td></tr>
<tr><td id="6-1b">23, 32</td><td id="6-1c"></td><td id="6-1d"></td></tr>
<tr><td id="6-1e">19, 24,</td><td id="6-1f">AGND</td><td id="6-1g">Analog Ground Pins</td></tr>
<tr><td id="6-1h">27, 28, 31</td><td id="6-1i"></td><td id="6-1j"></td></tr>
<tr><td id="6-1k">21</td><td id="6-1l">REFIO</td><td id="6-1m">Reference Output, 1.2 V Nominal</td></tr>
<tr><td id="6-1n">22</td><td id="6-1o">FSADJ</td><td id="6-1p">Full-Scale Current Adjust</td></tr>
<tr><td id="6-1q">25</td><td id="6-1r">IOUT-A</td><td id="6-1s">Transmit Channel A DAC Differential (-) Output</td></tr>
<tr><td id="6-1t">26</td><td id="6-1u">IOUT+A</td><td id="6-1v">Transmit Channel A DAC Differential (+) Output</td></tr>
<tr><td id="6-1w">29</td><td id="6-1x">IOUT+B</td><td id="6-1y">Transmit Channel B DAC Differential (+) Output</td></tr>
<tr><td id="6-1z">30</td><td id="6-1A">IOUT-B</td><td id="6-1B">Transmit Channel B DAC Differential (-) Output</td></tr>
<tr><td id="6-1C">37-48/50</td><td id="6-1D">Tx11/Tx13 to Tx0</td><td id="6-1E">12-/14-Bit Transmit DAC Data (Interleaved Data when Required)</td></tr>
<tr><td id="6-1F">51</td><td id="6-1G">TxSYNC</td><td id="6-1H">Synchronization Input for Transmitter</td></tr>
<tr><td id="6-1I">62</td><td id="6-1J">MODE/ TxBLANK*</td><td id="6-1K">Configures Default Timing Mode, Controls Tx Digital Power Down</td></tr>
</table>
*The logic level of the Mode/TxBLANK pin at power up defines the default timing
mode; a logic low configures Normal Operation, logic high configures Alternate
Operation Mode.

<a id='8459d6ca-79d0-45a9-9411-1a43a1ffac5f'></a>

<table id="6-1L">
<tr><td id="6-1M">Pin No.</td><td id="6-1N">Mnemonic</td><td id="6-1O">Function</td></tr>
<tr><td id="6-1P" colspan="3">Clock Pins</td></tr>
<tr><td id="6-1Q">10</td><td id="6-1R">DLL_Lock</td><td id="6-1S">DLL Lock Indicator Pin</td></tr>
<tr><td id="6-1T">11, 16</td><td id="6-1U">AGND</td><td id="6-1V">DLL Analog Ground Pins</td></tr>
<tr><td id="6-1W">12</td><td id="6-1X">NC</td><td id="6-1Y">No Connect</td></tr>
<tr><td id="6-1Z">13</td><td id="6-20">AVDD</td><td id="6-21">DLL Analog Supply Pin</td></tr>
<tr><td id="6-22">14</td><td id="6-23">OSC1</td><td id="6-24">Single Ended Input Clock (or Crystal Oscillator Input)</td></tr>
<tr><td id="6-25">15</td><td id="6-26">OSC2</td><td id="6-27">Crystal Oscillator Input</td></tr>
<tr><td id="6-28">17</td><td id="6-29">CLKSEL</td><td id="6-2a">Controls CLKOUT1 Rate</td></tr>
<tr><td id="6-2b">64</td><td id="6-2c">CLKOUT2</td><td id="6-2d">Clock Output Generated from Input Clock (DLL Multiplier Setting and CLKOUT2 Divide Factor)</td></tr>
<tr><td id="6-2e">65</td><td id="6-2f">CLKOUT1</td><td id="6-2g">Clock Output Generated from Input Clock (1× if CLKSEL = 1 or /2 if CLKSEL = 0)</td></tr>
<tr><td id="6-2h" colspan="3">Various Pins</td></tr>
<tr><td id="6-2i">1</td><td id="6-2j">AUX_ADC_A1</td><td id="6-2k">Auxiliary ADC A Input 1</td></tr>
<tr><td id="6-2l">3, 4, 13</td><td id="6-2m">AVDD</td><td id="6-2n">Analog Power Pins</td></tr>
<tr><td id="6-2o">2, 9</td><td id="6-2p">AGND</td><td id="6-2q">Analog Ground Pins</td></tr>
<tr><td id="6-2r">5</td><td id="6-2s">SIGDELT</td><td id="6-2t">Digital Output from Programmable Sigma-Delta</td></tr>
<tr><td id="6-2u">6</td><td id="6-2v">AUX_DAC_A</td><td id="6-2w">Auxiliary DAC A Output</td></tr>
<tr><td id="6-2x">7</td><td id="6-2y">AUX_DAC_B</td><td id="6-2z">Auxiliary DAC B Output</td></tr>
<tr><td id="6-2A">8</td><td id="6-2B">AUX_DAC_C</td><td id="6-2C">Auxiliary DAC C Output</td></tr>
<tr><td id="6-2D">33, 36, 53,</td><td id="6-2E">DVDD</td><td id="6-2F">Digital Power Supply Pin</td></tr>
<tr><td id="6-2G">59, 61, 66, 93</td><td id="6-2H"></td><td id="6-2I"></td></tr>
<tr><td id="6-2J">34, 35, 52</td><td id="6-2K">DGND</td><td id="6-2L">Digital Ground Pin</td></tr>
<tr><td id="6-2M">58, 60, 67, 94</td><td id="6-2N"></td><td id="6-2O"></td></tr>
<tr><td id="6-2P">54</td><td id="6-2Q">SCLK</td><td id="6-2R">Serial Bus Clock Input</td></tr>
<tr><td id="6-2S">55</td><td id="6-2T">SDO</td><td id="6-2U">Serial Bus Data Bit</td></tr>
<tr><td id="6-2V">56</td><td id="6-2W">SDIO</td><td id="6-2X">Serial Bus Data Bit</td></tr>
<tr><td id="6-2Y">57</td><td id="6-2Z">SEN</td><td id="6-30">Serial Bus Enable</td></tr>
<tr><td id="6-31">63</td><td id="6-32">RESETB</td><td id="6-33">Reset (SPI Registers and Logic)</td></tr>
<tr><td id="6-34">95</td><td id="6-35">AUX_SPI_do</td><td id="6-36">Optional Auxiliary ADC Serial Bus Data Out Bit</td></tr>
<tr><td id="6-37">96</td><td id="6-38">AUX_SPI_clk</td><td id="6-39">Optional Auxiliary ADC Serial Bus Data Out Latch Clock</td></tr>
<tr><td id="6-3a">97</td><td id="6-3b">AUX_SPI_csb</td><td id="6-3c">Optional Auxiliary ADC Serial Bus Chip Select Bit</td></tr>
<tr><td id="6-3d">128</td><td id="6-3e">AUX_ADC_A2</td><td id="6-3f">Auxiliary ADC A Input 2</td></tr>
<tr><td id="6-3g">126</td><td id="6-3h">AUX_ADC_B1</td><td id="6-3i">Auxiliary ADC B Input 1</td></tr>
<tr><td id="6-3j">125</td><td id="6-3k">AUX_ADC_B2</td><td id="6-3l">Auxiliary ADC B Input 2</td></tr>
<tr><td id="6-3m">127</td><td id="6-3n">AUX_ADC_REF</td><td id="6-3o">Auxiliary ADC Reference</td></tr>
</table>

<a id='69e4af4a-c83b-425d-83b4-680464a48e76'></a>

REV. 0

<a id='418e089e-7cc2-4dbe-a607-2ebf006d5e48'></a>

-7-