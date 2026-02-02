<a id='55cb16a1-1dc1-4967-9d80-510de4c647e8'></a>

7/23/22, 9:09 PM

<a id='57c20c87-bc72-4e59-b583-faedae2d6cba'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='015abf54-2e89-49c8-bcf7-da6b8486a312'></a>

master\examples\compass, XXXX is the location you installed the Arduino IDE.

<a id='b06a3a2f-02a2-497a-b6b8-e2ac0e8337f4'></a>

is
> This PC > Core (C:) > Users > seeed > Documents > Arduino > libraries > Seeed_ICM20600_AK09918-master > examples > compass

<table><thead><tr><th>Name</th><th>Date modified</th><th>Type</th><th>Size</th></tr></thead><tbody><tr><td>compass.ino</td><td>9/13/2018 9:05 AM</td><td>INO File</td><td>5 KB</td></tr></tbody></table>

<a id='496dbdf3-c7c7-4c99-b4c2-12125e6e99c7'></a>

c. Or, you can just click the icon \u2398 in upper right corner of the code block to copy the following code into a new sketch in the Arduino IDE.

<a id='d3665f06-3638-4ce5-9d08-0117d8f86856'></a>

1 #include "AK09918.h"
2 #include "ICM20600.h"
3 #include <Wire.h>
4 
5 AK09918_err_type_t err;
6 int32_t x, y, z;
7 AK09918 ak09918;
8 ICM20600 icm20600(true);
9 int16_t acc_x, acc_y, acc_z;
10 int32_t offset_x, offset_y, offset_z;
11 double roll, pitch;
12 // Find the magnetic declination at your Location
13 // http://www.magnetic-declination.com/
14 double declination_shenzhen = -2.2;
15 
16 void setup()
17 {
18 // join I2C bus (I2Cdev library doesn't do this aut
19 Wire.begin();
20 
21 err = ak09918.initialize();
22 icm20600.initialize();
23 ak09918.switchMode (AK09918_POWER_DOWN);
24 ak09918.switchMode(AK09918_CONTINUOUS_100HZ);
25 Serial.begin(9600);
26 
27 err = ak09918.isDataReady();
28 while (err != AK09918_ERR_OK)
29 {

<a id='05e65eb1-8981-4cd6-b6e5-0ef90cb4efa7'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='19faeee2-0e7f-4347-a6d3-9ad731704c95'></a>

12/23