<a id='faa29c76-6e38-4cc4-a510-34a294e5ffb4'></a>

ARDUINODOCS

<a id='b38e16b2-fced-45c9-b809-5db5d9153cdf'></a>

Nano Matter Temperature in Home Assistant

<a id='49109390-c147-43cf-bf93-80db826f2548'></a>

Be aware that the Matter integration for Home Assistant is still in BETA, it can receive major updates and its functionality may vary between different vendors.

<a id='ef24a045-f7ab-40ae-b818-c309ff33ca1d'></a>

## Arduino Cloud Set-Up

Let's walk through a step-by-step demonstration of how to set up the Arduino Cloud.

Log in to your Arduino Cloud account; you should see the following:

<a id='d33394c2-9a59-4ad6-a088-c1aa3f6657f7'></a>

app.arduino.cc

Arduino Cloud

Devices
1 online

Things
48 / 50

Members
20 in this Shared Space

CREATE NEW

Demo PRO BU
Christopher Wendell

Home
Sketches
Devices
Things
Dashboards
Triggers
Resources
IoT Templates
Integrations
Space Settings

Recent Files

All items ▾
Name
Owner
Last modified
Creation Date

Thing
Nano Matter Chris
Christopher Wendell
Mar 20, 2024, 10:47 AM
Mar 15, 2024, 11:25 AM

Dashboard
Nano Matter Temperature
Christopher Wendell
Mar 20, 2024, 10:38 AM
---

Getting Started

GETTING STARTED
Discover Arduino Cloud
Discover what Cloud can offer based on the device you have at hand

TUTORIAL
Arduino Cloud Editor
A step-by-step guide to set up your online development environment

DOCUMENTATION
Cloud Dashboard & Widgets
Learn about Dashboards and the different widgets that can be used

DOCUMENTATION
Arduino Cloud overview
Configure, program and connect your devices, it's easy with Arduino Cloud

Documentation

SEE ALL

Hardware documentation
Browse datasheets, guides and other technical documentation.

Arduino Cloud APIs
Arduino Cloud has two different set of APIs, read more in our documentation

All Systems Operational

<a id='9f6072e9-db6d-4a3e-9e94-02ee937b1aeb'></a>

Navigate to **Things** in the left bar menu and click on **+ Thing** to add a Thing:

<::A screenshot of a web application interface. On the left sidebar, a menu lists options such as "Home", "Sketches", "Devices", "Things", "Dashboards", "Triggers", "Resources", "IoT Templates", "Integrations", and "Space Settings". The "Things" option is highlighted with a red outline, indicating it is selected. The main content area shows a table header with columns: "Name", "Device", "Sketch", "Last modified", and "Creation date". Above the table, there's a search bar labeled "Search and filter Things". In the top right corner of the main content area, a prominent green button with a red outline reads "+ THING".
: screenshot::>

Creating a Thing

<a id='5fee4cef-f2d3-4a74-9ac2-13422a839584'></a>

Give your Thing a name and click on **ADD** to add the temperature variable:

<a id='e241d138-2ba8-4e7b-9daa-d59d8644f113'></a>

Nano Motor Chris Thing | Arduino IoT Cloud

app.arduino.cc/things/999ce296-212f-4000-84f5-5fce7180b44b/setup

Thing
Nano Motor Chris

Setup Sketch Metadata

Cloud Variables

ADD

Associated Device
Select the device you want to use or configure a new one.

Variables are what you can monitor or control to make your Thing function. For example a temperature or a smart lamp. Once created, you can use them in your Sketch.

GO
Select Device

Network
Enter your network credentials to connect your device.

GO
Configure

Set webhook

<a id='77b57814-5ea6-478b-9bd4-2dc950eee385'></a>

Adding a variable

<a id='e31b5a82-567d-4e74-b283-d48ecbd7b493'></a>

Define the variable with the following settings: