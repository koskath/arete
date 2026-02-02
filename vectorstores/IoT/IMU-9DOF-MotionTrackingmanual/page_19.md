<a id='9b7933a0-9657-4de5-906d-adad0be8ad6e'></a>

7/23/22, 9:09 PM

<a id='3ee3aed5-f7ba-4cc8-b945-30860ed0940e'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='bd0352f6-cfbf-4c07-9ab9-76356bb89609'></a>

<table id="18-1">
<tr><td id="18-2">range)</td><td id="18-3">accelerometer range to meet your own ne parameter acc_scale_type_t range list: RANGE_2G RANGE_4G RANGE_8G RANGE_16G e.g. icm20600.setAccScaleRange(RANGE_80 this code line will change the accelerome measurement range to ±8g</td></tr>
<tr><td id="18-4">getGyroscope(int16_t* x, int16_t* y, int16_t* z))</td><td id="18-5">You can use this function to get the gyros X/Y/Z 3-axis data at the same time, and t of the data is dps</td></tr>
<tr><td id="18-6">getGyroscopeX(void) getGyroscopeY(void) getGyroscopeZ(void)</td><td id="18-7">Or, you can get the gyroscope X/Y/Z 3-axi separately by using those three functions the unit of the data is dps</td></tr>
<tr><td id="18-8">getRawGyroscopeX(void) getRawGyroscopeX(void) getRawGyroscopeX(void)</td><td id="18-9">Those three functions get the raw data di from the register of ICM20600 without co the data unit to dps</td></tr>
<tr><td id="18-a">getAcceleration(int16_t* x, int16_t* y, int16_t* z)</td><td id="18-b">You can use this function to get the X/Y/Z acceleration at the same time, and the un data is mg</td></tr>
<tr><td id="18-c">getAccelerationX(void) getAccelerationY(void) getAccelerationZ(void)</td><td id="18-d">Or, you can get the X/Y/Z 3-axis accelerat separately by using those three functions the unit of the data is mg</td></tr>
<tr><td id="18-e">getRawAccelerationX(void) getRawAccelerationY(void) getRawAccelerationZ(void)</td><td id="18-f">Those three functions get the raw data di from the register of ICM20600 without co the data unit to mg</td></tr>
<tr><td id="18-g">getTemperature(void) Function</td><td id="18-h">You ca use this function to get the tempe Description</td></tr>
<tr><td id="18-i"></td><td id="18-j"></td></tr>
</table>

<a id='f02e06a6-98f8-46c5-9fdc-584a32163a9e'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='3d0b1c93-a499-4d67-9cc7-4bb2541cbb7f'></a>

19/23