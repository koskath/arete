<a id='e2e1ee68-5d4e-4e8d-a28c-21f41beb71e8'></a>

<::logo: AOSONG
AOSONG
Aosong Electronics
Blue stylized text "AOSONG" with "Aosong Electronics" underneath, framed by two blue horizontal lines.::>

<a id='e9993837-23c3-4e46-a0ec-fbc4c7d07e0a'></a>

Temp、Humidity & Dew point measurement experts

<a id='0e4edfdf-d7bb-413b-85e0-43b8788faf3b'></a>

<::Timing diagram: The diagram shows two signals, 'Host signal' and 'Signal from the machine', plotted against time. The Y-axis has two levels: VDD (high) and GND (low). The 'Host signal' (represented by a thick black line) starts at VDD, then drops to GND, and remains at GND. The 'Signal from the machine' (represented by a thick gray line) starts at GND, rises to VDD, remains at VDD for a period, then drops back to GND, and remains at GND. There is a horizontal arrow indicating an 80us duration between the 'Host signal' dropping to GND and the 'Signal from the machine' rising to VDD. Another horizontal arrow indicates an 80us duration for which the 'Signal from the machine' stays at VDD before dropping to GND. Next to the falling edge of the 'Signal from the machine', the text "Begins to transmit data" is shown.: figure::>

<a id='8364c893-998c-4a4a-b777-61b64436427d'></a>

Step four:
The
 The 40 bit data output by the DHT11 DATA pin, the microprocessor according to the change of
I/O level receive 40 bits of data, a data format of "0": high level and low level of 50 microseconds
and 26-28 microsecond, format data "1": low level 50 microsecond plus 70 microsecond high. Bit
data "0", "1" format signal as shown in fig:

<a id='73c37fdb-c61e-49ad-8aaf-6aa293a0c386'></a>

<::Timing diagram showing two bit data formats.

**Bit data "0" format:**
- Y-axis labels: VDD, GND.
- Host signal (black line): Starts at VDD, drops to GND, and stays at GND for 50us.
- Signal from the machine (gray line): Starts at GND, rises to VDD, stays at VDD for 26us-28us, then drops back to GND.

**Bit data "1" format:**
- Y-axis labels: VDD, GND.
- Host signal (black line): Starts at VDD, drops to GND, and stays at GND for 50us.
- Signal from the machine (gray line): Starts at GND, rises to VDD, stays at VDD for 70us, then drops back to GND.
: timing diagram::>

<a id='7fbb9e64-26ef-4955-add6-b200a7602dcb'></a>

End signal:
DHT11 the DATA pin output 40-bit data, the continued output low 50 microseconds after the entry into the state, due to the pull-up resistor attendant goes high. But DHT11 temperature and humidity inside the test-retest data, and record the data, awaiting the arrival of an external signal.

<a id='a268f14c-5095-4a82-9554-9428ecfaa166'></a>

## 8. Application Information

1. Working and storage conditions
The proposed scope of work may result in up to 3% RH temporary drift of the signal. Return to normal working conditions, the sensor calibration status will slowly recover. To speed up the recovery process can be found in "recovery process." The use of the product will accelerate the aging process for a long time under abnormal operating conditions.
Avoid placing components on a long-term condensation and dry conditions and the following environments.

<a id='aa3ffd6d-b408-470a-9529-69ec95b16728'></a>

Recommended Storage Environment

A. smoke
B. Acid or oxidizing gases such as sulfur dioxide, hydrochloric acid

<a id='b17cc366-dc37-4aa3-ab04-649204c6bb17'></a>

Temperature : 10~40C

Humidity : 60% RH or less

<a id='5997e0cf-82ab-4c55-a3a9-cddc6d876853'></a>

2. Effects of exposure to chemical substances
Sensing resistive humidity sensor will be disturbed chemical vapor layer, the diffusion layer in the induction of chemicals may cause drift and measurement sensitivity. In a clean environment, slowly release contaminants out. The recovery process described below to accelerate the process.

<a id='f5184dfc-82f3-4f95-8d76-c256cc9bad27'></a>

Aosong Guangzhou Electronics Co., Ltd.

<a id='37ed9327-4be9-410d-91e3-db303ff40f8a'></a>

Order by phone: 4006 305378

<a id='6447f7ef-9578-4aec-b1f9-1c79bc8d40cb'></a>

Enterprise QQ: 4006305378

<a id='6da01af6-8817-44e4-a2b0-81f15c6ffbf3'></a>

www.aosong.com