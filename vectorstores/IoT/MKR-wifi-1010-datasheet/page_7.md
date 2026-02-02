<a id='bf5df314-9e8e-4070-b557-65c6a2c3b553'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='5f871c12-e38c-473d-a07e-d1c58daf5df6'></a>

Arduino® MKR WiFi 1010

<a id='1fc78b9c-6631-4ca1-bc80-b5fa186312a6'></a>

2.2 Power Consumption
<table id="6-1">
<tr><td id="6-2">Symbol</td><td id="6-3">Description</td><td id="6-4">Min</td><td id="6-5">Typ</td><td id="6-6">Max</td><td id="6-7">Unit</td></tr>
<tr><td id="6-8">$VIN_{Max}$</td><td id="6-9">Maximum input voltage from VIN pad</td><td id="6-a">-0.3</td><td id="6-b"></td><td id="6-c">5.5</td><td id="6-d">V</td></tr>
<tr><td id="6-e">$VUSB_{Max}$</td><td id="6-f">Maximum input voltage from USB connector</td><td id="6-g">-0.3</td><td id="6-h"></td><td id="6-i">5.5</td><td id="6-j">V</td></tr>
<tr><td id="6-k">$P_{Max}$</td><td id="6-l">Maximum power consumption</td><td id="6-m"></td><td id="6-n"></td><td id="6-o">TBC</td><td id="6-p">mW</td></tr>
</table>

<a id='4a1643a0-4d88-4869-ab49-eb9a97a2ed77'></a>

## 3 Functional Overview

<a id='494808da-3a0b-4688-b5ac-5469e094de39'></a>

## 3.1 Processor
The Main Processor is a Arm® Cortex®-M0+ running at up to 48 MHz.

<a id='4100ed2a-4eb6-44ba-90f0-e0472d4932c3'></a>

Most of its pins are connected to the external headers, however some are reserved for internal communication to the communication module and to the internal SPI and I2C peripherals (Crypto). Communication with NINA Module W102 happens through UART and SPI through the following pins.

<a id='10e2db3b-befb-4d05-b893-9b5ace3e9d7e'></a>

<table id="6-q">
<tr><td id="6-r">Pin</td><td id="6-s">Acronym</td><td id="6-t">NINA Pin</td><td id="6-u">Acronym</td><td id="6-v">Description</td></tr>
<tr><td id="6-w">21</td><td id="6-x">PA12</td><td id="6-y">36</td><td id="6-z">GPIO12</td><td id="6-A">SPI MOSI</td></tr>
<tr><td id="6-B">22</td><td id="6-C">PA13</td><td id="6-D">21</td><td id="6-E">SPIV_DI</td><td id="6-F">NINA_MISO</td></tr>
<tr><td id="6-G">23</td><td id="6-H">PA14</td><td id="6-I">28</td><td id="6-J">SPIV_CS</td><td id="6-K">SPI CS</td></tr>
<tr><td id="6-L">24</td><td id="6-M">PA15</td><td id="6-N">29</td><td id="6-O">SPIV_CLK</td><td id="6-P">SPI CLK</td></tr>
<tr><td id="6-Q">39</td><td id="6-R">PA27</td><td id="6-S">27</td><td id="6-T">GPIOO</td><td id="6-U">NINA_GPIOO</td></tr>
<tr><td id="6-V">7</td><td id="6-W">PB08</td><td id="6-X">19</td><td id="6-Y">RESET</td><td id="6-Z">NINA RESET</td></tr>
<tr><td id="6-10">41</td><td id="6-11">PA28</td><td id="6-12">7</td><td id="6-13">GPIO_33</td><td id="6-14">NINA_ACK</td></tr>
<tr><td id="6-15">23</td><td id="6-16">PA14</td><td id="6-17">21</td><td id="6-18">UART_CTS</td><td id="6-19">NINA_CS</td></tr>
<tr><td id="6-1a">24</td><td id="6-1b">PA15</td><td id="6-1c">20</td><td id="6-1d">UART_CTS</td><td id="6-1e">NINA_SCK</td></tr>
<tr><td id="6-1f">38</td><td id="6-1g">PB23</td><td id="6-1h">22</td><td id="6-1i">UART_RXD</td><td id="6-1j">Serial1_RX</td></tr>
<tr><td id="6-1k">37</td><td id="6-1l">PA22</td><td id="6-1m">23</td><td id="6-1n">UART_TXD</td><td id="6-1o">Serial1_TX</td></tr>
</table>

<a id='11b37c77-01aa-40d8-83d8-770ce33455a4'></a>

7 / 16

<a id='82b70c2e-f065-4318-b936-4b9f7f79acbd'></a>

Arduino® MKR WiFi 1010

<a id='a952d87f-d6db-484c-9bd9-15c808497640'></a>

Modified: 05/11/2025