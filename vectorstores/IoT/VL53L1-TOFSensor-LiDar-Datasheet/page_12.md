<a id='dda3f7e6-7dd1-45ce-96c3-bfe17690622e'></a>

Functional description

<a id='8c082fe9-cce0-4c52-8c88-3c2bb8154546'></a>

VL53L1X

<a id='4279d6c5-3643-471b-b815-8f27cc1ec476'></a>

## 2.6 Power sequence

### 2.6.1 Power up and boot sequence

There are two options available for device power up/boot.
**Option 1**: the XSHUT pin is connected and controlled from the host.

This option optimizes power consumption as the VL53L1X can be completely powered when not used, and then woken up through a host GPIO (using the XSHUT pin).

<a id='c22ec438-5a9a-464d-b37a-ad07f7545fa4'></a>

Hardware (HW) standby mode is defined as the period when the power supply is present and XSHUT is low.

<a id='a2c5d766-1f1f-4e41-a875-f514ebc7136e'></a>

Figure 7. Power up and boot sequence
<::This figure illustrates the power up and boot sequence with two signal lines and system states over time. The y-axis labels are "Power Supply", "XShut", and "System State".

The "Power Supply" line starts low, then rises to a high level at the first vertical dotted line, and remains high.

The "XShut" line starts low, rises to a high level at the second vertical dotted line, and remains high.

The "System State" is represented by colored blocks along the bottom:
- "Power Off" is the initial state.
- At the first vertical dotted line, it transitions to "HW Standby".
- At the second vertical dotted line, it transitions to "Boot".
- Finally, it transitions to "SW Standby".
: figure::>

<a id='6b56afab-9454-4ca1-a34e-40ca479e3175'></a>

Note:
Boot duration is 1.2ms max.

**Option 2**: the XSHUT pin is not controlled by the host, it is tied to the power supply value through the pull up resistor.

<a id='9d8fabfb-7f2b-4ef7-9f50-dc55d4f38639'></a>

When the XSHUT pin is not not controlled, the power up sequence is presented in Figure 8. In this case, the device goes automatically to Software (SW) standby after boot, without entering HW standby.

<a id='3230a747-3d8c-4331-8c92-5b58efcceb08'></a>

Figure 8. Power up and boot sequence with XSHUT not controlled<::timing diagram::>The diagram illustrates a power up and boot sequence. It shows three rows: 'Power Supply', 'XShut', and 'System State'. The 'Power Supply' line starts low, then transitions to a high state. The 'XShut' line also starts low and transitions to a high state, occurring shortly after the 'Power Supply' transition. The 'System State' is depicted in three sequential blocks: 'Power Off', followed by 'Boot', and then 'SW Standby'. A vertical dashed line indicates the time when 'Power Supply' and 'XShut' transition to high, coinciding with the system state changing from 'Power Off' to 'Boot'. The system then transitions from 'Boot' to 'SW Standby' while 'Power Supply' and 'XShut' remain high.::>

<a id='7aa32125-d484-40ff-a3c6-d32e36386316'></a>

Note: Boot duration is 1.2 ms max.
Note: In all cases, XSHUT has to be raised only when the power supply is tied on.

<a id='0e3ed642-22ca-453e-bb5b-47df2de2e57e'></a>

12/35

<a id='9c6f626d-3e85-4685-8358-91c0548a3e91'></a>

DocID031281 Rev 3

<a id='9590fab0-c98f-4b30-b2bd-255e880e055b'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, futuristic font, with a horizontal line underneath.::>

<a id='89eba69c-afa4-4ab0-b127-41e0a16e521f'></a>

off