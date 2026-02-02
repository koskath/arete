<a id='ec79fe68-1226-44c3-9b8a-42b53059c438'></a>

<::Logo: adafruit logo::> adafruit Devices Feeds Dashboards Actions Power-Ups <::Button: New Device button with a plus icon::> New Device tyeth_demo / Feeds / BMP280: Pressure Sensor <::Button: Help button with a question mark icon::> <::Line chart: A line chart displaying 'BMP280: Pressure Sensor' data over time. The y-axis ranges from 1,017.125 to 1,017.165. A specific data point is highlighted with a tooltip showing "August 22nd 2023, 6:44:43PM BMP280: Pressure Sensor 1017.14". The legend at the bottom shows a blue square labeled "BMP280: Pressure Sensor".::> <::Icon: Info icon::> Feed Info <::Icon: Gear icon::> Manage feed name, key, description, and tags. <::Icon: Lock icon::> Privacy <::Icon: Gear icon::> This feed is: private. Only you can see it. <::Icon: Share icon::> Sharing <::Icon: Gear icon::> Not shared yet <::Icon: History icon::> Feed History <::Icon: Gear icon::> Feed history is ON Value size is limited to 1KB You have 8 data points from August 22nd 2023, 6:44PM to August 22nd 2023, 6:47PM. + Add Data <::Button: Download All Data button with a download icon and a filter dropdown icon::> Download All Data ▼ Filter < Prev First page 1 of 1 Next > Created at Value Location 2023/08/22 06:48:13PM 1017.166259765625 <::Icon: Red 'X' icon::> 2023/08/22 06:47:43PM 1017.1484985351562 <::Icon: Red 'X' icon::> 2023/08/22 06:47:13PM 1017.1607666015625 <::Icon: Red 'X' icon::> 2023/08/22 06:46:43PM 1017.1490478515625 <::Icon: Red 'X' icon::> <::Icon: Bell icon::> Notifications <::Icon: Gear icon::> This feed is Online You have no notifications active for this feed.

<a id='1fa402d1-27e9-454e-af7f-150d0d299576'></a>

F.A.Q.

---

How come the altitude calculation is wrong? Is my sensor broken?

<a id='c2ca850c-25ab-48d6-95bd-e2d21d815c84'></a>

No, your sensor is likely just fine. The altitude calculation depends on knowing the barometric pressure at sea level

<a id='4ac79cd1-6849-4f3b-9a58-b34b492e9c70'></a>

If you do not set the correct sea level pressure for your location FOR THE CURRENT DAY it will not be able to calculate the altitude accurately

<a id='27939518-8e90-4106-9cbf-6d0edfca4bc4'></a>

Barometric pressure at sea level changes daily based on the weather!

<a id='94a59918-1aed-4d32-be0d-39c55423f5e4'></a>

If I have long delays between reads, the first data read seems wrong?

<a id='e7260af3-b04d-4890-b86a-23db45dad2fe'></a>

The BMx280 'saves' the last reading in memory for you to query. Just read twice in
a row and toss out the first reading!

<a id='259909f9-15f9-4790-8716-77679c754110'></a>

© Adafruit Industries

<a id='8df25a27-524c-474e-a30c-826f056b84e9'></a>

Page 31 of 34