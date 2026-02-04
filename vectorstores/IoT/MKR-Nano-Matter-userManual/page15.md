<a id='095e8bc6-9f35-4cb2-80f0-64c1a3be53ee'></a>

ARDUINODOCS

<a id='88aca150-af97-435a-8a1a-a1ecffb389f8'></a>

```c
1 #include <Matter.h>
2 
3 void setup() {
4   // put your setup code here, to run once:
5   Serial.begin(115200);
6 
7   Matter.begin();
8   pinMode(BTN_BUILTIN, INPUT_PULLUP);
9   pinMode(LEDR, OUTPUT);
10  digitalWrite(LEDR, HIGH);
11 }
12 
13 void loop() {
14   // put your main code here, to run repeatedly:
15   decommission_handler();
16 }
17 
18 
19 void decommission_handler() {
20   if (digitalRead(BTN_BUILTIN) == LOW) { //Push button pressed
21     // measures time pressed
22     int startTime = millis();
23     while (digitalRead(BTN_BUILTIN) == LOW) {
24 
25     }
26     int elapsedTime = (millis() - startTime) / 1000.0;
27 
28     if (elapsedTime > 10) {
29       Serial.printf("Decommissioning!\n");
30       for (int i = 0; i < 10; i++) {
31 
32       }
33     }
34   }
35 }
```

<a id='9a0d3602-f6da-45bb-97dd-fd28760c7907'></a>

The sketch above allows you to decommission your board manually after **pressing** the Nano Matter user button for **10 seconds**. You can monitor the status in the Arduino IDE Serial Monitor.

<a id='1b6292e8-bb37-4afc-a8da-5c4e2b13e491'></a>

# Arduino Cloud
The Nano Matter has no built-in Wi-Fi® but can be seamlessly integrated with the Arduino Cloud using its API and Matter.

<a id='4ba261f7-a294-4db1-98aa-2760cbdd26da'></a>

We are going to use the Home Assistant Matter integration to create automations and scripts that help us forward the Nano Matter data to the Arduino Cloud.

<a id='ff6f6cf6-7c7a-4279-8f73-edb5506544f6'></a>

In case it is the first time you are using the Arduino Cloud:

* To use the Arduino Cloud, you need an account. If you do not have an account, create one for free here.
* See the Arduino Cloud plans and choose one that features **API** support.

<a id='039f8ea3-5a12-4472-83a2-66371da48bc5'></a>

As a practical example, we are going to use the Nano Matter CPU temperature sensor and send the data to Arduino Cloud for monitoring. We will leverage the variety of widgets to create a professional and nice-looking user interface.

<a id='5717385f-caa8-45be-b1eb-eb6ad2b871de'></a>

## Nano Matter Programming

The application sketch below is based on the `matter_temp_sensor` example that can be also found in **File > Examples > Matter**. This variation includes the `decommission` feature to show it implemented in a real application.

<a id='59ddb7bd-859d-4dba-b2d5-67eb23c12b3f'></a>