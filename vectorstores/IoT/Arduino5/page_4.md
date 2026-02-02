<a id='fce34620-3587-4c73-a33c-653e3fc33c34'></a>

12/4/25, 2:51 PM

<a id='5334e292-6edc-4465-bd66-6042537dcdde'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='29ff40b9-f0e6-4f26-8bc8-1ca846afb9ec'></a>

ARDUINODOCS

<a id='67b7ac35-8450-491d-aa71-1a0e87805a10'></a>

operate with a more constrained pressure
range between the extended temperature
range from -40 C to +85 C.

<a id='8e5610f3-4349-44d0-a8b1-7da95242e0e0'></a>

You can find more information about this sensor by reading it's datasheet.

<a id='5ed5c21e-83a4-4e46-aaf7-25d845a55296'></a>

TEMT6000 Light Sensor

<a id='1d87d72e-f2f9-40c5-a6fd-0f0cf6bc4758'></a>

<::image: An electronic development board (likely an Arduino Nano Every or similar) with various components, pins, and a micro-SD card slot. A specific component on the board, a light sensor, is highlighted with a blue glow and has a label "TEMT6000" pointing to it. The TEMT6000 sensor.::>

<a id='c4c4530a-d1e2-4549-9026-ce715c3117fa'></a>

The TEMT6000 sensor is a phototransistor, a component that will allow electrons to flow differently based on the amount of light shining on it. It has been calculated to be adapted to the human eye sensitivity. In other words, this sensor is telling you how intense light is for your eyes.

<a id='9da9d2bf-6172-4052-a920-147fc5e1fa36'></a>

The sensor's range and accuracy makes is suitable for a lot of scientific experiments. The sensor's opening angle is 60, and while it peaks up at 570 nm, it is detecting light in the range from 440 nm to 800 nm, in the temperature range from -40 C to +100 C.

<a id='a8ac93e1-1aae-4287-8bc6-bc98cb368df2'></a>

Using the command
`readIlluminance()`
will by default return a value measured in
`LUX`
. This unit represents one lumen per square meter. Unlike a measurement of Watts per square meter, which weights the power of signals in different frequencies of the spectrum differently, the lumens are calculated by looking at the mathematical response of the human eye to different wavelengths. In that way, LUX comes to be a measurement of how intense the light is for the human eye.

<a id='b8efab35-12e1-404a-9f9e-07a76bfde726'></a>

You can find more information about this sensor by reading it's datasheet.

<a id='cf67301b-ac08-412b-9347-8bd89ff4bc88'></a>

VEML6075 (Older Versions Only)

<a id='a87794c0-cfbb-469d-8775-6042fe2d9a1f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='b05ba20c-56cf-4555-80ab-fab225df30e1'></a>

4/8