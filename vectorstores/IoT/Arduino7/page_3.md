<a id='a3b2367b-97a8-487f-9edc-996fd74fd39b'></a>

12/4/25, 2:52 PM

<a id='5c05efa9-abbb-444a-8c40-701c1a3884d2'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='46a70e3f-b396-4aad-a6ab-03476d8466d8'></a>

ARDUINODOCS

<a id='3e309b8b-03e9-4cc7-ad2a-bf9107fa48b1'></a>

# Circuit

The circuit in this tutorial is pretty
simple, and the simplest assembly
is to connect an I2C cable from a
MKR board directly to the MKR
GPS Shield. This cable comes with
every GPS shield, and has an
ESLOV connector at each

<a id='15e8e2eb-1cf3-491a-80be-735f0e4311be'></a>

<::logo: [Not a Logo]
[No readable text]
[No notable visual elements]::>

<a id='05789e39-a902-4c55-b2b4-5751eb32148e'></a>

If you are using a third party cable to connect the MKR board and MKR GPS Shield via I2C, make sure the cable is wired identically to the cable that comes with the shield.

<a id='5ff27b31-98a1-494e-b4a6-2b6b180dd3a8'></a>

Programming the Board

<a id='c1f03eea-4da9-492b-b0e9-1b18000ddda2'></a>

We will now get to the
programming part of this tutorial.

1. First, let's make sure we have
the drivers installed for the board
we are using. If we are using the
Cloud Editor, we do not need to
install anything. If we are using an
offline editor, we need to install it
manually. This can be done by
navigating to **Tools > Board >**
**Board Manager**.... Here we need
to look for the **Arduino SAMD**
**boards (32-bits Arm® Cortex®-**
**M0+)** and install it.

<a id='24d8c736-0dc4-47a9-ad27-13756ded18d0'></a>

2. Now, we need to install the
library needed. If we are using the
Cloud Editor, there is no need to

<a id='da2dd7aa-f119-4757-ba3f-3fdd54349a87'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='8fe79c88-a9a1-47ca-9512-a4630efb9684'></a>

3/7