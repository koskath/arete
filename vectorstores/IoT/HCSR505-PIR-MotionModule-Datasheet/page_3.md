<a id='9cabbc48-af55-4a7a-9628-679a7ae23d2b'></a>

<::logo: TruSens
TruSens
The logo features the word "TruSens" with "Tru" in blue and "Sens" in red, separated by blue and red curved lines that resemble a signal icon.::>

<a id='759f9962-e744-4df5-a38d-d86cbc9e8c0b'></a>

PIR Motion Module
HC-SR505

<a id='6751f148-a884-48fe-bf6e-1055a9ec427b'></a>

Order code: **78-4110**

<a id='6fd7aabe-652f-44df-aa57-24e10c3c0773'></a>

## Hardware
Connect the PIR Motion Sensor to your Arduino/Crowduino power supply pin and digital pins.
You can can connect the "s" terminal to any of your arduino Pins, like the "D6" as belows:

<a id='f3a779b1-6dbe-4e85-bb08-16593e3cc6f4'></a>

<::An orange circuit board, resembling an Arduino, is connected via a blue USB cable to the left. Wires extend from the circuit board to a small sensor module on the right. Labels on the circuit board indicate connections: a yellow wire connected to "D6", a black wire connected to "GND", and a red wire connected to "5V". These three wires then connect to the sensor module, which has corresponding labels "+", "S", and "-" on its connector. The sensor module itself is green with a white dome, characteristic of a PIR motion sensor.: figure::>

<a id='0779355c-3c6f-4ccf-8565-638b95640023'></a>

## Programming

1. Copy the following program to Arduino IDE and upload to your Arduino/Crowduino:

<a id='fdaeb961-e117-44b8-bf01-1fd6903f21cc'></a>

void setup()
{
  Serial.begin(9600);
  pinMode (6, INPUT);
  digitalWrite(6,LOW);
}
void loop()
{
  if (digitalRead(6)==HIGH)
  {
    Serial.println("Somebody is here.");
  }
  else
  {
    Serial.println("Nobody.");
  }
  delay(1000);
}

<a id='bc04c920-95a9-4896-982a-8dbdcda4beca'></a>

Page 3 of 4

<a id='e4a7128b-231d-42a9-921d-a45e1ebae479'></a>

www.rapidonline.com