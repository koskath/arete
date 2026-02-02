<a id='1a55e575-9f64-44b8-a954-eddd49f3fba9'></a>

#include <SigFox.h>

<a id='3858d126-f243-4c51-ae8f-d8ef865f7dc0'></a>

void setup() {
  Serial.begin(9600);
}

<a id='dce69c13-9066-41ba-b390-9521427f1026'></a>

while(!Serial) {};

<a id='735a9936-ff27-4f9d-af45-f947cdf205f2'></a>

```c
if (!SigFox.begin()) {
    Serial.println("Shield error or not present!");
    return;
}
```

<a id='eac9b17a-20ed-4de7-9a87-8fdc9be13378'></a>

```
String version = SigFox.SigVersion();
String ID = SigFox.ID();
String PAC = SigFox.PAC();
```

<a id='45d912c5-2053-41d6-9001-a8ad19eb817d'></a>

// Display module information
Serial.println("MKRFox1200 Sigfox first configuration");
Serial.println("SigFox FW version " + version);
Serial.println("ID = " + ID);
Serial.println("PAC = " + PAC);

<a id='3c71095d-dd69-465a-af38-8779b9270774'></a>

Serial.println("");

<a id='74846a7c-eb1e-43e0-bcbc-75ae5ec6c763'></a>

Serial.print("Module temperature: ");
Serial.println(SigFox.internalTemperature());

<a id='cb21c66a-d6cb-4f71-a5cb-f15278a2e653'></a>

Serial.println("Register your board on https://backend.sigfox.com/activate with provided ID and PAC");

<a id='d72e0fab-acae-414a-88e1-57ce7ddae624'></a>

delay(100);

<a id='643219ab-91f4-4257-9396-867bd157b31a'></a>

// Send the module to the deepest sleep
SigFox.end();

<a id='4acdedb0-1136-43a6-814b-2461c8a89772'></a>

}
void loop() {
ר
// put your main code here, to run repeatedly:

<a id='032f70fa-9de5-43ee-ac29-0b75c825a3be'></a>

**Notice:** From this point on, it is assumed that the board has already been registered on the Sigfox account. If not, refer to the [First Configuration ↗](https://example.com/first-configuration-tutorial) tutorial from Arduino.

<a id='64c1192c-665a-4811-9514-83f27a5a67e1'></a>

Pushing data to Sigfox

<a id='7c9f481c-76d7-40b7-8878-954bf9a2b25e'></a>

10