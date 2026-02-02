<a id='63c14202-3e57-44af-8d42-ab8d220a2bb1'></a>

- **Conditions**: allows users to define one or more comparisons of a selected variable and a setpoint. These conditions specify the exact criteria that must be met for the alarm to be activated. By setting these conditions, users can precisely monitor the desired metrics and ensure alarms are only triggered when specific thresholds or ranges are met. The comparisons can be:
  - Greater than
  - Less than
  - Equal to
  - Not equal to
  - Within a range
  - Outside of a range

<a id='5cf2c14c-2fab-46ef-a682-da687bb97d4e'></a>

ⅰ Note that it is possible to create more complex behaviors by adding additional conditions to the rule

<a id='fd8c2895-526e-498e-bcc6-1a00cb3c1469'></a>

- **Confirmation**: This section helps to avoid false activations of the alarm. It is an essential step for filtering out transient or spurious events that do not require immediate attention, thus ensuring that alarms are only generated for sustained or repeated conditions. This can be configured in several ways:
  - Immediate Confirmation: The alarm is triggered as soon as the condition is met.
  - Sequence: The alarm is activated if the condition is met multiple times
  - Timespan: The alarm is only triggered if the condition remains true for a specified number of consecutive valid comparisons.
- **Notification**: This section allows users to define the endpoint profile (previously defined) that will be used to send the notification if the alarm is necessary. By configuring the notification settings, users can ensure that the right people are informed promptly about critical conditions, facilitating a quick and appropriate response.

<a id='e53e5641-eb6b-40ca-b805-be785289cb64'></a>

7