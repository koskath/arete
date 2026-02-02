<a id='1c7b9643-a924-405e-b565-668d016a81d1'></a>

```
unsigned long lastCheck = 0;

loop(){
    thing.handle(); // required thing handle

    unsigned long currentTs = millis();

    if(currentTs-lastCheck>=60*60*1000){
        lastCheck = currentTs;
        if(dht.readTemperature()>30){
            thing.call_endpoint("high_temp_email");
        }
    }
}
```

<a id='1faab68e-c51c-4f36-8272-960235c132bc'></a>

Endpoints offer significant creative flexibility, allowing for automation based on various events. For example, endpoints can be triggered by a presence sensor detection, a humidity sensor reporting no water in plants, or a device's unexpected location. Furthermore, endpoints can be integrated with services like IFTTT (If This Then That) to interact with multiple third-party platforms.

<a id='641c94fb-48f7-4fad-8141-44cafb30f1a8'></a>

# Sending Data to Endpoints

Sending data to an endpoint (in JSON format) is also quite easy. We also need to call the `call_endpoint` method, but in this case, adding some information based on the `pson` data format, which will be automatically converted to JSON. For example, if we want to report data to a third-party service like Keen.io, we can create such kind of endpoint in the console. Once configured, we can call the endpoint with our readings, for example, with humidity and temperature values from a DHT sensor.

<a id='3121e59c-ea77-4223-86a2-4d7f21b3b2de'></a>

```
// be careful of sending data at an appropriate rate!
pson data;
data["temperature"] = dht.readTemperature();
data["humidity"] = dht.readHumidity();
thing.call_endpoint("keen_endpoint", data);
```

<a id='cc576206-9e19-4c85-b82a-9ddad3c289ee'></a>

Data can also be sent based on a defined resource; for instance, if a resource already provides temperature and humidity. It is possible to reuse this definition for sending the same data to the endpoint, without having to redefine the sensor reading:

<a id='cb2d893a-2307-444a-8e94-ba8dfa5424cd'></a>

15