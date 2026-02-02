<a id='2a720072-34cc-4aa7-adb9-3fdacba73b5b'></a>

```c
void loop(){
  // handle connection
  thing.handle();

  if(digitalRead(SENSOR_PIN)!=previous_status){
    // write to bucket BucketId when the door changes its status
    thing.write_bucket("BucketId", "door_status");
  }
  previous_status=digitalRead(SENSOR_PIN);
}
```

<a id='ca97aecf-c8e2-4bbf-9748-0428ee8c776e'></a>

# Streaming Resources

In Thinger.io, WebSocket connections can be opened against devices to receive real-time sensor values, events, or other information. WebSockets are primarily utilized in the Console's Dashboard feature for streaming resources at a fixed, configurable interval. This functionality is available by default when an output resource is defined. However, to transmit information precisely when required, such as upon detection of movement or presence, a specific code, similar to calling an endpoint, must be programmed.

<a id='29a9b1e3-24e4-4b11-bca2-469c468dbae3'></a>

In such cases, it is necessary to detect when to stream the event, for example, when an accelerometer value exceeds a threshold, a presence sensor makes a detection, or the compass heading changes. The determination of when to stream new data is left to the implementer. Streaming resources also require that another endpoint is connected, listening for them (i.e., from a WebSocket connection), so if there is no one listening for this data, the data is not sent. This is handled automatically by the client library and the server, therefore, it is safe to stream data always, as the device will transmit the information only when there is a destination.

<a id='44ab51a3-f693-4da6-96a3-15c3635ca6dd'></a>

This example will report the compass heading in real-time if the heading value changes by more than 1 degree.

<a id='7a5ef1f4-dba6-4708-a495-2709b5bc0da8'></a>

19