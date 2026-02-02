<a id='454b4cdb-a337-42a6-8639-442334dd352a'></a>

Dashboard Settings

option Layout: [ ]
option Share: [ ]
option Developer: [ ]
option Placeholders: [ ]
option Functions: [x]
option Controls: [ ]

<a id='c7197115-512b-46dd-b3da-e6f8bcca7146'></a>

Dashboard Functions

JavaScript
f(x) Add Function

```javascript
function convertFunction(value, ts, series){
// use 'shared' variable to share information between functions
// access dash placeholders, i.e., shared.placeholders['Name'];
return value * shared.placeholders.precision_factor.multiplier;
}
```

Cancel Save

<a id='ed1fea63-59e5-43bd-bf5b-42acea44cf08'></a>

Dashboard function using the value of a placeholder

<a id='f7e35965-0e0a-4283-9ebe-8c4152da15ee'></a>

Transformation of value is done for each individual value, and not over a whole series.

<a id='979c0ffe-d9ff-42c2-91cc-8a39b510d427'></a>

# Controls

In the controls tab, some additional dashboard configuration can be done regarding time selection for time series sources, when a widget source belonging to a dashboard has a configurable timeframe and aggregation window.

<a id='bcb7bc17-2452-4df4-b4bd-ab29e342f1df'></a>

69