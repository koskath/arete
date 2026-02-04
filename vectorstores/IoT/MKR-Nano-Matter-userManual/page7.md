<a id='ce75791f-1bc1-4000-9fcb-435ef8dc6555'></a>

ARDUINODOCS

<a id='ceedb85c-a98f-4b78-9133-c38c17ea02d6'></a>

#include <Matter.h>
#include <MatterLightbulb.h>

#define LED_R LED_BUILTIN
#define LED_G LED_BUILTIN_1
#define LED_B LED_BUILTIN_2

MatterColorLightbulb matter_color_bulb;

void update_led_color();
void led_off();
void handle_button_press();
volatile bool button_pressed = false;

void setup()
{
  Serial.begin(115200);
  Matter.begin();
  matter_color_bulb.begin();
  matter_color_bulb.boost_saturation(51); // Boost saturation by

  // Set up the onboard button
  pinMode(BTN_BUILTIN, INPUT_PULLUP);
  attachInterrupt(BTN_BUILTIN, &handle_button_press, FALLING);

  // Turn the LED off
  led_off();

  Serial.println("Arduino Nano Matter - color lightbulb");
}

<a id='c55becab-e2ff-45ac-98a8-29fab581289b'></a>

Here is the example sketch main functions explanation:

* In the `setup()` function, Matter is initialized with `Matter.begin()` alongside the initial configurations of the board to handle the different inputs and outputs.
* The device commissioning is verified with `Matter.isDeviceCommissioned()` to show the user the network pairing credentials if needed, and the connection is confirmed with the `Matter.isDeviceThreadConnected()` function.
* With the `matter_color_bulb.is_online()` function, we confirm that the device is online and reachable by the coordinator app.
* In the `loop()` function, the RGB LED is controlled on and off with `matter_color_bulb.set_onoff(state)`, the current state is retrieved with `matter_color_bulb.get_onoff()` and the button state is read to control the LED manually.
* In the `update_led_color()` function, the color defined in the app is retrieved using the function `matter_color_bulb.get_rgb(&r, &g, &b)` that stores the requested color code in RGB format variables.

<a id='3824cf25-4d17-4656-a9e7-34caf628af4e'></a>

To upload the code to the Nano Matter, click the **Verify** button to compile the sketch and check for errors; then click the **Upload** button to program the board with the sketch.

<a id='429a10d9-6768-4117-832b-f54602e2b60a'></a>

<::screenshot of the Arduino IDE showing the 'nano_matter_lightbulb_color' sketch open. The toolbar is highlighted, specifically showing the 'Verify' (checkmark icon) and 'Upload' (right arrow icon) buttons, and a dropdown menu displaying "Arduino Nano Matter" as the selected board. A text label "VERIFY AND UPLOAD BUTTONS" points to these controls. The code editor window displays comments and code, including compatible boards "Arduino Nano Matter" and "x624 Dev Kit", and #define statements for LED pins. Upload the Matter RGB example: screenshot::>

<a id='148e3d6b-c155-42e4-9261-e83c70b79ce6'></a>

After the code is uploaded, open the Arduino IDE Serial Monitor and reset the board by