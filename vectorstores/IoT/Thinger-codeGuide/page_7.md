<a id='e4396056-5e8f-49e5-aed9-537ab6d1b74e'></a>

Defining an output resource is quite similar to defining an input resource, but in this case it is used the operator `>>`. In the callback function, we can fill the output value with any value we want, like in this case, the output from a sensor reading.

<a id='939f7db0-790d-4b2a-9c49-a0ad667a2648'></a>

thing["temperature"] >> [](pson& out){
    out = dht.readTemperature();
};

<a id='727b0a73-730a-43f7-a468-d22c8a64b62a'></a>

*Read multiple datasets*

In the same way, the input resources can receive multiple values at the same time, the
output resources can also provide multiple data. This is an example of providing both
latitude and longitude from a GPS.

<a id='a4854b79-a2da-483f-9916-3294a2986e55'></a>

```
thing["location"] >> [] (pson& out) {
    out["lat"] = gps.getLatitude();
    out["lon"] = gps.getLongitude();
};
```

<a id='2872323d-2f1c-4eb6-8897-1d749938129d'></a>

**Read sketch variables**

If the sketch cannot provide a single sensor reading, as it is doing some kind of data integration, an output resource can also be used for reading the sketch variables, where the computed result is updated frequently.

<a id='22354760-e547-4f5a-a2b0-77d09e8df6e4'></a>

float yaw = 0; // defined as a global variable
thing["yaw"] >> [] (pson& out){
out = yaw;
};

<a id='ce180313-8d11-4635-8017-98a541a1b066'></a>

## Input/Output Resources

The last resource type is a resource that not only takes an input or an output, but takes both parameters. This is particularly useful when an output is dependent on an input, such as when a changing reference value needs to be provided to a sensor.

<a id='a305c49b-7c77-41c2-a4be-d41e758f779c'></a>

7