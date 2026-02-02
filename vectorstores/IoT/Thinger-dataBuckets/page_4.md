<a id='eac8a2bd-68a8-4485-877b-7bc2416f73ab'></a>

```c
/*"TempHum" resource was declared in the setup() function
but the stream instuction is added in the loop*/
void loop() {
  thing.handle();
  // use own logic here to determine when to stream/record the
  resource.
  if(requires_recording) {
    thing.stream("TempHum");
  }
}
```

<a id='097e1117-a2e3-4cdb-9905-002182cb36be'></a>

! This instruction should NEVER be called each loop execution or at lower than 60s streaming rates, as the bucket system will only store data every 60s.

<a id='0db8a983-8ff6-49b2-8e16-4a4297a7cd72'></a>

# From device Write Call

This option sets the bucket in passive mode, waiting to be called by any Thinger.io "Generic Device" (with Thinger.h libraries on it) by means of the `write_bucket()` method. The distinguishing feature of this mode is its ability to store data from multiple devices in a single data bucket.

<a id='22b0ba20-aab2-4fe5-8d95-070c7c9dab96'></a>

Here is an example of an ESP8266 device writing information to a bucket using the `write_bucket` function:

<a id='90a0eb0e-74fd-4149-8e7a-163d7e7c2646'></a>

4