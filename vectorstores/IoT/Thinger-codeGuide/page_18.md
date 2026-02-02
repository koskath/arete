<a id='1b3171b1-d217-4028-8138-71505c72b892'></a>

# From Write Call

This option will allow setting the bucket in a state that it will not register any information by default, but it will just wait for writing calls, both from the Arduino library using the write_bucket method, as shown here, or calling the REST API directly, as done with Sigfox. This feature opens the option to register information in the same bucket from different devices, or store information from devices that are not connected permanently with the server, that are in sleep mode, or use a different technology like Sigfox.

<a id='5ef22aa1-a440-484d-a1ba-02bdfbbfa93b'></a>

Here is an example of an ESP8266 device writing information to a bucket using the write_bucket function:

<a id='c0ff637d-e8b6-4d4e-9c70-a284499d7f7b'></a>

void setup() {
  // define the resource with temperature and humidity
  thing["door_status"] >> [] (pson &out){
    out["OPEN"] = (bool)digitalRead(SENSOR_PIN);
  };
}

void loop() {
  // handle connection
  thing.handle();

  if(digitalRead(SENSOR_PIN)!=previous_status) {
    // write to bucket BucketId when the door changes its status
    thing.write_bucket("BucketId", "door_status");
  }
  previous_status=digitalRead(SENSOR_PIN);
}

<a id='2c32ff5e-9acf-4607-a45a-898f6d75a830'></a>

Note that this instruction will retrieve the ["door_status"] resource PSON, so it is also possible to call this function by attaching a custom PSON:

<a id='d1ea89b5-1b56-4cb5-a13e-67b80d872d3f'></a>

18