<a id='a0285a2e-9dac-47b6-8d6d-14eec88249ec'></a>

ARDUINODOCS

<a id='3f9e58ef-e689-452c-b8d5-4dc6442b4da7'></a>

```
1 python arduino_matter_provision.py nano_matter 1
```

<a id='53c6e1d7-8aa7-4833-b736-26d0bf716b22'></a>

Run the script to change the provisioning data using the given structure.
<::A screenshot of a Visual Studio Code window.
File, Edit, Selection, View, Go, Run menus are visible at the top.

The left sidebar shows the EXPLORER panel with the following structure:
- ARDUINO MATTER PROVISION
  - > binaries
  - arduino_matter_provision.py (highlighted)
  - readme.md
Below the explorer, there are sections for OUTLINE, TIMELINE, and SERIAL PORTS.

At the bottom, a terminal panel is open with tabs: PROBLEMS, OUTPUT, TERMINAL, PORTS, MEMORY, ARTIS, DEBUG CONSOLE. The TERMINAL tab is selected.
The terminal prompt reads: "D:\MyRepositories\arduino_matter_provision>"
On the right side of the terminal panel, there are options for "powershell" and "cmd".
: figure::>

<a id='c9bfe95d-6c17-434a-adf3-1da3365ba87f'></a>

Once the script finishes, open the **Arduino Serial Monitor**. You will see the updated commissioning credentials there, no need to re-upload the sketch.

<a id='5099cb5b-4c6c-46d6-b54f-c3e84b9f14a1'></a>

Here's what the new credentials might look like:

*   Manual Pairing Code: 00417637863
*   QR code URL:
    https://project-chip.github.io/connectedhomeip/qrcode.html?data=MT%3A8YT00-D000CQ-01VB10

<a id='6c96c91f-e7ad-40bb-9765-79ed399e268f'></a>

Make sure all your Nano Matter boards has been configured with a different ID.

<a id='b57b8fea-bff0-4c2a-905a-5673196a78bd'></a>

## Device Decommissioning

If you have a Matter device configured and working with a _specific platform_, for example with the Google Home ecosystem, and you want to integrate it with Alexa or Apple Home instead, you need to decommission it first from the previous service.

<a id='e1d3924a-1f27-458d-8706-165a85c9afe7'></a>

In simple terms, **decommissioning** refers to unpairing your device from a current service to be able to pair it with a new one.

<a id='66cceaab-1ce9-4bec-bff7-bdeebfb452de'></a>

i Use the library built-in example found in **File > Examples > Matter > matter_decommission.**

You can integrate this method in your solutions to leverage the Nano Matter built-in button to handle decommissioning: