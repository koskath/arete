<a id='2c47bd9f-5809-4cf9-bf58-a6572484a393'></a>

This option subscribes Thinger.io Server to a specific device resource (such as temperature, motion, and so on). It can be configured to retrieve data from the device in a specific sampling interval or wait for asynchronous communications from devices by means of the "Refresh mode" parameter.

<a id='b216bd2a-b630-4229-a0d8-23fdd610e3ad'></a>

Note that this option is only compatible with devices that have been provided with Thinger.io Software client libraries (Arduino, Linux or Raspberry), and it will only work properly if the device maintains a permanent connection with the server.

<a id='2a5b5973-021b-4a13-b2a3-89159a446394'></a>

*   **Sampling interval:** Configure the bucket profile to retrieve data from device resources at a specific timing, which can be changed on demand, without modifying the device sketch. Another benefit is that no additional codification is needed to implement this feature and start storing data. The next basic code example will store two variables in the data bucket when using the "sampling interval" configuration.

<a id='1eeaf7ef-449a-4e10-b8a7-59d3dc9272f7'></a>

```
// define the resource just once in the setup() section
thing["TempHum"] >> [] (pson &out){
    out["temperature"] = dht.readTemperature();
    out["humidity"] = dht.readHumidity();
};
```

<a id='2ac8cd74-2534-467e-b23d-cd6e71fb375d'></a>

- **Update by Device:** This option allows the device to stream the information when required, i.e., by raising an event when detected. In this case, refresh mode must be set as the `Update by Device` option while configuring the bucket, and the device source code will contain a streaming instruction for the resources (also described in more detail here ↗). This way, the data bucket will be listening to a device resource, and its information is registered in every stream call.

<a id='e23170a5-2d0f-40a2-858e-d5863fea829b'></a>

3