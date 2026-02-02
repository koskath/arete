<a id='048e1eef-45e1-4984-97ec-117829949e49'></a>

Electrical characteristics

<a id='6ce4e4ad-f0d3-44f1-994d-569fc85a89a9'></a>

VL53L1X

<a id='d180aff2-fb6e-490a-b424-c45e7cb72550'></a>

5.4 Current consumption
Table 16. Power consumption at ambient temperature (1)
<table id="23-1">
<tr><td id="23-2">Parameter</td><td id="23-3">Min.</td><td id="23-4">Typ.</td><td id="23-5">Max.</td><td id="23-6">Unit</td></tr>
<tr><td id="23-7">HW standby</td><td id="23-8">3</td><td id="23-9">5</td><td id="23-a">7</td><td id="23-b" rowspan="3">uA</td></tr>
<tr><td id="23-c">SW standby (2)</td><td id="23-d">4</td><td id="23-e">6</td><td id="23-f">9</td></tr>
<tr><td id="23-g">Inter measurement</td><td id="23-h"></td><td id="23-i">20</td><td id="23-j"></td></tr>
<tr><td id="23-k">Ranging average (AVDD + AVDDVCSEL) (3) (4)</td><td id="23-l"></td><td id="23-m">16</td><td id="23-n">18</td><td id="23-o">mA</td></tr>
<tr><td id="23-p">Average power consumption at 10 Hz with 33 ms timing budget</td><td id="23-q"></td><td id="23-r"></td><td id="23-s">20</td><td id="23-t" rowspan="3">mW</td></tr>
<tr><td id="23-u">Average power consumption at 1 Hz with 20 ms timing budget when no target detected</td><td id="23-v"></td><td id="23-w">0.9</td><td id="23-x"></td></tr>
<tr><td id="23-y">Average power consumption at 1 Hz with 20 ms timing budget when target detected</td><td id="23-z"></td><td id="23-A">1.4</td><td id="23-B"></td></tr>
</table>
1. All current consumption values include silicon process variations. Temperature and voltage are nominal
conditions (23 °C and AVDD 2v8). All values include AVDD and AVDDVCSEL.
2. In 2v8 (IOVDD) mode, pull ups have to be modified, then SW Standby consumption is increased by 0.6 μΑ.
3. Average consumption during ranging operation in long distance mode.
4. Peak current (including VCSEL) can reach 40 mA.

<a id='4c7a901f-f721-48f1-9cb1-6252deb2cd4a'></a>

5.5 Digital I/O electrical characteristics
Table 17. Digital I/O electrical characteristics
<table id="23-C">
<tr><td id="23-D"></td><td id="23-E">Symbol</td><td id="23-F">Parameter</td><td id="23-G">Min.</td><td id="23-H">Typ.</td><td id="23-I">Max.</td><td id="23-J">Unit</td></tr>
<tr><td id="23-K" rowspan="5">Interrupt pin (GPIO1)</td><td id="23-L">VIL</td><td id="23-M">Low level input voltage</td><td id="23-N">–</td><td id="23-O" rowspan="5"></td><td id="23-P">0.3 IOVDD</td><td id="23-Q" rowspan="4">V</td></tr>
<tr><td id="23-R">VIH</td><td id="23-S">High level input voltage</td><td id="23-T">0.7 IOVDD</td><td id="23-U"></td></tr>
<tr><td id="23-V">VOL</td><td id="23-W">Low level output voltage (IOUT = 4 mA)</td><td id="23-X">–</td><td id="23-Y">0.4</td></tr>
<tr><td id="23-Z">VOH</td><td id="23-10">High level output voltage (IOUT = 4 mA)</td><td id="23-11">IOVDD-0.4</td><td id="23-12"></td></tr>
<tr><td id="23-13">FGPIO</td><td id="23-14">Operating frequency (CLOAD = 20 pF)</td><td id="23-15">0</td><td id="23-16">108</td><td id="23-17">MHz</td></tr>
<tr><td id="23-18" rowspan="5">I²C interface (SDA/SCL)</td><td id="23-19">VIL</td><td id="23-1a">Low level input voltage</td><td id="23-1b">-0.5</td><td id="23-1c" rowspan="5"></td><td id="23-1d">0.6</td><td id="23-1e" rowspan="3">V</td></tr>
<tr><td id="23-1f">VIH</td><td id="23-1g">High level input voltage</td><td id="23-1h">1.12</td><td id="23-1i">IOVDD+0.5</td></tr>
<tr><td id="23-1j">VOL</td><td id="23-1k">Low level output voltage (IOUT = 4 mA)</td><td id="23-1l">- (hyphen)</td><td id="23-1m">0.4</td></tr>
<tr><td id="23-1n" rowspan="2">I_IL / I_IH</td><td id="23-1o">Leakage current (1)</td><td id="23-1p">- (hyphen)</td><td id="23-1q">10</td><td id="23-1r" rowspan="2">μA</td></tr>
<tr><td id="23-1s">Leakage current (2)</td><td id="23-1t"></td><td id="23-1u">0.15</td></tr>
</table>
1. AVDD = 0 V
2. AVDD = 2.85 V; I/O voltage = 1.8 V

<a id='025c47ea-73dd-466d-8346-0f49136c8bb6'></a>

24/35

<a id='2a07239d-a85e-4f01-ad0e-307d8ed738ed'></a>

DocID031281 Rev 3

<a id='ed279a70-56a8-432a-908a-5a017b4fa045'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>