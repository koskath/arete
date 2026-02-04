<a id='765ccc7a-b04c-4d7d-b328-58f3734bf834'></a>

ARDUINODOCS

<a id='192a574e-7d82-47cd-8065-a88bccef5ec7'></a>

OO
[illegible]

option All Systems Operational: [x]

Space ID

<a id='176b7651-ce21-4344-b421-db0056960374'></a>

If you can't see the *Space Settings* section is because you are using an Arduino Cloud free plan, check the **plans** with the API feature enabled.

<a id='9246eb6f-f90d-4318-b2f5-1a5e5bf1b475'></a>

At this point you should have three IDs related to your project:
* Variable ID
* Thing ID
* Space ID

<a id='f6d899f2-553f-45c5-897f-ac09e6e40b63'></a>

To properly authenticate the requests we are going to use to upload the data to the Arduino Cloud we need to create **API Keys**.

<a id='ba81c235-5e9a-4976-8ea2-98c642a116a9'></a>

For this, navigate to **API Keys** in the upper left corner drop-down menu and click on
**Create API Key**:

<a id='fe3d4c68-5e70-454c-ac09-f5f97f5e43ae'></a>

<::Screenshot of the Arduino Cloud web application showing the process of accessing and creating API keys. The image is split into two main sections:

Left section:
- A web browser window displaying the Arduino Cloud dashboard. The URL is `app.arduino.cc`.
- A left-hand navigation bar is visible, with "API keys" highlighted in a red box, indicating it has been selected.
- The main content area shows "ARDUINO CLOUD" at the top, followed by "Recent files" with entries like "Thing" and "Dashboard".
- Below that are "Getting Started" and "Documentation" sections.

Right section:
- Another web browser window, also displaying `app.arduino.cc`.
- This view shows the "API Keys" management page. There's a search bar labeled "Search API Keys".
- A prominent green button labeled "CREATE API KEY" is highlighted in a red box at the top right.
- Below the search bar, there are column headers "Client ID" and "Created", indicating a table for listing API keys.
- At the bottom, a message reads: "API keys cannot be used or viewed by members of a shared space." with a "SEE DETAILS" link.

This visual demonstrates the navigation to and interface for generating API keys within the Arduino Cloud platform.
: figure::>
API Keys generation

<a id='349899c5-4b08-46f3-8dd7-55b1e4849768'></a>

You should get a **Client ID** and a **Client Secret**. Save these credentials in a safe place, you will not be able to see them again.

<a id='91004158-523c-42a0-a5af-4bc5c2ca3877'></a>

## Home Assistant Set-Up

Now, let's configure Home Assistant to set the forwarding method to Arduino Cloud.

<a id='0cc1e6d5-0380-4166-9a3c-2d7317a98dfd'></a>

First, we are going to save and define our project IDs, credentials and Keys in a safe place inside the Home Assistant directory called **secrets.yaml**. Use the _File Editor_ Add-on to easily edit this file, and format the data as follows:

<a id='3c7db212-2b83-47b0-a3aa-ab8a6278aac3'></a>

```
arduino_organization: <Space ID>

token_get_payload: '{"grant_type":"client_credentials", "client_id"

arduino_temp_url: https://api2.arduino.cc/iot/v2/things/<your Thin
```

<a id='e9034a63-2e90-43b1-8b0c-68ced2072a8e'></a>

This will let us use this data without exposing it later.

<a id='1a63d5a4-776c-4bab-908a-7150069b3325'></a>

# Stage 2: Visual Content Expansion (Full Transcription)

<::
home-assistant.log.1
Wed, Tue 19 Oct 2021 07:08 PM
home-assistant.log.fault
Wed, Tue 19 Oct 2021 07:08 PM
home-assistant_v2.db
Wed, Wed 25 May 2022 11:07 PM BST
home-assistant_v2.db-shm
Wed, Wed 25 May 2022 11:07 PM BST
home-assistant_v2.db-wal
Wed, Wed 25 May 2022 11:07 PM BST
image
Wed, Sep 29 2021
scenes.yaml

/homeassistant/secrets.yaml
1
2 # Use this file to store secrets like usernames and passwords.
3 # Learn more at https://www.home-assistant.io/docs/configuration/secrets/
4
5 arduino_organization: a0a5b8fd3f3e79ea5bac08b9b4c7c6e
6
7 token_get_payload: {"grant_type": "client_credentials", "client_id": "020c029c0b5f0000f0d11g5", "client_secret": "020c029c0b5f0000f0d11g5",
8
9 arduino_temp_url: https://api2.arduino.cc/iot/v2/things/020c029c-0b5f-0000-f0d1-1g5e-080c0c0d12f3/properties/020c029c-0b5f-0000-f0d1-1g5e-080c0c0d12f3/publish
10 
: screenshot of a web browser displaying a file explorer on the left and a code editor on the right::>