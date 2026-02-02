<a id='1ae8a843-0880-4236-a91c-c0f906718335'></a>

12/4/25, 2:52 PM

<a id='01e9202a-1739-403f-ab56-69f68581dd52'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='bea3f173-b9c0-493b-8c2a-ced2d63aa6a8'></a>

ARDUINO DOCS

<a id='e58ebb5d-7a28-4495-baa8-d721b2b9bfd5'></a>

Search on Docs /

<a id='9877fb9f-809f-4d81-b783-b97bebbdefbc'></a>

← Go Back

# Hardware

---

< (navigation arrow)

<a id='6e94308d-cdff-4e5b-bd26-aace6bcb8e44'></a>

MKR GPS Shield

Tutorials
---
MKR GPS Shield Basics

<a id='f0fa55ef-c428-4f20-bb4e-bd0a4bcdd480'></a>

Home / Hardware / MKR GPS Shield / MKR GPS Shield Basics

<a id='9664b915-c2cb-4503-81b5-28ba398fce3e'></a>

# MKR GPS Shield Basics

Learn how to access GPS data from the module on board the MKR GPS Shield.

Author: Karl Söderby
Last revision: 17/07/2024

<a id='d83a91b4-8a11-453e-b45c-248a7eaa1988'></a>

# Introduction

The ability to pinpoint your exact location can be very useful for different types of projects. With the MKR GPS Shield, we can reach high accuracy with minimal power consumption.

<a id='059fe3f9-afcf-404a-aa6b-1d5c1989448c'></a>

In this tutorial, we will use a very
basic example from the
**Arduino_MKRGPS** library, which
records different geolocation data
directly from the GPS shield, and
prints them in the Serial Monitor.

<a id='a01e2521-e4be-4dd9-8508-f8098f66cde6'></a>

# Goals

The goals of this project are:

* Set up the MKR GPS Shield.
* Record longitude, latitude, speed and altitude.
* Print the data in the Serial Monitor.

<a id='c49f6e16-31ea-498e-9cd4-8f156fd4c1a4'></a>

Hardware &
Software Needed

<a id='01f748b8-2798-4ecf-8dca-1344e615e616'></a>

Arduino IDE (online or
offline).

Arduino_MKRGPS library

<a id='155825e0-badf-4601-813c-ace7e226baaa'></a>

ON THIS PAGE

<a id='b026d65e-f407-43d4-9ccf-102c9b470779'></a>

Introduction
- Goals
- Hardware & Software Needed
- Global Positioning System (GPS) —
  - Circuit
- Programming the Board
- Testing It Out —
  - Troubleshoot
- Conclusion

<a id='a273bd2f-ae18-4483-82f6-aab0ec2d11e2'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='763196b6-a54e-4ae9-8e49-29e73a25b181'></a>

1/7

<a id='dfef2815-1cce-40b3-bef6-30f5e5512b74'></a>

Help