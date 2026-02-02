<a id='432c8e33-aa2f-4bc5-a73e-fb6f997c53d6'></a>

<::logo: HaiWang
HaiWang
This logo features a blue stylized letter 'W' or 'U' shape above the brand name in red text.::>

<a id='8ce35872-ec9a-417c-8a23-6580672e4b15'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULE

<a id='ed437d20-70c6-485d-b4a3-b911ebb0da06'></a>

<::An illustration of a black capacitive soil moisture sensor. The top part of the sensor has a white connector with three wires (red, blue, brown) and some electronic components. Text on the sensor reads "Capacitive Soil Moisture Sensor v1.0DFROBOT" and "DRIVE THE FUTURE". A red horizontal line crosses the sensor, labeled "Warning Line" with a red downward arrow. Two green horizontal lines indicate a range on the sensor, labeled "Recommend Depth" with a green upward and downward arrow. Gray diagonal lines and the word "soil" are shown to the left of the sensor, indicating where it would be inserted into the ground.
: figure::>

<a id='c8119861-75b1-4595-aec4-0cc31a3a51be'></a>

<::transcription of the content
SOII
Recom
ctive
oixture
: figure::>

<a id='40ba57ff-9a30-4df4-ab3d-22ea0625f419'></a>

## Interval setting

Because the sensor value will be affected by the depth of the soil and the tightness of the soil, only the relative humidity of the soil can be detected. We divide the range of humidity into three equal parts, which means dry, humid, and very humid. The two data recorded before are the humidity interval. For example: the reading in the air is 520, and the reading in the water is 260, so it can be divided into (520,430), (430,350], (350,260). These three sections represent dry, wet, and very humid.

<a id='a3c22844-5f6f-476e-8975-fd4c79c25962'></a>

Note: Since this sensor will monitor soil moisture based on the principle of capacitive sensing, placing it in different places with different soil moisture, different tightness, and different insertion depth will reflect different humidity, even in the same place, at the same depth, at During the second insertion, since the first extraction has caused loosening of the soil, the humidity may be lower than the first reading. A

<a id='8faa3b07-7691-4a6b-b9b5-6c7bf9611a36'></a>

Note: Humidity is inversely proportional to the reading.

<a id='003488fc-74c6-49db-9a2e-73b082313863'></a>

## Test code

Bring the two sets of data just recorded into your test code.

<a id='d215dd63-f771-416a-a055-2d683b18da48'></a>

/***************************************************************
This example reads Capacitive Soil Moisture Sensor.

Created 2015-10-21
By berinie Chen <bernie.chen@dfrobot.com>