<a id='1771bd47-2f32-484a-97b9-f81c6fe706b0'></a>

<::Gray dot with label Source 1
: figure::>

<a id='e4c1f498-ed4e-4d89-9951-00b7bc13c204'></a>

Name: Source 1

Data Source: From Device Resource

Select Device: Select Device...

Time Period: 30 minutes

<a id='fba01c4d-ecaf-4897-9221-0a5225537165'></a>

<table id="10-1">
<tr><td id="10-2">+ Add Source</td><td id="10-3">Clone Source</td><td id="10-4">Remove Source</td></tr>
</table>

<a id='934924ab-6965-4362-ab45-e04b7181ed67'></a>

x Cancel

✓ Save

<a id='b17493f1-64f5-4117-a401-54ba181bbb82'></a>

Some display-type widgets provide aggregation features that can be selected in order to process the device's data before being displayed, which is quite interesting when working with raw senor-data in order to obtain the most accurate representation.

<a id='cc73ab17-1d3f-42a1-9288-0d543886f654'></a>

*   **Data Aggregation**: Showing raw data directly from a Bucket could be tricky when there are a lot of data points, especially if the measures are very noisy or irregular. This feature allows aggregating data using different statistics such as medians, means, minimum and maximum values, a counter of data points per period, and a data summary. The aggregation can be applied over different intervals that go from five minutes to one week, by using the next configuration inputs in the widget form, and also using the upper-right parameters on each time series chart widget.
*   **Data Transformation**: Some display-type widgets (time-series chart, *HTML* series) have a **Transform** selector, which works as an on-the-fly filter applied **after** the raw value is fetched from the device or bucket but **before** the widget renders it. The goal is to save users from rewriting firmware or setting up a separate data-processing pipeline just to polish how the metric is presented. According to the Thinger.io documentation, these functions "allow processing data before being used in widgets" for example, rounding numbers, computing rates, or converting units in place.

<a id='0cc9b116-20d8-49e9-9ad6-db0872a1df7d'></a>

11