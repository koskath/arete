<a id='6827d6df-9082-4835-a723-72b7a292d30a'></a>

thinger.io Overview Statistics Dashboards Devices Endpoints Account Profile Settings Resources Community Github Libraries Connect Twitter Email Resources ESP8266 Heading Heading <::A donut chart displaying a value of "268.51°" in the center, with approximately 75% of the circle filled.: chart::> <::A screenshot of a web browser's "Developer Tools" window, open to the "Network" tab. The table lists multiple network requests for "resource 'heading'" with columns including Name, Status, Type, Initiator, Size, and Time. Below the table, it shows "62 requests | 1.1 MB transferred | Finish: 7.35 s | DOMContentLoaded: 1.12 s | Load: 1.29 s".: screenshot::> <::An image of an ESP8266 development board with multiple wires connected to it, mounted vertically.: image::> © 2019 Copyright. Thinger.io

<a id='49cc9dba-d303-40c1-aa38-0ac9f07b7a40'></a>

```
void setup(){
  thing["heading"] >> [] (pson& out){
    out = getHeading();
  };
}

float previousHeading = 0;
void loop() {
  thing.handle();
  float currentHeading = getHeading();
  if(abs(currentHeading-previousHeading)>=1.0f){
    thing.stream(thing["heading"]);
    previousHeading=currentHeading;
  }
}
```

<a id='c665bf74-eb92-45ee-9d95-58299f60b704'></a>

# Enabling Debug Output

Thinger.io library provides extensive logging of its activities, which is especially useful when one needs to troubleshoot authentication and Wi-Fi connectivity issues. Include this definition in the sketch, but *make sure it comes first*, before any other includes (it was reported to cause crashes on some boards otherwise):

<a id='cf4017f6-066b-4a46-8502-67b49a9971f8'></a>

#define THINGER_SERIAL_DEBUG

// the rest of the sketch goes here

<a id='ac062a00-f361-4d4a-9f47-ef88e4bca074'></a>

20