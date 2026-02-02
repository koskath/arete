<a id='68082bc5-7ca5-4d63-ba79-4aab022d6a9e'></a>

12/4/25, 2:52 PM

<a id='2f184aa0-689c-451a-87dd-bbdd60bd33d8'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='affd4996-bb7f-47b8-9c44-e3ef2eaedb85'></a>

ARDUINO DOCS

<a id='11cc468d-7e48-4baf-928b-ec5146fc51ff'></a>

# Testing It Out

After we have uploaded the code to the board, we need to open the Serial Monitor to start the program. It is a good idea to have our setup close to a window. Once the data is available, it will start printing the values in the Serial Monitor.

<a id='94efe2d9-da27-407a-8d23-a04725e0ec6d'></a>

<::screenshot of Arduino IDE and Serial Monitor showing GPS data: screenshot::>
GPS data printed in the Serial Monitor.

**Arduino IDE 1.8.19 - Serial Monitor**
01:19:04 $GPRMC,011904.00,A,3540.84000,N,08233.16000,W,0.200,314.01,230421,,,A*7A
01:19:04 Lat: 35.680666
01:19:04 Lon: -82.552666
01:19:04 Speed: 0.20 km/h
01:19:04 Heading: 314.01
01:19:05 $GPRMC,011905.00,A,3540.84000,N,08233.16000,W,0.199,314.01,230421,,,A*7B
01:19:05 Lat: 35.680666
01:19:05 Lon: -82.552666
01:19:05 Speed: 0.20 km/h
01:19:05 Heading: 314.01
::>


<a id='805c0aa0-bdb5-4443-9b7a-5846f04c9569'></a>

Note: This process may take
some time. If no data is
available after 5 minutes or so,
try moving your device closer to
a window.

<a id='3953748c-6aed-4738-987e-b7c55c2a4162'></a>

Once we start getting the values,
we can double check that they are
alright. For example,

<a id='44995ebf-4c10-4965-a1a1-2566e7ed13a6'></a>

longitude
and
latitude
should be very accurate, and be
able to pinpoint almost your exact
location. You can enter the
coordinates in
Google Maps
for example, to see if the values
match.

<a id='e4e4ca5c-1d72-4615-8ff2-86071deed983'></a>

## Troubleshoot

If the code is not working, there
are some common issues we can
troubleshoot:

<a id='61e341a4-4ece-4f3b-8b2b-579be88ad826'></a>

We have not installed the
**MKRGPS** library.
We have selected the wrong
port and board to upload to.

<a id='d1d094ab-53ff-4107-a529-0950a9114493'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='1f1f96aa-5267-4005-9cdf-4eac2d7fb5ef'></a>

5/7