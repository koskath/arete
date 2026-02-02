<a id='8e2824f8-1475-4f7f-994d-43aa2d28813f'></a>

VL53L1X

<a id='6fb13a36-c430-4f71-a0a3-239e5210ca66'></a>

Functional description

<a id='534d08c7-97da-479d-b22e-54a34a0bbc56'></a>

## 2.5.2 Timing budget (TB)
The VL53L1X timing budget can be set from 20 ms up to 1000 ms.
* 20 ms is the minimum timing budget and can be used only in Short distance mode.
* 33 ms is the minimum timing budget which can work for all distance modes.
* 140 ms is the timing budget which allows the maximum distance of 4 m (in the dark on a white chart) to be reached under Long distance mode

<a id='7216213d-a1e4-4a18-a4fb-1a661dac778c'></a>

Increasing the timing budget increases the maximum distance the device can range and improves the repeatability error. However, average power consumption augments accordingly.

<a id='dcc82277-edaa-4c50-995f-248304e070c9'></a>

Figure 6. Maximum distance and repeatability error vs. timing budget<::chart: The figure displays three subplots, all titled "Measured distance & Repeatability error" and sharing a common X-axis labeled "Actual distance" ranging from 0 to 4000 (with major ticks at 0, 200, 400, ..., 4000). Each subplot has a left Y-axis with two scales: an upper scale for range from 0 to 3600 (with major ticks at 0, 1200, 1800, 2400, 3000, 3600) and a lower scale for repeatability error from 1.0 to 4.0 (with major ticks at 1.0, 1.6, 2.2, 2.8, 3.4, 4.0). The left Y-axis is labeled "Timing budget" with specific values for each subplot.  The charts plot two data series: "Mean range" (blue line with dots) and "Repeatability error" (red dots).  **Subplot 1: Timing budget = 33 ms**  The blue line for "Mean range" starts around (0, 1200) and increases linearly to approximately (3100, 3600). A label "Max dist = 310 cm" is associated with the end of this line. The red dots for "Repeatability error" start around (0, 3.4), decrease to a minimum around (1200, 1.0), and then slowly increase towards the end of the plot. A label "STDEV (1 sigma) = 5 mm" is associated with the repeatability error data.  **Subplot 2: Timing budget = 140 ms**  The blue line for "Mean range" starts around (0, 1200) and increases linearly to approximately (4000, 3600). A label "Max dist = 400 cm" is associated with the end of this line. The red dots for "Repeatability error" start around (0, 3.4), decrease to a minimum around (1200, 1.0), and then remain relatively low and flat. A label "STDEV = 3.5 mm" is associated with the repeatability error data.  **Subplot 3: Timing budget = 200 ms**  The blue line for "Mean range" starts around (0, 1200) and increases linearly to approximately (4000, 3600). A label "Max dist = 400 cm" is associated with the end of this line. The red dots for "Repeatability error" start around (0, 3.4), decrease to a minimum around (1200, 1.0), and then remain consistently low and flat. A label "STDEV = 2.5 mm" is associated with the repeatability error data.::>

<a id='27c11de0-537d-4ff6-99ae-0279fe18a446'></a>

Test conditions: timing budget = 33 ms, 140 ms, 200 ms, grey target 54 %,
ambient light = dark.

<a id='908c158a-1d95-4a7f-9f01-d15a397b7138'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, italicized blue font, with a horizontal line beneath it.::>

<a id='96e4a1cb-477c-4124-af9b-dedbb5af1720'></a>

DocID031281 Rev 3

<a id='105359b7-9ced-4a75-a8af-12b03daa6415'></a>

11/35