<a id='57234303-fcf5-422d-bb4b-54adf1a3bd00'></a>

VL53L1X

<a id='ac8f8a4f-7142-47ea-badc-836ece079a9e'></a>

Product overview

<a id='be149aff-187d-4a3b-8baa-3540c25374cd'></a>

## 1.3 Device pinout

Figure 2 shows the pinout of the VL53L1X (see also Figure 18).

<a id='464beb7a-954a-42a8-bac3-b441f8f9f5ca'></a>

Figure 2. VL53L1X pinout (bottom view)

<::VL53L1X pinout diagram:

GND3
GPIO1: 7
DNC: 8
SDA: 9
SCL: 10
AVDD: 11

XSHUT: 5
GND2: 4
GND: 3
AVSSVCSEL: 2
AVDDVCSEL: 1
12
GND4::>

<a id='21217f91-447f-4a05-af4d-a4b2cb12f637'></a>

Table 2. VL53L1X pin description
<table id="4-1">
<tr><td id="4-2">Pin number</td><td id="4-3">Signal name</td><td id="4-4">Signal type</td><td id="4-5">Signal description</td></tr>
<tr><td id="4-6">1</td><td id="4-7">AVDDVCSEL</td><td id="4-8">Supply</td><td id="4-9">VCSEL supply, to be connected to main supply</td></tr>
<tr><td id="4-a">2</td><td id="4-b">AVSSVCSEL</td><td id="4-c">Ground</td><td id="4-d">VCSEL ground, to be connected to main ground</td></tr>
<tr><td id="4-e">3</td><td id="4-f">GND</td><td id="4-g">Ground</td><td id="4-h">To be connected to main ground</td></tr>
<tr><td id="4-i">4</td><td id="4-j">GND2</td><td id="4-k">Ground</td><td id="4-l">To be connected to main ground</td></tr>
<tr><td id="4-m">5</td><td id="4-n">XSHUT</td><td id="4-o">Digital input</td><td id="4-p">Xshutdown pin, active low</td></tr>
<tr><td id="4-q">6</td><td id="4-r">GND3</td><td id="4-s">Ground</td><td id="4-t">To be connected to main ground</td></tr>
<tr><td id="4-u">7</td><td id="4-v">GPIO1</td><td id="4-w">Digital output</td><td id="4-x">Interrupt output. Open drain output</td></tr>
<tr><td id="4-y">8</td><td id="4-z">DNC</td><td id="4-A">Digital input</td><td id="4-B">Do not connect, must be left floating</td></tr>
<tr><td id="4-C">9</td><td id="4-D">SDA</td><td id="4-E">Digital input/output</td><td id="4-F">I²C serial data</td></tr>
<tr><td id="4-G">10</td><td id="4-H">SCL</td><td id="4-I">Digital input</td><td id="4-J">I²C serial clock input</td></tr>
<tr><td id="4-K">11</td><td id="4-L">AVDD</td><td id="4-M">Supply</td><td id="4-N">Supply, to be connected to main supply</td></tr>
<tr><td id="4-O">12</td><td id="4-P">GND4</td><td id="4-Q">Ground</td><td id="4-R">To be connected to main ground</td></tr>
</table>

<a id='fe1ffc7b-b322-48f7-8764-55884d9cdfd4'></a>

Note: AVSSVCSEL and GND are ground pins and can be connected together in the application schematics.

<a id='3006e783-ee30-4f09-be11-2cf7d202c8ef'></a>

GND2, GND3, and GND4 are standard pins that we force to the ground domain in the
application schematics to avoid possible instabilities if set to other states.

<a id='905c83ea-4850-43a5-983c-2bba877af9b0'></a>

<::logo: STMicroelectronics
ST
A blue stylized 'ST' logo with a horizontal line underneath.::>

<a id='b9095ec7-0a4c-49ad-a460-e1135952b8d8'></a>

DocID031281 Rev 3

<a id='f9938aff-0d5d-4b0a-9ac8-49689326dae1'></a>

5/35