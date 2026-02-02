<a id='42a1c667-ebfb-4a62-8e17-23933858b506'></a>

12/4/25, 2:51 PM

<a id='8268baae-a860-46a1-a5d2-a747337e36e4'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='10afe9b6-f4ce-4c88-983d-1d46980af104'></a>

ARDUINODOCS

Search on Docs /

<a id='aed4fee2-85e5-4061-96c3-98403b86faa9'></a>

← Go Back

## Hardware

<a id='bd9a884d-2e46-40a9-98b7-63ce728b1a2a'></a>

MKR ENV Shield

Tutorials

Reading Data From the
MKR ENV Shield

<a id='b9ffe4e0-2ff3-4310-aee7-4a575f54187a'></a>

Home / Hardware / MKR ENV Shield / Reading
Data From the MKR ENV Shield

<a id='b91b466b-0d12-4ac4-a84f-2cb6c72fa976'></a>

# Reading Data From the MKR ENV Shield

Learn how to access the different sensors, such as temperature, humidity & pressure.

---

Author: Karl Söderby
Last revision: 17/07/2024

<a id='ae5695ce-6df4-423e-afc5-dbedfa20c6ff'></a>

# Introduction

In this tutorial, we will go through the requirements of getting started with the MKR ENV Shield, a shield designed to capture environmental data from your surroundings. The shield can only be used with a MKR family board, where it can be easily mounted on top.

<a id='2a03fc02-8de6-413d-819d-f8d082d3ad3b'></a>

The MKR ENV Shield is a great option for
weather projects, where we can read
temperature, humidity, light intensity &
atmospheric pressure. Additionally, it also
comes equipped with an SD card holder, that
can be used to store the data captured from
the sensors.

<a id='18c28858-ca5b-423e-808a-6a72bc3882ed'></a>

*Note: The older MKR ENV Shield version (v1) comes with a UV sensor that can capture UVA & UVB wavelengths. The newer versions (v2 and up) does not include this sensor. This can be seen in the silk on the shield, where newer versions does not have a sun symbol marked on top.*

<a id='2298cd2a-5d2c-42fe-85df-c550acb62b03'></a>

# Goals

The goals of this project are:

* Learn how to use the **Arduino_MKRENV** library.
* Capture data from all the sensors on the shield.
* Print out the data in the Serial Monitor.

<a id='a2e3c9af-3efe-485a-8a08-8064a06f6bb8'></a>

ON THIS PAGE

<a id='176913b5-0c40-4cfb-8bb1-41a895b20d85'></a>

## Introduction
- Goals
- Hardware & Software Needed
- The Different Sensors on the Shield
  - HTS221 Temperature & Humidity Sensor
  - LPS22HB Atmospheric Pressure Sensor
  - TEMT6000 Light Sensor
  - VEML6075 (Older Versions Only)
- Circuit
- Programming the Board
- Testing It Out
  - Troubleshoot
- Conclusion

<a id='290168f5-e466-4954-93dd-e594117a309f'></a>

Hardware & Software

<a id='d40eed43-dd50-4dad-be2e-e6e91ba4dfd4'></a>

Needed
file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='58311146-efe6-4d6f-9e6d-702d4ba5b8a0'></a>

Help

<a id='60bde594-4ea6-4f5b-9286-16006385a215'></a>

1/8