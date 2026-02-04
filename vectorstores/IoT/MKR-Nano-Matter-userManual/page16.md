<a id='29d79e75-cbab-467a-aed4-db1a5950e848'></a>

ARDUINODOCS

<a id='3d0ae947-ac68-428b-9c6f-4d4405488e74'></a>

```cpp
1 #include <Matter.h>
2 #include <MatterTemperature.h>
3 
4 MatterTemperature matter_temp_sensor;
5 
6 void setup()
7 {
8   Serial.begin(115200);
9   Matter.begin();
10 
11   pinMode(BTN_BUILTIN, INPUT_PULLUP);
12   pinMode(LEDR, OUTPUT);
13   digitalWrite(LEDR, HIGH);
14 
15   matter_temp_sensor.begin();
16 
17   Serial.println("Matter temperature sensor");
18 
19   if (!Matter.isDeviceCommissioned()) {
20     Serial.println("Matter device is not commissioned");
21     Serial.println("Commission it to your Matter hub with the manual pairing code or QR code:");
22     Serial.printf("Manual pairing code: %s\n", Matter.getManualPairingCode());
23     Serial.printf("QR code URL: %s\n", Matter.getOnboardingQRCodeUrl());
24   }
25   while (!Matter.isDeviceCommissioned()) {
26     delay(200);
27     decommission_handler(); // if the user button is pressed for 3s
28   }
29 }
```

<a id='8dddf326-7b78-464f-8cd1-c56a764b14b0'></a>

The main code functions are explained below:

* The temperature sensor object is created with the `MatterTemperature matter_temp_sensor;` statement. To initiate it, in the `setup()` function, we used `matter_temp_sensor.begin();`
* The `decommission_handler()` lets us unpair the device from a previous platform.
* The microcontroller's internal temperature is measured with the function `getCPUTemp();`
* The temperature value is advertised using the `matter_temp_sensor.set_measured_value_celsius(current_cpu_temp);` function.

<a id='930ec7a0-28c5-4228-b8d7-35da652ffcc6'></a>

After uploading the code to the Nano Matter, verify it is decommissioned from any other service previously used. For this, open the Serial Monitor and reset the board by clicking on the reset button.

<a id='490614fe-559d-4267-a5bb-eca910efcaa5'></a>

If it is not decommissioned you will see temperature readings printed in the Serial Monitor. To decommission it, follow these steps:

* Press the user button for **10 seconds** until the board's built-in LED starts **blinking in red**. You will also see a message confirming the process in the Serial Monitor.
* Finally, reset the board by clicking on the reset button and you should see the Matter commissioning credentials in the Serial Monitor.

<a id='f3ae442b-09cc-42de-a821-a2408b6c5020'></a>

## Device Commissioning

Now it is time to commission the Nano Matter with Home Assistant, for this, follow the steps explained in this section.

<a id='ac2cee81-d961-4ff5-95ab-e742990b714f'></a>

Once you have everything set up and running you will be able to monitor the Nano
Matter temperature in Home Assistant:

<a id='43ed7769-4aec-4bf5-9d16-1366c3b4fdcf'></a>

<::Screenshot of a web browser displaying the Home Assistant interface, alongside a diagram illustrating a Thread Border Router connected to a circuit board.

**Home Assistant Interface:**
- Browser tab title: "Overview - Home Assistant"
- Address bar: `homesassistant.local:8123/lovelace/default_view`
- Left sidebar navigation:
  - "Home Assistant"
  - Overview: [x]
  - Energy
  - Map
  - Logbook
  - History
- Main content area (Home tab):
  - Weather card: Yellow circle icon, "Sunny", "Forecast Home", "25.6 °C", "72%"
  - Device card: Thermometer icon, "Matter device Temperature", "36.35 °C", followed by a partially visible line graph.

**Thread Border Router Diagram:**
- An icon representing a network device labeled "Thread Border Router".
- Arrows indicating connections from the Thread Border Router to a blue circuit board with multiple pins (e.g., RX, TX, RST, GND, 3V3, 5V, D0-D13, A0-A5) and various components.
: figure::>