<a id='8572c888-6d52-4947-ab94-40cf0ff9dfc8'></a>

<::logo: HaiWang
HaiWang
The logo features a stylized blue 'W' shape, which also incorporates an 'H' within its structure, with the brand name 'HaiWang' in red text below it.::>

<a id='b7e89a98-8f71-41a3-8bfc-a9fcae6614ae'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULE

<a id='5713b11a-b720-4957-9041-abd5406f4a41'></a>

GNU Lesser General Public License.
See <http://www.gnu.org/licenses/> for details.
All above must be included in any redistribution
***

<a id='eb84f2aa-8e24-4620-bd96-8926e1a568bd'></a>

/***Notice and Trouble shooting***
1. Connection and Diagram can be found here
2. This code is tested on Arduino Uno.
***/

<a id='b7c4d5a2-d3c7-429c-b047-1d382332211f'></a>

const int AirValue = 520; //you need to change this value that you had recorded in the air
const int WaterValue = 260; //you need to change this value that you had recorded in the water
int intervals = (AirValue - WaterValue)/3;
int soilMoistureValue = 0;

void setup() {

<a id='35fb35e5-7c56-4b8d-bec5-3b17631f0779'></a>

```c
}
void loop() {
  soilMoistureValue = analogRead(A0); //put Sensor insert into soil
  if (soilMoistureValue > WaterValue && soilMoistureValue < (WaterValue + intervals))
  {
    Serial.println("Very Wet");
  }
  else if (soilMoistureValue > (WaterValue + intervals) && soilMoistureValue < (AirValue - intervals))
  {
    Serial.println("Wet");
  }
  else if (soilMoistureValue < AirValue && soilMoistureValue > (AirValue - intervals))
```

<a id='2175af76-e81a-426e-af2a-b3e7e3082e47'></a>

{Serial.println("Dry");}delay(100);}
---

<a id='1ec32448-6c5d-4009-ae73-e208a991fe30'></a>

RFQ

Q 1. Why is my reading very different from the actual value, I use your Romeo?

<a id='013ac0c9-82b0-4cc5-ac82-915fb1d2224c'></a>

A: Hello! Because Romeo's analog port A0 has an external button, please set the switch next to the button to Off, or use another analog port.

<a id='059b0acc-2588-4792-9a03-627777be8fdb'></a>

Serial.begin(9600); // open serial port, set the baud rate to 9600 bps