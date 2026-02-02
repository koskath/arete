<a id='82cd3be8-65d5-478c-88a6-ae5ef600c5dc'></a>

The client library also includes some useful syntactic sugar definitions for declaring resources more easily without having to think about input or output resources. These syntactic sugar features are macros that are expanded automatically to define the resources in the standard way.

<a id='32c72c0b-4d63-4af1-a626-c05c03b3398f'></a>

The advantage of using this kind of definition is that resources will be able to handle the state when queried from the API. For example, if a digital pin is enabled or disabled, its current state will be visible in both the API explorer and a dashboard.

<a id='2ddc9314-f57f-4957-9d5a-414194232dfd'></a>

# Control a digital pin

This kind of resource will allow defining a resource for declaring control over a digital pin, so it is possible to alternate over on/off states, which can be used for controlling a LED, a relay, a light, etc.

<a id='6762a2bd-b7fb-419c-b172-490aa9c54d9f'></a>

It is required to define the digital pin as OUTPUT in the setup code, or the resource will not work properly.

```
thing["relay"] << digitalPin(PIN_NUMBER);
thing["relay"] << invertedDigitalPin(PIN_NUMBER);
```

<a id='8605d4d7-0c34-43a0-98a1-cd7c73242be9'></a>

## Define Output Resources

This kind of resource will allow defining a resource for declaring a read-only resource, like a value obtained from a sensor, or a given variable in our sketch.

<a id='141bae95-7f16-4ae5-b310-b80331b94f4b'></a>

In this example, we are defining a resource that exposes a sensor reading, like the DHT11 sensor temperature.

<a id='0d03a60e-39a1-45e7-8ac6-8338e115a325'></a>

thing["temperature"] >> outputValue(dht.readTemperature());

<a id='d605c159-8bb6-4ba5-8ba3-d0512c82946e'></a>

But it is also possible to define an output resource for any global variable in our sketch.

```
thing["variable"] >> outputValue(myVar);
```

<a id='90da2aca-c8d4-45fa-af0d-5365fb43a2f3'></a>

9