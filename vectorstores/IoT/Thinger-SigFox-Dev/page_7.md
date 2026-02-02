<a id='f4371619-4a0a-4255-ba82-153989031fbb'></a>

```
{
  "device" : "{device}",
  "snr" : {snr},
  "rssi" : {rssi},
  "station": "{station}",
  "latitude": {lat},
  "longitude": {1ng},
  "temperature" : {customData#temp},
  "humidity" : {customData#hum}
}
```

<a id='1d25086b-3295-407c-b4b5-5678060dcd81'></a>

Notice that we are mixing Sigfox variables, like `{device}`, with our own custom data in the payload, like `{customData#temp}`. This body is then processed on every message reception, and the variables will be replaced with the current values. So, the server will receive a JSON payload with the device identifier, device temperature, humidity, coarse location (km accuracy), and signal quality.

<a id='3b88c0f5-8c28-4584-9698-e3451f0bf82f'></a>

After these steps, we should now have a callback completely configured to push data to our data bucket.

<a id='302e72f8-d0bf-410a-a2cc-0ef324eab4e5'></a>

# Programming Sigfox Devices

Now it is time to program our Sigfox Device that will be sending data to our buckets. In this case, we provide examples for the SmartEverything device and the Arduino MKRFOX1200.

<a id='b950d5f1-d456-4d78-8f25-5f4b0f584d93'></a>

# Arduino MKRFOX1200

Arduino MKRFOX1200 has been designed to offer a practical and cost-effective solution for makers seeking to add SigFox connectivity to their projects with minimal previous experience in networking. It is based on the Microchip SAMD21 and an ATA8520 SigFox module. Can run for over six months on 2 AA 1.5V batteries with typical usage. The design includes the ability to power the board using two 1.5V AA or AAA batteries or an external 5V.

<a id='3112407e-6674-4960-b862-b37bad4fbc56'></a>

7