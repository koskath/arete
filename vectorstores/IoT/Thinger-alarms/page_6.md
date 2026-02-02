<a id='52f73718-fe81-4ac1-8200-2d1a1d344d51'></a>

The alarm activation refers to the process where the system monitors the variables specified in the "Sources" section and generates notifications when these conditions are met. This means the system continuously checks the data against the defined criteria to detect any deviations or specific events. It's also important to note that it is possible to define confirmation criteria that prevent false activations.

<a id='55739420-ead3-492b-a5b2-9cc0181b2ac4'></a>

The alarm activation section in Thinger.io consists of a form with three main sections:
**Conditions**, **Confirmation**, and **Notification**. Each of these sections plays a crucial role
in defining how and when alarms are triggered and how notifications are managed.

<a id='892ff780-429c-4ac2-8913-cdf8fddae257'></a>

Data Source Activation Normalization Reminder

Conditions

When Data1.temperature IS ABOVE 25

+ Add Condition

Confirmation

Timespan 5 minutes

Notification

Select Endpoint...

+ Add Notification

<a id='55e2200e-e01e-4bf9-b2e0-c716e3696237'></a>

In this example, we are using the variable "temperature" which comes from a datapoint that contains multiple variables:

`Data1`

`{"temperature":20,`
`"humidity":50,`
`"pressure":850`
`}`

The desired variable can be selected through the following structure in the input text:
`"Data1.temperature"`

<a id='c58a1059-3c45-4267-85a4-7e79827bb67f'></a>

6