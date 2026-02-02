<a id='3f55be34-92ff-4814-9c58-863b1c0badaa'></a>

VL53L1X

<a id='c26ddcd7-7e5a-401b-a09c-362f132cf583'></a>

Packaging and labeling

<a id='cd3e10f7-17b1-45df-b675-e154bc3c62e2'></a>

## 8.5 Pb-free solder reflow process

Table 18 and Figure 24 show the recommended and maximum values for the solder profile.
Customers have to tune the reflow profile depending on the PCB, solder paste, and material used. We expect customers to follow the recommended reflow profile, which is specifically tuned for VL53L1X package.

<a id='dad89e7b-b8b8-4010-a392-e820447d9531'></a>

For any reason, if a customer must perform a reflow profile which is different from the recommended one (especially peak >240 °C), this new profile must be qualified by the customer at their own risk. In any case, the profile has to be within the "maximum" profile limit described in _Table 18_.

<a id='5cbd71b3-f403-408f-bd4d-78ed8137a16f'></a>

Table 18. Recommended solder profile
<table id="30-1">
<tr><td id="30-2">Parameters</td><td id="30-3">Recommended</td><td id="30-4">Maximum</td><td id="30-5">Units</td></tr>
<tr><td id="30-6">Minimum temperature (Ts min)</td><td id="30-7">130</td><td id="30-8">150</td><td id="30-9">°C</td></tr>
<tr><td id="30-a">Maximum temperature (Ts max)</td><td id="30-b">200</td><td id="30-c">200</td><td id="30-d">°C</td></tr>
<tr><td id="30-e">Time ts (Ts min to Ts max)</td><td id="30-f">90-110</td><td id="30-g">60-120</td><td id="30-h">S</td></tr>
<tr><td id="30-i">Temperature (TL)</td><td id="30-j">217</td><td id="30-k">217</td><td id="30-l">°C</td></tr>
<tr><td id="30-m">Time (tL)</td><td id="30-n">55-65</td><td id="30-o">55 - 65</td><td id="30-p">s</td></tr>
<tr><td id="30-q">Ramp up</td><td id="30-r">2</td><td id="30-s">3</td><td id="30-t">°C/s</td></tr>
<tr><td id="30-u">Temperature (Tp-10)</td><td id="30-v"></td><td id="30-w">235</td><td id="30-x">°C</td></tr>
<tr><td id="30-y">Time (tp)</td><td id="30-z"></td><td id="30-A">10</td><td id="30-B">s</td></tr>
<tr><td id="30-C">Ramp up</td><td id="30-D"></td><td id="30-E">3</td><td id="30-F">°C/s</td></tr>
<tr><td id="30-G">Peak temperature (Tp)</td><td id="30-H">240</td><td id="30-I">245</td><td id="30-J">°C</td></tr>
<tr><td id="30-K">Time to peak</td><td id="30-L">300</td><td id="30-M">300</td><td id="30-N">s</td></tr>
<tr><td id="30-O">Ramp down (peak to T₁)</td><td id="30-P">-4</td><td id="30-Q">-6</td><td id="30-R">°C/s</td></tr>
</table>

<a id='14e93861-0410-4d3a-8d60-9573d71cdf51'></a>

Figure 24. Solder profile
<::A line graph illustrating a solder reflow profile. The y-axis represents temperature, with labeled points from bottom to top as T_Smin, T_Smax, T_L, T_p-10, and T_p. The x-axis represents time, labeled as "Time to peak" for the duration from the start to the highest temperature point. The graph shows a curve with four main segments:
1. An initial rise from the origin to T_Smin.
2. A slower rise from T_Smin to T_Smax, labeled with a time interval t_S.
3. A steeper rise from T_Smax to the peak temperature T_p.
4. A decrease from T_p back to the baseline.
Horizontal dashed lines extend from each temperature label (T_Smin, T_Smax, T_L, T_p-10, T_p) across the graph. Vertical dashed lines mark key points in time corresponding to these temperature levels. The graph also indicates:
- A time interval t_L, representing the duration the temperature is above T_L.
- A time interval t_p, representing the duration the temperature is above T_p-10, centered around the peak temperature T_p.
: chart::>

<a id='769bf51c-4b7e-40b4-bff7-35889552ffb0'></a>

Note: _Temperature mentioned in Table 18 is measured at the top of the VL53L1X package._
Note: _The component should be limited to a maximum of three passes through this solder profile._

<a id='5aae5d9c-a524-411b-8a82-581ab35dcb5c'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='f7cbb3bb-b66c-4f74-a44b-0c33af8aeeed'></a>

DocID031281 Rev 3

<a id='ab934024-a36b-4cc5-ad48-14f03c9262e9'></a>

31/35