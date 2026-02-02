<a id='1e4de423-82de-4476-acdd-5ef5349f7885'></a>

*   **Name:** The name of the source to be called.
*   **Color:** A color can be assigned to a data source by selecting it from the color picker. The color can be adjusted using the color spectrum bar, by manually entering RGB (Red, Green, Blue) values, or by moving the dot within the color gradient area. Depending on the data source, it may be possible to configure a single color or multiple colors for different data series.
*   **Data Source:** Designates the origin of the information utilized for visualization or analysis. For comprehensive details, refer to the '**Data Sources**' section above.
*   **Timeframe:** When working with historical data stored in *Data Bucket* or *Device Bucket* sources, the Timeframe parameter defines the specific period to be rendered. It provides multiple predefined and configurable range options.
    *   **Latest Value:** Displays only the most recent data point received.
    *   **Relative:** Displays data from a rolling time window, defined in relation to the current moment. Users can specify the duration of this window and the time units (in hours, minutes, or seconds).
    *   **Absolute:** Presents data within a precisely defined, static time frame. Users set both a fixed start date and time, as well as a fixed end date and time, for the data to be displayed.
    *   **Configurable:** This parameter offers crucial advanced configuration within the dashboard profile, enabling dynamic adjustment of the timeframe based on other dashboard elements or custom logic. These powerful options are essential for precisely tailoring the time duration and other settings to your specific visualization needs.
*   **Time Period:** This option allows setting up the time range during which the widget should retrieve and represent real-time data or the last received value.
*   **Data Aggregation:** Given potentially noisy or irregular raw Bucket data with numerous points, this feature enables data aggregation. Statistics, as detailed in the table below, can be applied over intervals ranging from five minutes to one week. Configuration is handled via widget form inputs and the upper-right parameters of each time series chart widget.

<a id='643b373f-dc5f-4196-b350-59ffb3a3b609'></a>

Apex charts customization options

<a id='fc8bf540-f136-4436-8c4f-ec8df2c60bae'></a>

17