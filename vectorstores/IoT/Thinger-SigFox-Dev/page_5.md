<a id='083d1f29-cedf-4af3-ad52-d6a9298ac83a'></a>

Type:
option DATA: [x]
option UPLINK: [x]

Channel:
option URL: [x]

Send duplicate: [ ]

Custom payload
config: temp::float:32:little-endian hum::float:32:little-endian

<a id='3e80f738-0a11-46b0-ac46-b493b36611f2'></a>

URL syntax: http://host/path?id={device}&time={time}&key1={var1}&key2={var2}...
Available variables: device, time, duplicate, snr, station, data, avgSnr, lat, lng, rssi, seqNumber
Custom variables: customData#temp, customData#hum
Url pattern https://api.thinger.io/v1/users/alvarolb/buckets/SmartEverything/data

<a id='31d1581f-1781-4c2c-b04a-067631c557da'></a>

Use HTTP Method option POST: [x]

Send SNI: [ ] (Server Name Indication) for SSL/TLS connections

Headers

<table><thead><tr><th>Authorization</th><th>Bearer eyJhbGciOiJIUzI1NilsInR5cCl6lkpXVCJ9.eyJqdGkiOiJTbWFydEV22</th></tr></thead><tbody><tr><td>header</td><td>value</td></tr></tbody></table>

<a id='6670a87f-8c4e-42c7-8313-412a22d24b01'></a>

Content type application/json
Body
{
"device": "{device}",
"snr": {snr},
"rssi": {rssi},
"station": "{station}",
"latitude": {lat},
"longitude": {lng},
"temperature": {customData#temp},
"humidity": {customData#hum}
}

<a id='baff2b34-96e0-4952-9edc-5d56a9f79e3f'></a>

The configuration in our example is:

1. `Type` is `DATA` with `UPLINK`, as we want to send our device data.
2. `Channel` is of type `URL`, as we will be calling an HTTP endpoint.
3. `Send duplicate` as disabled to avoid writing duplicate messages received by different base stations.
4. `Custom payload config` will completely depend on the payload sent by the device. In our case, our device will be sending the temperature and humidity as 32-bit floats, so we have configured the payload as `temp::float:32:little-endian hum::float:32:little-endian`, where we define the `temp` and `hum` parameters as 32-bit floats in little-endian. Notice that Sigfox only supports 12 bytes of payload per message, so it is a must to optimize this space, like sending temperature and humidity as integers if it is not required decimal accuracy. For example, this will work.

<a id='312c202b-1e6f-4614-84ad-6152918370d5'></a>

5