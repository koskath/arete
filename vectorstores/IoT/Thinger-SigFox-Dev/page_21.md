<a id='820278ce-c7a1-4a6e-a571-f5e487a35de5'></a>

Callback - OK

[OK] - Base station 06C9 < 1 second
200 - OK

[POST] https://api.thinger.io/v1/users/alvarolb/buckets/SmartEverything/data

<a id='cab6eb16-130a-4234-9594-f3283ae63720'></a>

Then we can also check that our data bucket is being populated with the data received from Sigfox. So, open the data bucket in Thinger.io. Nice! We have our data now being stored. **Notice** that the columns in the bucket are just the fields we configured in the Sigfox callback body.

<a id='8bd43ee5-c452-47b1-bd0a-bff6b3595add'></a>

Bucket Explorer
<table id="20-1">
<tr><td id="20-2">Date</td><td id="20-3">device</td><td id="20-4">humidity</td><td id="20-5">latitude</td><td id="20-6">longitude</td><td id="20-7">rssi</td><td id="20-8">snr</td><td id="20-9">station</td><td id="20-a">temperature</td></tr>
<tr><td id="20-b">2017-04-23T01:03:30.688+0200</td><td id="20-c">C378F</td><td id="20-d">41.874535</td><td id="20-e">41</td><td id="20-f">-4</td><td id="20-g">-130</td><td id="20-h">21.28</td><td id="20-i">06C9</td><td id="20-j">25.32931</td></tr>
<tr><td id="20-k">2017-04-23T00:53:22.895+0200</td><td id="20-l">C378F</td><td id="20-m">41.72929</td><td id="20-n">41</td><td id="20-o">-4</td><td id="20-p">-132</td><td id="20-q">19.29</td><td id="20-r">06C9</td><td id="20-s">25.386208</td></tr>
<tr><td id="20-t">2017-04-23T00:43:14.984+0200</td><td id="20-u">C378F</td><td id="20-v">41.384327</td><td id="20-w">41</td><td id="20-x">-4</td><td id="20-y">-129</td><td id="20-z">21.93</td><td id="20-A">06C9</td><td id="20-B">25.518965</td></tr>
<tr><td id="20-C">2017-04-23T00:33:07.300+0200</td><td id="20-D">C378F</td><td id="20-E">41.03574</td><td id="20-F">41</td><td id="20-G">-4</td><td id="20-H">-130</td><td id="20-I">21.36</td><td id="20-J">06C9</td><td id="20-K">25.765518</td></tr>
<tr><td id="20-L">2017-04-23T00:22:59.397+0200</td><td id="20-M">C378F</td><td id="20-N">40.774296</td><td id="20-O">41</td><td id="20-P">-4</td><td id="20-Q">-130</td><td id="20-R">21.01</td><td id="20-S">06C9</td><td id="20-T">25.936207</td></tr>
<tr><td id="20-U">2017-04-23T00:12:51.492+0200</td><td id="20-V">C378F</td><td id="20-W">40.53827</td><td id="20-X">41</td><td id="20-Y">-4</td><td id="20-Z">-129</td><td id="20-10">21.62</td><td id="20-11">06C9</td><td id="20-12">25.993103</td></tr>
<tr><td id="20-13">2017-04-23T00:02:43.686+0200</td><td id="20-14">C378F</td><td id="20-15">41.06842</td><td id="20-16">41</td><td id="20-17">-4</td><td id="20-18">-129</td><td id="20-19">22.02</td><td id="20-1a">06C9</td><td id="20-1b">25.822414</td></tr>
<tr><td id="20-1c">2017-04-22T23:52:35.800+0200</td><td id="20-1d">C378F</td><td id="20-1e">51.19207</td><td id="20-1f">41</td><td id="20-1g">-4</td><td id="20-1h">-130</td><td id="20-1i">20.77</td><td id="20-1j">1D62</td><td id="20-1k">23.47069</td></tr>
<tr><td id="20-1l">2017-04-22T23:37:00.903+0200</td><td id="20-1m">C378F</td><td id="20-1n">41.438797</td><td id="20-1o">41</td><td id="20-1p">-4</td><td id="20-1q">-131</td><td id="20-1r">19.81</td><td id="20-1s">1D62</td><td id="20-1t">25.424137</td></tr>
<tr><td id="20-1u">2017-04-22T23:26:53.076+0200</td><td id="20-1v">C378F</td><td id="20-1w">41.594936</td><td id="20-1x">41</td><td id="20-1y">-4</td><td id="20-1z">-133</td><td id="20-1A">18.21</td><td id="20-1B">06C9</td><td id="20-1C">25.348276</td></tr>
</table>
Refresh
Viewing 0 to 54 items

<a id='82511d0a-b501-4b83-91d7-33154f63bb8d'></a>

## Building a Dashboard

Now that we have our data in the bucket, we can just create a real-time dashboard from our Sigfox data. Create the widgets by selecting the bucket as the data source, and that's all!

<a id='04dd09cb-45ac-4d0e-a36e-bdb4dc7c7010'></a>

21