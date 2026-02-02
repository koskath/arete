<a id='7c0336d4-ba0f-4543-b6b0-a2f225cb31cc'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='341bd3f8-ed97-4c32-8906-84e29ef006cd'></a>

Arduino® MKR WiFi 1010

<a id='ca124b68-cfe9-41c1-bf7f-89706ea2f0fd'></a>

5 Connector Pinouts

<a id='8a8f328c-130e-437b-9915-e723d99e2fa6'></a>

5.1 USB
<table id="9-1">
<tr><td id="9-2">Pin</td><td id="9-3">Function</td><td id="9-4">Type</td><td id="9-5">Description</td></tr>
<tr><td id="9-6">1</td><td id="9-7">VUSB</td><td id="9-8">Power</td><td id="9-9">Power Supply Input. Output is powered via VUSB from header</td></tr>
<tr><td id="9-a">2</td><td id="9-b">D-</td><td id="9-c">Differential</td><td id="9-d">USB differential data -</td></tr>
<tr><td id="9-e">3</td><td id="9-f">D+</td><td id="9-g">Differential</td><td id="9-h">USB differential data +</td></tr>
<tr><td id="9-i">4</td><td id="9-j">ID</td><td id="9-k">Analog</td><td id="9-l">Selects Host/Device functionality</td></tr>
<tr><td id="9-m">5</td><td id="9-n">GND</td><td id="9-o">Power</td><td id="9-p">Supply Ground</td></tr>
</table>

<a id='271c4a86-16e5-423b-ab23-6a9b536ab8bc'></a>

NOTE: This board can support USB host mode only if powered via the VUSB pin and if the jumper close to the VUSB pin is shorted.

<a id='c1fb7ce4-ea2b-4207-ab73-25256b06c9d3'></a>

5.2 Headers

<a id='6de7e03a-1bbe-4d31-bfd1-13841cccee58'></a>

Board exposes two 28 pin connectors assembled with pin headers.
<table id="9-q">
<tr><td id="9-r">Pin</td><td id="9-s">Function</td><td id="9-t">Type</td><td id="9-u">Description</td></tr>
<tr><td id="9-v">1</td><td id="9-w">AREF</td><td id="9-x">Analog</td><td id="9-y">Analog Reference.</td></tr>
<tr><td id="9-z">2</td><td id="9-A">A0/DACO</td><td id="9-B">Analog</td><td id="9-C">ADC in/DAC out, Can be used as GPIO</td></tr>
<tr><td id="9-D">3</td><td id="9-E">A1</td><td id="9-F">Analog</td><td id="9-G">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-H">4</td><td id="9-I">A2</td><td id="9-J">Analog</td><td id="9-K">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-L">5</td><td id="9-M">A3</td><td id="9-N">Analog</td><td id="9-O">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-P">6</td><td id="9-Q">A4/SDA</td><td id="9-R">Analog</td><td id="9-S">ADC in, I2C SDA, Can be used as GPIO</td></tr>
<tr><td id="9-T">7</td><td id="9-U">A5/SCL</td><td id="9-V">Analog</td><td id="9-W">ADC in, I2C SCL, Can be used as GPIO</td></tr>
<tr><td id="9-X">8</td><td id="9-Y">A6</td><td id="9-Z">Analog</td><td id="9-10">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-11">9</td><td id="9-12">D0</td><td id="9-13">Digital</td><td id="9-14">GPIO, can be used as PWM</td></tr>
<tr><td id="9-15">10</td><td id="9-16">D1</td><td id="9-17"></td><td id="9-18">GPIO, can be used as PWM</td></tr>
<tr><td id="9-19">11</td><td id="9-1a">D2/PWM</td><td id="9-1b">Digital</td><td id="9-1c">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1d">12</td><td id="9-1e">D3/PWM</td><td id="9-1f">Digital</td><td id="9-1g">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1h">13</td><td id="9-1i">D4/PWM</td><td id="9-1j">Digital</td><td id="9-1k">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1l">14</td><td id="9-1m">D5/PWM</td><td id="9-1n">Digital</td><td id="9-1o">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1p">15</td><td id="9-1q">D6</td><td id="9-1r">Digital</td><td id="9-1s">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1t">16</td><td id="9-1u">D7</td><td id="9-1v">Digital</td><td id="9-1w">GPIO can be used as PWM</td></tr>
<tr><td id="9-1x">17</td><td id="9-1y">D8/MOSI</td><td id="9-1z">Digital</td><td id="9-1A">SPI MOSI, can be used as GPIO, can be used as PWM</td></tr>
<tr><td id="9-1B">18</td><td id="9-1C">D9/SCK</td><td id="9-1D">Digital</td><td id="9-1E">SPI SCK, can be used as GPIO, can be used as PWM</td></tr>
<tr><td id="9-1F">19</td><td id="9-1G">D10/MISO</td><td id="9-1H">Digital</td><td id="9-1I">SPI MISO, can be used as GPIO</td></tr>
<tr><td id="9-1J">20</td><td id="9-1K">D11/SDA</td><td id="9-1L">Digital</td><td id="9-1M">I2C SDA, can be used as GPIO</td></tr>
<tr><td id="9-1N">21</td><td id="9-1O">D12/SCL</td><td id="9-1P">Digital</td><td id="9-1Q">I2C SCL, can be used as GPIO</td></tr>
<tr><td id="9-1R">22</td><td id="9-1S">D13/RX</td><td id="9-1T">Digital</td><td id="9-1U">USART RX, can be used as GPIO</td></tr>
<tr><td id="9-1V">23</td><td id="9-1W">D14/TX</td><td id="9-1X">Digital</td><td id="9-1Y">USART TX, can be used as GPIO</td></tr>
<tr><td id="9-1Z">24</td><td id="9-20">RESETN</td><td id="9-21">Digital</td><td id="9-22">Reset input</td></tr>
<tr><td id="9-23">25</td><td id="9-24">GND</td><td id="9-25">Power</td><td id="9-26">Power Ground</td></tr>
<tr><td id="9-27">26</td><td id="9-28">+3V3</td><td id="9-29">Power Out</td><td id="9-2a"></td></tr>
</table>

<a id='d44687f5-c075-4086-a293-3d0e5258f41f'></a>

10 / 16

<a id='f69acb5b-163a-4343-95cd-aaa21cc9d194'></a>

Arduino® MKR WiFi 1010

<a id='bad0f957-88ee-4b77-ab0d-f8ee1d265af2'></a>

Modified: 05/11/2025