<a id='c6d092fc-0851-4efc-ac38-07e9e9e62884'></a>

7/23/22, 9:09 PM

<a id='b17df039-17e9-448c-898c-f04c656cbbc4'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='cdb2f59d-f980-4719-8bda-55e62e0e54e8'></a>

ICM Address<::A diagram illustrating jumper settings for ICM Address. The first configuration shows a jumper connecting the middle (grey) and right (black) pins, indicating address 0x68. The second configuration shows a jumper connecting the left (red) and middle (grey) pins, indicating address 0x69 Default. Below this, a blue circuit board is shown with various labels. A jumper block on the board is labeled "High" and "Low" with "AD(ICM20600)". Other text on the board includes "IMU 9DOF (ICM20600 & AK09918) v1.0", "address(icm20600) 0x69", and "address(ak09918C) 0x0c.". Numbered circles (5, 6, 7, 8) point to specific pins or areas on the board, corresponding to the descriptions below.: figure::>5 INT2: Interrupt digital output (totem pole or open-drain)6 INT1: Interrupt digital output (totem pole or open-drain)7 FSYNC: Frame synchronization digital input or No Connect8 VCC_1.8V: Provide 1.8V for ICM20600 and AK09918

<a id='943d085b-ff84-4669-859b-5db0a3d5fd22'></a>

**Danger**
The default I2C address of LCM20600 is 0x69, you can change it to 0x68.
The central pad is connected to the address wire, you can change the I2C
address by cutting the wire and re-welding it. For the safety of you and
others, please be careful with knife or welding gun you may use.

<a id='96049d48-8754-40f9-9b0f-b284af6042c7'></a>

Schematic

Power

<a id='0fa33023-e8d3-4537-9427-67c76a195f07'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='9fe8c67c-6d20-40c9-a2c9-e3420ef68895'></a>

6/23