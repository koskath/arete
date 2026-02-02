<a id='ae72b975-4bd7-446e-ae23-39324c493e00'></a>

An ApexChart is a modern JavaScript charting library that enables the creation of interactive and responsive data visualizations. It supports a wide range of chart types, including **line**, **bar**, **area**, **pie**, and **more**, and is commonly used for embedding charts in web applications with minimal configuration.

<a id='b5d875a8-fe01-4bf1-9bd9-bb9ca3209c7e'></a>

<::Chart 1: Cumul irrigation (m²/ha)
Type: Bar chart
Y-axis (Cumul irrigation m²/ha): 0.00, 10.00, 20.00, 30.00, 40.00
X-axis (Date): 26 Jun, 27 Jun, 28 Jun, 29 Jun, 30 Jun, Jul 25, 02 Jul
Data:
- 26 Jun: 0.00
- 27 Jun: 25.00
- 28 Jun: 26.00
- 29 Jun: 27.00
- 30 Jun: 30.00
- Jul 25: 27.00
- 02 Jul: 27.00

Chart 2: Eau Disponible
Type: Line and bar chart
Left Y-axis (Capacité aux Champs (%)): 0.00, 10.00, 20.00, 30.00, 40.00, 50.00, 60.00, 70.00, 80.00, 90.00, 100.00, 110.00, 120.00, 130.00, 140.00, 150.00, 160.00
Right Y-axis (Pluviométrie (mm)): 0.00, 2.00, 4.00, 6.00, 8.00, 10.00, 12.00, 14.00, 16.00, 18.00, 20.00, 22.00, 24.00, 26.00, 28.00, 30.00, 32.00
X-axis (Date): 26 Jun, 27 Jun, 28 Jun, 29 Jun, 30 Jun, Jul 25, 02 Jul
Legend:
- Prat 15 cm (line)
- Prat 40 cm (line)
- Prat 80 cm (line)
- Prat 40 cm entre goutteurs (line)
- Irrigation (vertical bars)

The chart shows multiple lines representing water capacity at different depths (15 cm, 40 cm, 80 cm, and 40 cm between drippers) fluctuating over time. The capacity generally decreases, then sharply increases due to irrigation events (represented by tall vertical bars). There are significant irrigation events on 27 Jun, 29 Jun, 30 Jun, Jul 25, and 02 Jul.::>

<a id='f0f7f3ab-e07f-4340-94d5-94993898358d'></a>

This widget is able to display data from multiple data sources in the same chart. Note that the configuration interface allows to add variables or clone a source configuration to make it easier.

<a id='c01d5fc3-c424-44a1-a2de-1268d6c16d49'></a>

Widget Settings
Widget Apex Charts Display Options

Source 1

Name i Source 1

Data Source i Select input source
<::Dropdown menu with options:
option Select input source: [x]
option From Data Bucket: [ ]
option From Device Bucket: [ ]
option From Device Resource: [ ]
option From Device Property: [ ]
option Manual: [ ]
: dropdown::>
+ Add Source Clone Source


<a id='5f7668e4-cffe-4700-85dc-a5424a7d0c32'></a>

16