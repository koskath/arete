<a id='23459c74-ea14-4146-a3e4-addad4a56b09'></a>

* Sigfox downlink processes to send configuration data to the device

<a id='96238bc3-9971-42f0-a403-2fcf9ca64949'></a>

␓ Payload data processing is only available using plugin integration

<a id='011c6b8b-abb6-41a2-87ac-d6f81c5cf1f3'></a>

To perform this integration, it is required to create a new HTTP device and configure its callback flows as it is explained in the HTTP devices section of this documentation:

<a id='1ec4be82-8b7d-4609-8f6c-2840e47b7224'></a>

<table id="2-1">
<tr><td id="2-2">HTTP DEVICES (right arrow)</td></tr>
</table>

<a id='d63a0572-a146-4dec-b3bd-fe728fa4aeb4'></a>

Once the new device has been created, Thinger.io will provide a REST API callback that can be used to configure the Sigfox cloud, as it is explained in the section below:

<a id='3be21c36-c0c5-4433-b48a-d5ba5055659b'></a>

# Sigfox Cloud Configuration

After making all the configurations that are required to get Thinger.io ready for receiving data, the next step is to configure the Sigfox Backend for pushing data to it, using our token identifier and the token we have generated.

<a id='7427fba5-a1a4-4bc1-bcb0-783c5c066028'></a>

# Creating Sigfox Callback

In this step, we will create a Sigfox callback that will push the information from our Sigfox device to our Thinger.io data bucket. In our example, a callback is just an endpoint that is called when the Sigfox device sends data over the network, so we will configure the callback to point to our data bucket.

<a id='bc0df201-d8f6-44bb-bdeb-f950bbd250b7'></a>

To create a callback in Sigfox:

1. Go to https://backend.sigfox.com and log in to the account. It is assumed that the device has already been registered with the platform.
2. Click on `Device Type` tab on the top, and then click on the desired device type name to configure. Alternatively, navigate to the `Device` tab and click on the `Device type` column of the device.
3. Click on `Callbacks` on left menu, and then create a new one.

<a id='a9c078a3-4906-451a-9481-1f1f557e48f4'></a>

3