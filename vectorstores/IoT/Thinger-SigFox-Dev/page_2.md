<a id='0c908e79-25a9-4389-a368-367c6273b2eb'></a>

This documentation will describe how to integrate SigFox devices and their data into the Thinger.io Platform. In the first steps, we will review how to configure Thinger.io resources, and then, on the Sigfox side, we will configure the communication with the platform for pushing our sensor's data.

<a id='93dcede8-1232-4e5a-bd09-91b7c76419ae'></a>

# Integrating a Sigfox Device with Thinger.io

This process is carried out in two parts: on the one hand, the preparation of Thinger.io to receive data from Sigfox and, on the other hand, the configuration of the Sigfox cloud callback that will send the information to Thinger.io. During the next sections, we will explain both parts, starting with Thinger.io side steps:

<a id='8c97744e-b04d-4e77-b4cf-c68a6d16eef4'></a>

There are two ways to configure Thinger.io to work with Sigfox devices. The best option is by deploying the "Sigfox Plugin", which will manage the integration, providing advanced features such as device auto-provisioning (good to integrate large networks), Uplink/Downlink payload processing and device management, but this option is only available for subscribed developers. Freemium accounts can also make individual Sigfox device integration using the "HTTP device". Both ways are explained below:

<a id='ae93b8ab-e604-450d-a8b3-8af9f2b14b8d'></a>

**Advanced Integration (with Sigfox plugin)**

> SigFox Plugin

<a id='b5d2739f-0665-491e-bb43-f2d6768dd4e8'></a>

## Single Device Integration (without plugins)

When implementing little prototypes or maker projects using the free account, it is possible to integrate an individual device using the "HTTP device" that allows using almost every Thinger.io platform feature, including:

* Store data in buckets
* Show data in customizable dashboards
* Send endpoints to post data on emails, social networks or third parties

<a id='13cbda64-00d9-4e82-adbe-68b760634e3d'></a>

2