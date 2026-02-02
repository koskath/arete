<a id='be4c1f2a-1de1-4e71-9f05-8980088a2f5b'></a>

Now that we have our toolchain running, it is time to code something to push data to the Sigfox Backend. Before presenting the code, **remember** that in the callback we have defined in the Sigfox, we established a payload config that is expecting to receive two floats representing both temperature and humidity. So, our payload must match this definition:

<a id='af70699a-c122-4ea7-8452-300891e7be01'></a>

temp::float:32:little-endian hum::float:32:little-endian

<a id='d5117b0f-34c4-4d69-9c94-3ba86977196e'></a>

In our code, this payload can be easily represented by a `struct` that holds two floats.
Defining custom structs with different data types is possible, but **structure padding** and
**architecture** must be carefully considered. The **Sigfox payload** will require
reconfiguration to ensure proper decoding of the transmitted fields.

<a id='9a753266-98cc-4b03-9b83-321f0d329b0d'></a>

```c
struct data{
    float temp;
    float hum;
};
```

<a id='8e662eea-533f-4120-893e-e735df40b549'></a>

In this case, we are using the Arduino MKRFOX1200 along with a DHT sensor providing temperature and humidity required for the callback we have configured in the Sigfox back-end. If a DHT sensor is unavailable, the board's internal temperature sensor can be utilized by calling `SigFox.internalTemperature()`, and setting the humidity value to zero or any other value.

<a id='614882ad-37d6-4593-b34d-f5e79e02a14b'></a>

11