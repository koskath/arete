<a id='942190fc-a3d9-4e11-95b8-6a5163ff1f64'></a>

<::logo: Aosong
AOSONG
Aosong Electronics
It features the company name "AOSONG" in large, stylized blue letters, with "Aosong Electronics" in smaller text below, flanked by two horizontal lines.::>

<a id='225fc0c3-172b-4605-aa5b-9d9b17c79a3e'></a>

Temp、Humidity & Dew point measurement experts

<a id='f719aad5-e2e0-4beb-bb19-628b8a75bee1'></a>

external approximately 5.1kΩ pull up resistor, so that when the bus is idle, the state is high. Because they are master-slave structure, only the host calls a slave, a slave to answer, so the host access devices must strictly follow the sequence of a single bus, if there is a sequence of confusion, the device will not respond to the host.

<a id='f4172d06-f504-48f7-9438-11032d030e5c'></a>

◉Single bus transfer data bit definition

DATA is used for communication between the microprocessor and DHT11 and
synchronization, single-bus data format, a 40-bit data transfer, high first-out.
Data formats:

<a id='f2a5f381-3445-451f-b554-fbba79110bb5'></a>

8bit humidity integer data + 8bit decimal data +8 bit temperature and humidity data + 8bit
temperature decimal integer data +8 bit parity bit.
Note: The fractional portion wherein the temperature and humidity of 0.

<a id='089490d5-223e-4c65-bed0-346499569c58'></a>

Parity bit data definition

"8bit humidity decimal integer data + 8bit humidity temperature data +8 bit decimal integer data + 8bit temperature data" 8bit parity bit is equal to the result of the end of eight.

Example One : 40 receives the data to:

<a id='b9180912-dd46-4eac-b7ae-c0d3130a988d'></a>

0011 0101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0000 0000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0001 1000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0000 0000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0100 1101

High humidity 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Low humidity 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; High temperature 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Low temperature 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parity bit

Calculated as follows:
0011 0101+0000 0000+0001 1000+0000 0000=0100 1101
Receive data is correct:
Humidity: 0011 0101=35H=53%RH
Temperature:0001 1000=18H=24°C

Example Two: The received data is 40:
0011 0101 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0000 0000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0001 1000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0000 0000 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0100 1001

High humidity 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; High humidity 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; High temperature 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; High temperature 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parity bit

Calculated as follows:

<a id='299ac393-4c0e-4fd8-b185-82120bc66909'></a>

0011 0101+0000 0000+0001 1000+0000 0000 = 0100 1101
01001001 is not equal to 01001101

<a id='934b560d-e343-493b-a51e-4026d85227c3'></a>

The received data is not correct, give up, again receiving data.

<a id='959f40dc-1efa-4cf5-8bc2-1246d77e3563'></a>

Data Timing Diagram

Hosts (MCU) after sending a start signal, DHT11 transition from a low-power mode to high-speed mode, the host until after the end of the start signal, DHT11 send a response signal, send 40bit data acquisition and trigger a letter. Signal transmission shown in fig.

<a id='f742f2bf-e3c6-45bc-ae7b-1610e427b6b4'></a>

Aosong Guangzhou Electronics Co., Ltd.

<a id='a4f8fe55-a696-4ca9-b054-7b038cc956ad'></a>

Order by phone: 4006 305378

<a id='c561e5e4-9b6e-4a6d-ab44-0471af437938'></a>

Enterprise QQ: 4006305378

<a id='a2b04972-118b-423f-83b9-33f53190cd21'></a>

www.aosong.com

<a id='214fbdaa-6854-453f-8be7-ef767659f1e7'></a>

- 4-