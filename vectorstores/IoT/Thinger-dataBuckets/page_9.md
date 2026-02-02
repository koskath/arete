<a id='bfa5dbd8-071b-49c8-a204-436bf40d7c2c'></a>

Buckets > DBClimaStick1 > Data

<a id='4871c0f9-3dfb-489a-b63a-6bd2d3c5e4c0'></a>

Data

<a id='d2fb675f-8b6a-4012-b0b2-8301b7668b38'></a>

Import

<a id='573f6933-a85c-495b-ab70-59ccfd622fcf'></a>

Export

<a id='3c03ad92-4fd6-464d-b371-2ef4e767b000'></a>

Clear

<a id='dc5aad9f-4552-4c4d-a0c5-80da9e49f038'></a>



<a id='f2f64e45-da8b-431c-9b6e-ea63414d691f'></a>

Last 24 hours

<a id='f21e2fd0-d584-4834-8b11-ef4ee63ec49b'></a>

Refresh
Last 24 hours
<table id="8-1">
<tr><td id="8-2">Date</td><td id="8-3">altitude</td><td id="8-4">humidity</td><td id="8-5">lux</td><td id="8-6">pressure</td><td id="8-7">temperature</td></tr>
<tr><td id="8-8">6/6/2025, 11:34:33</td><td id="8-9">683.7427978515625</td><td id="8-a">18.109375</td><td id="8-b">0</td><td id="8-c">933.7755737304688</td><td id="8-d">37.459999084472656</td></tr>
<tr><td id="8-e">6/6/2025, 11:34:28</td><td id="8-f">683.97705078125</td><td id="8-g">18.0390625</td><td id="8-h">0</td><td id="8-i">933.7492065429688</td><td id="8-j">37.5</td></tr>
<tr><td id="8-k">6/6/2025, 11:34:23</td><td id="8-l">683.9899291992188</td><td id="8-m">18.0869140625</td><td id="8-n">0</td><td id="8-o">933.7477416992188</td><td id="8-p">37.5099983215332</td></tr>
<tr><td id="8-q">6/6/2025, 11:34:18</td><td id="8-r">684.1339111328125</td><td id="8-s">18.111328125</td><td id="8-t">0</td><td id="8-u">933.7315673828125</td><td id="8-v">37.52000045776367</td></tr>
<tr><td id="8-w">6/6/2025, 11:34:13</td><td id="8-x">683.9147338867188</td><td id="8-y">18.1005859375</td><td id="8-z">0</td><td id="8-A">933.7562255859375</td><td id="8-B">37.560001373291016</td></tr>
<tr><td id="8-C">6/6/2025, 11:34:08</td><td id="8-D">683.8480834960938</td><td id="8-E">18.1572265625</td><td id="8-F">0</td><td id="8-G">933.7637329101562</td><td id="8-H">37.470001220703125</td></tr>
<tr><td id="8-I">6/6/2025, 11:34:03</td><td id="8-J">683.9968872070312</td><td id="8-K">18.205078125</td><td id="8-L">0</td><td id="8-M">933.7470092773438</td><td id="8-N">37.459999084472656</td></tr>
<tr><td id="8-O">6/6/2025, 11:33:58</td><td id="8-P">683.9953002929688</td><td id="8-Q">18.2041015625</td><td id="8-R">0</td><td id="8-S">933.7471923828125</td><td id="8-T">37.45000076293945</td></tr>
<tr><td id="8-U">6/6/2025, 11:33:53</td><td id="8-V">683.6176147460938</td><td id="8-W">18.103515625</td><td id="8-X">0</td><td id="8-Y">933.7896118164062</td><td id="8-Z">37.619998931884766</td></tr>
<tr><td id="8-10">6/6/2025, 11:33:48</td><td id="8-11">683.5880737304688</td><td id="8-12">18.06640625</td><td id="8-13">0</td><td id="8-14">933.79296875</td><td id="8-15">37.59000015258789</td></tr>
<tr><td id="8-16">6/6/2025, 11:33:43</td><td id="8-17">683.9577026367188</td><td id="8-18">18.13671875</td><td id="8-19">0</td><td id="8-1a">933.7514038085938</td><td id="8-1b">37.54999923706055</td></tr>
<tr><td id="8-1c">6/6/2025, 11:33:38</td><td id="8-1d">683.7562255859375</td><td id="8-1e">18.1796875</td><td id="8-1f">0</td><td id="8-1g">933.7740478515625</td><td id="8-1h">37.439998626708984</td></tr>
<tr><td id="8-1i">6/6/2025, 11:33:33</td><td id="8-1j">683.8201904296875</td><td id="8-1k">18.1796875</td><td id="8-1l">0</td><td id="8-1m">933.766845703125</td><td id="8-1n">37.43000030517578</td></tr>
</table>

<a id='7ac99d5d-9093-4f2a-8c47-51caf6c80f2b'></a>

# Bucket Data Import

In order to make bulk data upload or buckets backup processes, the data bucket system has been provided with an import feature that is able to retrieve information from .csv files from a Thinger.io **File System** and store its data using the timestream specified in the file rows.

<a id='1e49eb35-2176-4e5d-a946-6b97eab12618'></a>

Note that using this feature has a **few restrictions**.

1. Each row must contain just one variable and use a ";" separation mark.
2. The file must contain a column identified as "ts" with the Linux Timestream in milliseconds, which will be used to create the temporary serial.

<a id='f3653e39-f9af-40d4-901b-056104aba1cf'></a>

Also, the user account must be able to use File Systems, which is a premium feature, so freemium users can't perform these processes. The accompanying image serves merely as an example; labels such as "File Storage" and "File Name" may vary in the interface:

<a id='dcfc91ba-a9c0-4146-ae90-6b15d54cff94'></a>

9