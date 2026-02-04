<a id='0ba7eb94-fba1-4c0b-a5f9-547f507a3271'></a>

**ARDUINO**DOCS

<a id='cc76f3f3-275a-4108-b525-2624b434a65c'></a>

<::A composite image showing a smartphone screen on the left and an Arduino Nano Matter development board on the right.

The smartphone screen displays a "Light Colour" interface. At the top, there are "Cancel" and "Done" buttons, and the title "Light Colour". Below this, there are three tabs: "Colour", "Temperature", and "Swatch", with "Colour" being selected. The main part of the screen features a circular color picker displaying a spectrum of colors, with a white circle indicating a selected light yellow/green color. Below the color picker, there is a section labeled "BRIGHTNESS" with a slider set to "69%". Further down, there's a white square color swatch and a plus icon.

The Arduino Nano Matter development board is blue with various electronic components. It features a USB-C port on one end, and rows of gold-plated pin headers labeled with numbers and letters (e.g., D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, A0, A1, A2, A3, A4, A5, A6, A7, 3.3V, 5V, GND, RST). A prominent black chip with the "SILICON LABS" logo is visible. The board is labeled "ARDUINO NANO MATTER". There is a green LED illuminated near the USB-C port and a white LED illuminated near the center of the board.: figure::>

<a id='4d961056-819a-4fc6-b857-3edfdc17b678'></a>

You are also able to control your device using voice commands with your personal assistant.

<a id='8941eb2b-84c7-4a4f-b972-a916b22786e2'></a>

If you want to commission your Nano Matter solution with another service, follow the steps in the decommissioning section.

<a id='df2ad858-f6f4-443d-8d26-2f03da67e5c4'></a>

### With Home Assistant

To use Matter with Home Assistant, you will need one of the _Google Home_ or _Apple Home_ devices that can work as a **Thread® Border Router**, as listed in the previous sections.

<a id='810da84d-b0b7-49a4-9470-9deb1397388c'></a>

To set up Home Assistant so that it can manage Matter devices, we need first to install the **Matter Server** add-on. For this, navigate to **Settings** > **Add-Ons** > **Add-On Store** and search for **Matter server**:

<a id='bc31fcba-fc84-4652-8ac8-c9c3a45bd33f'></a>

<::Two screenshots of the Home Assistant web interface, demonstrating the process of installing the Matter Server add-on.

Left screenshot:
Home Assistant interface showing the "Add-ons" section. The left sidebar has menu items including "Settings" which is highlighted. The main content area lists various add-ons such as Cloudflared, ESPHome, File editor, Grafana, InfluxDB, Matter Server, and Terminal & SSH. A search bar for "Search add-ons" is visible. At the bottom right, there's a button labeled "Add to My Add-ons".

Right screenshot:
Home Assistant interface showing the "Add-on Store". The left sidebar again shows "Settings" highlighted. The main content area displays the "Add-on Store" with a search bar where "Matter" has been typed. Under "Official add-ons", "Matter Server" is listed and highlighted with a red box. Its description reads: "Matter WebSocket Server for Home Assistant Matter support". Below this, sections indicate "No results found in ESPHome" and "No results found in Home Assistant Community Add-ons".
: figure::>
Installing the Matter Server

<a id='5330face-9b46-464d-82d4-c7603d4dbbd2'></a>

When the Matter server is correctly installed, navigate to **Settings** > **Devices & Services** > **Add Integration** and search for **Matter**:

<a id='0f055c4a-b443-4ed2-8d5f-51ca8b8b72f9'></a>

<::figure: Two screenshots of a web application, likely Home Assistant, demonstrating the process of installing the Matter integration.The left screenshot shows a modal dialog titled "Select brand". A search bar contains "Matter". Below the search bar, "Matter (MTR)" is highlighted, indicating it's selected. Other options like "TP-Link" and "Serial Port/USB Matter" are visible. The main Home Assistant interface has "Settings" selected in the sidebar and a button "+ ADD INTEGRATION" at the bottom right.The right screenshot shows a subsequent modal dialog titled "What do you want to add?". It lists "Add Matter device" and below it, "Matter (MTR)" is highlighted, indicating selection. The main Home Assistant interface also has "Settings" selected in the sidebar and the "+ ADD INTEGRATION" button visible.:>Installing the Matter integration

<a id='aa76e01a-e8e6-43ee-b085-d65fbe1f20d4'></a>

A prompt will show up asking for a connection method; if you are working with custom
containers running the Matter cover uncheck the hov