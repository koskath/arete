<a id='ef9fa83f-6f9d-4cc3-90d3-8b65014fb23c'></a>

* **alarm_instance_create**: Displays events where a new alarm instance is created.
* **alarm_instance_delete**: Shows events where an alarm instance is deleted.
* **alarm_instance_normalize**: Displays events where an alarm instance is normalized, indicating that the triggering condition is back to normal.
* **alarm_instance_update**: Shows events where an alarm instance is updated with new information or conditions.
* **alarm_rule_create**: Displays events where a new alarm rule is created.
* **alarm_rule_delete**: Shows events where an alarm rule is deleted.
* **alarm_rule_execute**: Displays events where an alarm rule is executed, showing the process of checking conditions and triggering alarms.
* **alarm_rule_update**: Shows events where an alarm rule is updated with new parameters or conditions.

<a id='81cb2a5e-c3f8-4b72-b553-895224bd9dcb'></a>

# Device-events

The platform provides access to a set of system-generated signals that represent the current **state and metadata** of each device. These signals can be used for monitoring, automation, and alarm generation.

<a id='d29f0bc6-d8ed-43aa-8fce-c5d76b3cea7d'></a>

The available fields include:

*   **device**: The unique identifier (device ID).
*   **created**: Timestamp indicating when the device was initially created.
*   **modified**: Timestamp of the most recent configuration change.
*   **enabled**: Boolean flag indicating whether the device is currently enabled or disabled.
*   **connection.ts**: Timestamp of the last known connection activity.
*   **connection.active**: Boolean indicating whether the device is currently connected.

<a id='f407a575-f973-4375-b94d-f695d8aa7a3c'></a>

These signals are particularly useful for building automation logic or triggering alerts based on device status. For instance, a common practice when defining alarms is to **verify that a device is both disconnected and enabled**, in order to avoid generating alerts for devices that are intentionally disabled (e.g., under maintenance or decommissioned).

<a id='4693a54d-cb31-4eda-a9bd-4d0239d42554'></a>

12