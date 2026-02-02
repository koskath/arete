<a id='3c8d3b52-ed76-48c5-9201-6a7794534859'></a>

AD9860/AD9862

<a id='63239eed-9311-420d-b500-6af0a986235e'></a>

REGISTER MAP (0x00–0x3F)¹
<table id="11-1">
<tr><td id="11-2">Register Name</td><td id="11-3">Address²</td><td id="11-4">Bit 7</td><td id="11-5">Bit 6</td><td id="11-6">Bit 5</td><td id="11-7">Bit 4</td><td id="11-8">Bit 3</td><td id="11-9">Bit 2</td><td id="11-a">Bit 1</td><td id="11-b">Bit 0</td><td id="11-c">Purpose</td></tr>
<tr><td id="11-d">General</td><td id="11-e">0</td><td id="11-f">SDIO BiDir</td><td id="11-g">LSB First</td><td id="11-h">Soft Reset</td><td id="11-i"></td><td id="11-j"></td><td id="11-k"></td><td id="11-l"></td><td id="11-m"></td><td id="11-n">SPI Setup</td></tr>
<tr><td id="11-o">Rx Power Down</td><td id="11-p">1</td><td id="11-q">VREF (diff)</td><td id="11-r">VREF</td><td id="11-s">Rx Digital</td><td id="11-t">Rx Channel B</td><td id="11-u">Rx Channel A</td><td id="11-v">Buffer B</td><td id="11-w">Buffer A</td><td id="11-x">All Rx</td><td id="11-y" rowspan="6">Receive Path Setup</td></tr>
<tr><td id="11-z">Rx A</td><td id="11-A">2</td><td id="11-B">Byp Buffer A</td><td id="11-C"></td><td id="11-D"></td><td id="11-E" colspan="5">RxPGA A</td></tr>
<tr><td id="11-F">Rx B</td><td id="11-G">3</td><td id="11-H">Byp Buffer B</td><td id="11-I"></td><td id="11-J"></td><td id="11-K" colspan="5">RxPGA B</td></tr>
<tr><td id="11-L">Rx Misc</td><td id="11-M">4</td><td id="11-N"></td><td id="11-O"></td><td id="11-P"></td><td id="11-Q"></td><td id="11-R"></td><td id="11-S">HS Duty Cycle</td><td id="11-T">Shared Ref</td><td id="11-U">Clk Duty</td></tr>
<tr><td id="11-V">Rx I/F</td><td id="11-W">5</td><td id="11-X"></td><td id="11-Y"></td><td id="11-Z"></td><td id="11-10">Three State</td><td id="11-11">Rx Retime</td><td id="11-12">Twos Complement</td><td id="11-13">Inv RxSync</td><td id="11-14">Mux Out</td></tr>
<tr><td id="11-15">Rx Digital</td><td id="11-16">6</td><td id="11-17"></td><td id="11-18"></td><td id="11-19"></td><td id="11-1a"></td><td id="11-1b">2 Channel</td><td id="11-1c">Keep -ve</td><td id="11-1d">Hilbert</td><td id="11-1e">Decimate</td></tr>
<tr><td id="11-1f">RSV</td><td id="11-1g">7</td><td id="11-1h" colspan="8">Reserved for Future Use</td><td id="11-1i" rowspan="14">Transmit Path Setup</td></tr>
<tr><td id="11-1j">Tx Power Down</td><td id="11-1k">8</td><td id="11-1l"></td><td id="11-1m"></td><td id="11-1n">Alt Timing Mode</td><td id="11-1o">TxOff Enable</td><td id="11-1p">Tx Digital</td><td id="11-1q" colspan="3">Tx Analog Power Down [2:0]</td></tr>
<tr><td id="11-1r">RSV</td><td id="11-1s">9</td><td id="11-1t" colspan="8">Reserved for Future Use</td></tr>
<tr><td id="11-1u">Tx A Offset</td><td id="11-1v">10</td><td id="11-1w" colspan="2">DAC A Offset [1:0]</td><td id="11-1x"></td><td id="11-1y"></td><td id="11-1z"></td><td id="11-1A"></td><td id="11-1B"></td><td id="11-1C">DAC A Offset Direction</td></tr>
<tr><td id="11-1D">Tx A Offset</td><td id="11-1E">11</td><td id="11-1F" colspan="8">DAC A Offset [9:2]</td></tr>
<tr><td id="11-1G">Tx B Offset</td><td id="11-1H">12</td><td id="11-1I" colspan="2">DAC B Offset [1:0]</td><td id="11-1J"></td><td id="11-1K"></td><td id="11-1L"></td><td id="11-1M"></td><td id="11-1N"></td><td id="11-1O">DAC B Offset Direction</td></tr>
<tr><td id="11-1P">Tx B Offset</td><td id="11-1Q">13</td><td id="11-1R" colspan="8">DAC B Offset [9:2]</td></tr>
<tr><td id="11-1S">Tx A Gain</td><td id="11-1T">14</td><td id="11-1U" colspan="2">DAC A Coarse Gain</td><td id="11-1V" colspan="6">DAC A Fine Gain</td></tr>
<tr><td id="11-1W">Tx B Gain</td><td id="11-1X">15</td><td id="11-1Y" colspan="2">DAC B Coarse Gain</td><td id="11-1Z" colspan="6">DAC B Fine Gain</td></tr>
<tr><td id="11-20">Tx PGA Gain</td><td id="11-21">16</td><td id="11-22" colspan="8">Tx PGA Gain</td></tr>
<tr><td id="11-23">Tx Misc</td><td id="11-24">17</td><td id="11-25"></td><td id="11-26"></td><td id="11-27"></td><td id="11-28"></td><td id="11-29"></td><td id="11-2a"></td><td id="11-2b">Slave Enable</td><td id="11-2c">Tx PGA Fast</td></tr>
<tr><td id="11-2d">Tx I/F</td><td id="11-2e">18</td><td id="11-2f"></td><td id="11-2g">Tx Retime</td><td id="11-2h">Q/I Order</td><td id="11-2i">Inv TxSync</td><td id="11-2j">Twos Complement</td><td id="11-2k">Inverse Sample</td><td id="11-2l">2 Edges</td><td id="11-2m">Interleaved</td></tr>
<tr><td id="11-2n">Tx Digital</td><td id="11-2o">19</td><td id="11-2p"></td><td id="11-2q"></td><td id="11-2r"></td><td id="11-2s">2 Data Paths</td><td id="11-2t">Keep -ve</td><td id="11-2u">Hilbert</td><td id="11-2v" colspan="2">Interpolation Control</td></tr>
<tr><td id="11-2w">Tx Modulator</td><td id="11-2x">20</td><td id="11-2y"></td><td id="11-2z"></td><td id="11-2A">Neg. Fine Tune</td><td id="11-2B">Fine Mode</td><td id="11-2C">Real Mix</td><td id="11-2D">Neg. Coarse Tune</td><td id="11-2E" colspan="2">Coarse Modulation</td></tr>
<tr><td id="11-2F">NCO Tuning Word</td><td id="11-2G">21</td><td id="11-2H" colspan="8">FTW [7:0]</td><td id="11-2I" rowspan="3">NCO Setup</td></tr>
<tr><td id="11-2J">NCO Tuning Word</td><td id="11-2K">22</td><td id="11-2L" colspan="8">FTW [15:8]</td></tr>
<tr><td id="11-2M">NCO Tuning Word</td><td id="11-2N">23</td><td id="11-2O" colspan="8">FTW [23:16]</td></tr>
<tr><td id="11-2P">DLL</td><td id="11-2Q">24</td><td id="11-2R">Reserved</td><td id="11-2S">Input Control Clock</td><td id="11-2T">ADC Div 2</td><td id="11-2U" colspan="2">DLL Multiplier</td><td id="11-2V">DLL Power Down</td><td id="11-2W"></td><td id="11-2X">DLL FAST</td><td id="11-2Y" rowspan="2">Clock Setup</td></tr>
<tr><td id="11-2Z">CLKOUT</td><td id="11-30">25</td><td id="11-31" colspan="2">CLKOUT2 Divide Factor</td><td id="11-32">Inv2</td><td id="11-33">Dis2</td><td id="11-34"></td><td id="11-35"></td><td id="11-36">Inv1</td><td id="11-37">Dis 1</td></tr>
<tr><td id="11-38">Aux ADC A2</td><td id="11-39">26</td><td id="11-3a" colspan="2">Aux ADC A2 Data [1:0]</td><td id="11-3b"></td><td id="11-3c"></td><td id="11-3d"></td><td id="11-3e"></td><td id="11-3f" colspan="2"></td><td id="11-3g" rowspan="10">Auxiliary ADC Data and Setup</td></tr>
<tr><td id="11-3h">Aux ADC A2</td><td id="11-3i">27</td><td id="11-3j" colspan="8">Aux ADC A2 Data [9:2]</td></tr>
<tr><td id="11-3k">Aux ADC A1</td><td id="11-3l">28</td><td id="11-3m" colspan="2">Aux ADC A1 Data [1:0]</td><td id="11-3n"></td><td id="11-3o"></td><td id="11-3p"></td><td id="11-3q"></td><td id="11-3r"></td><td id="11-3s"></td></tr>
<tr><td id="11-3t">Aux ADC A1</td><td id="11-3u">29</td><td id="11-3v" colspan="8">Aux ADC A1 Data [9:2]</td></tr>
<tr><td id="11-3w">Aux ADC B2</td><td id="11-3x">30</td><td id="11-3y" colspan="2">Aux ADC B2 Data [1:0]</td><td id="11-3z"></td><td id="11-3A"></td><td id="11-3B"></td><td id="11-3C"></td><td id="11-3D"></td><td id="11-3E"></td></tr>
<tr><td id="11-3F">Aux ADC B2</td><td id="11-3G">31</td><td id="11-3H" colspan="8">Aux ADC B2 Data [9:2]</td></tr>
<tr><td id="11-3I">Aux ADC B1</td><td id="11-3J">32</td><td id="11-3K" colspan="2">Aux ADC B1 Data [1:0]</td><td id="11-3L"></td><td id="11-3M"></td><td id="11-3N"></td><td id="11-3O"></td><td id="11-3P"></td><td id="11-3Q"></td></tr>
<tr><td id="11-3R">Aux ADC B1</td><td id="11-3S">33</td><td id="11-3T" colspan="8">Aux ADC B1 Data [9:2]</td></tr>
<tr><td id="11-3U">Aux ADC Control</td><td id="11-3V">34</td><td id="11-3W">Aux SPI</td><td id="11-3X">SelBnot A</td><td id="11-3Y">Refsel B</td><td id="11-3Z">Select B</td><td id="11-40">Start B</td><td id="11-41">Refsel A</td><td id="11-42">Select A</td><td id="11-43">Start A</td></tr>
<tr><td id="11-44">Aux ADC Clock</td><td id="11-45">35</td><td id="11-46"></td><td id="11-47"></td><td id="11-48"></td><td id="11-49"></td><td id="11-4a"></td><td id="11-4b"></td><td id="11-4c"></td><td id="11-4d">CLK/4</td></tr>
<tr><td id="11-4e">Aux DAC A</td><td id="11-4f">36</td><td id="11-4g" colspan="8">Aux DAC A</td><td id="11-4h" rowspan="6">Auxiliary DAC Data and Setup</td></tr>
<tr><td id="11-4i">Aux DAC B</td><td id="11-4j">37</td><td id="11-4k" colspan="8">Aux DAC B</td></tr>
<tr><td id="11-4l">Aux DAC C</td><td id="11-4m">38</td><td id="11-4n" colspan="8">Aux DAC C</td></tr>
<tr><td id="11-4o">Aux DAC</td><td id="11-4p">39</td><td id="11-4q" colspan="2">Slave Enable</td><td id="11-4r"></td><td id="11-4s"></td><td id="11-4t"></td><td id="11-4u">Update C</td><td id="11-4v">Update B</td><td id="11-4w">Update A</td></tr>
<tr><td id="11-4x">Update Aux DAC</td><td id="11-4y">40</td><td id="11-4z"></td><td id="11-4A"></td><td id="11-4B"></td><td id="11-4C"></td><td id="11-4D"></td><td id="11-4E">Power Down C</td><td id="11-4F">Power Down B</td><td id="11-4G">Power Down A</td></tr>
<tr><td id="11-4H">DAC Control</td><td id="11-4I">41</td><td id="11-4J"></td><td id="11-4K"></td><td id="11-4L"></td><td id="11-4M">Inv C</td><td id="11-4N"></td><td id="11-4O">Inv B</td><td id="11-4P"></td><td id="11-4Q">Inv A</td></tr>
<tr><td id="11-4R">SigDelt</td><td id="11-4S">42</td><td id="11-4T" colspan="4">Sigma-Delta Control Word [3:0]</td><td id="11-4U"></td><td id="11-4V"></td><td id="11-4W"></td><td id="11-4X">Flag</td><td id="11-4Y" rowspan="2">Sigma-Delta Data and Setup</td></tr>
<tr><td id="11-4Z">SigDelt</td><td id="11-50">43</td><td id="11-51" colspan="8">Sigma-Delta Control Word [11:4]</td></tr>
<tr><td id="11-52">ADC Low Power</td><td id="11-53">49, 50</td><td id="11-54" colspan="8">Low Power Register for Rx Path Operation below 32 MSPS</td><td id="11-55" rowspan="2">Rx Low Power</td></tr>
<tr><td id="11-56" rowspan="2">RSV</td><td id="11-57" rowspan="2">44–62</td><td id="11-58" rowspan="2" colspan="8">Reserved for Future Use</td></tr>
<tr><td id="11-59">Reserved</td></tr>
<tr><td id="11-5a"></td><td id="11-5b">63</td><td id="11-5c" colspan="8">Chip Rev ID</td><td id="11-5d">Chip ID</td></tr>
</table>

<a id='7abae037-adc1-415b-8e49-4658a403ae5a'></a>

NOTES
1 When writing to a register with unassigned register bit(s), a logic low must be written to the unassigned bit(s). By default, after power up or RESET, all registers are set low, except for the bits in the shaded boxes, which are set high.
2 Decimal

<a id='bc63c3a1-b0b2-4d70-8f0b-3c3e4a324b37'></a>

-12-

<a id='5afb9712-8ee7-4731-9dc5-65795530f349'></a>

REV. 0