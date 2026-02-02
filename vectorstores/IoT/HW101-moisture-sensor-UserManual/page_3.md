<a id='9678fec9-59b2-458b-be2e-b9b30232f432'></a>

<::logo: HaiWang
HaiWang
A blue stylized 'W' shape with a central rectangular cut-out sits above the company name in red text.::>

<a id='2b001a1d-7dea-4741-b476-c1b4fccb6bdf'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULI

<a id='5e346f59-c429-48c3-8943-62192358a7f0'></a>

<::An image showing an Arduino board (DFRduino UNO v3.0[R3]) connected to a Capacitive Soil Moisture Sensor v1.0. The DFRduino board is black with various components and headers, including a USB port, power jack, digital pins (0-13, GND, AREF), analog pins (A0-A5), and power pins (IOREF, RESET, 3V3, 5V, GND, GND, VIN). The board has 'DFROBOT DFRduino UNO v3.0[R3]' printed on it. The capacitive soil moisture sensor is a black, elongated, spade-shaped PCB with 'Capacitive Soil Moisture Sensor v1.0 DFROBOT' printed on it. It has a 3-pin connector. Three wires connect the sensor to the Arduino: a red wire from the sensor to the 5V pin on the Arduino, a gray wire from the sensor to a GND pin on the Arduino, and a blue wire from the sensor to the A0 analog input pin on the Arduino.: figure::>

<a id='b466aad7-fa97-42e5-b4ca-3b58b0503aa4'></a>

# Calibration code

1. Before officially testing the soil moisture, a calibration process is required;
2. Burn in the calibration code to the Arduino main control board;
3. Open the serial monitoring assistant.
---


<a id='13f6dcf7-26c6-483f-bcf9-516bd7cf38af'></a>

```
void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop() {
  int val;
  val = analogRead(0); //connect sensor to Analog 0
  Serial.print(val); //print the value to serial
  delay(100);
}
```

<a id='1a458595-a1c3-442e-8275-facac3e81bc9'></a>

# Calibration procedure

## Dry humidity calibration

Calibration instructions: define a measurement range by reading the sensor values in air and water respectively.
Open the serial monitor and set the baud rate to 9600 according to the program.

<a id='cf478a0b-80d6-4d4d-a1c7-8fa78a5ec642'></a>

First, place the sensor in the air to read the analog value, which represents the reading when dry. Then take a glass of water, insert the sensor into the water to a certain depth (make a mark, this depth is the depth you will insert into the soil), must not exceed the red warning line! And record the analog value read at this time, which represents 100% humidity. (The output data is inversely proportional to the humidity, and the output in the water is the smallest.) The insertion depth is recommended as shown in the figure.