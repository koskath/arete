<a id='fd35ef73-d248-411a-a965-0be782d386c4'></a>

If we want to communicate devices from different accounts, we can do that by calling an endpoint of type `Thinger.io Device Call`. Just register an endpoint of this type in the console:

<a id='c2287865-5a4a-4d3c-bb94-a0192b756c05'></a>

## Endpoint Details

Endpoint Identifier: DeviceACall
Endpoint Name: Endpoint
Endpoint Description: Endpoint for calling Device A from
option Enabled: [ ]
Endpoint Type: Thinger.io Device Call
Device Owner Username: otherUser
Device Identifier: deviceA
Resource Name: resourceOnA
Device Access Token: paste here a deviceA token device that gives you access to the device

[x] Add Endpoint

<a id='5a4a6d9d-63ba-4b19-992e-df206262ae62'></a>

In this case, it is required to define different parameters in the endpoint:

*   Endpoint Identifier: The endpoint ID that the device will use for calling the device.
*   Endpoint Name: The name of the endpoint, which does not need to equal the "Endpoint Identifier". The endpoint will show in the list of endpoints with this name.
*   Endpoint Description: This is an optional field. It is useful to remember what the endpoint consists of.
*   Device Owner: The device owner's username.
*   Device Identifier: The device ID of the other account.
*   Resource Name: The resource on the device to be called.
*   Device Access Token: A device token generated in the other account for granting external access to the device.

<a id='620b2347-3b02-4a7b-8f60-6912e3493217'></a>

Once defined, the device will be able to call the endpoint, as explained in the following section. It basically consists of calling the `call_endpoint` method.

<a id='1d3d7640-fd60-4cdf-b361-f8160b9d61ea'></a>

```
thing.call_endpoint("DeviceACall");
```

<a id='e0825346-76c4-482f-97a2-ab34518c5a9e'></a>

13