<a id='6cbc0f38-2b77-4722-aff1-ea35cdde21fa'></a>

Contents

<a id='c2e67bf6-f9ea-4f44-b143-bb84c81896ef'></a>

VL53L1X

<a id='f33f3751-4a3e-4ada-a081-ab1414f87b19'></a>

Contents
<table id="1-1">
<tr><td id="1-2">1</td><td id="1-3" colspan="2">&lt;MISSING CELL VALUE&gt;</td></tr>
<tr><td id="1-4"></td><td id="1-5">1.1</td><td id="1-6">Technical specification ........................ 4</td></tr>
<tr><td id="1-7"></td><td id="1-8">1.2</td><td id="1-9">System block diagram .......................... 4</td></tr>
<tr><td id="1-a"></td><td id="1-b">1.3</td><td id="1-c">Device pinout ..................................... 5</td></tr>
<tr><td id="1-d"></td><td id="1-e">1.4</td><td id="1-f">Application schematic ........................... 6</td></tr>
<tr><td id="1-g">2</td><td id="1-h" colspan="2">&lt;MISSING CELL VALUE&gt;</td></tr>
<tr><td id="1-i"></td><td id="1-j">2.1</td><td id="1-k">System functional description ...................... 7</td></tr>
<tr><td id="1-l"></td><td id="1-m">2.2</td><td id="1-n">System state machine description .................. 8</td></tr>
<tr><td id="1-o"></td><td id="1-p">2.3</td><td id="1-q">Customer manufacturing calibration flow ............ 9</td></tr>
<tr><td id="1-r"></td><td id="1-s">2.4</td><td id="1-t">Ranging description ............................... 9</td></tr>
<tr><td id="1-u"></td><td id="1-v">2.5</td><td id="1-w">Key parameters .......................................... 10</td></tr>
<tr><td id="1-x"></td><td id="1-y"></td><td id="1-z">2.5.1 Distance mode .................................... 10</td></tr>
<tr><td id="1-A"></td><td id="1-B"></td><td id="1-C">2.5.2 Timing budget (TB) ................................ 11</td></tr>
<tr><td id="1-D"></td><td id="1-E">2.6</td><td id="1-F">Power sequence .......................................... 12</td></tr>
<tr><td id="1-G"></td><td id="1-H"></td><td id="1-I">2.6.1 Power up and boot sequence ........................ 12</td></tr>
<tr><td id="1-J"></td><td id="1-K">2.7</td><td id="1-L">Ranging sequences ........................................ 13</td></tr>
<tr><td id="1-M"></td><td id="1-N">2.8</td><td id="1-O">Sensing array optical center .................................... 14</td></tr>
<tr><td id="1-P">3</td><td id="1-Q" colspan="2">&lt;MISSING CELL VALUE&gt;</td></tr>
<tr><td id="1-R"></td><td id="1-S">3.1</td><td id="1-T">Test conditions ............................................. 15</td></tr>
<tr><td id="1-U"></td><td id="1-V">3.2</td><td id="1-W">Accuracy, repeatability, and ranging error definitions ................ 16</td></tr>
<tr><td id="1-X"></td><td id="1-Y"></td><td id="1-Z">3.2.1 Accuracy definition ................................. 16</td></tr>
<tr><td id="1-10"></td><td id="1-11"></td><td id="1-12">3.2.2 Repeatability definition ............................ 16</td></tr>
<tr><td id="1-13"></td><td id="1-14"></td><td id="1-15">3.2.3 Ranging error definition ............................ 16</td></tr>
<tr><td id="1-16"></td><td id="1-17">3.3</td><td id="1-18">Minimum ranging distance ................................ 16</td></tr>
<tr><td id="1-19"></td><td id="1-1a">3.4</td><td id="1-1b">Performances in dark conditions ......................... 16</td></tr>
<tr><td id="1-1c"></td><td id="1-1d">3.5</td><td id="1-1e">Performances in ambient light conditions . . . . . . . . . . . . . . . . 17</td></tr>
<tr><td id="1-1f"></td><td id="1-1g"></td><td id="1-1h">3.5.1 Long distance mode . . . . . . . . . . . . . . . . . . . . . . . . 17</td></tr>
<tr><td id="1-1i"></td><td id="1-1j"></td><td id="1-1k">3.5.2 Short distance mode . . . . . . . . . . . . . . . . . . . . . . . . 17</td></tr>
<tr><td id="1-1l"></td><td id="1-1m">3.6</td><td id="1-1n">Performances in partial ROI in dark conditions . . . . . . . . . . . 18</td></tr>
</table>

<a id='94a7c296-aace-4dbb-bafb-ba7c3263f905'></a>

2/35

<a id='26c5ed0e-28ba-4238-807f-711fdfdd214d'></a>

DocID031281 Rev 3

<a id='c4262e39-e8cf-41a4-bce0-aad46418a995'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>