<a id='d78b6723-72b2-432d-b9ad-4e2f293a6fe6'></a>

Ranging performances

<a id='00d2b042-2ce4-40f2-98ba-0c693902b026'></a>

VL53L1X

<a id='d5136169-ac98-4d8b-91c2-3e0efbaf5149'></a>

## 3.2 Accuracy, repeatability, and ranging error definitions

### 3.2.1 Accuracy definition

Accuracy = mean distance – actual distance
*   Mean distance is the average of 32 measured distances
*   Actual distance is the actual target distance

Accuracy can be affected by an offset error, a temperature drift, and a voltage drift.

### 3.2.2 Repeatability definition

Repeatability is the standard deviation of the mean ranging value of 32 measurements. It can be improved by increasing the timing budget. A typical repeatability value for VL53L1X is from \u00b11 % to \u00b10.15 % depending on the timing budget and the ambient light.

### 3.2.3 Ranging error definition

Ranging error = accuracy + repeatability error.

This ranging error value is our metrics in the following performances tables.

## 3.3 Minimum ranging distance

The minimum ranging distance is 4 cm. Under this minimum distance, the sensor will detect a target, but the measurement will not be accurate.

<a id='588b489c-7e1d-406d-8782-29b21b0d17d8'></a>

3.4 Performances in dark conditions
Table 6. Performances in dark conditions
<table id="15-1">
<tr><td id="15-2">Parameter</td><td id="15-3">Target reflectance</td><td id="15-4">Min. value</td><td id="15-5">Typ. value</td></tr>
<tr><td id="15-6" rowspan="3">Max distance (cm)</td><td id="15-7">White 88 %</td><td id="15-8">260</td><td id="15-9">360 (400 with TB = 140 ms)</td></tr>
<tr><td id="15-a">Grey 54 %</td><td id="15-b">220</td><td id="15-c">340</td></tr>
<tr><td id="15-d">Grey 17 %</td><td id="15-e">80</td><td id="15-f">170</td></tr>
<tr><td id="15-g" colspan="2">Ranging error (mm)</td><td id="15-h" colspan="2">± 20</td></tr>
</table>

<a id='e95ef8a5-b7ec-47fe-96f6-99dc5b5ff620'></a>

Test conditions (including those described in _Section 3.1: Test conditions_) are:
* Ambient light = dark
* Timing budget = 100 ms unless mentioned
* Long distance mode

<a id='d77adf99-b134-4c0a-8e0a-f5fd565f542c'></a>

16/35

<a id='b87f57c6-385c-44ef-86d6-09385b59e250'></a>

DocID031281 Rev 3

<a id='d7b8999b-194e-4ede-ac75-be46055ecf27'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a horizontal line beneath it.::>