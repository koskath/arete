<a id='9b2a8f59-cf66-46a9-b48c-582a29efcfc8'></a>

void setup() {
  // define the resource with temperature and humidity
  thing["TempHum"] >> [] (pson &out){
    out["temperature"] = dht.readTemperature();
    out["humidity"] = dht.readHumidity();
  };
}

void loop() {
  // handle connection
  thing.handle();
  // write to bucket BucketId the TempHum resource
  thing.write_bucket("BucketId", "TempHum");
  // sleep the device SLEEP_MS milliseconds
  ESP.deepSleep(SLEEP_MS*1000, WAKE_RF_DEFAULT);
}

<a id='e27f75c5-3002-42c2-8228-514e5e88d285'></a>

## From API Request (for 3rd parties):

This configuration allows to store data from any other device or data source that can't be equipped with Thinger.io libraries on its codification. The data bucket will be set in passive mode, waiting to receive data from any **HTTP Device Callback** that has been properly configured to send data to this data bucket.

<a id='b09a4a8a-3d12-4ffa-b749-be32f6b5f0d2'></a>

This feature can also be used to store data directly from any third-party platform just calling the data bucket REST API and sending information in JSON format. But it is preferable to use the HTTP device way.

<a id='8695d6b1-e656-4a3f-aa5a-b675c8ad94e7'></a>

## From MQTT Topic

Data buckets can be configured to subscribe to an MQTT topic in the same way as another MQTT client can. This feature enables storing published data within the same topic. Therefore, caution is advised if multiple devices are publishing to it. This configuration can be applied during the creation of a new data bucket or later using the Settings tab.

<a id='f62b989f-3e22-486b-805c-986133fcefce'></a>

5