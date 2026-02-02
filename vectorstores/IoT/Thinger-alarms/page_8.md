<a id='0722bc4f-ad1c-48be-9fcc-7f5772d80206'></a>

# Understanding Alarm Activation Fields

The following fields are available to determine when an alarm should be activated:

*   **device**: The unique identifier of the device.
*   **created**: Timestamp indicating when the device was originally created.
*   **modified**: Timestamp of the last modification to the device's settings or status.
*   **enabled**: Whether the device is currently enabled. Alarms are typically only triggered for devices that are enabled.
*   **connection.ts**: The timestamp of the last known connection attempt or session.
*   **connection.active**: This is the most critical field. It indicates whether the device is currently online and connected to the Thinger.io server. Use this field to detect connectivity issues or trigger alerts when a device goes offline.

These fields allow alarms to be precisely tuned to changes in device state, ensuring that only relevant alerts are generated.

<a id='264c78e5-472b-4918-b373-31348de916bd'></a>

## Normalization
The normalization section of the rules configuration allows users to define the platform's behavior for deactivating an alarm when the necessary conditions for it to be cleared are met in the device's data. This configuration uses the same elements as in the activation section, but with the focus on setting values that ensure a reliable deactivation of the alarm.

<a id='56b11fe3-485e-4e09-bb7c-c051a22834d0'></a>

Data Source Activation Normalization Reminder

Conditions (i)

When Data.temperature IS BELOW 24 [trash icon]

+ Add Condition

Confirmation (i)

Timespan 5 minutes

Notification (i)

+ Add Notification

<a id='b4138366-bbd6-430f-95ba-e7d715d184ce'></a>

8