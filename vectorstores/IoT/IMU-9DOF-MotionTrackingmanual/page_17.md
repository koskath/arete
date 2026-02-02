<a id='bd02dc04-fea6-4726-9f21-168bf3bfd7e3'></a>

7/23/22, 9:09 PM

<a id='68b8b952-ae92-42c8-8236-984f5f96cd12'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='355649c3-29b8-4a47-bd9b-2e35689e8931'></a>

This example gets magnetic data and acceleration data, to count pitch and roll, and make a compass application.

<a id='990d6a2f-5473-4516-8c7e-a7f70f17b936'></a>

- **Step 4.** Upload the demo. If you do not know how to upload the code, please check [How to upload code](https://wiki.seeedstudio.com/Upload_Code/).
- **Step 5.** Open the **Serial Monitor** of Arduino IDE by click **Tool**->**Serial Monitor**. Or tap the Ctrl + Shift + M key at the same time. Set the baud rate to **9600**.

<a id='f5930aa6-a293-4542-a098-78493bea5ae4'></a>

Success
If every thing goes well, when you open the Serial Monitor, the notice will pop up--*Start figure-8 calibration after 2 seconds*. Which means in order to calibrate this module, you should move it and draw the number 8 trajectory in the air. When the "..." appears, you can start your calibration.

<a id='50240cbe-bec8-405f-a9ed-55b70f19080f'></a>

Start figure-8 calibration after 2 seconds.
...
A: -362, -205, 738 mg
G: -45, 12, -1 dps
M: -6, -23, -33 uT
Roll: -15.53
Pitch: 25.30
Heading: 23.99
---
A: -269, 583, 61 mg
G: 102, 377, -2 dps
M: 18, -21, -18 uT
Roll: 84.03
Pitch: 24.65
Heading: 215.58
---
A: -495, 229, 37 mg
G: -43, -231, 201 dps
M: 7, -30, 6 uT

<a id='19519c2c-0d60-4750-af54-06c3085d1ab8'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='99bae08d-c889-4e4b-a19a-cb4e71c3247d'></a>

17/23