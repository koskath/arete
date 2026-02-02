<a id='0d8898af-dd94-4b92-adb9-07da56c5ddcb'></a>

Functional description

<a id='8cdf1700-592e-4f45-90c6-c67b38652e6e'></a>

VL53L1X

<a id='a8217fbd-cb73-49ef-8bc3-50181cb3ba2b'></a>

2.5 Key parameters

<a id='b7aa2897-379c-447b-b9a7-6b55bbfdef4c'></a>

## 2.5.1 Distance mode

The VL53L1X has three distance modes (DM): short, medium, and long.

<a id='71c3fab0-ba83-49af-89e0-d949a2de7665'></a>

Long distance mode allows the longest possible ranging distance of 4 m to be reached.
However, this maximum ranging distance is impacted by ambient light.

<a id='cbbbb242-9132-4977-8468-da2c66fe105c'></a>

Short distance mode is more immune to ambient light, but its maximum ranging distance is typically limited to 1.3 m.

<a id='01f2c932-8cc1-449d-a033-b54f0331acde'></a>

Table 4. Maximum distance vs. Distance mode under ambient light
<table id="9-1">
<tr><td id="9-2">Distance mode</td><td id="9-3">Max. distance in dark (cm)</td><td id="9-4">Max. distance under strong ambient light (cm)</td></tr>
<tr><td id="9-5">Short</td><td id="9-6">136</td><td id="9-7">135</td></tr>
<tr><td id="9-8">Medium</td><td id="9-9">290</td><td id="9-a">76</td></tr>
<tr><td id="9-b">Long</td><td id="9-c">360</td><td id="9-d">73</td></tr>
</table>

<a id='c5bddc78-0ec0-4a64-8e3a-d7795c4fc4a9'></a>

Test conditions: timing budget = 100 ms, white target 88%, dark = no IR ambient,
ambient light = 200 kcps/SPAD.

<a id='a7c681aa-86c2-45bf-a9aa-7b6bb2a17a08'></a>

10/35

<a id='7d94a4d4-3296-4f5f-baa3-e481341435ee'></a>

DocID031281 Rev 3

<a id='5e63e7f4-1c88-4a27-8f03-538eb2f7f084'></a>

<::logo: STMicroelectronics
ST
The logo features a stylized blue 'ST' symbol with a horizontal line beneath it.::>