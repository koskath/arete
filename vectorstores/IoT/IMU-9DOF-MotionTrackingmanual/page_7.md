<a id='fecf1f89-2389-41b7-953d-8f0bd8fd57d0'></a>

7/23/22, 9:09 PM

<a id='28faafbe-8a9b-42ce-9ae4-a512ab6defb3'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='34ae9661-0d69-4086-8922-c4efe711a775'></a>

<::An electronic circuit diagram for a voltage regulator. The main component is an IC labeled U5, XC6206P182MR, which has pins VIN, VSS, and VOUT. Pin 3 is VIN, pin 1 is VSS, and pin 2 is VOUT. The input voltage, labeled VCC, is connected to the VIN pin. In parallel with the VIN input, there are two capacitors, C2 (100nF) and C1 (10uF), connected to ground. The VOUT pin is connected to an output labeled 1V8. In parallel with the VOUT output, there are two capacitors, C11 (100nF) and C10 (10uF), connected to ground. A test point, TP7+, is also connected to the VOUT line. The VSS pin of the IC is connected directly to ground.: circuit diagram::>

<a id='df0d9da6-effb-40b3-87f6-e221ac8da153'></a>

Since the operating voltage range of LCM20600 is 1.71V to 3.45V, and the operating voltage range of AK09918 is 1.65V to 1.95V, we use a power conversion chip **XC6206P182MR** to provide a stable 1.8V for both chips.

<a id='7b1b07a5-953c-4e70-bbdd-b95ed371a015'></a>

Bi-directional level shifter circuit
<::circuit diagram
: The diagram shows a bi-directional level shifter circuit. It features two identical sections, one for SDA and one for SCL, each using an N-channel MOSFET (CJ2102) for level shifting.

Top section (SDA):
- An input labeled "SDA_1V8" is connected through a 4.7K resistor (R3) to the source of MOSFET Q1 (CJ2102).
- The gate of Q1 is connected to a 1V8 rail.
- The drain of Q1 is connected to an output labeled "SDA_VCC" and also through a 4.7K resistor (R4) to a VCC rail.
- The 1V8 rail is also connected to the source side of Q1 via a direct connection.

Bottom section (SCL):
- An input labeled "SCL_1V8" is connected through a 4.7K resistor (R5) to the source of MOSFET Q2 (CJ2102).
- The gate of Q2 is connected to the same 1V8 rail.
- The drain of Q2 is connected to an output labeled "SCL_VCC" and also through a 4.7K resistor (R2) to the same VCC rail.
- The 1V8 rail is also connected to the source side of Q2 via a direct connection.

Both MOSFETs, Q1 and Q2, are depicted with their internal body diodes.::>

<a id='8c17a49f-6fad-4ac6-8cb7-8fbe739a68e4'></a>

This is a typical Bi-directional level shifter circuit to connect two different voltage section of an I²C bus. The I²C bus of two chips use 1.8V, if the I²C bus of the Arduino use 5V or 3.3V, this circuit will be needed. In the schematic above, **Q1** and **Q2** are N-Channel MOSFET CJ2102 [https://files.seeedstudio.com/wiki/Grove-IMU_9DOF-Icm20600_AK09918/res/CJ2102.pdf], which act as a

<a id='e227ef4f-ea04-4f99-af21-e3a0c9f43c04'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='e67be9d4-b5a1-4bd2-a0f9-9960bee962de'></a>

7/23