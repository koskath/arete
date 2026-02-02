<a id='94d181af-28d9-4dae-9b65-4a41d2e147fa'></a>

# From Code Snippet

To create a basic widget with a simple code, such as a data table, a ready-to-paste script from any website, or any other easy integration. The source code can be written using a small text editor in the widget form. Note that this code will be executed in the browser as a part of an AngularJS directive, where some scope has already been defined and initialized. In particular:

<a id='aceae1e2-421b-44c6-be11-14daeda0c2f2'></a>

- `ts`: Timestamp of the data.
- `value`: Value with the selected value in the configuration, i.e., a device property, bucket data, or real-time data from a device.

<a id='79409554-060d-4ddb-913c-0f694260e02f'></a>

Those values can be used in the HTML content with the AngularJS two-way data binding using double brackets, i.e., using {{ts}} or {{value}}. The property's data is displayed on the view, and at the same time, the property will be updated when there is any change.

<a id='49413b1e-e771-429c-91a3-d2340c0205d1'></a>

40