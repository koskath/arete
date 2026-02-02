<a id='90bebc64-1778-45bf-a62e-2fb09b2eb45d'></a>

7/23/22, 9:09 PM

<a id='5b385715-0fe1-4e06-9d81-d8b15e5cc2bc'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='ce16a879-2ebf-4594-a725-5a18bbc4cfb2'></a>

20 Roll: 80.83
21 Pitch: 64.90
22 Heading: 21.76
23 ---

<a id='7764ba17-52dc-475c-99b3-b8cdd37afabe'></a>

Note
As you can see, the result of compass example includes three parameter:
roll, pitch and Heading. There are the terminology of Euler angles
[https://en.wikipedia.org/wiki/Euler_angles](click to check more
information).

<a id='c7bb5de6-ac11-4969-9786-e4d5ef02903e'></a>

Fuction table
<table id="17-1">
<tr><td id="17-2">Function</td><td id="17-3">Description</td></tr>
<tr><td id="17-4">ICM20600</td><td id="17-5"></td></tr>
<tr><td id="17-6">initialize()</td><td id="17-7">Initialize the chip LCM20600, by default: the measurement range of gyroscope is ± dps the measurement range of accelerometer</td></tr>
<tr><td id="17-8">setGyroScaleRange(gyro_scale_type_t range)</td><td id="17-9">After the initialization, you can set the gyr range to meet your own needs, the param gyro_scale_type_t range list: RANGE_250_DPS RANGE_500_DPS RANGE_1K_DPS RANGE_2K_DPS e.g. icm20600.setGyroScaleRange(RANGE_1 this code line will change the gyroscope measurement range to ±1000dps</td></tr>
<tr><td id="17-a">Function setAccScaleRange(acc_scale_type_t</td><td id="17-b">Description After the initialization, you can set the</td></tr>
</table>

<a id='2bca5fda-234f-477a-8129-b6ce55286b8f'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='8c1d78a1-2432-4ac5-80dd-afd91d47d1af'></a>

18/23