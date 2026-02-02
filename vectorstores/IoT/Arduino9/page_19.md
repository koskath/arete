<a id='950fe3f4-8278-41cb-837f-2e0fa896bb40'></a>

12/4/25, 2:52 PM

<a id='d6a75bdc-1393-40eb-bb98-84b2f63ea1bf'></a>

WiFiNINA | Arduino Documentation

<a id='955be11e-cedb-47cc-986f-70b3e22f4e66'></a>

ARDUINODOCS

<a id='81c943a9-b290-47c8-8633-90885610926d'></a>

WL_NO_MODULE: assigned when the
communication with an integrated
WiFi module fails;
WL_IDLE_STATUS: it is a temporary
status assigned when WiFi.begin() is
called and remains active until the
number of attempts expires (resulting
in WL_CONNECT_FAILED) or a
connection is established (resulting in
WL_CONNECTED);
WL_NO_SSID_AVAIL: assigned when no
SSID are available;
WL_SCAN_COMPLETED: assigned
when the scan networks is completed;
WL_CONNECT_FAILED: assigned when
the connection fails for all the
attempts;
WL_CONNECTION_LOST: assigned
when the connection is lost;
WL_DISCONNECTED: assigned when
disconnected from a network;

<a id='aa95b717-0f10-4437-a6f3-651c42830af4'></a>

Example

```
#include <SPI.h>
#include <WiFiNINA.h>

char ssid[] = "yourNetwork";
char key[] = "DØDØDEADFØDABB";
int keyIndex = 0;
int status = WL_IDLE_STATUS;

void setup() {
  //Initialize serial and wai
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port
  }

  // attempt to connect to Wi
  while (status != WL_CONNEC) {
    Serial.print("Attempting");
    Serial.println(ssid);
    status = WiFi.begin(ssid, key);
  }

  // wait 10 seconds for co
  delay(10000);

  // once you are connected :
  Serial.print("You're connec");
}
```

<a id='4c598a92-9a11-4b1c-9a73-6f987e3010e6'></a>

WiFi.macAddress()

<a id='cb238207-bb09-4d15-b1a4-836c1109d81e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='08998486-4938-4498-8c7e-bf7001090375'></a>

20/30