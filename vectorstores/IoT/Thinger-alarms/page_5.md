<a id='a4851f42-3656-487b-944d-b0293415fb80'></a>

• Name: Use a unique identifier, avoiding spaces or special characters. This name will be used to identify the JSON that contains the data point.
• Data source: Note that depending on the data source type, the menu may expose filtering options that allow working with multiple devices with the same behavior, so just one rule can be used to monitor multiple devices. There are multiple options:
  o From Device Resource: This option requires the device to be connected in real-time. The widget will display data as it is received from the device. It's important to note that, when fed directly from a device resource, the widget will not retain the information if the dashboard is closed or refreshed, as it only displays live data from the device to the dashboard.
  o From Data Bucket: With this option, the widget takes information from a Data Bucket previously configured in the account to display historical data. This means that the information will persist even if the dashboard is closed or reloaded.
  o From Device Bucket: This option is used to retrieve historical data specifically from a Device Bucket, which stores a history of device properties or aggregated data. It functions similarly to a Data Bucket but is intrinsically linked to a device's historical properties.
  o From Device Property: This option is ideal for retrieving data from a device's configurable properties, making it particularly useful for visualizing static or infrequently changing device configuration data, such as firmware versions or location IDs, as well as displaying the last received data from HTTP devices that do not maintain a persistent connection.

<a id='a0873206-9793-4fc1-a3b3-4786a1bace4c'></a>

☑ When working with device data, it is recommended to use a product data bucket instead of individual data buckets. This way, just one rule will monitor every product devices.

<a id='edabbbda-aac8-402f-b5ba-ee1a29e27a98'></a>

## Multiple data sources

In the "Data Sources" section of the rule configuration menu in Thinger.io, the "**+ Add Source**" button allows users to add variables to a specific rule. This feature is essential for configuring the rule with the necessary data for evaluation.

<a id='1e79746a-c004-4945-bb61-5f769535838c'></a>

Activation

<a id='116c8247-3d55-4181-8e8f-ecd9147d8afa'></a>

5