<a id='cdf5de3e-5e4b-4f2a-b878-86c2bada30a5'></a>

// example of datapoint with custom timestamp
{
  "ts": 1671536877360,
  "lat": 40.416775,
  "lng": -3.70379,
  "temperature": 23.33,
  "humidity": 32.44
}

<a id='05c0434e-69eb-4dd6-85a8-8b6b0b6620b3'></a>

The time must be expressed with a standard Epoch Timestamp expressed in milliseconds. This functionality allows storing data by the time they were produced instead of being stored. It also allows to correct or modify data already stored in the platform.

<a id='1d9ef91b-4795-4b27-8f40-ea4f3bd7269f'></a>

! Note that if the TS of a new datapoint matches with an old data bucket entry, it will be overwritten.

<a id='1726092b-402d-418d-abb9-ffbb8c9b0e00'></a>

## Review Bucket Data

Once the data bucket has been configured and it starts to record data from a device or from write calls, it will display the information inside a table. Every record contains the server timestamp in UTC (but shown in local time zone in the console) and the record value. The value stored in the data bucket can be a single value or any other JSON document. If the JSON document is composed of key-value pairs, like in the previous examples, they will be displayed in tabular format:

<a id='b2c412e5-652a-49b3-9ec3-85a5f38ab232'></a>

8