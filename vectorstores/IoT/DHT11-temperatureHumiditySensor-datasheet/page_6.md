<a id='e34c3d0e-0396-475a-9b85-ad8c9b939377'></a>

<::logo: Aosong
AOSONG
Aosong Electronics
The logo features the company name "AOSONG" in a stylized, bold, blue font, with "Aosong Electronics" written in a smaller font underneath, framed by horizontal lines on either side.::>

<a id='3681df0f-4c3c-4c08-b853-a60761c58558'></a>

Temp、Humidity & Dew point measurement experts

<a id='393ffd5a-1462-4457-828b-6d6b9465f6df'></a>

<::Timing diagram of a signal bus interaction between a host and a machine.

**Y-axis labels:**
- VDD (top line, representing high voltage)
- GND (bottom line, representing ground/low voltage)
- Signal bus (label for the overall signal)

**Legend:**
- Host signal: Solid thick black line
- Signal from the machine: Solid thin gray line (with a dashed gray line for a portion)

**Timeline of events (left to right):**
1.  **Host send a start signal:** The host signal transitions from VDD to GND, stays at GND, then transitions back to VDD.
2.  **Pulled wait:** The host signal remains at VDD. The machine signal is at GND.
3.  **Response signal:** The machine signal transitions from GND to VDD, stays at VDD, then transitions back to GND.
4.  **Pulled ready output:** The machine signal transitions from GND to VDD.
5.  **Data "0" bit:** The machine signal transitions from VDD to GND, stays at GND, then transitions back to VDD.
6.  **Data "1" bit:** The machine signal transitions from VDD to GND, stays at GND for a longer duration, then transitions back to VDD. A dashed gray line indicates a continuation or alternative state for the machine signal after the "Data '1' bit" phase.
7.  **Low end:** The machine signal transitions from VDD to GND.
8.  **Release the bus:** The host signal transitions from GND to VDD.
: timing diagram::>

<a id='01b988e7-6a52-4feb-aa66-5b9cefb277f6'></a>

Data Timing Diagram
Note: The host reads temperature and humidity data from DHT11 always previous measurements, such as the two measured time interval is long, please read twice in a row is the second time in real time temperature and humidity values.

<a id='04cfce2a-7067-467b-90f9-ed1b07fdfee6'></a>

* Peripheral reading step
Communication between master and slave can be completed by the following steps (peripherals
(such as a microprocessor) to read step DHT11 data).
Step one:

<a id='63ff109e-c8dd-4dd9-995b-53f2e3533703'></a>

DHT11 after power (power after DHT11 1S to wait to cross the unstable state during this period can't send any commands), test environment temperature and humidity data, and record data while the data lines DATA DHT11 pulled by a pull-up resistor remains high; DHT11 this time the DATA pin is the input state, always detect external signals.
Step two:

<a id='dc273cc4-41bf-4fa9-8280-6ffc09de7ff0'></a>

Microprocessor I / O output while the output is set to low, and low retention time can't be less than 18ms, then the microprocessor I / O is set to enter the state, due to the pull-up resistor, the microprocessor I / O that the data lines DHT11 also will go high, waiting to answer DHT11 signals transmitted signal as shown:
<::
chart: A timing diagram showing a signal waveform.
- Y-axis labels: VDD (top line), GND (bottom line).
- The waveform starts at VDD, drops to GND, stays at GND for a period, then rises back to VDD.
- The low period is labeled with a duration of ">18ms".
- Near the rising edge, there is text: "After releasing the bus master pulling".
- Legend:
  - Thick black line: Host signal
  - Thin gray line: Signal from the machine
The host sends a start signal
::>


<a id='e5bb46c5-c129-4ab8-801c-c59a62ee1387'></a>

Step three:
DHT11 the DATA pin when external signals detected low, waiting for the external signal low end, after a delay DHT11 the DATA pin is an output, the output low as 80 microseconds response signal, followed by the output of 80 micro-notify the second high peripheral is ready to receive data, the microprocessor I / O at this time in the input state detecting I / O with low (DHT11 echo signal) to the wait for 80 microseconds high data receiving and sending signals as shown:

<a id='298e09ec-8d4f-46f6-a2d1-3f17e7737061'></a>

- 5-

<a id='ad8b588b-370f-47c1-8547-249b8a7135ba'></a>

Aosong Guangzhou Electronics Co., Ltd.

<a id='d457389a-abd8-4a4c-bf35-8aeb4588ee53'></a>

Order by phone: 4006 305378

<a id='74bd810a-df11-40f4-8a06-483aefd96bc4'></a>

Enterprise QQ: 4006305378

<a id='3efd6345-dd22-4c2c-a914-6ad121aecc1a'></a>

www.aosong.com