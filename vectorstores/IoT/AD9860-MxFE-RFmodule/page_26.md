<a id='16cce169-abdc-45e9-90e3-36bdf5e7899e'></a>

AD9860/AD9862

The timing block diagrams in Figures 10 and 11 show how the various clocks of the single and dual Tx path are affected by the various register settings.

<a id='a42f7cb2-ecf5-4fc8-8e4a-9e80cabab83d'></a>

For dual Tx data, an option to redirect demultiplexed data to
either path is available. For example, the AD9860/AD9862 can
accept complex data in the form of I then Q data or Q then I data,
controlled through QI Order register.

<a id='bce8fa1a-ad79-43eb-96f2-7fbe239729a2'></a>

For the dual Tx data cases, the Tx_SYNC Pin input logic level defines what data is currently on the Tx data bus. By default, when Tx_SYNC is low, Channel A data (first of the set) should be on the data bus; if TxSYNC is high, Channel B data (or the second of the set) should be on the Tx bus. This can be reversed be setting the Inv TxSYNC register.

<a id='5430d899-9264-43f1-b6b9-2413346eb8db'></a>

**Rx Path (Alternative Timing Operation)**
The ADC sampling rate, the Rx data output rate and the rate of CLKOUT1 (clock used to latch output data) are the parameters of interest for the receive path data. These parameters, in addition to the data bandwidth, are related to CLKIN by decimation filters, divide by two circuits, data multiplexer logic retiming latches and also the DLL multiplication setting (which is not the case for Normal Operation mode). This mode can be configured by default by forcing the Tx_Blank_In pin to a logic high level during power up.

<a id='aa13c3a5-7407-456e-b3fe-65571664e3f2'></a>

The Rx path timing can be broken into two separate relationships:
the ADC sample rate relative to the input clock, CLKIN and
the output data rate relative to CLKOUT1.

<a id='8165c49b-d84a-41e9-a2e2-84de7a8a026f'></a>

The ADCs sample rate relative to CLKIN is controlled by the ADC Div2 register and the DLL Multiplier register. The sample rate can be equal to or one half of the DLL output clock rate.

<a id='b48d24b6-dd6a-4293-b42e-95d5f3166d1f'></a>

The output data rate relative to CLKOUT1 for the Alternative
Operation Mode has the same configuration options as in the
Normal Operation Mode. The different options are shown in
Figure 9. Table Ia. and Ib. describe the setup required to obtain
the desired data timing.

<a id='3fb16e94-a751-46c9-a374-593799250d96'></a>

The Rx data (unless retimed using the Rx Retime register) is timed relative to the CLKOUT1 pin output. The Rx output data can be decimated (halving the data rate) or both channels can be multiplexed onto the Channel A data bus (doubling the data rate).

<a id='9be4b0bb-5805-4272-a2c1-17893851c5cb'></a>

Decimation enables oversampling while maintaining a slower external data transfer rate and provides superior suppression of out of band signals and noise. Multiplexing enables fewer digital output bits to be used to transfer data from the Rx path to the digital ASIC collecting the data.

<a id='b109bf77-46a3-4f2f-bc82-24c4e7a7424c'></a>

When Multiplexing mode is enabled with an output data rate equal to CLKOUT1 (Timing No. 3 in Figure 9), then the RxSync pin is required to identify which channel's output data is on the output data bus. RxSync output is aligned with the output data and by default, a logic low indicates data from Rx Channel B is currently on the output data bus. If RxSync is logic high, then data from Rx Channel A is currently on the output data bus. The Inv RxSync register can be used to switch this notation.

<a id='a68571d2-1aee-462b-aad3-91756ff77555'></a>

The CLKOUT1 pin outputs a clock at a frequency of CLKIN or CLKIN/2 depending on the voltage level applied to the CLKSEL

<a id='774c3831-4b5b-4e74-b345-361127403f48'></a>

pin. If a logic low is applied to CLKSEL, CLKOUT1 will run at half the CLKIN rate; if CLKSEL is set to logic high, CLKOUT1 outputs a clock equal to CLKIN.

<a id='b5dcba5a-e6a4-4e21-a07d-758f2405d846'></a>

This timing flexibility, along with the invert option for CLKOUT1 controlled by the Inv 1 Register, allows for various methods of latching data from the Rx path to the digital ASIC, which will pro-cess the data. These options are shown in Table Ia and Ib along with a timing diagram in Figure 9. Not shown is the option to invert CLKOUT1, controlled by the Inv 1 register. For this mode, relative timing remains the same except the opposite edges of CLKOUT1 would be used.

<a id='a90d549d-6054-486d-96f4-de17d514c99e'></a>

Overall, relative timing can be found by using the Alternative
Operation Mode Master Timing Guide in Table V and using Rx
timing shown in Figure 9.

<a id='1d660943-67f5-4fa8-9529-ac5d146de8c5'></a>

**Tx Path (Alternative Timing Operation)**
The DAC update rate, the Tx input data rate and the rate of CLKOUT2 (clock used to latch Tx input data) are the parameters of interest for the transmit path data. These parameters in addition to the output signal bandwidth are related to CLKIN by the settings of the DLL multiplier, the CLKOUT2 Div, the two edge and the Interpolation registers (in this mode, the ADC Div2 register does not affect Tx timing).

<a id='98a0be30-b95d-4c1c-ab0e-1bebf8224188'></a>

The Tx data is timed relative to the CLKOUT2 pin (unless it is retimed relative to CLKOUT1 by setting Tx Retime register) and remains the same as it does in Normal Operation Mode. The input Tx data is latched on each rising edge, each falling edge or both edges (controlled through the Inverse Sample and two edge regis- ters). The timing diagrams for these cases are shown in Figure 12.

<a id='483213b5-e948-4447-a683-45283d52290a'></a>

The Dual Tx data is multiplexed onto a single bus so that fewer
digital bits are necessary to transfer data. Throughout this discus-
sion of Tx path timing, Tx digital processing options other than
interpolation are ignored because they do not change data timing;
Tx data timing reflects whether single or dual channel data is
latched into the AD9860/AD9862.

<a id='de6c25a1-9219-41b5-add9-c75fa12aa8b8'></a>

The rates of CLKOUT2 (and the input data rate) are related to CLKIN by the DLL Multiplier register and the setting of the CLKOUT2 Divide Factor register. These relationships are shown in Table III.

<a id='51d68241-ecb4-43b0-b014-b34aa4a75aa5'></a>

Table III. CLKOUT2 Timing Relative to CLKIN
In Alternative Operation Mode
<table id="27-1">
<tr><td id="27-2">DLL Mult</td><td id="27-3">CLKOUT2 Div Factor</td><td id="27-4">CLKOUT2</td></tr>
<tr><td id="27-5">1X</td><td id="27-6">/1</td><td id="27-7">CLKIN</td></tr>
<tr><td id="27-8"></td><td id="27-9">/2</td><td id="27-a">CLKIN/2</td></tr>
<tr><td id="27-b"></td><td id="27-c">/4</td><td id="27-d">CLKIN/4</td></tr>
<tr><td id="27-e">2X</td><td id="27-f">/1</td><td id="27-g">2×CLKIN</td></tr>
<tr><td id="27-h"></td><td id="27-i">/2</td><td id="27-j">CLKIN</td></tr>
<tr><td id="27-k"></td><td id="27-l">/4</td><td id="27-m">CLKIN/2</td></tr>
<tr><td id="27-n">4X</td><td id="27-o">/1</td><td id="27-p">4XCLKIN</td></tr>
<tr><td id="27-q"></td><td id="27-r">/2</td><td id="27-s">2XCLKIN</td></tr>
<tr><td id="27-t"></td><td id="27-u">/4</td><td id="27-v">CLKIN</td></tr>
</table>

<a id='1dd479a8-cb10-41da-96bf-ac1688ab1398'></a>

-28-

<a id='272dac48-e753-4142-b20c-a9d584330d6e'></a>

REV. 0