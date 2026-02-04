## [cite_start]ARDUINODOCS [cite: 1]

---

![Device added flow](https://t3.gstatic.com/images?pjs=av&q=tbn:ANd9GcR07k2yJ6S9v-Vv649A_uR_jM8m_5uV5uO9v3Kz4Y6k5w)

[cite_start]Then, wait for the device to be commissioned and added to the Google Home app: [cite: 2]

## Device Commissioning Process

This sequence illustrates the process of adding a Matter-compatible device to the Google Home ecosystem.

---

### 1. Consent and Authorization
The first screen displays the heading **"Connect this device to your Google Account"**.
* **Control**: Users are informed that this setup allows for control via **Google Assistant** or the **Google Home app**.
* **Data Handling**: It explains that Google shares local network credentials (like Wi-Fi) with the device and may receive device state information.
* **Firmware**: Google may provide firmware updates from the manufacturer for debugging and product improvement.
* **User Action**: The setup requires the user to tap the **"Agree"** button located at the bottom right.

### 2. Connection Phase
The middle screen shows the status **"Connecting to device..."**.
* **Visual Indicator**: The center features the **Matter logo** surrounded by various geometric shapes (circles, triangles, squares), indicating an active pairing or commissioning session.

### 3. Confirmation
The final screen displays **"Device connected"** accompanied by a checkmark.
* [cite_start]**Completion**: This indicates the device has been successfully commissioned and added to the app[cite: 2, 3].
* **User Action**: The user completes the flow by tapping the **"Done"** button.

---

### Post-Setup Capabilities
Once commissioned, the **Nano Matter** device functions as follows:
* [cite_start]**Manual Control**: You can toggle the built-in **RGB LED** on/off and adjust its **color** and **brightness**[cite: 4, 5].
* [cite_start]**Voice Control**: The device can be operated using **voice commands** through a personal assistant[cite: 6].




[cite_start]**Device added** [cite: 3]

[cite_start]Finally, you will be able to control the Nano Matter built-in RGB LED as a native smart device. [cite: 4] [cite_start]You can turn it on and off and control its color and brightness. [cite: 5] [cite_start]You are also able to control your device using voice commands with your personal assistant. [cite: 6]

![Arduino IDE and Mobile Control Interface](https://t3.gstatic.com/images?pjs=av&q=tbn:ANd9GcT7fS3_v0r3b9O5v8u9L8v9O0L8v9O0L8v9O0L8v9O0L8v9O0L8v9O0)

## Arduino Nano Matter Commissioning and Control

The following images detail the process of connecting an Arduino Nano Matter to a Google account via Matter and controlling its built-in RGB LED.

---

### **1. Device Commissioning Flow**

This three-step process shows the addition of the device to the Google Home app:

* [cite_start]**Step 1: Authorization**: The user is prompted to "**Connect this device to your Google Account**"[cite: 3]. [cite_start]This screen explains that Google will share local network credentials (e.g., Wi-Fi) to get the device online and may receive device state information[cite: 3].
* [cite_start]**Step 2: Connection**: The middle screen shows the status "**Connecting to device...**" with an animated Matter logo[cite: 2, 3].
* [cite_start]**Step 3: Success**: The final screen displays "**Device connected**" with a checkmark[cite: 3]. [cite_start]The user completes the process by tapping the **"Done"** button[cite: 3].

---

### **2. Control and Development Interface**

Once commissioned, the device can be controlled as a native smart device:

* **Arduino IDE**: The left pane shows the C++ code used for the device, including libraries like `<Matter.h>` and `<MatterLightbulb.h>`. The serial monitor displays real-time logs such as "**Setting bulb color to > r: 254 g: 254 b: 254**".
* **Mobile Interface**: The center image shows the Google Home "Matter bulb" interface, featuring a circular color picker for adjusting the LED's hue and saturation.
* **Hardware**: The right image shows the **Arduino Nano Matter** board with its built-in RGB LED illuminated.

---

### **3. Voice and Third-Party Compatibility**

* [cite_start]**Voice Control**: Users can manage the device using voice commands with their personal assistant[cite: 6].
* [cite_start]**Amazon Alexa**: The solution is also compatible with Amazon Alexa products that act as Matter hubs through Thread, such as the Echo (4th Gen), Echo Hub, and various eero models[cite: 8, 9, 10, 13, 16].

You are also able to control your device using voice commands with your personal assistant.


[cite_start]If you want to commission your Nano Matter solution with another service, follow the steps in the decommissioning section. [cite: 7]

---

### [cite_start]With Amazon Alexa [cite: 8]

[cite_start]The Amazon Alexa products that can work as a Matter hub through Thread are listed below: [cite: 9]

* [cite_start]**Echo (4th Gen)** [cite: 10]
* [cite_start]**Echo Show 10 (3rd Gen)** [cite: 11]
* [cite_start]**Echo Show 8 (3rd Gen)** [cite: 12]
* [cite_start]**Echo Hub** [cite: 13]
* [cite_start]**Echo Studio (2nd Gen)** [cite: 14]
* [cite_start]**Echo Plus (2nd Gen)** [cite: 15]
* [cite_start]**eero Pro 6 and 6E** [cite: 16]
* [cite_start]**eero 6 and 5+** [cite: 17]
* [cite_start]**eero PoE 6 and gateway** [cite: 18]
* [cite_start]**eero Pro** [cite: 19]
* [cite_start]**eero Beacon** [cite: 20]
* [cite_start]**eero Max 7** [cite: 21]

[cite_start]Other Amazon devices are compatible with Matter but not Thread. [cite: 22]

[cite_start]To commission your device, open the Amazon Alexa app, click on the upper right **+** symbol, select **device**, and select the **Matter** option. [cite: 23, 24]