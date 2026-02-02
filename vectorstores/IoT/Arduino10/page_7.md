<a id='d35485ad-a7be-474e-a22d-2f886175bdc4'></a>

12/4/25, 2:52 PM

<a id='591b2356-2341-4d88-9c20-3f93b544c586'></a>

WiFiNINA | Arduino Documentation

<a id='b0c84f2e-8c53-4878-bcb7-585404f11ba7'></a>

ARDUINODOCS

<a id='be15d152-b655-463c-bdc5-452e14f4993a'></a>

```c
#include <SPI.h>
#include <WiFiNINA.h>

char ssid[] = "myNetwork";
char pass[] = "myPassword";

int status = WL_IDLE_STATUS;
char servername[]="google.com";

WiFiClient client;

void setup() {
  Serial.begin(9600);
  Serial.println("Attempting");
  Serial.print("SSID: ");
  Serial.println(ssid);

  status = WiFi.begin(ssid, pass);
  if ( status != WL_CONNECTED ) {
    Serial.println("Couldn't");
    // don't do anything else
    while(true);
  }
  else {
    Serial.println("Connected");
    Serial.println("\nStartin");
    // if you get a connectio
    if (client.connect(server
```

<a id='8cb52e65-600c-440a-94b8-a34ed050b944'></a>

client.connectSSL()

<a id='ebb97f72-778e-4cfe-972e-8350dcfbe896'></a>

# Description
Connect to the IP address and port specified in the constructor using the SSL protocol. The method connectSSL is required when the server provides only HTTPS connections. Before using this method, it is required to load the SSL certificate used by the server into the Arduino WiFi module. The boards come already loaded with certificates and it should be ready to use. To change or upload new SSL certificates you should follow the procedures that will be made available. connectSSL() also supports DNS lookups when using a domain name (e.g., google.com).

<a id='318efe34-338f-43a5-b54d-1db8d0aa0639'></a>

# Syntax

```
1 client.connectSSL (ip, port)
2 client.connectSSL (URL, port)
```

<a id='2cd96d1e-b6ba-45a5-893d-f7780b4f1bda'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e9c41620-4a40-4d02-9a03-1748efa629d6'></a>

7/16