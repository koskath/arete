<a id='b41f5883-6901-4f4a-8cd7-f669ec585a03'></a>

```c
#include <SigFox.h>
#include <SimpleDHT.h>
#include <ArduinoLowPower.h>

#define DHT11_PIN 0

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}
```

<a id='939615ce-750c-445f-ade3-e11d12f79ed5'></a>

```c
void blink(unsigned int count, unsigned long ms){
    for(int i=0; i<count; i++){
        digitalWrite(LED_BUILTIN, HIGH);
        delay(ms);
        digitalWrite(LED_BUILTIN, LOW);
        delay(ms);
    }
}
```

<a id='b67ab491-b486-4357-874b-cfd6d5bfeff6'></a>

void send_data(){
//Initialize Sigfox module
SigFox.begin();
delay(100);

// Enable debug LED and disable automatic deep sleep
SigFox.debug();

// clears all pending interrupts
SigFox.status();
delay(1);

// define Sigfox payload data structure
struct data{
  float temp;
  float hum;
};

// read temperature and humidity from DHT sensor connected at
pin DHT11_PIN
SimpleDHT11 dht11;
byte temp, hum;
dht11.read(DHT11_PIN, &temp, &hum, NULL);

<a id='98c5296d-d2ba-4822-913d-1da729dd13e7'></a>

// NOTE! It is not quite efficient sending bytes as floats over
the net, but this is just for illustrative purposes
struct data reading;
reading.temp = temp;

<a id='03df01b7-9d9f-4a45-90c3-07c2bebc1bbc'></a>

13