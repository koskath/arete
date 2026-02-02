<a id='ceeb7202-f5ed-4370-b55f-28e379ec5821'></a>

# Using Endpoints

In Thinger.io, an endpoint is defined as some kind of external resource that can be accessed by the device. With the endpoints feature, devices can easily send emails, SMS, push data to external Web Services, interact with IFTTT, and perform any general action that can be made by using WebHooks (Calling HTTP/HTTPS URLs).

<a id='653b1701-e2f9-4e4b-ae55-76c87f6441de'></a>

Calling an endpoint is so easy from the Arduino sketch, as it only requires calling the `call_endpoint` method over the `thing` variable.

```
thing.call_endpoint("endpoint_id");
```

<a id='bed3994c-5a36-423a-a228-5613615219a8'></a>

Endpoints can be called from the device code in order to execute any action, like sending a predefined email. The call can also include some reading values, which is especially useful to send the device's data to third-party services.

<a id='5ae5a266-6b81-4dee-a503-f1a1a43f19bd'></a>

① Extra attention must be taken while calling resources, in order to avoid uncontrolled recurrency. If the interval is too short, the server will lock the device connection

<a id='6bca64e6-c3cd-40f2-82d4-4bf6c97e99ef'></a>

## Calling Endpoints

In this case, we will see a simple example to send an email alert based on a temperature value. For this example, we have configured an email endpoint `high_temp_email` that contains some warning text about the temperature. For this case, we do not want to check the temperature every millisecond, so we are introducing some variables to control the sensing and warning frequency. In this example, the temperature is checked every hour, and if it is above 30°C, it will call the endpoint called `high_temp_email` which will send us an email with the predefined text. It is important here **not to add delays** inside the loop method, as it will prevent the required execution of the `thing.handle()` method, so we are using a non-blocking delay based on the `millis()` function.

<a id='ab70e7c7-2b17-476a-8c75-92e5ef35edd6'></a>

14